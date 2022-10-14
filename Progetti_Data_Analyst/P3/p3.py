from msilib.schema import tables
import mysql.connector
conn = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='ecommerce')
cursor = conn.cursor()

def select_table(name_column, table_name):   #Query per selezionare una tabella
    name_column = str(name_column)
    query = 'select' + name_column + 'from' + table_name + ';'
    return query

sql = select_table('cid', 'nome')



def insert_table(table_name):      #Query per inserire una nuova tabella
    insert = 'select' + table_name + ';'
    return insert

sql = insert_table('')

def insert_tables(tables_names):   #query per inserire piu' tabelle "almeno credo"
    if len(tables_names) > '':
        for i in tables:
            name = tables_names[i]
            val = (name)
            sql = "INSERT INTO database"
            cursor.execute(sql, val)


def insert_product(product_name, product_quantity):  # query per inserire un prodotto
    product_name = str(product_name)
    product_quantity = int(product_quantity)
    insert = "select product_name from product_quantity"
    return insert

sql = insert_product('Scheda Asrock', 12)


def insert_products(products, products_quantity):  #query per inserire piu' prodotti
    if len(products) ==  len(products_quantity):
        for i in range(len(products)):
            name = products[i]
            quantity = products_quantity[i]
            val = (name, quantity)
            sql = "INSERT INTO prodotto (pid, nome) values (%s, %s)"
            cursor.execute(sql, val)


def delete_marca(mid, nome, immagine, url):   #query per eliminare una marca
    sql = "DELETE FROM marca WHERE mid =%s and nome = %s and immagine = %s and url = %s "
    mid = int(mid)
    nome = str(nome)
    immagine = str(immagine)
    url = str(url)
    val = (mid, nome, immagine, url)
    cursor.execute(val, sql)

def delete_product(pid, nome, descr_breve, descr_lunga, cid, quantita, arrivo, impegnati, mid):     #query per cancellare un prodotto
    sql = "DELETE FROM prodotto WHERE pid = %s and nome = %s and descr_breve = %s and descr_lunga = %s and cid = %s and quantita = %s and pid = %s and arrivo impegnati = %s and mid = %s"
    pid = str(pid)
    nome = str(nome)
    descr_breve = str(descr_breve)
    descr_lunga = str(descr_lunga)
    cid = int(cid)
    quantita = int(quantita)
    arrivo = int(arrivo)
    impegnati = int(impegnati)
    mid = int(mid)
    val = (pid, nome, descr_breve, descr_lunga, cid, quantita, arrivo, impegnati, mid)
    cursor.execute(val, sql)


    
def table_join(first_table, second_table):   #query per unire due tabelle
    sql = "SELECT categoria.nome, categoria.cid, marca.mid, marca.nome, marca.immagine, marca.url FROM ecommerce INNER JOIN marca ON categoria = categoria.id"
    first_table = ''
    second_table = ''
    val = (first_table, second_table)
    cursor.execute(val, sql)



sql = "SELECT nome, quantita FROM prodotto WHERE quantita > 99 ORDER BY quantita DESC;"    #query per ordinamento in modo decrescente di un prodotto
cursor.execute(sql)
conn.commit()
result = cursor.fetchall()
print(result)
conn.close()



sql = "SELECT COUNT pid, arrivo FROM prodotto GROUP BY arrivo HAVING COUNT(pid) > 0 ORDER BY COUNT(pid) DESC;" #query per contare i prodotti in arrivo in ordine decrescente
cursor.execute(sql)
conn.commit()
result = cursor.fetchall()
print(result)
conn.close()


