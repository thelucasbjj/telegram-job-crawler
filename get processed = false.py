import psycopg2

connection = psycopg2.connect(user="postgres",
                              # пароль, который указали при установке PostgreSQL
                              password="****",
                              host="127.0.0.1",
                              port="5432",
                              database="postgres_db")
cursor = connection.cursor()

cursor.execute("SELECT job_offers FROM processed")
for i in cursor.fetchall():
    print(i)

cursor.close()
connection.close()