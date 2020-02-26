# -*- coding: utf-8 -*-

import time
import threading

LOADERS = {
        'default': {
            'interval': 0.1,
            'frames': ('/', '-', '|', '\\', '-')
        },
        'dots': {
            'interval': 0.2,
            'frames': ('⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏')
        },
        'dots-bar': {
            'interval': 0.2,
            'frames': ('.    ', ' .   ', '  .  ','   . ', '    .',
                       '   . ', '  .  ', ' .   ')
        },
        'bar': {
            'interval': 0.2,
            'frames': ('-    ', ' =   ', '  -  ','   = ', '    -',
                       '   = ', '  -  ', ' =   ')
        },
        'arrow': {
            'interval': 0.2,
            'frames': ('>    ', ' >   ', '  >  ','   > ', '    >',
                       '   < ', '  <  ', ' <   ')
        }
    }

class Lowder:
    __run = True
    __loader_screen = LOADERS['default']
    __result = None
    
    def __init__(self):
        super().__init__()
        
    def stop(self, message):
        self.__run = False
        time.sleep(1)
        print(message)
        
    def __loader(self, message):
        while self.__run:
            for char in self.__loader_screen['frames']:
                print(f"{char} {message}", end="\r")
                time.sleep(self.__loader_screen['interval'])
            
    def __call(self, callback):
        self.__result = callback()
    
    def start(self, message, callback, loader = LOADERS['default']):
        self.__loader_screen = loader
        self.__run = True
        
        y = threading.Thread(target=self.__call, args=(callback,))
        y.start()
        
        x = threading.Thread(target=self.__loader, args=(message,))
        x.start()
        
        x.join()
        y.join()
