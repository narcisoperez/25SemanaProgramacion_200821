# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:18:27 2021

@author: NarW10
"""


import time
from multiprocessing import Pool


def increment(input2):
    print(input2)
    for i in range(1000):
        input2 = input2 + 1
        print(input2)

if __name__ == "__main__":
    inputs = [1] * 100000
    pool = Pool(50)
    started = time.time()
    pool.map(increment, inputs)
    

    elapsed = time.time()
    print('Time taken MultiProcess :', elapsed - started)

    pool.close()