"""
# Copyright 2020 by Vihangam Yoga Karnataka.
# All rights reserved.
# This file is part of the Vihangan Yoga Operations of Ashram Management Software Package(VYOAM),
# and is released under the "VY License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
# Vihangan Yoga Operations  of Ashram Management Software
# File Name : app_common.py
# Developer : Sant Anurag Deo
# Version : 1.0
"""

from app_defines import *
import socket
import MySQLdb as sql_db


class CommonUtil:

    def __init__(self):
        print("constructor called for CommonUtil edit ")
        self._new_member_id = 0
        self.currentUser = ""

    def print_statement_file(self, src_file, pathToPrint, starting_index):
        # if pdf doesn't exists ,convert to pdf
        os.startfile(pathToPrint, 'print')
        print("File is sent for printing to default printer !!!")
        # delete the new records in template file

        wb_template = openpyxl.load_workbook(src_file)
        template_sheet = wb_template.active

        for rows in range(15, starting_index + 1):
            for columns in range(1, 7):
                template_sheet.cell(row=rows, column=columns).value = ""

        wb_template.save(src_file)

    def open_statement_file(self, src_file, pathToPrint, starting_index):
        # if pdf doesn't exists ,convert to pdf

        os.startfile(pathToPrint)
        print("File is sent for opening on desktop")
        # delete the new records in template file

        # executed only if
        wb_template = openpyxl.load_workbook(src_file)
        template_sheet = wb_template.active

        for rows in range(15, starting_index + 1):
            for columns in range(1, 7):
                template_sheet.cell(row=rows, column=columns).value = ""

        wb_template.save(src_file)

    def clearSales_InvoiceData(self, src_file, starting_index):
        print("clearing the template data for re-use next time")
        wb_template = openpyxl.load_workbook(src_file)
        template_sheet = wb_template.active

        for rows in range(19, starting_index + 1):
            for columns in range(1, 7):
                template_sheet.cell(row=rows, column=columns).value = ""

        wb_template.save(src_file)

    def preparePDFStatement_file(self, src_file, pathToPrint, destination_copy_folder):
        self.convertExcelToPdf(src_file, pathToPrint)
        self.copyTheStatementFileToDesktop_file(pathToPrint, destination_copy_folder)
        # copy to software repo
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Statements"
        shutil.copy(pathToPrint, dirname)

    def preparePDFStatement_forStockInfo(self, src_file, pathToPrint, destination_copy_folder):
        self.convertExcelToPdf(src_file, pathToPrint)
        print("Converted and created in local")
        self.copyTheStatementFileToDesktop_file(pathToPrint, destination_copy_folder)
        print("Copied to desktop")

    def copyTheStatementFileToDesktop_file(self, src_file, destination_copy_folder):
        shutil.copy(src_file, destination_copy_folder)

    def create_backup(self, src_folder, destination_copy_folder):
        shutil.copytree(src_folder, destination_copy_folder)

    def donothing(self, event=None):
        print("Button is disabled")
        pass

    def convertExcelToPdf(self, src_file, dest_file):
        # Path to original excel file
        WB_PATH = os.path.abspath(src_file)
        # PDF path when saving
        PATH_TO_PDF = os.path.abspath(dest_file)

        excel = win32com.client.Dispatch("Excel.Application")

        excel.Visible = False
        wb = excel.Workbooks.Open(WB_PATH)
        try:
            print('Start conversion to PDF')

            # Specify the sheet you want to save by index. 1 is the first (leftmost) sheet.
            ws_index_list = [1]
            wb.WorkSheets(ws_index_list).Select()

            # Save
            wb.ActiveSheet.ExportAsFixedFormat(0, PATH_TO_PDF)
        except com_error as e:
            print('failed.')
        else:
            print('Succeeded.')
        finally:
            wb.Close()
            excel.Quit()

    def getCurrentYearFolderName(self):
        today = datetime.now()
        year = today.strftime("%Y")
        return year

    def prepare_dateFromString(self, dateStr):
        # print("Received str for date conversion : ", dateStr)

        new_date = dateStr.split('-')
        new_Day = new_date[0]
        new_Month = new_date[1]
        new_Year = new_date[2]

        date_final = date(int(new_Year), int(new_Month), int(new_Day))
        return date_final

    # common methods to disable all children in tkinter widget
    def disableChildren(self, parent):
        for child in parent.winfo_children():
            wtype = child.winfo_class()
            if wtype not in ('Frame', 'Labelframe'):
                child.configure(state='disable')
            else:
                self.disableChildren(child)

    # common methods to enable all children in tkinter widget
    def enableChildren(self, parent):
        for child in parent.winfo_children():
            wtype = child.winfo_class()
            print(wtype)
            if wtype not in ('Frame', 'Labelframe'):
                child.configure(state='normal')
            else:
                self.enableChildren(child)

    def LOG_DEBUG(self, bEnable, message):
        if bEnable:
            print(message)

    def disableAllLogingPrints(self):
        sys.stdout = open(os.devnull, 'w')

    # Restore
    def enableAllLogingPrints(self):
        sys.stdout = sys.__stdout__

    def get_authorNames(self):
        print("get_authorNames--> Start for item name: ")
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        result_query = cursor.execute("SELECT author_Name FROM author")
        result = cursor.fetchall()
        conn.close()
        return result

    def get_centerNames(self):
        print("get_centerNames--> Start ")
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        result_query = cursor.execute("SELECT merchandise_Name FROM merchandise")
        result = cursor.fetchall()
        conn.close()
        return result

    def logActivity(self, activity_details):
        print("logging Activity --> ")
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        now = datetime.now()
        hostname = socket.gethostname()
        ipaddress = socket.gethostbyname(socket.gethostname())

        dateForLogging = now.strftime("%d-%b-%Y")
        timeForLogging = now.strftime("%H-%M-%S")
        username = CurrentUser.get_instance().getCurrentUser()
        sql = "INSERT INTO activity_logs VALUES(%s,%s,%s,%s,%s,%s)"
        values = (dateForLogging,timeForLogging,hostname,ipaddress,username,activity_details)
        cursor.execute(sql, values)

        conn.commit()
        conn.close()
        print("Activity Logged !!! ")

    def setCurrentUser(self, userName):
        print("Store user as current user :", userName)
        self.currentUser = userName

    def getCurrentUser(self):
        return self.currentUser
