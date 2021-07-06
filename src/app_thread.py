"""
# Copyright 2020 by Vihangam Yoga Karnataka.
# All rights reserved.
# This file is part of the Vihangan Yoga Operations of Ashram Management Software Package(VYOAM),
# and is released under the "VY License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
# Vihangan Yoga Operations  of Ashram Management Software
# File Name : app_thread.py
# Developer : Sant Anurag Deo
# Version : 2.0
"""

from app_common import *
import pythoncom

import threading
import os.path
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, src_file,
                 destination_file, starting_index, viewPDF, printBtn, infoLabel, destination_copy_folder):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.src_name = src_file
        self.dest_name = destination_file
        self.starting_index = starting_index
        self.btnToEnable1 = viewPDF
        self.btnToEnable2 = printBtn
        self.labelinfo = infoLabel
        self.destination_copy_folder = destination_copy_folder

    def run(self):
        print("Starting ", self.name)
        pythoncom.CoInitialize()
        objCommonUtil = CommonUtil()

        if self.name == "loadingvyoam":
            window = Tk()

            time.sleep(3)
            window.destroy()

        elif self.name == "stockinfoThread":
            if self.btnToEnable1 != "Dummy":
                self.btnToEnable1.configure(state=DISABLED, bg="light grey")
            if self.btnToEnable2 != "Dummy":
                self.btnToEnable2.configure(state=NORMAL, bg="light grey")
            objCommonUtil.preparePDFStatement_forStockInfo(self.src_name,
                                                           self.dest_name, self.destination_copy_folder)
        else:
            objCommonUtil.preparePDFStatement_file(self.src_name,
                                                   self.dest_name, self.destination_copy_folder)
        if self.btnToEnable1 != "Dummy":
            self.btnToEnable1.configure(state=NORMAL, bg="RosyBrown1")
        if self.btnToEnable2 != "Dummy":
            self.btnToEnable2.configure(state=NORMAL, bg="RosyBrown1")
        text_info = "Statement Generation is complete. Press View to open file."
        if self.labelinfo != "Dummy":
            self.labelinfo.configure(text=text_info, fg='purple')
        print("Exiting ", self.name)


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
