from pymongo import MongoClient
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
client = MongoClient('mongodb://localhost:27017/')
db = client['teste']
collection = db['os_checklist_financial']
data = list(collection.find())
transformed_data = []
for item in data:
    _id = str(item.get('_id'))
    unique_key = item.get('unique_key')
    customer_id = item.get('customer_id')
    os_id = item.get('os_id')
    createdAt = item.get('createdAt')
    updatedAt = item.get('updatedAt')    
    for d in item['data']:        
            if d.isnumeric() and d in item['data']:
                new_item = {}
                new_item['_id'] = str(_id)
                new_item['unique_key'] = unique_key
                new_item['customer_id'] = customer_id
                new_item['os_id'] = os_id            
                new_item['createdAt'] = createdAt
                new_item['updatedAt'] = updatedAt
                new_item['sale_quantity'] = item['data'][d]["sale_quantity"]
                new_item['sale_value'] = item['data'][d]["sale_value"]
                try:
                    new_item['sale_total'] = locale.atof(item['data'][d]["sale_total"])
                except ValueError:
                    new_item['sale_total'] = 0 
                new_item['done_quantity'] = item['data'][d]["done_quantity"]
                if item['data'][d]['done_value'] == "":
                    new_item['done_value']= 0                                
                else:
                    new_item['done_value'] = item['data'][d]['done_value']
                         
                new_item['done_total'] = item['data'][d]['done_total']
                new_item['diff_quantity'] = item['data'][d]['diff_quantity']
                new_item['diff_total'] = item['data'][d]['diff_total']
                #display([new_item['done_value']])                

#                 print("id: ", new_item['_id'])
#                 print("unique_key: ", new_item['unique_key'])
#                 print("os_id: ", new_item['os_id'])
#                 print("createdAt: ", new_item['createdAt'])
#                 print("sale_quantity: ", new_item['sale_quantity'])
#                 print("sale_value: ", new_item['sale_value'])
#                 print("sale_total: ", new_item['sale_total'])
                transformed_data.append(new_item) 
            else:
              # Handle the case where d is not a valid integer or d doesn't exist in the item['data']
                pass

import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='teste',
    auth_plugin='mysql_native_password'
)
cursor = cnx.cursor()

# Iterando sobre os dados transformados
for item in transformed_data:
    # Inserindo os dados no MySQL
        cursor.execute("INSERT INTO data_os_checklist_financial (id_mongo_os_checklist, unique_key, customer_id, os_id, createdAt, updatedAt, sale_quantity, sale_value, sale_total, done_quantity, done_value, done_total, diff_quantity, diff_total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (item['_id'], item['unique_key'], item['customer_id'], item['os_id'], item['createdAt'], item['updatedAt'], item['sale_quantity'], item['sale_value'], item['sale_total'], item['done_quantity'], item['done_value'], item['done_total'], item['diff_quantity'], item['diff_total']))
        cnx.commit()

# Fechando a conexão
cursor.close()
cnx.close()


