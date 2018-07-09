import signal
import threading
import time

#參數為必須
def userInterupt(signal, frame):
    print('->觸發中斷事件：Control + C')
    global continueLoop
    continueLoop = False

if __name__=='__main__':
    signal.signal(signal.SIGINT, userInterupt)
    count = 0
    continueLoop = True
    while continueLoop:
        count += 1
        print('進入主程式迴圈內,第{}圈'.format(count))
        time.sleep(1)
        
