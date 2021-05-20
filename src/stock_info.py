from app_defines import *
from app_common import *
from init_database import *
from app_thread import *


class StockInfo:
    # constructor for Library class
    def __init__(self):
        print("constructor called for noncommercial edit ")
        self.obj_commonUtil = CommonUtil()
        self.dateTimeOp = DatetimeOperation()

    def view_stock_info(self, master):
        self.stockinfo_window = Toplevel(master)

        self.stockinfo_window.title("Stock Information")
        self.stockinfo_window.geometry('840x330+180+170')
        self.stockinfo_window.configure(background='wheat')
        self.stockinfo_window.resizable(width=True, height=False)

        # delete "X" button in window will be not-operational
        self.stockinfo_window.protocol('WM_DELETE_WINDOW', self.obj_commonUtil.donothing)

        imageFrame = Frame(self.stockinfo_window, width=65, height=60,
                           bg="wheat")
        canvas_width, canvas_height = 60, 60
        canvas = Canvas(imageFrame, width=canvas_width, height=canvas_height, highlightthickness=0)
        myimage = ImageTk.PhotoImage(PIL.Image.open("..\\Images\\a_wheat.png").resize((60, 60)))
        canvas.create_image(0, 0, anchor=NW, image=myimage)
        imageFrame.grid(row=0, column=0, pady=2, columnspan=2)
        canvas.grid(row=0, column=0)

        upperFrame = Frame(self.stockinfo_window, width=290, height=100, bd=4, relief='ridge', bg="light yellow")
        infoFrame = Frame(self.stockinfo_window, width=290, height=100, bd=4, relief='ridge', bg="light yellow")
        upperFrame.grid(row=2, column=1, padx=25, pady=10, sticky=W)
        infoFrame.grid(row=3, column=1, padx=115, pady=7, sticky=W)

        info_label = Label(infoFrame, text="Select the appropriate stock type for statement generation", width=60,
                           justify=CENTER,
                           font=('times new roman', 14, 'normal'), bg='light yellow', fg='purple')
        info_label.grid(row=0, column=0)
        dataframe = Frame(upperFrame, width=290, height=100, bg="light yellow")
        dataframe.grid(row=1, column=0, padx=130, pady=3, sticky=W)

        self.middleFrame_bookdisplay = Frame(self.stockinfo_window, width=0, height=0, bd=8, relief='ridge',
                                             bg='light yellow')

        heading = Label(self.stockinfo_window, text="Critical Stock Info", font=('times new roman', 25, 'normal'),
                        bg="wheat")

        stkType_label = Label(dataframe, text="Stock Type", width=12, anchor=W, justify=LEFT,
                              font=('times new roman', 15, 'normal'), bg='light yellow')
        centername_label = Label(dataframe, text="Center Name", width=12, anchor=W, justify=LEFT,
                                 font=('times new roman', 15, 'normal'), bg='light yellow')
        heading.grid(row=1, column=0, columnspan=3)
        stkType_label.grid(row=1, column=2, padx=20, pady=5)
        centername_label.grid(row=2, column=2, padx=20, pady=5)

        stockType_varaible = StringVar(dataframe)
        stockType_varaible.set("Commercial Stock")
        stock_typeOptionMenu = OptionMenu(dataframe, stockType_varaible, 'Commercial Stock',
                                          'Non-Commercial Stock', 'Donated Stock', 'Critical Commercial Stock')
        stock_typeOptionMenu.configure(bg='snow', width=28, fg='black', font=NORM_FONT,
                                       state=NORMAL)

        local_centerText = StringVar(dataframe)
        localCenterList = self.obj_commonUtil.getLocalCenterNames()
        print("Center list  - ", localCenterList)
        local_centerText.set(localCenterList[0])
        localcenter_menu = OptionMenu(dataframe, local_centerText, *localCenterList)
        localcenter_menu.configure(bg='snow', width=28, fg='black', font=NORM_FONT,
                                   state=NORMAL)

        stock_typeOptionMenu.grid(row=1, column=3, padx=15, pady=5)
        localcenter_menu.grid(row=2, column=3, padx=15, pady=5)

        # ---------------------------------Button Frame Start----------------------------------------
        buttonFrame = Frame(upperFrame, width=200, height=100, bd=4, relief='ridge')
        buttonFrame.grid(row=2, column=0, padx=150, pady=5, sticky=W, columnspan=3)

        viewPDF = Button(buttonFrame, text="View PDF", fg="Black",
                         font=NORM_FONT, width=11, bg='light grey', state=DISABLED)
        printBtn = Button(buttonFrame, text="Print", fg="Black",
                          font=NORM_FONT, width=11, bg='light grey', state=DISABLED)
        cancel = Button(buttonFrame, text="Close", fg="Black", command=self.stockinfo_window.destroy,
                        font=NORM_FONT, width=13, bg='light cyan')
        search_result = partial(self.search_stock_info, self.stockinfo_window, stockType_varaible, local_centerText,
                                printBtn, viewPDF, info_label, cancel)

        # create a Search Button and place into the self.stockinfo_window window

        submit = Button(buttonFrame, text="Search", fg="Black", command=search_result,
                        font=NORM_FONT, width=13, bg='light cyan')
        submit.grid(row=0, column=0)
        viewPDF.grid(row=0, column=1)
        printBtn.grid(row=0, column=2)

        # create a Close Button and place into the self.stockinfo_window window
        cancel.grid(row=0, column=3)
        # ---------------------------------Button Frame End----------------------------------------
        # self.middleFrame_bookdisplay.grid(row=2, column=2, padx=65, pady=10, sticky=W)

        self.stockinfo_window.bind('<Return>', lambda event=None: submit.invoke())
        self.stockinfo_window.bind('<Alt-c>', lambda event=None: cancel.invoke())

        self.stockinfo_window.focus()
        self.stockinfo_window.grab_set()
        mainloop()

    def search_stock_info(self, stockInfo_window, stockType_varaible, local_centerText, printBtn, viewPDF, info_label,
                          cancelBtn):
        info_label.configure(text="")
        if stockType_varaible.get() == "Commercial Stock" or \
                stockType_varaible.get() == "Critical Commercial Stock":
            subdir_commercialstock = "..\\Library_Stock\\" + local_centerText.get() + "\\Commercial_Stock"
            filename = subdir_commercialstock + "\\Commercial_Stock.xlsx"
        elif stockType_varaible.get() == "Non-Commercial Stock" or \
                stockType_varaible.get() == "Donated Stock":
            subdir_commercialstock = "..\\Library_Stock\\" + local_centerText.get() + "\\NonCommercial_Stock"
            filename = subdir_commercialstock + "\\noncommercial_stock.xlsx"
        else:
            pass
        print("Filename : ", filename)
        wb_stock = openpyxl.load_workbook(filename)
        stock_sheet = wb_stock.active
        wb_template = openpyxl.load_workbook(PATH_STOCK_INFO_TEMPLATE)
        template_sheet = wb_template.active
        total_records = self.obj_commonUtil.totalrecords_excelDataBase(filename)
        dict_index = 5
        bValidRecord = False
        estimated_value = 0
        if stockType_varaible.get() == "Commercial Stock":
            info_label.configure(text="Statement Generation in progress....please wait ", fg='purple')
            for row_index in range(0, total_records):
                if local_centerText.get() == str(stock_sheet.cell(row=row_index + 2, column=10).value):
                    for column_index in range(1, 10):
                        bValidRecord = True
                        if column_index == 1:
                            text_value = str(dict_index - 4)
                        elif column_index == 2:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=column_index).value)
                        elif column_index == 3:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=9).value)
                        elif column_index == 4:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=3).value)
                        elif column_index == 5:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=4).value)
                        elif column_index == 6:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=8).value)
                        elif column_index == 7:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=5).value)
                        elif column_index == 8:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=7).value)
                        elif column_index == 9:
                            text_value = str(int(stock_sheet.cell(row=row_index + 2, column=7).value) * int(
                                stock_sheet.cell(row=row_index + 2, column=5).value))
                            estimated_value = estimated_value + int(text_value)
                        else:
                            pass
                        template_sheet.cell(row=dict_index, column=column_index).font = Font(size=13,
                                                                                             name='Times New Roman',
                                                                                             bold=False)
                        template_sheet.cell(row=dict_index, column=column_index).alignment = Alignment(
                            horizontal='center', vertical='center', wrapText=True)
                        template_sheet.cell(row=dict_index, column=column_index).value = text_value
                    dict_index = dict_index + 1
            template_sheet.cell(row=2, column=1).value = local_centerText.get()
            template_sheet.cell(row=3, column=3).value = "Rs." + str(estimated_value)
            template_sheet.cell(row=3, column=8).value = str(dict_index - 5)

        elif stockType_varaible.get() == "Critical Commercial Stock":
            info_label.configure(text="Statement Generation in progress....please wait ", fg='purple')
            for row_index in range(0, total_records):
                if int(str(stock_sheet.cell(row=row_index + 2, column=7).value)) < CRITICAL_QUANTITY_LIMIT:
                    if local_centerText.get() == str(stock_sheet.cell(row=row_index + 2, column=10).value):
                        for column_index in range(1, 10):
                            bValidRecord = True
                            if column_index == 1:
                                text_value = str(dict_index - 4)
                            elif column_index == 2:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=column_index).value)
                            elif column_index == 3:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=9).value)
                            elif column_index == 4:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=3).value)
                            elif column_index == 5:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=4).value)
                            elif column_index == 6:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=8).value)
                            elif column_index == 7:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=5).value)
                            elif column_index == 8:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=7).value)
                            elif column_index == 9:
                                text_value = str(int(stock_sheet.cell(row=row_index + 2, column=7).value) * int(
                                    stock_sheet.cell(row=row_index + 2, column=5).value))
                                estimated_value = estimated_value + int(text_value)
                            else:
                                pass
                            template_sheet.cell(row=dict_index, column=column_index).font = Font(size=13,
                                                                                                 name='Times New Roman',
                                                                                                 bold=False)
                            template_sheet.cell(row=dict_index, column=column_index).alignment = Alignment(
                                horizontal='center', vertical='center', wrapText=True)
                            template_sheet.cell(row=dict_index, column=column_index).value = text_value
                        dict_index = dict_index + 1
            template_sheet.cell(row=2, column=1).value = str(stock_sheet.cell(row=row_index + 2, column=10).value)
            template_sheet.cell(row=3, column=3).value = "Rs." + str(estimated_value)
            template_sheet.cell(row=3, column=8).value = str(dict_index - 5)

        elif stockType_varaible.get() == "Non-Commercial Stock":
            info_label.configure(text="Statement Generation in progress....please wait ", fg='purple')
            for row_index in range(0, total_records):
                if local_centerText.get() == str(stock_sheet.cell(row=row_index + 2, column=17).value):
                    for column_index in range(1, 10):
                        bValidRecord = True
                        if column_index == 1:
                            text_value = str(dict_index - 4)
                        elif column_index == 2:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=column_index).value)
                        elif column_index == 3:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=9).value)
                        elif column_index == 4:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=3).value)
                        elif column_index == 5:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=15).value)
                        elif column_index == 6:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=16).value)
                        elif column_index == 7:
                            text_value = "Not Applicable"
                        elif column_index == 8:
                            text_value = str(stock_sheet.cell(row=row_index + 2, column=4).value)
                        elif column_index == 9:
                            text_value = str(int(stock_sheet.cell(row=row_index + 2, column=5).value))
                            estimated_value = estimated_value + int(text_value)
                        else:
                            pass
                        template_sheet.cell(row=dict_index, column=column_index).font = Font(size=13,
                                                                                             name='Times New Roman',
                                                                                             bold=False)
                        template_sheet.cell(row=dict_index, column=column_index).alignment = Alignment(
                            horizontal='center', vertical='center', wrapText=True)
                        template_sheet.cell(row=dict_index, column=column_index).value = text_value
                    dict_index = dict_index + 1
            # filling the center name
            template_sheet.cell(row=2, column=1).value = local_centerText.get()
            template_sheet.cell(row=3, column=3).value = "Rs." + str(estimated_value)
            template_sheet.cell(row=3, column=8).value = str(dict_index - 5)

        elif stockType_varaible.get() == "Donated Stock":
            text_info = "Statement Generation in progress....please wait"
            info_label.configure(text=text_info, fg='purple')
            for row_index in range(0, total_records):
                if (str(stock_sheet.cell(row=row_index + 2, column=15).value)) == "Donated":
                    if local_centerText.get() == str(stock_sheet.cell(row=row_index + 2, column=17).value):
                        for column_index in range(1, 10):
                            bValidRecord = True
                            if column_index == 1:
                                text_value = str(dict_index - 4)
                            elif column_index == 2:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=column_index).value)
                            elif column_index == 3:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=9).value)
                            elif column_index == 4:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=3).value)
                            elif column_index == 5:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=15).value)
                            elif column_index == 6:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=16).value)
                            elif column_index == 7:
                                text_value = "Not Applicable"
                            elif column_index == 8:
                                text_value = str(stock_sheet.cell(row=row_index + 2, column=4).value)
                            elif column_index == 9:
                                text_value = str(int(stock_sheet.cell(row=row_index + 2, column=5).value))
                                estimated_value = estimated_value + int(text_value)
                            else:
                                pass
                            template_sheet.cell(row=dict_index, column=column_index).font = Font(size=13,
                                                                                                 name='Times New Roman',
                                                                                                 bold=False)
                            template_sheet.cell(row=dict_index, column=column_index).alignment = Alignment(
                                horizontal='center', vertical='center', wrapText=True)
                            template_sheet.cell(row=dict_index, column=column_index).value = text_value
                        dict_index = dict_index + 1
            template_sheet.cell(row=2, column=1).value = local_centerText.get()
            template_sheet.cell(row=3, column=3).value = "Rs." + str(estimated_value)
            template_sheet.cell(row=3, column=8).value = str(dict_index - 5)

        if bValidRecord:
            now = datetime.now()
            dt_string = now.strftime("%d_%b_%Y_%H%M%S")
            dateForSheet = now.strftime("%d-%b-%Y")

            # writting the date in the template sheet
            template_sheet.cell(row=2, column=8).value = str(dateForSheet)
            template_sheet.cell(row=2, column=4).value = str(stockType_varaible.get())
            wb_template.save(PATH_STOCK_INFO_TEMPLATE)

            destination_file = "..\\Library_Stock\\Stock_Statement\\Stock_Statement_" + dt_string + ".pdf"
            desktop_repo = InitDatabase.getInstance().get_desktop_statement_directory_path()
            obj_threadClass = myThread(12, "stockinfoThread", 1, PATH_STOCK_INFO_TEMPLATE,
                                       destination_file, dict_index, viewPDF, printBtn, info_label,
                                       desktop_repo)
            obj_threadClass.start()

            viewPDF.configure(state=NORMAL, bg="light cyan")
            view_result = partial(self.viewPDF, destination_file, dict_index)
            viewPDF.configure(command=view_result)

            printBtn.configure(state=NORMAL, bg="light cyan")
            print_result = partial(self.print_inventory, destination_file, dict_index)
            printBtn.configure(command=print_result)

            close_result = partial(self.clearExcelandCloseWindow, dict_index, stockInfo_window)
            cancelBtn.configure(command=close_result)
        else:
            info_label.configure(text="No record found !!!", fg='red')
            viewPDF.configure(state=DISABLED, bg="light grey")
            printBtn.configure(state=DISABLED, bg="light grey")


    def print_inventory(self, fileToPrint, dict_index):
        os.startfile(fileToPrint, 'print')
        self.clearStockInfoTemplateSheet(dict_index)

    def viewPDF(self, fileToPrint, dict_index):
        os.startfile(fileToPrint)
        self.clearStockInfoTemplateSheet(dict_index)

    def clearStockInfoTemplateSheet(self, totatrecords):
        # executed only if
        wb_template = openpyxl.load_workbook(PATH_STOCK_INFO_TEMPLATE)
        template_sheet = wb_template.active
        print("Total records for clearing :", totatrecords)
        for rows in range(5, totatrecords + 1):
            for columns in range(1, 10):
                template_sheet.cell(row=rows, column=columns).value = ""

        wb_template.save(PATH_STOCK_INFO_TEMPLATE)

    def clearExcelandCloseWindow(self, dict_index, current_window):
        self.clearStockInfoTemplateSheet(dict_index)
        current_window.destroy()
