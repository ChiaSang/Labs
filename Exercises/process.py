import os
import time
ret = os.fork()
if ret == 0:
    while True:
        print('---this is a test---\n')
        time.sleep(1)
else:
    while True:
        print('----------this is a test---------\n')
        time.sleep(1)
