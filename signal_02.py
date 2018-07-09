#參考網址https://blog.csdn.net/John_xyz/article/details/80150428
import signal
#透過按下CTRL+Z來傳送SIGTSTP事件
def signalHandler(signalNum, frame):
    print('(2)發生觸發事件，事件代碼＝({0})。'.format(signalNum))

if __name__=='__main__':
    print('=====開始測試=====')
    print('(1)進程等待中，請按下CTRL+Z，事件代碼(signal.SIGTSTP)＝{0}'.format(signal.SIGTSTP))
    signal.signal(signal.SIGTSTP, signalHandler)
    #進程暫停，等待訊號
    signal.pause()
    print('(3)=====終止訊號測試=====')
