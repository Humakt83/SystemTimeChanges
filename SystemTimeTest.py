#!/usr/bin/env python
# -*- coding: utf_8 -*-

import datetime
import time
import win32api
import random

class SystemTimeTest:

    def run(self):
        print "Starting time test in infinite loop"
        while True:         
            self.changeSystemTime()
            time.sleep(1)  
    
    def changeSystemTime(self):
        tt = win32api.GetSystemTime()
        print "System time before change:"
        self.printTime(tt)
        win32api.SetSystemTime(tt[0], tt[1], tt[2], tt[3], tt[4], tt[5], tt[6] -1, random.randint(0, 999))
        print "System time after change:"
        self.printTime(win32api.GetSystemTime())
    
    def printTime(self, timeTuple):
        tt = map(str, timeTuple)        
        print "" + tt[0] + "-" + tt[1] + "-" + tt[3] + " " + tt[4] + ":" + tt[5] + ":" + tt[6] + "." + tt[7]
    
if __name__ == "__main__":
    timeTest = SystemTimeTest()
    
    try:
        timeTest.run()
        
    except Exception, excpt:
        print excpt