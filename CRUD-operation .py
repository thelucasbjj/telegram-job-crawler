# Выполнение CRUD-операций из Python
import psycopg2
from psycopg2 import Error

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="141194",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

    cursor = connection.cursor()
    # Выполнение SQL-запроса для вставки данных в таблицу
    insert_query = """INSERT INTO  job_offers (id, created_at, updated_at, published_at, raw_text, reference, processed, title, location, description, position) VALUES ()"""
    cursor.execute(insert_query)
    connection.commit()
    print("1 запись успешно вставлена")
    # Получить результат
    cursor.execute("SELECT * from  job_offers")
    record = cursor.fetchall()
    print("Результат", record)

    # Выполнение SQL-запроса для обновления таблицы
    update_query = """Update job_offers """
    cursor.execute(update_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Запись успешно удалена")
    # Получить результат
    cursor.execute("SELECT * from job_offers")
    print("Результат", cursor.fetchall())

    # Выполнение SQL-запроса для удаления таблицы
    #delete_query = """Delete from job_offers where id = 1"""
    #cursor.execute(delete_query)
    #connection.commit()
    #count = cursor.rowcount
    #print(count, "Запись успешно удалена")
    # Получить результат
    #cursor.execute("SELECT * from job_offers")
    #print("Результат", cursor.fetchall())

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")