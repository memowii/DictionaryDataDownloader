import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='english_sounds_app',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "select id, name from WordClass where name=%s"
        cursor.execute(sql, ('verbb',))
        result = cursor.fetchone()
        if result == None:
            print('es none')
        #print(result['id'])
finally:
    connection.close()