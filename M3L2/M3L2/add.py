import sqlite3
from config import DATABASE

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

table_name = 'projects'

new_column_name = 'black_panter'
new_column_type = 'TEXT'

alter_query = f"ALTER TABLE {table_name} ADD COLUMN {new_column_name} {new_column_type}"
cursor.execute(alter_query)

conn.commit()
conn.close()