"""
# Copyright 2020 by Vihangam Yoga Karnataka.
# All rights reserved.
# This file is part of the Vihangan Yoga Operations of Ashram Management Software Package(VYOAM),
# and is released under the "VY License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
# Vihangan Yoga Operations  of Ashram Management Software
# File Name : app_common.py
# Developer : Sant Anurag Deo
# Version : 2.0
"""

from app_defines import *
import MySQLdb as sql_db


class CommonUtil:

    def __init__(self):
        print("constructor called for CommonUtil edit ")
        self._new_member_id = 0
        self.currentUser = ""

    def totalrecords_excelDataBase(self, path):
        # to open the workbook
        # workbook object is created
        wb_obj = openpyxl.load_workbook(path)
        sheet_obj = wb_obj.active

        # print the total number of rows
        return sheet_obj.max_row - 1

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
        # self.change_permissions_recursive(src_folder, 0o777)
        # self.change_permissions_recursive(destination_copy_folder,0o777)

    def donothing(self, event=None):
        print("Button is disabled")
        pass

    def fetchRecordsfromExcel(self, startRow_index, NoOfColumns, filename, reqNoOfRecords):
        wb_obj = openpyxl.load_workbook(filename)
        wb_sheet = wb_obj.active
        record_list = []
        for row_index in range(startRow_index, (startRow_index + reqNoOfRecords + 1)):
            arr_InvoiceRecords = []
            for column_index in range(1, NoOfColumns):
                arr_InvoiceRecords.append(wb_sheet.cell(row=row_index, column=column_index).value)
            record_list.append(arr_InvoiceRecords)
        return record_list

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

    def sortExcelSheetByDate(self, src_file, dest_file):
        x = datetime.now()
        print("started at :", x)
        df = pd.read_excel(src_file)

        df['Date'] = pd.to_datetime(df['Date']).dt.date
        df.sort_values(['Date'], axis=0, ascending=True, inplace=True)
        df.to_excel(dest_file, index=False)
        y = datetime.now()
        print("Sorting finished in :", y - x)

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

    def updateInvoiceTable(self, invoice_id, invoice_path):

        print("updateInvoiceTable -->start")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Invoices"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Invoices.xlsx"

        wb_obj = openpyxl.load_workbook(path)
        wb_sheet = wb_obj.active
        total_records = self.totalrecords_excelDataBase(path)
        wb_sheet.cell(row=total_records + 2, column=1).value = str(total_records + 1)
        wb_sheet.cell(row=total_records + 2, column=2).value = str(invoice_id)
        wb_sheet.cell(row=total_records + 2, column=3).value = str(invoice_path)
        wb_obj.save(path)
        print("Invoice table updated")

    def updateMonetaryDonationReceiptBooklet(self, invoice_id, trustType):
        print("updateInvoiceTable -->start")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Receipts\\Template"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)

        if trustType == VIHANGAM_YOGA_KARNATAKA_TRUST:
            path = dirname + "\\Donation_Receipt_Booklet.xlsx"
        if trustType == SADGURU_SADAFAL_AADARSH_GAUSHALA_TRUST:
            path = dirname + "\\Gaushala_Donation_Receipt_Booklet.xlsx"

        wb_obj = openpyxl.load_workbook(path)
        wb_sheet = wb_obj.active
        total_records = self.totalrecords_excelDataBase(path)
        wb_sheet.cell(row=total_records + 2, column=1).value = str(total_records + 1)
        wb_sheet.cell(row=total_records + 2, column=2).value = str(invoice_id)
        wb_obj.save(path)
        print("Receipt booklet updated")

    def updateExpanseVoucherReceiptBooklet(self, invoice_id, trustType):
        print("updateExpanseVoucherReceiptBooklet -->start")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Expanse\\Receipts\\Template"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)

        if trustType == VIHANGAM_YOGA_KARNATAKA_TRUST:
            path = dirname + "\\Ashram_Expanse_Voucher_Receipt_Booklet.xlsx"
        if trustType == SADGURU_SADAFAL_AADARSH_GAUSHALA_TRUST:
            path = dirname + "\\Gaushala_Expanse_Voucher_Receipt_Booklet.xlsx"

        wb_obj = openpyxl.load_workbook(path)
        wb_sheet = wb_obj.active
        total_records = self.totalrecords_excelDataBase(path)
        wb_sheet.cell(row=total_records + 2, column=1).value = str(total_records + 1)
        wb_sheet.cell(row=total_records + 2, column=2).value = str(invoice_id)
        wb_obj.save(path)
        print("Expanse Voucher booklet updated")

    def generateMonetaryDonationReceiptId(self, trustType):
        print("updateInvoiceTable -->start")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Receipts\\Template"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        if trustType == VIHANGAM_YOGA_KARNATAKA_TRUST:
            path = dirname + "\\Donation_Receipt_Booklet.xlsx"
            temp_str = "RV-"
        else:
            path = dirname + "\\Gaushala_Donation_Receipt_Booklet.xlsx"
            temp_str = "GRV-"

        wb_obj = openpyxl.load_workbook(path)
        wb_sheet = wb_obj.active
        total_records = self.totalrecords_excelDataBase(path)
        if len(str(total_records + 1)) == 1:
            temp_id = "00" + str(total_records + 1)
        elif len(str(total_records + 1)) == 2:
            temp_id = "0" + str(total_records + 1)
        else:
            temp_id = ""
        return temp_str + temp_id

    def encryptDatabase(self):
        print(" Encrypting Database !!!!!")
        today = datetime.now()
        year = today.strftime("%Y")
        for index in range(0, 5):
            if index == 0:
                directory = "..\\Expanse_data\\"
            elif index == 1:
                directory = "..\\Library_Stock\\"
            elif index == 2:
                directory = "..\\Member_Data\\"
            elif index == 3:
                directory = "..\\Staff_Data\\"
            elif index == 4:
                directory = "..\\Common_Files\\"
            else:
                pass
            for subdir, dirs, files in os.walk(directory):
                for filename in files:
                    if filename.find('.xlsx') > 0:
                        filePath = os.path.join(subdir, filename)  # get the path to your file
                        newFilePath = filePath.replace(".xlsx", ".vyoamd")  # create the new name
                        # print("directory :", directory, "filePath :", filePath, "newFilePath :", newFilePath)
                        os.rename(filePath, newFilePath)  # rename your file

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

    def addTrustName(self, trustName):
        print("addTrustName -->start")
        dirname = "..\\Config"
        subdir = "..\\Config\\Trust"
        if not os.path.exists(dirname):
            print("Config directory not available, hence building one")
            os.makedirs(dirname)
        if not os.path.exists(subdir):
            print("Config directory not available, hence building one")
            os.makedirs(subdir)

        path = dirname + "\\Trust_name.txt"

        infile = open(path, 'a')
        content = trustName + "\n"
        infile.write(content)
        infile.close()
        print("addTrustName -->end")

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

    def setCurrentUser(self, userName):
        print("Store user as current user :", userName)
        self.currentUser = userName

    def getCurrentUser(self):
        return self.currentUser
