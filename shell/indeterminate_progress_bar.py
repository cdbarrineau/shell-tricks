import time

def multi_step():
    print ('Multi-step')
    total_steps=5
    for progress in range(total_steps):
        filled = int(progress * 20 / total_steps)
        bar = ''
        for i in range (filled):
            bar = bar + '#'
        
        print("\x1b[2K", end="")
        print('[' + bar + ']', end="\r")

        # progress = progress + 1
        time.sleep(0.5)
        
def single_step():
    print ('Single Step')
    total_steps=5
    progress = 0
    for r in range(total_steps):
        bar = ''
        for i in range (progress):
            bar = bar + '#'
        
        print("\x1b[2K", end="")
        print('[' + bar + ']', end="\r")
    
        progress = progress + 1
        time.sleep(0.5)

def spinner():
    print ('Spinner')
    total_steps=2
    chars = ['\u2014', '\\', '|', '/' , '\u2014', '\\', '|', '/']
    
    for r in range(total_steps):
        i = 0
        while i < len(chars):
            print("\x1b[2K", end="")
            
            print (chars[i], end = '\r')
            i = i + 1
            
            time.sleep(0.5)


if __name__ == '__main__':
    multi_step()
    
    print ()
    
    single_step()
    
    print()
    
    spinner()
    
    print('Done')