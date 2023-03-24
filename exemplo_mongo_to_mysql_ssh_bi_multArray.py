# Importando bibliotecas necessárias
import sys
import os
import time
from pymongo import MongoClient
import pymysql

# Adicionando caminho absoluto para importação de classes
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

# Importando classes necessárias
from utilidades.database_classes import SSHMySQL
from utilidades.database_classes import MongoDB
from utilidades.utils import strtodate, status_fill

# Início do cálculo de tempo de execução
start_time = time.time()

# Conexão com o banco de dados MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["exemplo_db"]
mongo_collection = mongo_db["exemplo_collection"]

# Filtrando dados da coleção MongoDB
data = mongo_collection.find({"type": "exemplo_folder"})

# Função para obter a menor data de envio dos documentos
def get_min_send_date(control_docs):
    first_send_dates = []
    for doc in control_docs:
        send_date = doc.get('send_date')
        if send_date:
            first_send_dates.append(strtodate(send_date))
    return min(first_send_dates, default=None)

# Função para obter a maior data de recebimento dos documentos
def get_max_receipt_date(control_docs):
    last_receipt_date = [doc.get('receipt_date') for doc in control_docs if doc.get('receipt_date') is not None]
    if last_receipt_date:
        return max(last_receipt_date)
    else:
        return None

# Preparando dados não relacionais para inserção no MySQL
transformed_data = []
for item in data:
    receipt_documents = item.get('data', {}).get('receipt_documents')
    if receipt_documents is not None:
        _id = str(item.get('_id'))
        count_control_of_personal_documents = len(receipt_documents.get('control_of_personal_documents', [])) 
        count_control_exemplo_documents = len(receipt_documents.get('control_exemplo_documents', []))
        control_docs = receipt_documents.get('control_exemplo_documents', [])
        min_send_date = get_min_send_date(control_docs)
        max_receipt_date = get_max_receipt_date(control_docs)
        status_control_exemplo_documents = status_fill(item)
        
        transformed_data.append((_id,count_control_of_personal_documents,count_control_exemplo_documents,min_send_date,max_receipt_date,status_control_exemplo_documents))
        print(_id,min_send_date,max_receipt_date,status_control_exemplo_documents)  

# Conexão e inserção no MySQL
mysql_con = SSHMySQL()
mysql_con.start_ssh_tunnel()
conn = mysql_con.open_connection_mysql()

try:
    cursor = conn.cursor()
    query = "INSERT INTO exemplo_folder_exemplo_receipt_documents(id_os,count_control_of_personal_documents,count_control_exemplo_documents,fist_send_date,last_receipt_date,status_control_exemplo_documents) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.executemany(query, transformed_data)
    conn.commit()
except Exception as e:
    print('Erro:', e)
finally:
    mysql_con.close_connection_mysql()
    mysql_con.stop_ssh_tunnel()

# Final do cálculo de tempo de execução e impressão do tempo total
end_time = time.time()
total_time = end_time - start_time
print('Tempo total de processamento:', total_time, 'segundos')
