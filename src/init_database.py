"""
# Copyright 2020 by Vihangam Yoga Karnataka.
# All rights reserved.
# This file is part of the Vihangan Yoga Operations of Ashram Management Software Package(VYOAM),
# and is released under the "VY License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
# Vihangan Yoga Operations  of Ashram Management Software
# File Name : init_database.py
# Developer : Sant Anurag Deo
# Version : 2.0
"""

from tkinter import *
from app_defines import *
from app_common import *


class InitDatabase:
    # constructor for Library class
    __instance = None

    # staticmethod
    def getInstance():
        """ Static access method. """
        if InitDatabase.__instance == None:
            InitDatabase()
        return InitDatabase.__instance

    def __init__(self):
        print("constructor called for Database initilization called ")
        """ Virtually private constructor. """
        if InitDatabase.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            InitDatabase.__instance = self

        self.obj_commonUtil = CommonUtil()
        self.seva_deposit_database_name = ""
        self.expanse_database_name = ""
        self.advance_database_name = ""
        self.transaction_database_name = ""
        self.non_monetarydonation_database_name = ""
        self.akshay_patra_database_name = ""
        self.magazine_subscription_database_name = ""
        self.monthly_seva_database_name = ""
        self.gaushala_seva_database_name = ""
        self.hawan_seva_database_name = ""
        self.prachar_event_seva_database_name = ""
        self.aarti_seva_database_name = ""
        self.ashram_seva_database_name = ""
        self.yoga_seva_database_name = ""
        self.ashram_nirmaan_seva_database_name = ""
        self.sortedseva_deposit_database_name = ""
        self.sortedakshay_patra_database_name = ""
        self.sortedashramnirmaan_seva_database_name = ""
        self.sortedyoga_seva_database_name = ""
        self.sortedashram_seva_database_name = ""
        self.sortedaarti_seva_database_name = ""
        self.sortedprachar_event_database_name = ""
        self.sortedhawan_database_name = ""
        self.sortedgaushala_database_name = ""
        self.sortedmonthly_database_name = ""
        self.sorted_purchase_record_database_name = ""
        self.statement_desktop_directory_path_name = ""
        self.statement_template_path_name = ""
        self.sortedtransaction_database_name = ""
        self.splittransaction_database_name = ""
        self.invoices_database_name = ""
        self.software_statement_directory_name = ""
        self.invoice_directory_name = ""
        self.donation_receipt_booklet_name = ""
        self.magazine_distribution_database_name = ""
        self.gaushala_invoice_name = ""
        self.gaushala_expanse_database_name = ""
        self.gaushala_transaction_database_name = ""
        self.gaushala_donation_receipt_booklet_name = ""
        self.gaushala_expanse_voucher_booklet_name = ""
        self.ashram_expanse_voucher_booklet_name = ""
        self.current_year_pledge_payment_database_name = ""

    def initilizealldatabase(self):
        #self.initilize_stock_database()
        self.initilize_member_database()
        self.initilize_staff_database()
        self.initilize_critical_stock_database()
        #self.initilize_non_commercial_database()
        self.initilize_new_directories()

        # new databases -start
        self.initilize_current_year_seva_deposit_database()
        self.initilize_current_year_Expanse_database()
        self.initilize_current_year_Advance_database()
        self.initilize_current_year_Transaction_database()
        #self.initilize_non_monetary_donation_database()
        self.initilize_current_year_akshay_patra_database()
        self.initilize_current_year_purchase_record_database()
        self.initilize_current_year_magazine_subscription_database()
        self.initilize_current_year_monthly_seva_database()
        self.initilize_current_year_gaushala_seva_database()
        self.initilize_current_year_hawan_seva_database()
        self.initilize_current_year_prachar_event_seva_database()
        self.initilize_current_year_aarti_seva_database()
        self.initilize_current_year_ashram_seva_database()
        self.initilize_current_year_yoga_seva_database()
        self.initilize_current_year_ashram_Nirmaan_seva_database()
        self.initilize_statements_repo()
        self.initilize_current_year_SplitTransaction_database()
        self.initilize_invoice_database()
        self.initilize_software_statement_directory()
        self.initilize_receipt_booklet()
        self.initilize_magazine_distribution_database()
        self.initilize_current_year_gaushala_Expanse_database()
        self.initilize_current_year_Gaushala_Transaction_database()
        self.initilize_gaushala_receipt_booklet()
        self.initilize_gaushala_expanse_voucher_booklet()
        self.initilize_ashram_expanse_voucher_receipt_booklet()
        #  new databases -end

    def initilize_statements_repo(self):
        print("initilize_statements_repo")
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        print("The Desktop path is: " + desktop)

        dirname = desktop + "\\VYOAM\\Statements"
        templates = desktop + "\\VYOAM\\Invoices"
        self.statement_desktop_directory_path_name = dirname
        self.statement_template_path_name = templates
        if not os.path.exists(dirname):
            print("Statements ready")
            os.makedirs(dirname)
        if not os.path.exists(templates):
            print("Statement Template")
            os.makedirs(templates)

    def get_desktop_statement_directory_path(self):
        return self.statement_desktop_directory_path_name

    def get_desktop_invoices_directory_path(self):
        return self.statement_template_path_name

    def initilize_current_year_seva_deposit_database(self):
        print("initilize_current_year_seva_deposit_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Monetary_Donation.xlsx"
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id', 'Bank ref id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Seva deposit !! Initialization not required ")
        self.seva_deposit_database_name = path

    def get_seva_deposit_database_name(self):
        return self.seva_deposit_database_name

    def initilize_current_year_Expanse_database(self):
        print("initilize_current_year_seva_deposit_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Expanse"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Expanse.xlsx"

        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.No', 'Expanse Amt.(Rs.)', 'Description', 'Receiver (ID)', 'Receiver Name', 'Date',
                            'Authorizor ID', 'Authorizor Name', 'Mode of Payment',
                            'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J']
            for iLoop in range(1, 10):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['H'].width = 40
            wb.save(path)
            print(" Database for Expanse created successfully ")
        else:
            print(" Database already exists for Expanse !! Initialization not required ")
        self.expanse_database_name = path

    def get_expanse_database_name(self):
        return self.expanse_database_name

    def initilize_current_year_gaushala_Expanse_database(self):
        print("initilize_current_year_gaushala_Expanse_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Expanse"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Gaushala_Expanse.xlsx"

        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.No', 'Expanse Amt.(Rs.)', 'Description', 'Receiver (ID)', 'Receiver Name', 'Date',
                            'Authorizor ID', 'Authorizor Name', 'Mode of Payment',
                            'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J']
            for iLoop in range(1, 10):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['H'].width = 40
            wb.save(path)
            print(" Database for Gaushala Expanse created successfully ")
        else:
            print(" Database already exists for gaushala Expanse !! Initialization not required ")
        self.gaushala_expanse_database_name = path

    def get_gaushala_expanse_database_name(self):
        return self.gaushala_expanse_database_name

    def initilize_current_year_Advance_database(self):
        print("initilize_current_year_seva_deposit_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Expanse"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Advance.xlsx"
        # path = PATH_ADVANCE_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.No', 'Date', 'Advance Amt.(Rs.)', 'Balance', 'Description', 'Receiver (ID)',
                            'Receiver Name',
                            'Authorizor ID', 'Authorizor Name', 'Mode of Payment', 'Advance Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'H', 'I']
            for iLoop in range(1, 12):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['E'].width = 40
            wb.save(path)
            print(" Database for Advance amount created successfully ")
        else:
            print(" Database already exists for Advance amount !! Initialization not required ")
        self.advance_database_name = path

    def get_advance_database_name(self):
        return self.advance_database_name

    def initilize_current_year_Transaction_database(self):
        print("initilize_current_year_Transaction_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Transaction"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Transaction.xlsx"
        # path = PATH_TRANSACTION_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.No', 'Date', 'Credit Amt.(Rs.)', 'Debit Amt.(Rs)', 'Description', 'Mode of Transaction',
                            'Transaction By(Id)', 'Transaction By(Name)', 'Balance (Rs.)', 'Invoice ID']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K']
            for iLoop in range(1, 11):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['E'].width = 40
            wb.save(path)
            print(" Database for Transaction initialized successfully ")
        else:
            print(" Database already exists for Transaction !! Initialization not required ")
        self.transaction_database_name = path

    def initilize_current_year_Gaushala_Transaction_database(self):
        print("initilize_current_year_Gaushala_Transaction_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Transaction"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Gaushala_Transaction.xlsx"
        # path = PATH_TRANSACTION_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.No', 'Date', 'Credit Amt.(Rs.)', 'Debit Amt.(Rs)', 'Description', 'Mode of Transaction',
                            'Transaction By(Id)', 'Transaction By(Name)', 'Balance (Rs.)', 'Invoice ID']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K']
            for iLoop in range(1, 11):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['E'].width = 40
            wb.save(path)
            print(" Database for gaushala Transaction initialized successfully ")
        else:
            print(" Database already exists for Gaushala Transaction !! Initialization not required ")
        self.gaushala_transaction_database_name = path

    def get_gaushala_transaction_database_name(self):
        return self.gaushala_transaction_database_name

    def initilize_current_year_SplitTransaction_database(self):
        print("initilize_current_year_SplitTransaction_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Transaction"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Split_Transaction.xlsx"
        # path = PATH_TRANSACTION_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.No', 'Date', 'Amount.(Rs.)', 'Split Status', 'Description', 'Mode of Transaction',
                            'Transaction By(Id)', 'Transaction By(Name)', 'Balance (Rs.)', 'Invoice ID']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            for iLoop in range(1, 11):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['E'].width = 40
            wb.save(path)
            print(" Database for Split Transaction initialized successfully ")
        else:
            print(" Database already exists for Split Transaction !! Initialization not required ")
        self.splittransaction_database_name = path

    def get_transaction_database_name(self):
        return self.transaction_database_name

    def get_splittransaction_database_name(self):
        return self.splittransaction_database_name

    def initilize_non_monetary_donation_database(self):
        print("initilize_current_year_non_monetary_donation_database")
        path = PATH_NON_MONETARY_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Inventory ID', 'Item Name', 'Quantity', 'Est. Value(Rs)', 'Donator Id',
                            'Donator Name', 'Address',
                            'Date',
                            'Receiver Id', 'Receiver Name', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['G'].width = 40
            wb.save(path)
            print(" Database for Non Monetary donation Initialization success ")
        else:
            print(" Database already exists for Non Monetary !! Initialization not required ")
        self.non_monetarydonation_database_name = path

    def get_nonmonetary_database_name(self):
        return self.non_monetarydonation_database_name

    def initilize_current_year_akshay_patra_database(self):
        print("initilize_current_year_akshay_patra_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Akshay_patra.xlsx"
        # path = PATH_AKSHAY_PATRA_DATABASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Akshay Patra(No.)',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id', 'Bank ref id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['F'].width = 40
            wb.save(path)
            print(" Database for Akshay Patra Initialization success ")
        else:
            print(" Database already exists for Akshay Patra !! Initialization not required ")
        self.akshay_patra_database_name = path

    def get_akshay_patra_database_name(self):
        return self.akshay_patra_database_name

    def initilize_current_year_purchase_record_database(self):
        print("initilize_current_year_purchase_record_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Transaction\\StockSell"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Purchase_Transaction.xlsx"
        self.purchase_record_database_name = path
        # path = PATH_PURCHASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Member Id', 'Member Name', 'Book Id', 'Book Name', 'Date',
                            'Paid Amount(Rs.)', 'Balance', 'Invoice Id', 'Quantity']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K']
            for iLoop in range(1, 11):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path)
            print(" Database template ready purchase transactions ")
        else:
            print(" Database already exists forPurchase transactions!! Initialization not required ")

    def get_purchase_record_database_name(self):
        return self.purchase_record_database_name

    def initilize_invoice_database(self):
        print("initilize_invoice_databse -->start")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Invoices"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Invoices.xlsx"
        gaushala_invoice = dirname + "\\Gaushala_Invoices.xlsx"
        self.invoices_database_name = path
        self.invoice_directory_name = dirname
        self.gaushala_invoice_name = gaushala_invoice
        # path = PATH_PURCHASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Invoice_Id', 'Path']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D']
            for iLoop in range(1, 4):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 25
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center',
                                                                      wrapText=True)
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['C'].width = 50
            wb.save(path)
            print(" Database template ready initilize_invoice_database ")
        else:
            print(" Database already exists for initilize_invoice_database!! Initialization not required ")

        # for gaushala
        if not os.path.isfile(gaushala_invoice):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Invoice_Id', 'Path']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D']
            for iLoop in range(1, 4):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 25
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center',
                                                                      wrapText=True)
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['C'].width = 50
            wb.save(gaushala_invoice)
            print(" Database template ready initilize_gaushala invoice_database ")
        else:
            print(" Database already exists for initilize_gaushala_invoice_database!! Initialization not required ")

    def get_invoice_database_name(self):
        return self.invoices_database_name

    def get_gaushala_invoice_database_name(self):
        return self.gaushala_invoice_name

    def initilize_receipt_booklet(self):
        print("initilize_receipt_booklet -->start")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Receipts\\Template"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Donation_Receipt_Booklet.xlsx"
        self.donation_receipt_booklet_name = path

        # path = PATH_PURCHASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'RV_Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C']
            for iLoop in range(1, 3):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 25
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center',
                                                                      wrapText=True)
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path)
            print(" initilize_receipt_booklet success ")
        else:
            print(" initilize_receipt_booklet already done!! Initialization not required ")

    def get_receipt_booklet_path(self):
        return self.donation_receipt_booklet_name

    def initilize_gaushala_receipt_booklet(self):
        print("initilize_gaushala_receipt_booklet -->start")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Receipts\\Template"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Gaushala_Donation_Receipt_Booklet.xlsx"
        self.gaushala_donation_receipt_booklet_name = path

        # path = PATH_PURCHASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'RV_Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C']
            for iLoop in range(1, 3):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 25
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center',
                                                                      wrapText=True)
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path)
            print(" initilize_gaushala_receipt_booklet success ")
        else:
            print(" initilize_gaushala_receipt_booklet already done!! Initialization not required ")

    def get_gaushala_receipt_booklet_path(self):
        return self.gaushala_donation_receipt_booklet_name

    def initilize_ashram_expanse_voucher_receipt_booklet(self):
        print("initilize_ashram_expanse_voucher_receipt_booklet -->start")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Expanse\\Receipts\\Template"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Ashram_Expanse_Voucher_Receipt_Booklet.xlsx"
        self.ashram_expanse_voucher_booklet_name = path

        # path = PATH_PURCHASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'RV_Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C']
            for iLoop in range(1, 3):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 25
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center',
                                                                      wrapText=True)
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path)
            print(" initilize_ashram_expanse_voucher_receipt_booklet success ")
        else:
            print(" initilize_ashram_expanse_voucher_receipt_booklet already done!! Initialization not required ")

    def get_ashram_expanse_voucher_booklet_path(self):
        return self.ashram_expanse_voucher_booklet_name

    def initilize_gaushala_expanse_voucher_booklet(self):
        print("initilize_gaushala_receipt_booklet -->start")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Expanse\\Receipts\\Template"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Gaushala_Expanse_Voucher_Receipt_Booklet.xlsx"
        self.gaushala_expanse_voucher_booklet_name = path

        # path = PATH_PURCHASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'RV_Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C']
            for iLoop in range(1, 3):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 25
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center',
                                                                      wrapText=True)
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path)
            print(" initilize_gaushala_expanse_voucher_booklet success ")
        else:
            print(" initilize_gaushala_expanse_voucher_booklet already done!! Initialization not required ")

    def gaushala_expanse_voucher_booklet_name(self):
        return self.gaushala_expanse_voucher_booklet_name

    def get_invoice_directory_name(self):
        return self.invoice_directory_name

    def initilize_software_statement_directory(self):
        print("initilize_statement_directory -->start")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Statements"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        print("initilize_statement_directory -->end")
        self.software_statement_directory_name = dirname

    def get_software_statement_directory_name(self):
        return self.software_statement_directory_name

    def initilize_sorted_purchase_record_database(self):
        print("initilize_current_year_sorted_purchase_record_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Transaction\\StockSell\\Sorted"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Purchase_Transaction.xlsx"
        self.sorted_purchase_record_database_name = path
        # path = PATH_PURCHASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Member Id', 'Member Name', 'Book Id', 'Book Name', 'Date',
                            'Paid Amount(Rs.)', 'Balance', 'Invoice Id', 'Quantity']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K']
            for iLoop in range(1, 11):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path)
            print(" initilize_current_year_sorted_purchase_record_database success ")
        else:
            print(" Database already exists forPurchase transactions!! Initialization not required ")

    def get_sorted_purchase_record_database(self):
        return self.sorted_purchase_record_database_name

    def initilize_current_year_magazine_subscription_database(self):
        print("initilize_current_year_magazine_subscription_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Magazine_Subscription"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Subscription.xlsx"
        # path = PATH_MAGAZINE_SUBSCRIPTION_DATABASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Member Id', 'Member Name', 'Date', 'Magazine Name', 'Quantity',
                            'Paid Amount(Rs.)', 'Mailing Address', 'Collected By(ID)', 'Collector Name', 'Payment Mode',
                            'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
            for iLoop in range(1, 13):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['H'].width = 40
            wb.save(path)
            print(" Database template ready magazine subscription ")
        else:
            print(" Database already exists for Magazine Subscription!! Initialization not required ")
        self.magazine_subscription_database_name = path

    def get_magazine_subscription_database_name(self):
        return self.magazine_subscription_database_name

    def initilize_magazine_distribution_database(self):
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Magazine_Subscription\\Subscriber_Data"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\" + "Magazine_Distribution.xlsx"

        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Member Id', 'January', 'February', 'March', 'April',
                            'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path)
            print("initilize_magazine_distribution_database finished ")
        else:
            print(" Database already exists for Magazine Distribution!! Initialization not required ")
        self.magazine_distribution_database_name = path

    def get_magazine_distribution_database_name(self):
        return self.magazine_distribution_database_name

    def initilize_current_year_monthly_seva_database(self):
        print("initilize_current_year_monthly_seva_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Monthly_Donation.xlsx"
        self.monthly_seva_database_name = path
        # path = PATH_MONTHLY_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id', 'Bank ref id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Monthly Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Monthly Seva deposit !! Initialization not required ")

    def get_monthly_seva_database_name(self):
        print("get_monthly_seva_database_name --> Path :", self.monthly_seva_database_name)
        return self.monthly_seva_database_name

    def initilize_current_year_gaushala_seva_database(self):
        print("initilize_current_year_monthly_seva_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Gaushala_Donation.xlsx"

        # path = PATH_GAUSHALA_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id', 'Bank ref id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Monthly Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Monthly Seva deposit !! Initialization not required ")
        self.gaushala_seva_database_name = path

    def get_gaushala_seva_database_name(self):
        return self.gaushala_seva_database_name

    def initilize_current_year_hawan_seva_database(self):
        print("initilize_current_year_hawan_seva_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Hawan_Donation.xlsx"
        # path = PATH_HAWAN_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id', 'Bank ref id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" initilize_current_year_hawan_seva_database successfully ")
        else:
            print(" Database already exists for Hawan Seva deposit !! Initialization not required ")
        self.hawan_seva_database_name = path

    def get_hawan_seva_database_name(self):
        return self.hawan_seva_database_name

    def initilize_current_year_prachar_event_seva_database(self):
        print("initilize_current_year_prachar_event_seva_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Event_prachar_Donation.xlsx"
        # path = PATH_EVENT_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id', 'Bank ref id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" initilize_current_year_prachar_event_seva_database successfully ")
        else:
            print(" Database already exists for Event Seva deposit !! Initialization not required ")
        self.prachar_event_seva_database_name = path

    def get_prachar_event_seva_database_name(self):
        return self.prachar_event_seva_database_name

    def initilize_current_year_aarti_seva_database(self):
        print("initilize_current_year_aarti_seva_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Aarti_Donation.xlsx"
        # path = PATH_AARTI_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id', 'Bank ref id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" initilize_current_year_aarti_seva_database initialized successfully ")
        else:
            print(" Database already exists for Arti Seva deposit !! Initialization not required ")
        self.aarti_seva_database_name = path

    def get_aarti_seva_database_name(self):
        return self.aarti_seva_database_name

    def initilize_current_year_ashram_seva_database(self):
        print("initilize_current_year_ashram_seva_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Ashram_Generic_Donation.xlsx"
        # path = PATH_ASHRAM_GENERIC_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id', 'Bank ref id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" initilize_current_year_ashram_seva_database initialized successfully ")
        else:
            print(" Database already exists for Ashram Generic Seva!! Initialization not required ")
        self.ashram_seva_database_name = path

    def get_ashram_seva_database_name(self):
        return self.ashram_seva_database_name

    def initilize_current_year_yoga_seva_database(self):
        print("initilize_current_year_yoga_seva_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Yoga_Fees_Donation.xlsx"
        # path = PATH_YOGA_FEES_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id', 'Bank ref id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" initilize_current_year_yoga_seva_database initialized successfully ")
        else:
            print(" Database already exists for Yoga Seva deposit !! Initialization not required ")
        self.yoga_seva_database_name = path

    def get_yoga_seva_database_name(self):
        return self.yoga_seva_database_name

    def initilize_current_year_ashram_Nirmaan_seva_database(self):
        print("initilize_current_year_ashram_Nirmaan_seva_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Ashram_Nirmaan_Donation.xlsx"
        # path = PATH_YOGA_FEES_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id', 'Bank ref id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 15):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" initilize_current_year_ashram_Nirmaan_seva_database initialized successfully ")
        else:
            print(" Database already exists for Yoga Seva deposit !! Initialization not required ")
        self.ashram_nirmaan_seva_database_name = path

    def get_ashram_nirmaan_seva_database_name(self):
        return self.ashram_nirmaan_seva_database_name

    def initilize_member_database(self):
        path = PATH_MEMBER
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Member Id', 'National Identifier', 'Name', 'Father Name', 'Mother Name',
                            'Date of Birth', 'Gender', 'Address',
                            'City', 'State', 'Pincode', 'Contact no.', 'Country', 'Nationality', 'Email-Id',
                            'Member photo Path', 'Id photo path', 'ID Type', 'Associated Since', 'Profession',
                            'Updestha', 'Practicing Level', 'Designation', 'Has Akshay Patra?', 'Akshay Patra No.',
                            'Patrika Subscribed?', 'Akshay Patra Allocation Date']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC']
            for iLoop in range(1, MAX_RECORD_ENTRY):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='00CCFFFF')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['I'].width = 40
            wb.save(path)
            print(" Database for Member Initialization success ")
        else:
            print(" Database already exists for Member !! Initialization not required ")

    def initilize_stock_database(self):
        dirname = "..\\Library_Stock\\Commercial_Stock\\"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = PATH_STOCK
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Book Id', 'Name', 'Author Name', 'Price', 'Borrow Fee',
                            'Quantity', 'Rack Number', 'Stock Receival Date', 'Center Name']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            for iLoop in range(1, 11):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['H'].width = 40
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Stock Initialization success ")
        else:
            print(" Database already exists for Library stock !! Initialization not required ")

    def initilize_non_monetary_donation_database(self):
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Library_Stock\\NonMonetary_Donation\\"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = PATH_NON_MONETARY_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Item Name', 'Quantity', 'Est. Value(Rs)', 'Donator Id', 'Donator Name', 'Address',
                            'Date',
                            'Receiver Id', 'Receiver Name', 'Authorizor ID', 'Authorizor Name', 'Invoice Id',
                            'Owner Type']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['G'].width = 40
            wb.save(path)
            print(" Database for Non Monetary donation Initialization success ")
        else:
            print(" Database already exists for Non Monetary !! Initialization not required ")

    def initilize_critical_stock_database(self):
        path = "..\\Library_Stock\\Critical_Stock.xlsx"
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Book Id', 'Name', 'Author Name', 'Quantity']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E']
            for iLoop in range(1, 6):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['H'].width = 40
            wb.save(path)
            print(" Database for Critical Initialization success ")
        else:
            print(" Database already exists for critical_stock !! Initialization not required ")

    def initilize_staff_database(self):
        # prepare main staff record database
        path = "..\\Staff_Data\\Staff.xlsx"
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Member Id', 'National Identifier', 'Name', 'Father Name', 'Mother Name',
                            'Date of Birth',
                            'Gender', 'Address',
                            'City', 'State', 'Pincode', 'Contact no.', 'Country', 'Nationality', 'Email-Id',
                            'Member photo Path', 'Id photo path', 'ID Type']

            # preparing the top headers of the excel sheet.
            excel_cell = {}

            sheet.row_dimensions[1].height = 20
            sheet.column_dimensions['H'].width = 40
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T']
            for iLoop in range(1, 20):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path)
            print(" Database for Staff Initialization success ")
        else:
            print(" Database already exists for Staff !! Initialization not required ")

        # prepare main staff-login record database
        path_staff_credentials = "..\\Staff_Data\\Staff_credentials.xlsx"
        if not os.path.isfile(path_staff_credentials):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Member Id', 'Password']
            excel_cell = {}

            sheet.row_dimensions[1].height = 20
            sheet.column_dimensions['H'].width = 40
            alphabet_dict = ['A', 'B', 'C']
            for iLoop in range(1, 4):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path_staff_credentials)
            print(" Database for Staff Credentials Initialization success ")
        else:
            print(" Database already exists for Staff credentials !! Initialization not required ")

    def initilize_Expanse_database(self):
        path = PATH_EXPANSE_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.No', 'Expanse Amt.(Rs.)', 'Description', 'Receiver (ID)', 'Receiver Name', 'Date',
                            'Authorizor ID', 'Authorizor Name', 'Mode of Payment',
                            'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J']
            for iLoop in range(1, 10):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['H'].width = 40
            wb.save(path)
            print(" Database for Expanse created successfully ")
        else:
            print(" Database already exists for Expanse !! Initialization not required ")

    def initilize_Advance_database(self):
        path = PATH_ADVANCE_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.No', 'Date', 'Advance Amt.(Rs.)', 'Balance', 'Description', 'Receiver (ID)',
                            'Receiver Name',
                            'Authorizor ID', 'Authorizor Name', 'Mode of Payment', 'Advance Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'H', 'I']
            for iLoop in range(1, 12):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['E'].width = 40
            wb.save(path)
            print(" Database for Advance amount created successfully ")
        else:
            print(" Database already exists for Advance amount !! Initialization not required ")

    def initilize_Transaction_database(self):
        path = PATH_TRANSACTION_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.No', 'Date', 'Credit Amt.(Rs.)', 'Debit Amt.(Rs)', 'Description', 'Mode of Transaction',
                            'Transaction By(Id)', 'Transaction By(Name)', 'Balance (Rs.)']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J']
            for iLoop in range(1, 10):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['E'].width = 40
            wb.save(path)
            print(" Database for Transaction initialized successfully ")
        else:
            print(" Database already exists for Transaction !! Initialization not required ")

    def initilize_non_commercial_database(self):
        dirname = "..\\Library_Stock\\NonCommercial_Stock\\"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = PATH_NON_COMMERCIAL_STOCK
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Inventory ID', 'Item Name', 'Quantity', 'Est. Value(Rs)', 'Donator Id',
                            'Donator Name', 'Address',
                            'Date',
                            'Receiver Id', 'Receiver Name', 'Authorizor ID', 'Authorizor Name', 'Invoice Id',
                            'Owner Type', 'Rack No.', 'Center Name']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']
            for iLoop in range(1, 18):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['G'].width = 30
            wb.save(path)
            print(" Database for initilize_non_commercial_database success ")
        else:
            print(" Database already exists for non_commercial !! Initialization not required ")

    def initilize_member_borrow_database(self, path):
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Member Id', 'Member Name', 'Book Id', 'Book Name', 'Date of borrow',
                            'Date of Return', 'Paid Fee']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            for iLoop in range(1, 9):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path)
            print(" Database template ready for member ")
        else:
            print(" Database already exists for Library stock !! Initialization not required ")

    def initilize_purchase_record_database(self):
        path = PATH_PURCHASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Member Id', 'Member Name', 'Book Id', 'Book Name', 'Date of Purchase',
                            'Paid Amount(Rs.)', 'Balance', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J']
            for iLoop in range(1, 10):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            wb.save(path)
            print(" Database template ready purchase transactions ")
        else:
            print(" Database already exists forPurchase transactions!! Initialization not required ")

    def initilize_seva_deposit_database(self):
        path = PATH_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Seva deposit !! Initialization not required ")

    def initilize_monthly_seva_database(self):
        path = PATH_MONTHLY_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Monthly Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Monthly Seva deposit !! Initialization not required ")

    def initilize_gaushala_seva_database(self):
        path = PATH_GAUSHALA_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Monthly Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Monthly Seva deposit !! Initialization not required ")

    def initilize_hawan_seva_database(self):
        path = PATH_HAWAN_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Hawan Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Hawan Seva deposit !! Initialization not required ")

    def initilize_prachar_event_seva_database(self):
        path = PATH_EVENT_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Event\Prachar deposit initialized successfully ")
        else:
            print(" Database already exists for Event Seva deposit !! Initialization not required ")

    def initilize_aarti_seva_database(self):
        path = PATH_AARTI_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Aarti Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Arti Seva deposit !! Initialization not required ")

    def initilize_ashram_seva_database(self):
        path = PATH_ASHRAM_GENERIC_SEVA_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Ashram Generic Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Ashram Generic Seva!! Initialization not required ")

    def initilize_yoga_seva_database(self):
        path = PATH_YOGA_FEES_SHEET
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Yoga fees deposit initialized successfully ")
        else:
            print(" Database already exists for Yoga Seva deposit !! Initialization not required ")

    def initilize_akshay_patra_database(self):
        path = PATH_AKSHAY_PATRA_DATABASE
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Akshay Patra(No.)',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['F'].width = 40
            wb.save(path)
            print(" Database for Akshay Patra Initialization success ")
        else:
            print(" Database already exists for Akshay Patra !! Initialization not required ")

    def initilize_sortedmonthly_seva_database(self):
        print("initilize_sortedmonthly_seva_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Monthly_Donation.xlsx"
        # path = PATH_SORTEDMONTHLY_SEVA_SHEET
        self.sortedmonthly_database_name = path
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 15):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['F'].width = 40
        wb.save(path)
        print(" Database for Sorted Monthly Seva deposit initialized successfully ")

    def get_sortedmonthly_database_name(self):
        return self.sortedmonthly_database_name

    def initilize_sortedmonthly_seva_databasepast(self, year):
        print("initilize_sortedmonthly_seva_database")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Monthly_Donation.xlsx"
        # path = PATH_SORTEDMONTHLY_SEVA_SHEET
        self.sortedmonthly_database_name = path
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 15):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['F'].width = 40
        wb.save(path)
        print(" Database for Sorted Monthly Seva deposit initialized successfully ")

    def initilize_sortedgaushala_seva_database(self):
        print("initilize_sortedgaushala_seva_database ")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Gaushala_Donation.xlsx"
        # path = PATH_SORTEDGAUSHALA_SEVA_SHEET
        self.sortedgaushala_database_name = path
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Monthly Seva deposit initialized successfully ")

    def get_sortedgaushala_database_name(self):
        return self.sortedgaushala_database_name

    def initilize_sortedgaushala_seva_databasepast(self, year):
        print("initilize_sortedgaushala_seva_database past")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("past year is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Gaushala_Donation.xlsx"
        # path = PATH_SORTEDGAUSHALA_SEVA_SHEET
        self.sortedgaushala_database_name = path
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Monthly Seva deposit initialized successfully ")

    def initilize_sortedhawan_seva_database(self):
        print("initilize_sortedhawan_seva_database ")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Hawan_Donation.xlsx"
        self.sortedhawan_database_name = path
        # path = PATH_SORTEDHAWAN_SEVA_SHEET
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Hawan Seva deposit initialized successfully ")

    def get_sortedhawan_database_name(self):
        return self.sortedhawan_database_name

    def initilize_sortedhawan_seva_databasepast(self, year):
        print("initilize_sortedhawan_seva_database past ")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Past year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Hawan_Donation.xlsx"
        self.sortedhawan_database_name = path
        # path = PATH_SORTEDHAWAN_SEVA_SHEET
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Hawan Seva deposit initialized successfully ")

    def initilize_sortedprachar_event_seva_database(self):
        print("initilize_sortedprachar_event_seva_database ")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Event_prachar_Donation.xlsx"
        self.sortedprachar_event_database_name = path
        # path = PATH_SORTEDEVENT_SEVA_SHEET
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Event\Prachar deposit initialized successfully ")

    def get_sortedprachar_event_database_name(self):
        return self.sortedprachar_event_database_name

    def initilize_sortedprachar_event_seva_databasepast(self, year):
        print("initilize_sortedprachar_event_seva_database ")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("past year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Event_prachar_Donation.xlsx"
        self.sortedprachar_event_database_name = path
        # path = PATH_SORTEDEVENT_SEVA_SHEET
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for past Sorted Event\Prachar deposit initialized successfully ")

    def initilize_sortedaarti_seva_database(self):
        print("initilize_sortedaarti_seva_database ")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Aarti_Donation.xlsx"
        # path = PATH_SORTEDAARTI_SEVA_SHEET
        self.sortedaarti_seva_database_name = path
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Aarti Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Arti Seva deposit !! Initialization not required ")

    def get_sortedaarti_seva_database_name(self):
        return self.sortedaarti_seva_database_name

    def initilize_sortedaarti_seva_databasepast(self, year):
        print("initilize_sortedaarti_seva_databasepast ")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Aarti_Donation.xlsx"
        # path = PATH_SORTEDAARTI_SEVA_SHEET
        self.sortedaarti_seva_database_name = ""
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" Database for Aarti Seva deposit initialized successfully ")
        else:
            print(" Database already exists for Arti Seva deposit !! Initialization not required ")

    def initilize_sortedashram_seva_database(self):
        print("initilize_sortedashram_seva_database ")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Ashram_Generic_Donation.xlsx"
        # path = PATH_SORTEDASHRAM_GENERIC_SEVA_SHEET
        self.sortedashram_seva_database_name = path
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Ashram Generic Seva deposit initialized successfully ")

    def get_sortedashram_seva_database_name(self):
        return self.sortedashram_seva_database_name

    def initilize_sortedashram_seva_databasepast(self, year):
        today = datetime.now()
        year = today.strftime("%Y")
        print("initilize_sortedashram_seva_database ")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Ashram_Generic_Donation.xlsx"
        # path = PATH_SORTEDASHRAM_GENERIC_SEVA_SHEET
        self.sortedashram_seva_database_name = path
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Ashram Generic Seva deposit initialized successfully ")

    def initilize_sortedyoga_seva_database(self):
        print("initilize_sortedyoga_seva_database ")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Yoga_Fees_Donation.xlsx"

        # path = PATH_SORTEDYOGA_FEES_SHEET
        self.sortedyoga_seva_database_name = path
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Yoga fees deposit initialized successfully ")

    def get_sortedyoga_seva_database_name(self):
        return self.sortedyoga_seva_database_name

    def initilize_sortedyoga_seva_databasepast(self, year):
        print("initilize_sortedyoga_seva_database ")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Yoga_Fees_Donation.xlsx"

        # path = PATH_SORTEDYOGA_FEES_SHEET
        self.sortedyoga_seva_database_name = path
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Yoga fees deposit initialized successfully ")

    def initilize_sortedashramnirmaan_seva_database(self):
        print("initilize_sortedashramnirmaan_seva_database ")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Ashram_Nirmaan_Donation.xlsx"
        # path = PATH_SORTEDASHRAM_NIRMAAN_SHEET
        self.sortedashramnirmaan_seva_database_name = path
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Yoga fees deposit initialized successfully ")

    def get_sortedashramnirmaan_seva_database_name(self):
        return self.sortedashramnirmaan_seva_database_name

    def initilize_sortedashramnirmaan_seva_databasepast(self, year):
        print("initilize_sortedashramnirmaan_seva_database ")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Ashram_Nirmaan_Donation.xlsx"
        # path = PATH_SORTEDASHRAM_NIRMAAN_SHEET
        self.sortedashramnirmaan_seva_database_name = path
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Yoga fees deposit initialized successfully ")

    def initilize_sortedakshay_patra_database(self):
        print("initilize_sortedakshay_patra_database ")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Akshay_patra.xlsx"
        self.sortedakshay_patra_database_name = path
        # path = PATH_SORTEDAKSHAY_PATRA_DATABASE

        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Akshay Patra(No.)',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['F'].width = 40
        wb.save(path)
        print(" Database for Sorted Akshay Patra Initialization success ")

    def get_sortedakshay_patra_database_name(self):
        return self.sortedakshay_patra_database_name

    def initilize_sortedakshay_patra_databasepast(self, year):
        print("initilize_sortedakshay_patra_database ")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Akshay_patra.xlsx"
        self.sortedakshay_patra_database_name = path
        # path = PATH_SORTEDAKSHAY_PATRA_DATABASE

        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Akshay Patra(No.)',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['F'].width = 40
        wb.save(path)
        print(" Database for Sorted Akshay Patra Initialization success ")

    def initilize_sortedseva_deposit_database(self):
        print("initilize_sortedseva_deposit_database ")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Monetary_Donation.xlsx"
        self.sortedseva_deposit_database_name = path
        # path = PATH_SORTEDSEVA_SHEET
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From', 'Date',
                        'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Seva deposit initialized successfully ")

    def get_sortedseva_deposit_database_name(self):
        return self.sortedseva_deposit_database_name

    def initilize_sortedseva_deposit_databasepast(self, year):
        print("initilize_sortedseva_deposit_database ")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Monetary_Donation.xlsx"
        self.sortedseva_deposit_database_name = path
        # path = PATH_SORTEDSEVA_SHEET
        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Seva Amt.(Rs.)', 'Total Balance(Rs.)', 'Received From(ID)', 'Received From', 'Date',
                        'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['J'].width = 40
        wb.save(path)
        print(" Database for Sorted Seva deposit initialized successfully ")

    def initilize_pledgeitem_database(self, trustName, pledgeItem):
        print("initilize_pledgeitem_database ")
        dirname = "..\\Sankalp\\" + trustName.get()
        if not os.path.exists(dirname):
            print("sankalp directory is not available , hence building one")
            os.makedirs(dirname)

        path = dirname + "\\" + pledgeItem + ".xlsx"
        if not os.path.exists(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Member ID', 'Member Name', 'Contact No', 'Pledge Amount(Rs.)', 'Pledge Item',
                            'Pledge Date',
                            'Coordinator ID', 'Coordinator Name',
                            'Pledge Duration', 'Payment Schedule', 'Rem. Balance(Rs.)', 'Status']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['F'].width = 30
            sheet.column_dimensions['A'].width = 10
            wb.save(path)

        print(" initilize_pledgeitem_database end  ")
        return path

    def initilize_sorted_pledgeitem_database(self, trustName, pledgeItem):
        print("initilize_sorted_pledgeitem_database ")
        dirname = "..\\Sankalp\\Sorted_List\\" + trustName.get()
        if not os.path.exists(dirname):
            print("sankalp directory is not available , hence building one")
            os.makedirs(dirname)

        path = dirname + "\\" + pledgeItem + ".xlsx"

        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Member ID', 'Member Name', 'Contact No', 'Pledge Amount(Rs.)', 'Pledge Item',
                        'Date',
                        'Coordinator ID', 'Coordinator Name',
                        'Pledge Duration', 'Payment Schedule', 'Rem. Balance(Rs.)', 'Status']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['F'].width = 30
        sheet.column_dimensions['A'].width = 10
        wb.save(path)
        return path

        print(" initilize_pledge_master_database end  ")
        return path

    def initilize_current_year_pledge_payment_database(self, trust_name, pledge_item):
        print("initilize_pledge_payment_database")
        print("Trust name :", trust_name, "Pledge item :", pledge_item)
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Pledge\\" + trust_name
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Payment_" + pledge_item + ".xlsx"
        self.current_year_pledge_payment_database_name = path
        if not os.path.isfile(path):
            wb = openpyxl.Workbook()
            sheet = wb.active
            heading_list = ['S.no', 'Payment(Rs.)', 'Received From(ID)', 'Received From',
                            'Date', 'Category',
                            'Receiver(Id)', 'Receiver Name', 'Address',
                            'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

            # preparing the top headers of the excel sheet.
            sheet.row_dimensions[1].height = 25

            excel_cell = {}
            alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
            for iLoop in range(1, 14):
                sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
                sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
                sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
                # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
                excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
                excel_cell[iLoop].value = heading_list[iLoop - 1]
            sheet.column_dimensions['J'].width = 40
            wb.save(path)
            print(" initilize_current_year_pledge_payment_database initialized successfully ")
        else:
            print("Database already exists for Payment Master !! Initialization not required ")
        return path

    def initilize_sorted_current_year_pledge_payment_database(self):
        print("initilize_sorted_current_year_pledge_payment_database ")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Pledge_donation.xlsx"

        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.no', 'Payment(Rs.)', 'Received From(ID)', 'Received From',
                        'Date', 'Category',
                        'Receiver(Id)', 'Receiver Name', 'Address',
                        'Mode of Payment', 'Authorizor ID', 'Authorizor Name', 'Invoice Id']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
        for iLoop in range(1, 14):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['F'].width = 40
        wb.save(path)
        print(" Database for Sorted Current year pledge payment Initialization success ")

        return path

    def current_year_pledge_payment_database_name(self, trust_name, pledge_item):
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Pledge\\" + trust_name.get()
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Payment_" + pledge_item + ".xlsx"
        return path

    def initilize_sorted_Transaction_database(self):
        print("initilize_aorted_Transaction_database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Expanse_Data\\" + year + "\\Transaction\\Sorted_List"
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        path = dirname + "\\Transaction.xlsx"
        self.sortedtransaction_database_name = path

        wb = openpyxl.Workbook()
        sheet = wb.active
        heading_list = ['S.No', 'Date', 'Credit Amt.(Rs.)', 'Debit Amt.(Rs)', 'Description', 'Mode of Transaction',
                        'Transaction By(Id)', 'Transaction By(Name)', 'Balance (Rs.)', 'Invoice ID']

        # preparing the top headers of the excel sheet.
        sheet.row_dimensions[1].height = 25

        excel_cell = {}
        alphabet_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K']
        for iLoop in range(1, 11):
            sheet.cell(row=1, column=iLoop).font = Font(size=12, name='Times New Roman', bold=True)
            sheet.column_dimensions[alphabet_dict[iLoop - 1]].width = 22
            sheet.cell(row=1, column=iLoop).alignment = Alignment(horizontal='center', vertical='center')
            # sheet.cell(row=1, column=iLoop).fill = PatternFill(fgColor='20489F', fill_type='solid')
            excel_cell[iLoop] = sheet.cell(row=1, column=iLoop)
            excel_cell[iLoop].value = heading_list[iLoop - 1]
        sheet.column_dimensions['E'].width = 40
        wb.save(path)
        print(" Database for  Sorted Transaction initialized successfully ")

    def get_sorted_transaction_database_name(self):
        return self.sortedtransaction_database_name

    def initilize_new_directories(self):
        print("Initilize VYOAM Dir Structure")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname1 = "..\\Expanse_Data\\" + year + "\\Expanse"
        dirname2 = "..\\Expanse_Data\\" + year + "\\Expanse\\Receipts"
        dirname3 = "..\\Expanse_Data\\" + year + "\\Expanse\\Receipts\\Receipts"
        dirname4 = "..\\Expanse_Data\\" + year + "\\Expanse\\Receipts\\Template"

        dirname5 = "..\\Expanse_Data\\" + year + "\\Invoices"

        dirname6 = "..\\Expanse_Data\\" + year + "\\Magazine_Subscription"
        dirname7 = "..\\Expanse_Data\\" + year + "\\Magazine_Subscription\\Receipt"
        dirname8 = "..\\Expanse_Data\\" + year + "\\Magazine_Subscription\\Receipt\\Receipts"
        dirname9 = "..\\Expanse_Data\\" + year + "\\Magazine_Subscription\\Receipt\\Template"

        dirname10 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi"
        dirname11 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        dirname12 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        dirname13 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Receipts"
        dirname14 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Receipts\\Receipts"
        dirname15 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Receipts\\Template"
        dirname16 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Statements"
        dirname17 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Template"

        dirname18 = "..\\Expanse_Data\\" + year + "\\Statements"

        dirname19 = "..\\Expanse_Data\\" + year + "\\Transaction"
        dirname20 = "..\\Expanse_Data\\" + year + "\\Transaction\\Account_Statement"
        dirname21 = "..\\Expanse_Data\\" + year + "\\Transaction\\Account_Statement\\Statements"
        dirname22 = "..\\Expanse_Data\\" + year + "\\Transaction\\Account_Statement\\Template"
        dirname23 = "..\\Expanse_Data\\" + year + "\\Transaction\\Sorted_List"
        dirname24 = "..\\Expanse_Data\\" + year + "\\Transaction\\StockSell"
        dirname25 = "..\\Expanse_Data\\" + year + "\\Transaction\\StockSell\\Sorted"
        dirname26 = "..\\Expanse_Data\\" + year + "\\Transaction\\StockSell\\Statements"
        dirname27 = "..\\Expanse_Data\\" + year + "\\Transaction\\StockSell\\Template"

        directory_list = [dirname1, dirname2, dirname3, dirname4, dirname5, dirname6, dirname7,
                          dirname8, dirname9, dirname10, dirname11, dirname12, dirname13, dirname14,
                          dirname15, dirname16, dirname17, dirname18, dirname19, dirname20, dirname21,
                          dirname22, dirname23, dirname24, dirname25, dirname26, dirname27]

        for index in range(0, len(directory_list)):
            if not os.path.exists(directory_list[index]):
                print(directory_list[index], " ...created")
                os.makedirs(directory_list[index])

        print("VYOAM Dir Structure initialized")
        print("VYOAM Copying  common file start")
        shutil.copy("..\\Common_Files\\Ashram_Voucher_Receipt_Template.xlsx", dirname4)
        shutil.copy("..\\Common_Files\\Gaushala_Voucher_Receipt_Template.xlsx", dirname4)
        shutil.copy("..\\Common_Files\\Subscription_Receipt_Template.xlsx", dirname9)
        shutil.copy("..\\Common_Files\\Donation_Receipt_Template.xlsx", dirname15)
        shutil.copy("..\\Common_Files\\Donation_NonMonetary_Receipt_Template.xlsx", dirname15)

        shutil.copy("..\\Common_Files\\Split_Donation_Open.xlsx", dirname22)
        shutil.copy("..\\Common_Files\\Transaction_template.xlsx", dirname22)
        shutil.copy("..\\Common_Files\\stock_sales_account_template.xlsx", dirname27)
        shutil.copy("..\\Common_Files\\member_statement_template.xlsx", dirname17)
        shutil.copy("..\\Common_Files\\account_statement_template.xlsx", dirname17)
        shutil.copy("..\\Common_Files\\pledge_statement_template.xlsx", dirname17)
        shutil.copy("..\\Common_Files\\pledge_statement_template_gaushala.xlsx", dirname17)
        shutil.copy("..\\Common_Files\\Pledge_Item_template.xlsx", dirname17)
        shutil.copy("..\\Common_Files\\Pledge_Item_template_gaushala.xlsx", dirname17)

        # copy booklets , if they do not exists
        filename_donation_booklet = dirname15 + "\\Donation_Receipt_Booklet.xlsx"
        if not os.path.exists(filename_donation_booklet):
            print("Ashram Donation booklet new copied")
            shutil.copy("..\\Common_Files\\Donation_Receipt_Booklet.xlsx", dirname15)
        else:
            print("Ashram Donation booklet already exist")

        filename_gaushala_donation_booklet = dirname15 + "\\Gaushala_Donation_Receipt_Booklet.xlsx"
        if not os.path.exists(filename_gaushala_donation_booklet):
            print("gaushala Donation booklet new copied")
            shutil.copy("..\\Common_Files\\Gaushala_Donation_Receipt_Booklet.xlsx", dirname15)
        else:
            print("Gaushala Donation booklet already exist")

        # copy booklets , if they do not exists
        filename_Ashram_Expanse_Voucher__booklet = dirname4 + "\\Ashram_Expanse_Voucher_Receipt_Booklet.xlsx"
        if not os.path.exists(filename_Ashram_Expanse_Voucher__booklet):
            print("Ashram_Expanse_Voucher__booklet new copied")
            shutil.copy("..\\Common_Files\\Ashram_Expanse_Voucher_Receipt_Booklet.xlsx", dirname4)
        else:
            print("Ashram_Expanse_Voucher booklet already exist")

        filename_Gaushala_Expanse_Voucher_Receipt_Booklet = dirname4 + "\\Gaushala_Expanse_Voucher_Receipt_Booklet.xlsx"
        if not os.path.exists(filename_Gaushala_Expanse_Voucher_Receipt_Booklet):
            print("Gaushala_Expanse_Voucher__booklet new copied")
            shutil.copy("..\\Common_Files\\Gaushala_Expanse_Voucher_Receipt_Booklet.xlsx", dirname4)
        else:
            # copy not required
            print("Gaushala_Expanse_Voucher booklet already exist")

        print("VYOAM Copying  common files completed")

    def resetallExpanseData(self):
        print("VYOAM Deleting Expanse Database")
        today = datetime.now()
        year = today.strftime("%Y")
        dirname1 = "..\\Expanse_Data\\" + year + "\\Expanse"
        dirname2 = "..\\Expanse_Data\\" + year + "\\Expanse\\Receipts"
        dirname3 = "..\\Expanse_Data\\" + year + "\\Expanse\\Receipts\\Receipts"
        dirname4 = "..\\Expanse_Data\\" + year + "\\Expanse\\Receipts\\Template"

        dirname5 = "..\\Expanse_Data\\" + year + "\\Invoices"

        dirname6 = "..\\Expanse_Data\\" + year + "\\Magazine_Subscription"
        dirname7 = "..\\Expanse_Data\\" + year + "\\Magazine_Subscription\\Receipt"
        dirname8 = "..\\Expanse_Data\\" + year + "\\Magazine_Subscription\\Receipt\\Receipts"
        dirname9 = "..\\Expanse_Data\\" + year + "\\Magazine_Subscription\\Receipt\\Template"

        dirname10 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi"
        dirname11 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation"
        dirname12 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Donation\\Sorted_List"
        dirname13 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Receipts"
        dirname14 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Receipts\\Receipts"
        dirname15 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Receipts\\Template"
        dirname16 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Statements"
        dirname17 = "..\\Expanse_Data\\" + year + "\\Seva_Rashi\\Template"

        dirname18 = "..\\Expanse_Data\\" + year + "\\Statements"

        dirname19 = "..\\Expanse_Data\\" + year + "\\Transaction"
        dirname20 = "..\\Expanse_Data\\" + year + "\\Transaction\\Account_Statement"
        dirname21 = "..\\Expanse_Data\\" + year + "\\Transaction\\Account_Statement\\Statements"
        dirname22 = "..\\Expanse_Data\\" + year + "\\Transaction\\Account_Statement\\Template"
        dirname23 = "..\\Expanse_Data\\" + year + "\\Transaction\\Sorted_List"
        dirname24 = "..\\Expanse_Data\\" + year + "\\Transaction\\StockSell"
        dirname25 = "..\\Expanse_Data\\" + year + "\\Transaction\\StockSell\\Sorted"
        dirname26 = "..\\Expanse_Data\\" + year + "\\Transaction\\StockSell\\Statements"
        dirname27 = "..\\Expanse_Data\\" + year + "\\Transaction\\StockSell\\Template"

        directory_list = [dirname1, dirname2, dirname3, dirname4, dirname5, dirname6, dirname7,
                          dirname8, dirname9, dirname10, dirname11, dirname12, dirname13, dirname14,
                          dirname15, dirname16, dirname17, dirname18, dirname19, dirname20, dirname21,
                          dirname22, dirname23, dirname24, dirname25, dirname26, dirname27]

        for index in range(0, len(directory_list)):
            if os.path.exists(directory_list[index]):
                print(directory_list[index], " ...deleted")
                shutil.rmtree(directory_list[index])
