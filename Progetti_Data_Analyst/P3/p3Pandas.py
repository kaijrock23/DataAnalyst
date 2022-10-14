from sqlalchemy import create_engine
import pandas as pd
db_connection_str = 'mysql+pymysql://root:root@127.0.0.1/ecommerce'
db_connection = create_engine(db_connection_str)
prova = pd.read_sql("prodotto", db_connection)
print(prova)

query = "'select' + name_column + 'from' + table_name + ';'"
df = pd.read_sql_query(query, db_connection)

query = "INSERT INTO database"
df = pd.read_sql_query(query, db_connection)

query = "select product_name from product_quantity"
df = pd.read_sql_query(query, db_connection)

query = "INSERT INTO prodotto (pid, nome) values (%s, %s)"
df = pd.read_sql_query(query, db_connection)

query = "DELETE FROM marca WHERE mid =%s and nome = %s and immagine = %s and url = %s "
df = pd.read_sql_query(query, db_connection)

query = "DELETE FROM prodotto WHERE pid = %s and nome = %s and descr_breve = %s and descr_lunga = %s and cid = %s and quantita = %s and pid = %s and arrivo impegnati = %s and mid = %s"
df = pd.read_sql_query(query, db_connection)

query = "SELECT categoria.nome, categoria.cid, marca.mid, marca.nome, marca.immagine, marca.url FROM ecommerce INNER JOIN marca ON categoria = categoria.id"
df = pd.read_sql_query(query, db_connection)

query = "SELECT nome, quantita FROM prodotto WHERE quantita > 99 ORDER BY quantita DESC;"
df = pd.read_sql_query(query, db_connection)

query = "SELECT COUNT pid, arrivo FROM prodotto GROUP BY arrivo HAVING COUNT(pid) > 0 ORDER BY COUNT(pid) DESC;"
df = pd.read_sql_query(query, db_connection)

query = "'select' + table_name + ';'"
df = pd.read_sql_query(query, db_connection)

