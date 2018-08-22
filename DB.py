import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='english_sounds_app',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

class Db:

    a = ''