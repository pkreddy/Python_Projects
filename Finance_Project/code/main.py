import _thread
import time
import pip
#defining a dummy function for thread which keeps on checking on current time
def print_time():
   global current_time
   global kill
   while not kill:
      current_time = time.ctime(time.time())
      time.sleep(2)
   print('Killing thread print_time')

def getTime():
    print('type the command \'time\' to get the time')
    print('type quit to quit the program')
    global current_time
    global kill
    input_from_user = input()
    while input_from_user:
        if input_from_user == 'time':
            print(current_time)
        elif input_from_user == 'help':
            print('type the command \'time\' to get the time')
            print('type quit to quit the program')
        elif input_from_user == 'quit':
            kill = 1
            print('Started cleaning threads')
            time.sleep(2)
            print('Killing thread getTime')
            time.sleep(1)
            break
        else:
            print('input not recognized')
        input_from_user = input()
try:
    current_time=1;
    kill = 0;
    _thread.start_new_thread( print_time, ())
    _thread.start_new_thread( getTime, ())
    #thread1 = _thread.start_new_thread( print_time, ())
    #thread2 = _thread.start_new_thread( getTime, ())
    #thread1.daemon = True
    #thread2.daemon = True
    #thread1.start()
    #thread2.start()
    print('Killed all threads')
except Exception:
    traceback.print_exc()
    print('error in thread')
