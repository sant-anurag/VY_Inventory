from app_defines import *
from app_common import *
from init_database import *
from app_thread import *
import MySQLdb as sql_db


class InventoryReport:

    # constructor for Library class
    def __init__(self, master):
        self.obj_commonUtil = CommonUtil()
        self.dateTimeOp = DatetimeOperation()
        self.stock_info_window = Toplevel(master)
        self.stock_info_window.title("Inventory Report")
        self.stock_info_window.geometry('800x270+700+380')
        self.stock_info_window.configure(background='wheat')
        self.stock_info_window.resizable(width=False, height=False)
        self.stock_info_window.protocol('WM_DELETE_WINDOW', self.obj_commonUtil.donothing)
        self.list_InvoicePrint = []
        canvas_width, canvas_height = 800, 270
        canvas = Canvas(self.stock_info_window, width=canvas_width, height=canvas_height)
        myimage = ImageTk.PhotoImage(
            PIL.Image.open("..\\Images\\Logos\\Geometry-Header-1920x1080.jpg"))
        canvas.create_image(0, 0, anchor=NW, image=myimage)
        canvas.pack()

        self.stockReportFrame = Frame(self.stock_info_window, width=760, height=120, bd=4, relief='ridge',
                                      bg='snow')
        self.stockReportFrame.pack()

        self.infoFrame = Frame(self.stock_info_window, width=760, height=50, bd=4, relief='ridge', bg="light yellow")
        self.infoFrame.pack()

        self.btn_generate = Button(self.stock_info_window)
        self.btn_generate.configure(text="Generate", fg="Black", font=XL_FONT, width=12, state=NORMAL, bg='RosyBrown1')
        self.btn_viewPDF = Button(self.stock_info_window, text="View PDF", fg="Black", font=XL_FONT, width=12,
                                  bg='light grey', state=DISABLED)
        self.btn_printBtn = Button(self.stock_info_window, text="Print", fg="Black", font=XL_FONT, width=12,
                                   bg='light grey', state=DISABLED)
        self.btn_cancel = Button(self.stock_info_window, text="Exit", fg="Black",
                                 font=XL_FONT, width=12, state=NORMAL, bg='RosyBrown1')
        self.btn_cancel.configure(command=self.stock_info_window.destroy)

        self.info_label = Label(self.infoFrame, text="Select the parameters and press <Generate>", width=49,
                                justify=CENTER,
                                font=L_FONT, bg='light yellow', fg='purple')

        # Bottom button panel - end
        self.btn_generate.place(x=20, y=142)
        self.btn_viewPDF.place(x=210, y=142)
        self.btn_printBtn.place(x=400, y=142)
        self.btn_cancel.place(x=590, y=142)

        print("constructor called for sales ")

        # default window is "Add New Inventor" when window opens
        self.report_inventory_item(master)

    def myfunction(self, mycanvas, frame, event):
        print("Scroll Encountered")
        mycanvas.configure(scrollregion=mycanvas.bbox("all"), width=722, height=400)

    def report_inventory_item(self, master):
        center_label = Label(self.stockReportFrame, text="Item Name", width=11, anchor=W, justify=LEFT,
                             font=('times new roman', 20, 'normal'),
                             bg='snow')

        stockType_label = Label(self.stockReportFrame, text="Author", width=11, anchor=W, justify=LEFT,
                                font=('times new roman', 20, 'normal'),
                                bg='snow')

        local_centerText = StringVar(self.stockReportFrame)
        localCenterList = self.obj_commonUtil.get_centerNames()
        print("Center list  - ", localCenterList)
        newCenterList = []
        iloop = 0
        for x in localCenterList:
            newCenterList.append(x[0])
            iloop = iloop + 1
        print("Center list  - ", newCenterList)
        local_centerText.set(newCenterList[0])
        localcenter_menu = OptionMenu(self.stockReportFrame, local_centerText, *newCenterList)
        localcenter_menu.configure(width=45, font=('times new roman', 17, 'normal'), bg='light cyan', anchor=W,
                                   justify=LEFT)

        item_TypeText = StringVar(self.stockReportFrame)
        itemtypeList = ['Commercial', 'Non-Commercial', 'Critical Stock']
        print("Item Type list  - ", itemtypeList)
        item_TypeText.set(itemtypeList[0])
        item_Typemenu = OptionMenu(self.stockReportFrame, item_TypeText, *itemtypeList)
        item_Typemenu.configure(width=45, font=('times new roman', 17, 'normal'), bg='light cyan', anchor=W,
                                justify=LEFT)

        self.stockReportFrame.place(x=20, y=20)
        self.infoFrame.place(x=20, y=200)

        center_label.place(x=30, y=5)
        stockType_label.place(x=30, y=50)
        localcenter_menu.place(x=180, y=5)
        item_Typemenu.place(x=180, y=50)
        self.info_label.place(x=2, y=2)
        search_result = partial(self.search_stock_info, local_centerText, item_TypeText)
        self.btn_generate.configure(command=search_result)

        self.stock_info_window.bind('<Return>', lambda event=None: self.btn_generate.invoke())
        self.stock_info_window.bind('<F10>', lambda event=None: self.btn_generate.invoke())
        self.stock_info_window.bind('<F9>', lambda event=None: self.btn_viewPDF.invoke())
        self.stock_info_window.bind('<Escape>', lambda event=None: self.btn_cancel.invoke())

        self.stock_info_window.focus()
        self.stock_info_window.grab_set()
        mainloop()

    def search_stock_info(self, localcenter_menu, item_Typemenu):
        print("searching the specified list for :", localcenter_menu.get(), " Of Stock type :", item_Typemenu.get())
        result_list = []
        search_type = REGULAR_STOCK
        if item_Typemenu.get() == "Critical Stock":
            search_type = CRITICAL_STOCK
        result_list = self.getSearchList(localcenter_menu, item_Typemenu,search_type)
        print(result_list)

        wb_template = openpyxl.load_workbook(PATH_STOCK_INFO_TEMPLATE)
        template_sheet = wb_template.active
        dict_index = 5
        bValidRecord = False
        estimated_value = 0
        for row_index in range(0, len(result_list)):
            for column_index in range(1, 10):
                bValidRecord = True
                if column_index == 1:
                    text_value = str(dict_index - 4)
                elif column_index == 2:
                    text_value = str(result_list[row_index][1])
                elif column_index == 3:
                    text_value = str(result_list[row_index][8])
                elif column_index == 4:
                    text_value = str(result_list[row_index][2])
                elif column_index == 5:
                    text_value = str(result_list[row_index][3])
                elif column_index == 6:
                    text_value = str(result_list[row_index][7])
                elif column_index == 7:
                    text_value = str(result_list[row_index][4])
                elif column_index == 8:
                    text_value = str(result_list[row_index][6])
                elif column_index == 9:
                    text_value = str(int(str(result_list[row_index][4])) * int(str(result_list[row_index][6])))
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

        template_sheet.cell(row=2, column=1).value = localcenter_menu.get()
        template_sheet.cell(row=3, column=3).value = "Rs." + str(estimated_value)
        template_sheet.cell(row=3, column=8).value = str(dict_index - 5)

        if bValidRecord:
            now = datetime.now()
            dt_string = now.strftime("%d_%b_%Y_%H%M%S")
            dateForSheet = now.strftime("%d-%b-%Y")

            # writing the date in the template sheet
            template_sheet.cell(row=2, column=8).value = str(dateForSheet)
            template_sheet.cell(row=2, column=4).value = str(item_Typemenu.get())
            wb_template.save(PATH_STOCK_INFO_TEMPLATE)

            destination_file = "..\\Library_Stock\\Stock_Statement\\Stock_Statement_" + dt_string + ".pdf"

            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

            print("The Desktop path is: " + desktop)

            desktop_repo = desktop + "\\Inventory\\Statements"

            if not os.path.exists(desktop_repo):
                print("Statements Directory")
                os.makedirs(desktop_repo)

            obj_threadClass = myThread(12, "stockinfoThread", 1, PATH_STOCK_INFO_TEMPLATE,
                                       destination_file, dict_index, self.btn_viewPDF, self.btn_printBtn,
                                       self.info_label,
                                       desktop_repo)
            obj_threadClass.start()

            self.btn_viewPDF.configure(state=NORMAL, bg="RosyBrown1")
            view_result = partial(self.viewPDF, destination_file, dict_index)
            self.btn_viewPDF.configure(command=view_result)

            self.btn_printBtn.configure(state=NORMAL, bg="RosyBrown1")
            print_result = partial(self.print_inventory, destination_file, dict_index)
            self.btn_printBtn.configure(command=print_result)

            close_result = partial(self.clearExcelandCloseWindow, dict_index, self.stock_info_window)
            self.btn_cancel.configure(command=close_result)
        else:
            self.info_label.configure(text="No record found !!!", fg='red')
            self.btn_viewPDF.configure(state=DISABLED, bg="light grey")
            self.btn_printBtn.configure(state=DISABLED, bg="light grey")

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

    def getSearchList(self, localcenter_menu, item_Typemenu,search_type):
        print("getSearchList--> Start ")
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        if search_type == REGULAR_STOCK:
            result_query = cursor.execute("SELECT * FROM inventory_stock where Center_Name = %s and Stock_Type = %s",
                                          (localcenter_menu.get(), item_Typemenu.get()))
        elif search_type == CRITICAL_STOCK:
            # CRITICAL STOCK is defined Quantity < 5 for an inventory item
            result_query = cursor.execute("SELECT * FROM inventory_stock where Center_Name = %s and Quantity < '5'",
                                          (localcenter_menu.get(),))
        result = cursor.fetchall()
        return result
