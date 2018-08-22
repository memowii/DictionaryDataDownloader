# https://gist.github.com/ikegami-yukino/51b247080976cb41fe93
# https://www.scrapehero.com/tutorial-web-scraping-hotel-prices-using-selenium-and-python/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='english_sounds_app',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def getIdWordClass(dbConnection, wordClass):
    if not wordClass:
        return 'null'

    try:
        with dbConnection.cursor() as cursor:
            sql = "select `id`, `name` from `WordClass` where `name`=%s"
            cursor.execute(sql, (wordClass))
            result = cursor.fetchone()

            if not result:
                sql = "INSERT INTO `WordClass` (`id`, `name`) VALUES (null, %s)"
                cursor.execute(sql, (wordClass))
                dbConnection.commit()

                sql = "select `id`, `name` from `WordClass` where `name`=%s"
                cursor.execute(sql, (wordClass))
                result = cursor.fetchone()

            return result['id']
    except Exception as e:
        print(e, wordClass, sql)

def insertNewDuolingoWord(dbConnection, word, worClassId):
    try:
        with dbConnection.cursor() as cursor:
            if worClassId != 'null':
                sql = "insert into `DuolingoWord` values (null, %s, null, null, %s);"
                cursor.execute(sql, (word, worClassId))
            else:
                sql = "insert into `DuolingoWord` values (null, %s, null, null, null);"
                cursor.execute(sql, (word))
        dbConnection.commit()
    except Exception as e:
        print(e, word, worClassId, sql.format(word, worClassId))

mail_address = 'memogl25@gmail.com'
password = 'generalmemo'
google_account_url = 'https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin'
duolingo_url = 'https://www.duolingo.com/'

driver = webdriver.Chrome()
driver.get(google_account_url)

driver.find_element_by_id("identifierId").send_keys(mail_address)
driver.find_element_by_id("identifierNext").click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type=password]"))
    )
    element.send_keys(password)
finally:
    driver.find_element_by_id("passwordNext").click()
sleep(3)
driver.get(duolingo_url)
driver.find_element_by_id("sign-in-btn").click()
sleep(3)
try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "_2vIpC"))
    )
    element.click()
finally:
    pass
sleep(3)
try:
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "_2QyU5"))
    )
    elements[1].click()
finally:
    pass

table = WebDriverWait(driver, 3).until(
    EC.visibility_of_element_located((By.TAG_NAME, 'table'))
)

table = driver.find_element_by_tag_name('table')
rows = table.find_elements_by_tag_name('tr')
for i in range(1, len(rows)):
    row = rows[i]
    tds = row.find_elements_by_tag_name('td')
    word = tds[0].text
    word_class = tds[1].text.lower()
    id_word_class = getIdWordClass(connection, word_class)
    insertNewDuolingoWord(connection, word, id_word_class)

connection.close()
driver.close()