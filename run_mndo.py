#!/usr/bin/env python2
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org>
import numpy as np
from scipy.optimize import minimize
from numpy.linalg import norm
import os
from copy import deepcopy
import threading
import subprocess

from matplotlib import pyplot
import time
import seaborn as sns
import pandas as pd


def run_mndo99_nodisk():
    
    output1 = []
    output2 = []
    output3 = []
    output4 = []

    def task1():
        global output1
        cmd = ["./run_mndo99", "master1.inp"]
        output1 = subprocess.check_output(cmd)

    def task2():
        global output2
        cmd = ["./run_mndo99", "master2.inp"]
        output2 = subprocess.check_output(cmd)

    def task3():
        global output3
        cmd = ["./run_mndo99", "master3.inp"]
        output3 = subprocess.check_output(cmd)

    def task4():
        global output4
        cmd = ["./run_mndo99", "master4.inp"]
        output4 = subprocess.check_output(cmd)
    

    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t3 = threading.Thread(target=task3)
    t4 = threading.Thread(target=task4)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    return output1 + output2 + output3 + output4


if __name__ == "__main__":

    lol = run_mndo99_nodisk()

    print lol

