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

    def updatePronAndSoundFile(self, id_duolingo_word, pronunciation):
        try:
            with self.connection.cursor() as cursor:
                sql = 'update DuolingoWord set pronunciation=%s where id=%s'
                cursor.execute(sql, (pronunciation, id_duolingo_word))
            self.connection.commit()
        except Exception as e:
            print(e, pronunciation)

    def getWordsWithIpa(self, ipa):
        try:
            with self.connection.cursor() as cursor:
                sql = 'select * from DuolingoWord where locate(%s, DuolingoWord.pronunciation) > 0'
                cursor.execute(sql, (ipa))
                return cursor.fetchall()
            self.connection.commit()
        except Exception as e:
            print(e)

    def disconnect(self):
        self.connection.close()