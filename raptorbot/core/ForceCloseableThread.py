import ctypes
import json
import sys
import threading
import time
from threading import Thread
from time import sleep


class ForceCloseableThread(threading.Thread): 
    def __init__(self, func, *args): 
        threading.Thread.__init__(self) 
        self.func = func
        self.args = args
        self._thread_id = None
              
    def run(self): 
  
        # target function of the thread class 
        try: 
            self.func(self.args)
            
        except SystemExit:
            print("WARNING: The thread was forcefully closed and did not finish executing. Did your code take too long?")

    def get_id(self): 
        # returns id of the respective thread 
        if hasattr(self, '_thread_id') and self._thread_id is not None: 
            return self._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self: 
                self._thread_id = id
                return id
   
    def forcefully_close(self): 
        if self.isAlive() is False:
            return
        thread_id = self.get_id() 
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
              ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure') 
