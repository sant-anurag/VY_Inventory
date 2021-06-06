"""
# Copyright 2021 by Deo Tech.
# All rights reserved.
# This file is part of the Software Package,
# and is released under the "VY License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
# Vihangan Yoga Operations  of Ashram Management Software
# File Name : stocksales_statement.py
# Developer : Sant Anurag Deo
# Version : 2.0
"""

from app_defines import *
from app_common import *
from app_thread import *


class StocksalesStatement:
    # constructor for Library class
    def __init__(self, master):
        """ constructor for the Stock Sales statement"""
        print("constructor ")
        self.obj_commonUtil = CommonUtil()
        self.dateTimeOp = DatetimeOperation()
        self.stocksales_sheet(master)

    def stocksales_sheet(self, master):
        stocksales_statement_window = Toplevel(master)
        stocksales_statement_window.title("Stock Sales Statement ")
        stocksales_statement_window.geometry('770x450+120+40')
        stocksales_statement_window.configure(background='wheat')
        stocksales_statement_window.resizable(width=False, height=False)

        # delete "X" button in window will be not-operational
        stocksales_statement_window.protocol('WM_DELETE_WINDOW', self.obj_commonUtil.donothing)

        infoFrame = Frame(stocksales_statement_window, width=300, height=100, bd=6, relief='ridge',
                          bg="wheat")
        topFrame = Frame(stocksales_statement_window, width=300, height=100, bd=6, relief='ridge',
                         bg="light yellow")
        topFrame.grid(row=2, column=0, padx=20, pady=10, sticky=W)
        infoFrame.grid(row=3, column=0, padx=80, pady=10, sticky=W)
        infoLabel = Label(infoFrame, text="Select appropriate parameters and press Search", width=65,
                          justify='center', font=('arial narrow', 13, 'bold'),
                          bg='snow', fg='green', state=NORMAL)
        infoLabel.grid(row=0, column=0)

        heading = Label(stocksales_statement_window, text="Stock Sales Statement",
                        font=('times new roman', 20, 'bold'),
                        bg="wheat")

        heading.grid(row=1, column=0)

        dateFrame = Frame(topFrame, width=100, height=100, bd=2, relief='ridge', bg='light yellow')
        fromDate = Label(dateFrame, text="From Date", width=10, anchor=W, justify='center',
                         font=NORM_FONT,
                         bg='light yellow', state=DISABLED)
        cal_dateFrom = DateEntry(dateFrame, width=15, date_pattern='dd/MM/yyyy', font=NORM_FONT,
                                 state=DISABLED, justify=LEFT, anchor=W)
        toDate = Label(dateFrame, text="To Date", width=10, justify='center', font=NORM_FONT,
                       bg='light yellow', state=DISABLED)
        cal_toDate = DateEntry(dateFrame, width=15, date_pattern='dd/MM/yyyy', font=NORM_FONT,
                               state=DISABLED, justify='center')
        viewByMonth_Month = Label(dateFrame, text="Month", width=10, justify=LEFT, anchor=W,
                                  font=NORM_FONT,
                                  bg='light yellow', state=DISABLED)
        viewByMonth_Year = Label(dateFrame, text="Year", width=10, justify=LEFT, anchor=W,
                                 font=NORM_FONT,
                                 bg='light yellow', state=DISABLED)
        viewByYear_Year = Label(dateFrame, text="Year", width=10, justify=LEFT, anchor=W,
                                font=NORM_FONT,
                                bg='light yellow', state=NORMAL)

        month_variable = StringVar(dateFrame)
        now = datetime.now()
        month_variable.set(self.dateTimeOp.fetchMonthName(now.month))

        viewbyMonth_monthTxt = OptionMenu(dateFrame, month_variable, 'January', 'February', 'March', 'April', 'May',
                                          'June', 'July', 'August', 'September', 'October',
                                          'November', 'December')
        viewbyMonth_monthTxt.configure(bg='snow', width=13, fg='black', font=NORM_FONT,
                                       state=DISABLED)

        year_variable = StringVar(dateFrame)
        year_variable.set("2021")

        viewbymonth_yearTxt = OptionMenu(dateFrame, year_variable, '2021', '2022', '2023', '2024',
                                         '2025', '2026', '2027', '2028', '2029', '2030')
        viewbymonth_yearTxt.configure(bg='snow', width=13, fg='black', font=NORM_FONT,
                                      state=DISABLED)

        year_yearvariable = StringVar(dateFrame)
        year_yearvariable.set("2021")
        viewbyYear_yearTxt = OptionMenu(dateFrame, year_yearvariable, '2021', '2022', '2023', '2024',
                                        '2025', '2026', '2027', '2028', '2029', '2030')
        viewbyYear_yearTxt.configure(bg='snow', width=13, fg='black', font=NORM_FONT,
                                     state=NORMAL)

        var = IntVar()
        var.set(3)
        viewSelFrame_Result = partial(self.enableViewBy_RadioSelection, var, fromDate, cal_dateFrom, toDate, cal_toDate,
                                      viewByMonth_Month, viewbyMonth_monthTxt, viewByMonth_Year, viewbymonth_yearTxt,
                                      viewByYear_Year, viewbyYear_yearTxt)
        viewbydate_radioBtn = Radiobutton(dateFrame, text="View By Date", variable=var, value=1,
                                          command=viewSelFrame_Result, width=12, bg='light yellow',
                                          font=NORM_FONT, anchor=W, justify=LEFT)
        viewbymonth_radioBtn = Radiobutton(dateFrame, text="View By Month", variable=var, value=2,
                                           command=viewSelFrame_Result, width=12, bg='light yellow',
                                           font=NORM_FONT, anchor=W, justify=LEFT)
        viewbyyear_radioBtn = Radiobutton(dateFrame, text="View By Year", variable=var, value=3,
                                          command=viewSelFrame_Result, width=12, bg='light yellow',
                                          font=NORM_FONT, anchor=W, justify=LEFT)
        viewbydate_radioBtn.grid(row=0, column=0, padx=20)
        fromDate.grid(row=1, column=0, padx=20)
        cal_dateFrom.grid(row=1, column=1)
        toDate.grid(row=1, column=2, padx=10)
        cal_toDate.grid(row=1, column=3)

        viewbymonth_radioBtn.grid(row=2, column=0, padx=30)
        viewByMonth_Month.grid(row=3, column=0, padx=20)
        viewbyMonth_monthTxt.grid(row=3, column=1)
        viewByMonth_Year.grid(row=3, column=2, padx=10)
        viewbymonth_yearTxt.grid(row=3, column=3)

        viewbyyear_radioBtn.grid(row=4, column=0, padx=30)
        viewByYear_Year.grid(row=5, column=1, padx=20)
        viewbyYear_yearTxt.grid(row=5, column=2)
        # ---------------------------------Button Frame Start----------------------------------------
        buttonFrame = Frame(topFrame, width=100, height=100, bd=4, relief='ridge', bg="light yellow")
        buttonFrame.grid(row=1, column=0, padx=10, pady=5, columnspan=3)

        viewPDF = Button(buttonFrame, text="View Statement", fg="Black",
                         font=NORM_FONT, width=12, bg='light grey', state=DISABLED)

        printBtn = Button(buttonFrame, text="Print Statement", fg="Black",
                          font=NORM_FONT, width=12, bg='light grey', state=DISABLED)
        cancel = Button(buttonFrame, text="Close", fg="Black", command=stocksales_statement_window.destroy,
                        font=NORM_FONT, width=12, bg='light cyan')
        '''
        search_result = partial(self.prepare_account_statement_Excel, stocksales_statement_window, printBtn,
                                cal_dateFrom,
                                cal_toDate, month_variable, year_variable,
                                year_yearvariable, var, viewPDF, infoLabel, cancel)
                                '''
        submit = Button(buttonFrame, text="Search", fg="Black", command=None,
                        font=NORM_FONT, width=12, bg='light cyan')
        submit.grid(row=0, column=0)
        viewPDF.grid(row=0, column=1)
        printBtn.grid(row=0, column=2)

        dateFrame.grid(row=0, column=0, padx=10, pady=10)
        fromDate.grid(row=1, column=0, padx=10)
        cal_dateFrom.grid(row=1, column=1)
        toDate.grid(row=1, column=2, padx=10)
        cal_toDate.grid(row=1, column=3)

        # create a Close Button and place into the stocksales_statement_window window

        cancel.grid(row=0, column=3)
        # ---------------------------------Button Frame End----------------------------------------

        stocksales_statement_window.bind('<Return>', lambda event=None: submit.invoke())
        stocksales_statement_window.bind('<Alt-c>', lambda event=None: cancel.invoke())

        stocksales_statement_window.focus()
        stocksales_statement_window.grab_set()
        mainloop()

    def checkCategoryChange(self, n, m, x, src_file, starting_index, dummy):
        print("Category has been changed !!!")
        src_filename = n
        wb_template = openpyxl.load_workbook(src_filename)
        template_sheet = wb_template.active
        print("Source file name: ", src_filename)

        for rows in range(15, m + 1):
            for columns in range(1, 6):
                template_sheet.cell(row=rows, column=columns).value = ""

        wb_template.save(src_filename)

    def enableViewBy_RadioSelection(self, var, fromDate, cal_dateFrom, toDate, cal_toDate,
                                    viewByMonth_Month, viewbyMonth_monthTxt, viewByMonth_Year, viewbymonth_yearTxt,
                                    viewByYear_Year, viewbyYear_yearTxt):
        print("Enabling the view by date section Radiobutton :", var.get())

        # all elements are disabled in begining
        # based on the selection of the radio button, respective ones are enabled

        fromDate.configure(state=DISABLED)
        cal_dateFrom.configure(state=DISABLED)
        toDate.configure(state=DISABLED)
        cal_toDate.configure(state=DISABLED)
        viewByMonth_Month.configure(state=DISABLED)
        viewbyMonth_monthTxt.configure(state=DISABLED)
        viewByMonth_Year.configure(state=DISABLED)
        viewbymonth_yearTxt.configure(state=DISABLED)
        viewByYear_Year.configure(state=DISABLED)
        viewbyYear_yearTxt.configure(state=DISABLED)

        if var.get() == 1:
            print("Enabling view by date")
            fromDate.configure(state=NORMAL, bg='light yellow')
            cal_dateFrom.configure(state=NORMAL)
            toDate.configure(state=NORMAL, bg='light yellow')
            cal_toDate.configure(state=NORMAL)
        elif var.get() == 2:
            viewByMonth_Month.configure(state=NORMAL, bg='light yellow')
            viewbyMonth_monthTxt.configure(state=NORMAL)
            viewByMonth_Year.configure(state=NORMAL, bg='light yellow')
            viewbymonth_yearTxt.configure(state=NORMAL)
        elif var.get() == 3:
            viewByYear_Year.configure(state=NORMAL, bg='light yellow')
            viewbyYear_yearTxt.configure(state=NORMAL)
        else:
            pass

    def myfunction(self, mycanvas, event):
        mycanvas.configure(scrollregion=mycanvas.bbox("all"), width=725, height=407)

    def closepage(self, src_file, starting_index, account_statement_window):
        print("closepage :", src_file)
        account_statement_window.destroy()
        # erase the written records in template sheet
        # executed only if
        wb_template = openpyxl.load_workbook(src_file)
        template_sheet = wb_template.active

        for rows in range(15, starting_index + 1):
            for columns in range(1, 7):
                template_sheet.cell(row=rows, column=columns).value = ""

        wb_template.save(src_file)

    def prepare_account_statement_Excel(self, account_statement_window, printBtn, cal_dateFrom,
                                        cal_toDate, viewbyMonth_monthTxt, viewbymonth_yearTxt,
                                        viewbyYear_yearTxt, var, viewPDF, infoLabel, cancelbtn):
        print("prepare_account_statement_Excel --> var:", var.get())

        viewPDF.configure(state=DISABLED, bg="light grey")
        printBtn.configure(state=DISABLED, bg="light grey")
        if var.get() == 1:
            dateTimeObj_From = cal_dateFrom.get_date()
            from_Date = dateTimeObj_From.strftime("%Y-%m-%d")
            dateTimeObj_To = cal_toDate.get_date()
            to_Date = dateTimeObj_To.strftime("%Y-%m-%d")
            fromDate = self.dateTimeOp.prepare_dateFromString(from_Date)
            toDate = self.dateTimeOp.prepare_dateFromString(to_Date)
        elif var.get() == 2:
            noOfDays, month_number = self.dateTimeOp.calculateNoOfDaysInMonth(viewbyMonth_monthTxt.get(),
                                                                              viewbymonth_yearTxt.get())
            fromDate, toDate = self.dateTimeOp.getFromAndToDates_Account_Statement(month_number,
                                                                                   viewbymonth_yearTxt.get(),
                                                                                   noOfDays)
            frdateforstatement = fromDate.strftime("%b-%d-%Y")
            todateforstatement = toDate.strftime("%b-%d-%Y")
        else:
            print("Requested year is :", viewbyYear_yearTxt.get())
            noOfDays = self.dateTimeOp.calculateNoOfDaysInYear(viewbyYear_yearTxt.get())
            fromDate, toDate = self.dateTimeOp.getFromAndToDates_Account_Statement(1, viewbyYear_yearTxt.get(),
                                                                                   noOfDays)

        from_year = fromDate.strftime("%Y")
        to_year = toDate.strftime("%Y")
        to_month = toDate.strftime('%m')
        today_date = datetime.now()
        formatted_date = today_date.strftime("%Y-%m-%d")
        currentDate = self.dateTimeOp.prepare_dateFromString(formatted_date)
        current_year = currentDate.strftime("%Y")
        print("From Year :", from_year, " To Year :", to_year)
        bDateConditionsValid = True
        if fromDate > toDate:
            error_info = "From date cannot be grater than to date !!!"
            bDateConditionsValid = False
        elif ((toDate > currentDate) or (fromDate > currentDate)) and \
                ((var.get() == 1) or (var.get() == 2)):

            if var.get() == 2:
                current_month = datetime.today().month
                current_year = datetime.today().year
                print("to_year : ", to_year, "current_year :", current_year, "to_month :", to_month, "current_month :",
                      current_month)
                if int(to_year) > int(current_year) or int(to_month) > int(current_month):
                    error_info = "Year/Month can not be future !!!"
                    bDateConditionsValid = False
                if int(to_year) == int(current_year) and int(to_month) == int(current_month):
                    bDateConditionsValid = True
            else:
                error_info = "From/To Date cannot be greater than today!!!"
                bDateConditionsValid = False
        elif ((toDate - fromDate).days > 180) and (var.get() == 1):
            error_info = "Statements can be generated for maximum of 180 days !!! "
            bDateConditionsValid = False
        else:
            # check if the selected years are less than or equal to current date ,
            # but no database exists for them
            dir_name = "..\\Expanse_Data\\" + str(from_year)
            if not os.path.exists(dir_name):
                error_info = "Database does not exists for " + str(from_year) + " Please correct !!!"
                bDateConditionsValid = False
            pass

        # algorithm generates the statement when from and start date has the same year
        # same current year directory needs to be referred for these statement generations
        print("bDateConditionsValid :", bDateConditionsValid)
        if bDateConditionsValid:
            if from_year == self.obj_commonUtil.getCurrentYearFolderName() and \
                    to_year == self.obj_commonUtil.getCurrentYearFolderName():
                bAlike_seva = True
                print("This is current year transaction")

                path_seva_sheet = InitDatabase.getInstance().get_purchase_record_database_name()  # STOCK SALES DATABASE
                InitDatabase.getInstance().initilize_sorted_purchase_record_database()
                sorted_seva_sheet = InitDatabase.getInstance().get_sorted_purchase_record_database()

                if bAlike_seva:
                    print("path_seva_sheet :", path_seva_sheet)
                    wb_obj = openpyxl.load_workbook(path_seva_sheet)
                    wb_sorted_obj = openpyxl.load_workbook(sorted_seva_sheet)
                    sheet_obj = wb_obj.active
                    sheet_sorted_obj = wb_sorted_obj.active
                    total_records = self.obj_commonUtil.totalrecords_excelDataBase(path_seva_sheet)
                    if total_records > 0:
                        sort_sheet_index = 2
                        print("Total records  in transaction sheet:", total_records)
                        for row_index in range(0, total_records):
                            # critical stock ->stock with quantity is 0 or 1
                            # print("Date from sheet is :", sheet_obj.cell(row=row_index + 2, column=6).value)
                            dateFromTransactionSheet = self.dateTimeOp.prepare_dateFromString(
                                sheet_obj.cell(row=row_index + 2, column=6).value)
                            # print("dateFromMon_DepositSheet :", dateFromTransactionSheet, "fromDate :", fromDate, " toDate:", toDate)

                            if ((dateFromTransactionSheet > fromDate or dateFromTransactionSheet == fromDate)
                                    and (dateFromTransactionSheet < toDate or dateFromTransactionSheet == toDate)):

                                for column_index in range(1, 11):
                                    text_value = str(sheet_obj.cell(row=row_index + 2, column=column_index).value)

                                    sheet_sorted_obj.cell(row=sort_sheet_index, column=column_index).font = Font(size=8,
                                                                                                                 name='Arial',
                                                                                                                 bold=False)
                                    sheet_sorted_obj.cell(row=sort_sheet_index,
                                                          column=column_index).alignment = Alignment(
                                        horizontal='left', vertical='center', wrapText=True)
                                    sheet_sorted_obj.cell(row=sort_sheet_index, column=column_index).value = text_value

                                sort_sheet_index = sort_sheet_index + 1

                        today = date.today()
                        dt_today = today.strftime("%d-%b-%Y")
                        wb_sorted_obj.save(sorted_seva_sheet)
                        print("Sorted sheet created for sorting")
                        self.obj_commonUtil.sortExcelSheetByDate(sorted_seva_sheet, sorted_seva_sheet)

                        now = datetime.now()
                        dt_string = now.strftime("%d_%b_%Y_%H%M%S")
                        currentyear = now.strftime("%Y")
                        destination_file = "..\\Expanse_Data\\" + currentyear + "\\Transaction\\StockSell\\Statements\\Statement_StockSales" + dt_string + ".pdf"
                        # write the  sorted record in statement template
                        template_sheet = "..\\Expanse_Data\\" + currentyear + "\\Transaction\\StockSell\\Template\\stock_sales_account_template.xlsx"
                        wb_critical_stock = openpyxl.load_workbook(template_sheet)
                        critical_stock_sheet = wb_critical_stock.active
                        total_sorted_records = self.obj_commonUtil.totalrecords_excelDataBase(sorted_seva_sheet)
                        wb_sort = openpyxl.load_workbook(sorted_seva_sheet)
                        sort_sheet = wb_sort.active
                        dict_index = 1
                        starting_index = 15
                        print("Total sorted records :", total_sorted_records)
                        if total_sorted_records > 0:
                            text_info = "Statement is being generated for Stock Sales.Please wait ...."
                            infoLabel.configure(text=text_info, fg='purple')
                            for row_index in range(1, total_sorted_records + 1):
                                #print("credit amount is :", sort_sheet.cell(row=row_index + 1, column=8).value)
                                if dict_index == 1:
                                    balance = int(sort_sheet.cell(row=row_index + 1, column=7).value)
                                else:
                                    balance = balance + int(sort_sheet.cell(row=row_index + 1, column=7).value)

                                for column_index in range(1, 7):
                                    if column_index == 1:  # Date
                                        text_value = sort_sheet.cell(row=row_index + 1, column=6).value
                                        text_value = text_value.strftime("%d-%b-%Y")
                                    elif column_index == 2:  # Invoice
                                        text_value = sort_sheet.cell(row=row_index + 1, column=9).value
                                    elif column_index == 3:  # Description
                                        text_value = str(sort_sheet.cell(row=row_index + 1, column=4).value) + "-By " + \
                                                     str(sort_sheet.cell(row=row_index + 1, column=3).value)
                                    elif column_index == 4:  # quantity
                                        text_value = sort_sheet.cell(row=row_index + 1, column=10).value
                                    elif column_index == 5:  # credit
                                        text_value = sort_sheet.cell(row=row_index + 1, column=7).value
                                    elif column_index == 6:  # balance
                                        text_value = str(balance)
                                    else:
                                        pass
                                    critical_stock_sheet.cell(row=starting_index, column=column_index).font = Font(
                                        size=8,
                                        name='Arial',
                                        bold=False)
                                    if column_index == 4 or column_index == 5 or column_index == 6:
                                        critical_stock_sheet.cell(row=starting_index,
                                                                  column=column_index).alignment = Alignment(
                                            horizontal='center', vertical='center', wrapText=True)
                                    else:
                                        critical_stock_sheet.cell(row=starting_index,
                                                                  column=column_index).alignment = Alignment(
                                            horizontal='left', vertical='center', wrapText=True)

                                    critical_stock_sheet.cell(row=starting_index,
                                                              column=column_index).value = text_value
                                dict_index = dict_index + 1
                                starting_index = starting_index + 1

                            frdateforstatement = fromDate.strftime("%d-%b-%Y")
                            todateforstatement = toDate.strftime("%d-%b-%Y")
                            critical_stock_sheet.cell(row=3, column=6).value = dt_today
                            critical_stock_sheet.cell(row=5, column=6).value = "Stock Sales"
                            critical_stock_sheet.cell(row=8, column=6).value = str(balance)
                            critical_stock_sheet.cell(row=9, column=6).value = str(starting_index - 15)
                            critical_stock_sheet.cell(row=10, column=6).value = frdateforstatement
                            critical_stock_sheet.cell(row=11, column=6).value = todateforstatement
                            wb_critical_stock.save(template_sheet)
                            print("File has been saved for template")
                            destination_copy_folder = InitDatabase.getInstance().get_desktop_statement_directory_path()
                            obj_threadClass = myThread(10, "statementThread", 1, template_sheet,
                                                       destination_file, starting_index, viewPDF, printBtn, infoLabel,destination_copy_folder)
                            obj_threadClass.start()
                            print_result = partial(self.obj_commonUtil.open_statement_file,
                                                   template_sheet,
                                                   destination_file, starting_index)
                            printBtn.configure(command=print_result)
                            view_result = partial(self.obj_commonUtil.open_statement_file, template_sheet,
                                                  destination_file, starting_index)
                            viewPDF.configure(command=view_result, )

                            cancel_result = partial(self.closepage, template_sheet, starting_index,
                                                    account_statement_window)
                            cancelbtn.configure(command=cancel_result)
                        else:
                            text_error = "No records present for Stock Sales in specified period!!!"
                            infoLabel.configure(text=text_error, fg='red')
                    else:
                        text_error = "No records present for  Stock sales"
                        infoLabel.configure(text=text_error, fg='red')
            else:
                # algorithm generates the statement when from and start date has different year
                # same current year directory needs to be referred for these statement generations
                print(" From year and to year are different")

                # Since the maximum viewed transaction are only 6 months
                # only 2 year numbers can be considered at max
                # hence same loop with different from and to dates in executed twice
                # this is possible only in case of view by date
                yearDiff = int(to_year) - int(from_year)
                loop_range = yearDiff + 2

                print("Year diff :", yearDiff, " loop_range :", loop_range)
                for year_loop in range(1, loop_range):
                    if var.get() == 1:
                        if year_loop == 1:
                            fDate = fromDate
                            yearOfFromdate = fDate.strftime("%Y")
                            yearFolderToSearch = yearOfFromdate
                            tDate = self.obj_commonUtil.prepare_dateFromString("31" + "-" + "12" + "-" + yearOfFromdate)
                        elif year_loop == 2:
                            yearOfTodate = toDate.strftime("%Y")
                            fDate = self.obj_commonUtil.prepare_dateFromString("1" + "-" + "1" + "-" + yearOfTodate)
                            yearOfTodate = toDate.strftime("%Y")
                            yearFolderToSearch = yearOfTodate
                            tDate = toDate
                        else:
                            pass
                    elif var.get() == 2 or var.get() == 3:
                        fDate = fromDate
                        tDate = toDate
                        yearOfFromdate = fDate.strftime("%Y")
                        yearFolderToSearch = yearOfFromdate
                    else:
                        pass

                    print("fDate :", fDate, "tDate:", tDate, "yearFolderToSearch :", yearFolderToSearch)

                    path_seva_sheet = "..\\Expanse_Data\\" + yearFolderToSearch + "\\Transaction\\StockSell\\Purchase_Transaction.xlsx"
                    if year_loop == 1:
                        InitDatabase.getInstance().initilize_sortedmonthly_seva_database()
                        sorted_seva_sheet = InitDatabase.getInstance().get_sortedmonthly_database_name()

                    print("path_seva_sheet :", path_seva_sheet)
                    wb_obj = openpyxl.load_workbook(path_seva_sheet)
                    wb_sorted_obj = openpyxl.load_workbook(sorted_seva_sheet)
                    sheet_obj = wb_obj.active
                    sheet_sorted_obj = wb_sorted_obj.active
                    total_records = self.obj_commonUtil.totalrecords_excelDataBase(path_seva_sheet)
                    if total_records > 0:
                        sort_sheet_index = self.obj_commonUtil.totalrecords_excelDataBase(sorted_seva_sheet) + 2
                        print("Sorted sheet will now start from row:", sort_sheet_index)
                        print("Total records  in transaction sheet:", total_records)
                        for row_index in range(0, total_records):
                            # critical stock ->stock with quantity is 0 or 1
                            # print("Date from sheet is :", sheet_obj.cell(row=row_index + 2, column=6).value)
                            dateFromTransactionSheet = self.dateTimeOp.prepare_dateFromString(
                                sheet_obj.cell(row=row_index + 2, column=6).value)
                            # print("dateFromMon_DepositSheet :", dateFromTransactionSheet, "fromDate :", fromDate, " toDate:", toDate)

                            if ((dateFromTransactionSheet > fDate or dateFromTransactionSheet == fDate)
                                    and (dateFromTransactionSheet < tDate or dateFromTransactionSheet == tDate)):
                                for column_index in range(1, 11):
                                    text_value = str(sheet_obj.cell(row=row_index + 2, column=column_index).value)

                                    sheet_sorted_obj.cell(row=sort_sheet_index, column=column_index).font = Font(size=8,
                                                                                                                 name='Arial',
                                                                                                                 bold=False)
                                    sheet_sorted_obj.cell(row=sort_sheet_index,
                                                          column=column_index).alignment = Alignment(
                                        horizontal='left', vertical='center', wrapText=True)
                                    sheet_sorted_obj.cell(row=sort_sheet_index, column=column_index).value = text_value

                                sort_sheet_index = sort_sheet_index + 1

                        today = date.today()
                        dt_today = today.strftime("%d-%b-%Y")
                        wb_sorted_obj.save(sorted_seva_sheet)
                        print("Sorted sheet created for sorting")
                        self.obj_commonUtil.sortExcelSheetByDate(sorted_seva_sheet, sorted_seva_sheet)
                        now = datetime.now()
                        dt_string = now.strftime("%d_%b_%Y_%H%M%S")
                        currentyear = now.strftime("%Y")
                        destination_file = "..\\Expanse_Data\\" + currentyear + "\\Transaction\\StockSell\\Statements\\Statement_StockSales" + dt_string + ".pdf"
                        # write the  sorted record in statement template
                        template_sheet = "..\\Expanse_Data\\" + currentyear + "\\Transaction\\StockSell\\Template\\stock_sales_account_template.xlsx"
                        wb_critical_stock = openpyxl.load_workbook(template_sheet)
                        critical_stock_sheet = wb_critical_stock.active
                        total_sorted_records = self.obj_commonUtil.totalrecords_excelDataBase(sorted_seva_sheet)
                        wb_sort = openpyxl.load_workbook(sorted_seva_sheet)
                        sort_sheet = wb_sort.active
                        dict_index = 1
                        starting_index = 15
                        print("Total sorted records :", total_sorted_records)
                        if total_sorted_records > 0:
                            text_info = "Statement is being generated for Stock Sales.Please wait ...."
                            infoLabel.configure(text=text_info, fg='purple')
                            for row_index in range(1, total_sorted_records + 1):
                                if dict_index == 1:
                                    balance = int(sort_sheet.cell(row=row_index + 1, column=2).value)
                                else:
                                    balance = balance + int(sort_sheet.cell(row=row_index + 1, column=2).value)

                                for column_index in range(1, 7):
                                    if column_index == 1:  # Date
                                        text_value = sort_sheet.cell(row=row_index + 1, column=6).value
                                        text_value = text_value.strftime("%d-%b-%Y")
                                    elif column_index == 2:  # Invoice
                                        text_value = sort_sheet.cell(row=row_index + 1, column=9).value
                                    elif column_index == 3:  # Description
                                        text_value = sort_sheet.cell(row=row_index + 1, column=7).value + "-By " + \
                                                     sort_sheet.cell(row=row_index + 1, column=11).value + \
                                                     " From " + sort_sheet.cell(row=row_index + 1, column=5).value
                                    elif column_index == 4:  # Quantity
                                        text_value = sort_sheet.cell(row=row_index + 1, column=10).value
                                    elif column_index == 5:  # credit
                                        text_value = sort_sheet.cell(row=row_index + 1, column=2).value
                                    elif column_index == 6:  # balance
                                        text_value = str(balance)
                                    else:
                                        pass
                                    # print("Text value :", text_value)
                                    critical_stock_sheet.cell(row=starting_index, column=column_index).font = Font(
                                        size=8,
                                        name='Arial',
                                        bold=False)
                                    if column_index == 4 or column_index == 5:
                                        critical_stock_sheet.cell(row=starting_index,
                                                                  column=column_index).alignment = Alignment(
                                            horizontal='center', vertical='center', wrapText=True)
                                    else:
                                        critical_stock_sheet.cell(row=starting_index,
                                                                  column=column_index).alignment = Alignment(
                                            horizontal='left', vertical='center', wrapText=True)
                                    critical_stock_sheet.cell(row=starting_index,
                                                              column=column_index).value = text_value
                                dict_index = dict_index + 1
                                starting_index = starting_index + 1

                            frdateforstatement = fromDate.strftime("%d-%b-%Y")
                            todateforstatement = toDate.strftime("%d-%b-%Y")
                            critical_stock_sheet.cell(row=3, column=6).value = dt_today
                            critical_stock_sheet.cell(row=5, column=6).value = "Stock Sales"
                            critical_stock_sheet.cell(row=8, column=6).value = str(balance)
                            critical_stock_sheet.cell(row=9, column=6).value = str(starting_index - 15)
                            critical_stock_sheet.cell(row=10, column=6).value = frdateforstatement
                            critical_stock_sheet.cell(row=11, column=6).value = todateforstatement
                            wb_critical_stock.save(template_sheet)
                            print("File has been saved for template")
                            destination_copy_folder = InitDatabase.getInstance().get_statement_directory_path()
                            obj_threadClass = myThread(10, "statementThread", 1, template_sheet,
                                                       destination_file, starting_index, viewPDF, printBtn, infoLabel,destination_copy_folder)
                            obj_threadClass.start()

                            print_result = partial(self.obj_commonUtil.open_statement_file,
                                                   template_sheet,
                                                   destination_file, starting_index)
                            printBtn.configure(command=print_result)
                            view_result = partial(self.obj_commonUtil.open_statement_file, template_sheet,
                                                  destination_file, starting_index)
                            viewPDF.configure(command=view_result, )

                            cancel_result = partial(self.closepage, template_sheet, starting_index,
                                                    account_statement_window)
                            cancelbtn.configure(command=cancel_result)
                        else:
                            text_error = "No records present for Stock Sales in specified period!!!"
                            infoLabel.configure(text=text_error, fg='red')
                    else:
                        text_error = "No records present for Stock Sales in specified period!!!"
                        infoLabel.configure(text=text_error, fg='red')
        else:
            infoLabel.configure(text=error_info, fg='red')
