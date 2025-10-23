import time
import threading

keep_spinning = True

def spinner_with_stop():
    global keep_spinning
    print ('Spinner with Stop')
    t = threading.Thread(target=start_spinner())
    t.daemon = True
    t.start()
    
    try:
        i = input('Press Enter to Stop').strip().lower()
        if i == 's':
            keep_spinning = False
    except KeyboardInterrupt:
        keep_spinning = False

def start_spinner():
    global keep_spinning
    
    # total_steps=10
    chars = ['\u2014', '\\', '|', '/' , '\u2014', '\\', '|', '/']
    
    print ('Press s to stop')
    # for r in range(total_steps):
    while keep_spinning:
        i = 0
        while i < len(chars):
            print("\x1b[2K", end="")
            
            # print ('{: >20}\t(Press s to stop)'.format(*chars[i] ), end = '\r')
            print (chars[i], end = '\r')
            i = i + 1
            
            time.sleep(0.5)
            
if __name__ == '__main__':

    spinner_with_stop()
    
    print('Done')