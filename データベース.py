import sqlite3
conn_DB=sqlite3.connect(":memory:")
cur_DB = conn_DB.cursor()
cur_DB.execute('select * from country2')
for id_data,code_data,name_data in cur_DB:
    print(id_data,f'zero padding:{code_data:02}',name_data)
cur_DB.close()
conn_DB.close()