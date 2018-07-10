import time
import datetime
import threading
#
import signal
#
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#json檔案路徑
myCertificate = 'xxx.json'

def uploadToFirestore():
    print ('=====START=====')
    dataString = 'Some data'
    print('Data: ' + dataString)
    #取得節點
    firestoreRef = db.collection('recordsOfData').document()
    t = time.time()
    date = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d-%H-%M-%S")
    #
    firestoreRef.set({'datatime': date, 'content': dataString})
    #
    #threading.Timer(5,uploadToFirestore).start()


def endUpload(signal, frame):
    global continueUploading
    print ('ctrl+C captured, ending read.')
    continueUploading = False

if __name__ == "__main__":

    #initial firestore
    #firebase認證->在控制台->帳戶服務->可以複製來貼上
    cred = credentials.Certificate(myCertificate)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    #
    continueUploading = True
    #ctrl + c gameover
    signal.signal(signal.SIGINT, endUpload)

    while continueUploading:
        #
        uploadToFirestore()
        time.sleep(5)
