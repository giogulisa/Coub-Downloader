import subprocess
import threading
import sys

import Cb_Dn

# Cmd input
url = sys.argv[1]

# Just Url
# url = ....   <-- Url Of Coub U Want To Download

CleanUrl = url.replace('https://coub.com/view/', '')

thread1 = threading.Thread(target=Cb_Dn.Coub().video, args=(url,))
thread1.start()

thread2 = threading.Thread(target=Cb_Dn.Coub().audio, args=(url,))
thread2.start()

thread1.join()
thread2.join()

cmd = 'ffmpeg -i ' + CleanUrl + '.mp4' + ' -i ' + CleanUrl + ".mp3" + ' -shortest ' + CleanUrl + 'Final.mp4'

subprocess.call(cmd, shell=True)
