import pymysql


connection = pymysql.connect(host='localhost',
                       user='root',
                       password='Colobuc')

with connection:
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE news')


