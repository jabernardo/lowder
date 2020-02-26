# -*- coding: utf-8 -*-

import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import time
from lowder import Lowder, LOADERS

loader = Lowder()

def test():
    time.sleep(3)
    loader.stop('Waiting success!!!')

loader.start('Loading...', test)
loader.start('Processing', test, LOADERS['dots'])
