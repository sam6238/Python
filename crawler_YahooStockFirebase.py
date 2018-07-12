# Yahoo股市
import requests
from bs4 import BeautifulSoup
#
import datetime
import time
from threading import Timer
#
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# initial firebase
# firebase認證->在控制台->帳戶服務->可以複製來貼上
cred = credentials.Certificate(xxxxxx.json')
firebase_admin.initialize_app(
    cred, {'databaseURL': 'https://xxxxxxxxxx.firebaseio.com/'})
#refData = db.reference('raspberrypi/YahooStock')
refData = db.reference('raspberrypi/YahooNews')

# 進行計時
since = time.time()
interval = time.time() - since

# 初步建置
targetURL = 'https://tw.stock.yahoo.com/'
req = requests.get(targetURL)
soup = BeautifulSoup(req.text, 'lxml')

# 開始解析
tableParent = soup.find('table', attrs={'id': 'M1News'})
tableChild = tableParent.find('table')
spans = tableChild.find_all('span', class_='mbody')

#以下使用函數來解析
def autoWriteToFirebase():
    # 增加一個序號，避免時間重複
    serialNum = 0
    for span in spans:
        #
        date = datetime.datetime.now()
        strDate = date.strftime('%Y-%m-%d-%H-%M-%S-')
        strKey = strDate + str(serialNum)
        print('資料：', strKey, span.text)
        #開始上傳->這裡使用update
        try:
            refData.update({
                strKey: {
                    'date': strKey,
                    'content': span.text
                }

            })
        except:
            print('發生錯誤')
        finally:
            serialNum += 1
    #每10秒重複執行一次->實務運作時的時間設定要拉長，甚至另外製作「比對」功能
    Timer(10, autoWriteToFirebase).start()


autoWriteToFirebase()
