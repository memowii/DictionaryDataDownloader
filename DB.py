import pymysql.cursors

class DB:

    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='english_sounds_app',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    def getAllDuolingoWords(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "select * from DuolingoWord"
                cursor.execute(sql)
                return cursor.fetchall()
        except Exception as e:
            print(e)

    def updatePronAndSoundFile(self, id_duolingo_word, pronunciation, sound_file):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                sql = 'update DuolingoWord set pronunciation=%s, sound_file=%s where id=%s'
                cursor.execute(sql, (pronunciation, sound_file, id_duolingo_word))
            self.connection.commit()
        except Exception as e:
            print(e, pronunciation, sound_file)

    def disconnect(self):
        self.connection.close()