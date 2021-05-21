from app_defines import *
from app_common import *
from app_thread import *
import MySQLdb as sql_db


class InventorySales:

    # constructor for Library class
    def __init__(self, master):
        self.obj_commonUtil = CommonUtil()
        self.dateTimeOp = DatetimeOperation()
        self.sales_window = Toplevel(master)
        self.sales_window.title("Sales")
        self.sales_window.geometry('1000x750+700+150')
        self.sales_window.configure(background='wheat')
        self.sales_window.resizable(width=False, height=False)
        self.sales_window.protocol('WM_DELETE_WINDOW', self.obj_commonUtil.donothing)
        self.list_InvoicePrint = []
        canvas_width, canvas_height = 1000, 750
        canvas = Canvas(self.sales_window, width=canvas_width, height=canvas_height)
        myimage = ImageTk.PhotoImage(
            PIL.Image.open("..\\Images\\Logos\\Geometry-Header-1920x1080.jpg"))
        canvas.create_image(0, 0, anchor=NW, image=myimage)
        canvas.pack()

        self.dataEntryFrame = Frame(self.sales_window, width=800, height=500, bd=4, relief='ridge',
                                    bg='snow')
        self.dataEntryFrame.pack()
        self.dataModifyFrame = Frame(self.sales_window, width=800, height=500, bd=4, relief='ridge',
                                     bg='snow')
        self.dataModifyFrame.pack()
        self.dataSearchFrame = Frame(self.sales_window, width=800, height=500, bd=4, relief='ridge',
                                     bg='snow')
        self.dataSearchFrame.pack()

        self.authorFrame = Frame(self.sales_window, width=800, height=500, bd=4, relief='ridge',
                                 bg='snow')
        self.authorFrame.pack()

        self.btn_addToCart = Button(self.sales_window)
        self.btn_addToCart.configure(text="Add To Cart", fg="Black", font=XXL_FONT, width=13, state=NORMAL,
                                     bg='RosyBrown1')
        self.btn_print = Button(self.sales_window)
        self.btn_print.configure(text="Print", fg="Black", font=XXL_FONT, width=13, state=NORMAL,
                                 bg='RosyBrown1')

        self.btn_submit = Button(self.sales_window)
        self.btn_submit.configure(text="Buy", fg="Black", font=XXL_FONT, width=13, state=NORMAL, bg='RosyBrown1')

        self.btn_cancel = Button(self.sales_window, text="Exit", fg="Black",
                                 font=XXL_FONT, width=13, state=NORMAL, bg='RosyBrown1')
        self.btn_cancel.configure(command=self.sales_window.destroy)
        self.btn_clear = Button(self.sales_window, text="Reset", fg="Black",
                                font=XXL_FONT, width=13, state=NORMAL, bg='RosyBrown1')

        # Bottom button panel - end
        self.btn_addToCart.place(x=5, y=675)
        self.btn_submit.place(x=253, y=675)
        self.btn_clear.place(x=500, y=675)
        self.btn_cancel.place(x=748, y=675)
        print("constructor called for sales ")

        # default window is "Add New Inventor" when window opens
        self.sales_inventory_item(master)

    def myfunction(self, mycanvas, frame, event):
        print("Scroll Encountered")
        mycanvas.configure(scrollregion=mycanvas.bbox("all"), width=722, height=400)

    def sales_inventory_item(self, master):
        self.dataEntryFrame.destroy()
        self.dataModifyFrame.destroy()
        self.dataSearchFrame = Frame(self.sales_window, width=760, height=650, bd=4, relief='ridge',
                                     bg='snow')
        self.dataSearchFrame.pack()

        salesSummaryframe = Frame(self.sales_window, width=230, height=650, bd=4, relief='ridge',
                                  bg='light yellow')
        salesSummaryframe.pack()

        frameSearch = Frame(self.dataSearchFrame, width=735, height=50, bd=4, relief='ridge',
                            bg='snow')
        frameSearch.pack()
        framedisplay = Frame(self.dataSearchFrame, width=735, height=300, bd=4, relief='ridge',
                             bg='snow')
        framedisplay.pack()

        framepurchase = Frame(self.dataSearchFrame, width=735, height=250, bd=4, relief='ridge',
                              bg='snow')
        framepurchase.pack()

        framelower = Frame(self.dataSearchFrame, width=735, height=90, bd=4, relief='ridge',
                           bg='snow')
        framelower.pack()

        # create a item Name label

        item_SearchId = Label(frameSearch, text="Search Item Id", width=11, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'),
                              bg='snow')

        item_namelabel = Label(framedisplay, text="Item Name", width=11, anchor=W, justify=LEFT,
                               font=('times new roman', 20, 'normal'),
                               bg='snow')

        author = Label(framedisplay, text="Author", width=11, anchor=W, justify=LEFT,
                       font=('times new roman', 20, 'normal'),
                       bg='snow')

        # create a Price label
        price = Label(framedisplay, text="Price(Rs.)", width=13, anchor=W, justify=LEFT,
                      font=('times new roman', 20, 'normal'), bg='snow')

        # create a Quantity label
        quantity = Label(framedisplay, text="Quantity", width=13, anchor=W, justify=LEFT,
                         font=('times new roman', 20, 'normal'), bg='snow')

        # create a borrow fee label
        borrowFee = Label(framedisplay, text="Center", width=13, anchor=W, justify=LEFT,
                          font=('times new roman', 20, 'normal'), bg='snow')

        purchase_headline = Label(framepurchase, text="Purchase Details", width=13, anchor=W, justify=LEFT,
                                  font=('times new roman', 20, 'normal'), bg='snow', fg='red')

        purchase_quantitylbl = Label(framepurchase, text="Quantity", width=13, anchor=W, justify=LEFT,
                                     font=('times new roman', 20, 'normal'), bg='snow')
        purchase_CustomerNamelbl = Label(framepurchase, text="Name", width=13, anchor=W, justify=LEFT,
                                         font=('times new roman', 20, 'normal'), bg='snow')
        purchase_ContactNolbl = Label(framepurchase, text="Contact Number", width=13, anchor=W, justify=LEFT,
                                      font=('times new roman', 20, 'normal'), bg='snow')
        purchase_Addresslbl = Label(framepurchase, text="Address", width=13, anchor=W, justify=LEFT,
                                    font=('times new roman', 20, 'normal'), bg='snow')

        self.dataSearchFrame.place(x=5, y=20)
        salesSummaryframe.place(x=765, y=20)
        frameSearch.place(x=10, y=5)
        framedisplay.place(x=10, y=60)
        framepurchase.place(x=10, y=300)

        item_SearchId.place(x=30, y=5)

        item_namelabel.place(x=30, y=5)
        author.place(x=30, y=50)
        price.place(x=30, y=100)
        quantity.place(x=30, y=140)
        borrowFee.place(x=30, y=185)

        purchase_headline.place(x=30, y=5)
        purchase_quantitylbl.place(x=30, y=50)
        purchase_CustomerNamelbl.place(x=30, y=95)
        purchase_ContactNolbl.place(x=30, y=140)
        purchase_Addresslbl.place(x=30, y=195)

        item_idforSearch = Entry(frameSearch, width=20, font=('times new roman', 20, 'normal'), bg='light cyan')
        btn_search = Button(frameSearch)

        item_name = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                          font=('times new roman', 20, 'normal'),
                          bg='light cyan')

        author_menu = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                            font=('times new roman', 20, 'normal'),
                            bg='light cyan')

        item_price = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                           font=('times new roman', 20, 'normal'),
                           bg='light cyan')

        item_quantity = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'),
                              bg='light cyan')
        item_borrowfee = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                               font=('times new roman', 20, 'normal'),
                               bg='light cyan')
        localcenter_menu = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                                 font=('times new roman', 20, 'normal'),
                                 bg='light cyan')
        item_idforSearch.place(x=240, y=5)
        item_name.place(x=240, y=5)
        author_menu.place(x=240, y=50)
        item_price.place(x=240, y=100)
        item_quantity.place(x=240, y=145)
        item_borrowfee.place(x=240, y=190)
        localcenter_menu.place(x=240, y=235)

        quantity_entry = Entry(framepurchase, width=34,font=('times new roman', 20, 'normal'), bg='light cyan')

        name_entry = Entry(framepurchase, width=34, font=('times new roman', 20, 'normal'), bg='light cyan')

        contact_entry = Entry(framepurchase, width=34, font=('times new roman', 20, 'normal'), bg='light cyan')
        address_entry = Entry(framepurchase, width=34, text='0', font=('times new roman', 20, 'normal'),
                              bg='light cyan')

        quantity_entry.place(x=240, y=50)
        name_entry.place(x=240, y=100)
        contact_entry.place(x=240, y=145)
        address_entry.place(x=240, y=190)

        cartCount_label = Label(framelower, text="Cart Count", width=13, anchor=W, justify=LEFT,
                                font=('times new roman', 20, 'normal'), bg='snow')
        billAmount_label = Label(framelower, text="Bill Amt.(Rs.)", width=13, anchor=W, justify=LEFT,
                                 font=('times new roman', 20, 'normal'), bg='snow')

        cartCount_text = Label(framelower, width=10, anchor=W, justify=LEFT,
                               font=('times new roman', 20, 'normal'),
                               bg='light cyan')
        billAmount_text = Label(framelower, width=14, anchor=W, justify=LEFT,
                                font=('times new roman', 20, 'normal'),
                                bg='light cyan')

        cartCount_label.place(x=30, y=15)
        cartCount_text.place(x=170, y=15)
        billAmount_label.place(x=330, y=15)
        billAmount_text.place(x=500, y=15)

        search_result = partial(self.search_itemId, item_idforSearch, item_name, author_menu,
                                item_price,
                                item_borrowfee,
                                item_quantity, OPERATION_SEARCH)

        btn_search.configure(text="Search", fg="Black", command=search_result,
                             font=('arial narrow', 14, 'normal'), width=19, state=NORMAL, bg='RosyBrown1')
        btn_search.place(x=540, y=2)
        addToCart_result = partial(self.addToCart, item_idforSearch, item_name, quantity_entry, item_price,
                                   cartCount_text, billAmount_text)
        self.btn_addToCart.configure(command=addToCart_result)
        purchase_result = partial(self.purchase_stock_item, name_entry, contact_entry, address_entry)
        self.btn_submit.configure(command=purchase_result)
        self.btn_submit.configure(state=DISABLED, bg='light grey')
        framelower.place(x=10, y=550)
        # Bottom button panel - start

        self.sales_window.bind('<Return>', lambda event=None: btn_search.invoke())
        self.sales_window.bind('<Alt-b>', lambda event=None: self.btn_submit.invoke())
        self.sales_window.bind('<Escape>', lambda event=None: self.btn_cancel.invoke())
        self.sales_window.bind('<Alt-r>', lambda event=None: self.btn_clear.invoke())

        self.sales_window.focus()
        self.sales_window.grab_set()
        mainloop()

    def addToCart(self, item_idforSearch, item_name, quantity_entry, item_price, cartCount_text, billAmount_text):
        print("Adding to Cart Item Id :", item_idforSearch.get())
        bItemExists = False
        bValidQuantity = True
        # validate if item already exists in cart
        for iLoop in range(0, len(self.list_InvoicePrint)):
            if item_idforSearch.get() == self.list_InvoicePrint[iLoop][0]:
                print("Item Already exists in Cart")
                messagebox.showwarning("Duplicate Entry", "Item already in cart")
                bItemExists = True
        if not bItemExists:
            # check for valid quantity availability
            bValidQuantity = self.isQuantityValid(item_idforSearch.get(), quantity_entry.get())
            print("Valid Quantity :", bValidQuantity)
            if bValidQuantity:
                # prepare the cart locally and retain it as long as purchase button is pressed
                # this implementation list of array strategy to store the temporary cart items
                # cart items are flushed out once "Buy" event is executed
                arr_InvoiceRecords = [item_idforSearch.get(), item_name.cget("text"), quantity_entry.get(),
                                      int(item_price.cget("text"))]
                self.list_InvoicePrint.append(arr_InvoiceRecords)

                cartCount_text['text'] = str(len(self.list_InvoicePrint))

                # calculate the total mrp
                total_cart_mrp = 0
                for iLoop in range(0, len(self.list_InvoicePrint)):
                    total_cart_mrp = total_cart_mrp + (int(self.list_InvoicePrint[iLoop][2]) * int(
                        self.list_InvoicePrint[iLoop][3]))

                billAmount_text['text'] = str(total_cart_mrp)
                self.btn_submit.configure(state=NORMAL, bg='light cyan')
                print("Added to Cart Item Id :", item_idforSearch)
            else:
                messagebox.showwarning("Invalid Quantity !", "Quantity is Invalid")

    def purchase_stock_item(self, customer_name, customer_contact, customer_address):
        self.btn_addToCart.configure(state=DISABLED, bg='light grey')
        print("Customer Name :", customer_name.get(), "Contact :", customer_contact.get(), "Address :",
              customer_address.get())
        libMemberId = "Not Available"
        dateTimeObj = date.today()
        dateOfPurchase = dateTimeObj.strftime("%Y-%m-%d ")
        # validate the member , if  already registered
        print(" Cart items :", self.list_InvoicePrint)
        invoice_id = self.generate_StockPurchase_invoiceID()
        # reading the cart and modifying the database with new quantity
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')
        for cartLoop in range(0, len(self.list_InvoicePrint)):
            print("Purchase step 1  -  Modifying Quantity of Item :", self.list_InvoicePrint[cartLoop][1])
            # Creating a cursor object using the cursor() method
            cursor = conn.cursor()
            current_stock_quantity = self.get_currentStockQuantity(self.list_InvoicePrint[cartLoop][0])
            new_quantity = current_stock_quantity - int(self.list_InvoicePrint[cartLoop][2])
            sql = "UPDATE inventory_stock set Quantity = %s where Item_Id = %s "
            values = (new_quantity, self.list_InvoicePrint[cartLoop][0])
            cursor.execute(sql, values)
            conn.commit()
        conn.close()
        self.btn_submit.configure(state=DISABLED, bg='light grey')

        # Clear the cart since , purchase has happened .
        self.list_InvoicePrint = []

        # generate Invoice
        self.generateInvoicePage(customer_name,
                                 libMemberId,
                                 dateOfPurchase,
                                 customer_contact,
                                 customer_address,
                                 invoice_id)

    def generateInvoicePage(self, customer_name,
                            libMemberId,
                            dateOfPurchase,
                            customer_contact,
                            customer_address,
                            invoice_id):

        print("Purchase Step 2 - Generating Invoice")
        file_name = "..\\Library_Stock\\Invoices\\Template\\sales-invoice.xlsx"
        # searchinfo_label.configure(text="Invoice is being generated. Please wait ...", fg="purple")
        wb_obj = openpyxl.load_workbook(file_name)
        sheet_obj = wb_obj.active

        sheet_obj.cell(row=10, column=1).value = "Address"
        sheet_obj.cell(row=11, column=1).value = customer_address.get()
        sheet_obj.cell(row=12, column=1).value = "Pin-code : NA"

        sheet_obj.cell(row=2, column=6).value = dateOfPurchase
        sheet_obj.cell(row=3, column=6).value = invoice_id
        sheet_obj.cell(row=9, column=1).value = customer_name.get()

        sheet_obj.cell(row=13, column=1).value = customer_contact.get()

        sheet_obj.cell(row=16, column=1).value = "Admin"
        sheet_obj.cell(row=16, column=2).value = customer_name.get()
        sheet_obj.cell(row=16, column=3).value = libMemberId
        sheet_obj.cell(row=16, column=4).value = customer_contact.get()

        final_paymentValue = 0
        # clear the existing sales template
        for iLoop_row in range(0, 10):
            for iLoop_column in range(1, 7):
                sheet_obj.cell(row=19 + iLoop_row, column=iLoop_column).value = ""

        # filling the purchase details in invoice
        for iLoop in range(0, len(self.list_InvoicePrint)):
            tax = int(self.list_InvoicePrint[iLoop][2]) * (TAX_ON_MRP / 100)
            sheet_obj.cell(row=19 + iLoop, column=1).value = str(iLoop + 1)
            sheet_obj.cell(row=19 + iLoop, column=2).value = str(self.list_InvoicePrint[iLoop][1])  # Name
            sheet_obj.cell(row=19 + iLoop, column=3).value = str(self.list_InvoicePrint[iLoop][2])  # quantity
            sheet_obj.cell(row=19 + iLoop, column=4).value = str(self.list_InvoicePrint[iLoop][3])  # price of each item
            sheet_obj.cell(row=19 + iLoop, column=5).value = str(tax)
            sheet_obj.cell(row=19 + iLoop, column=6).value = str(
                ((int(self.list_InvoicePrint[iLoop][2])) * int(self.list_InvoicePrint[iLoop][3])) + int(tax))
            final_paymentValue = final_paymentValue + int(sheet_obj.cell(row=19 + iLoop, column=6).value)

        sheet_obj.cell(row=29, column=6).value = str(final_paymentValue)

        # print("Invoice records  :")
        # for iLoop in range(0, len(self.list_InvoicePrint)):
        # print(" Record :", iLoop + 1, " :", self.list_InvoicePrint[iLoop][1])

        wb_obj.save(file_name)
        today = datetime.now()
        year = today.strftime("%Y")
        dirname = "..\\Library_Stock\\Invoices\\" + year
        if not os.path.exists(dirname):
            print("Current year directory is not available , hence building one")
            os.makedirs(dirname)
        dest_file = dirname + "\\" + invoice_id + ".pdf "
        dest_desktop_file = self.obj_initDatabase.get_desktop_invoices_directory_path() + "\\" + invoice_id + ".pdf "
        self.obj_commonUtil.convertExcelToPdf(file_name, dest_file)
        # os.startfile(dest_file, 'print')
        # invoice_info = "Invoice is ready ! Invoice Id : " + invoice_id
        # searchinfo_label.configure(text=invoice_info, fg='purple')
        # copyfile(dest_file, dest_desktop_file)

        self.btn_print.configure(state=NORMAL, bg='light cyan')
        #        print_result = partial(self.printInvoice, dest_file)
        # self.btn_print.configure(command=print_result)

        # disable to add to cart and purchase button, so that same invoice is not generated twice
        self.btn_submit.configure(state=DISABLED, bg='light grey')
        self.btn_addToCart.configure(state=DISABLED, bg='light grey')

        # update the invoice table
        # self.obj_commonUtil.updateInvoiceTable(invoice_id, dest_file)

        # self.obj_commonUtil.clearSales_InvoiceData(file_name,len(self.list_InvoicePrint))

    def check_SaveItemBtn_state(self, *args):
        print("Tracing  entry input")

        if self.default_text1.get() != "" and \
                self.default_text3.get() != "" and \
                self.default_text4.get() != "" and \
                self.default_text5.get() != "":

            self.btn_submit.configure(state=NORMAL, bg='RosyBrown1')
        else:
            self.btn_submit.configure(state=DISABLED, bg='light grey')

    # Function for clearing the
    # contents of text entry boxes
    def clear_form(self, name, author, price, quantity, borrowFee):
        # clear the content of text entry box
        name.delete(0, END)
        name.configure(fg='black')
        # author.delete(0, END)
        # author.configure(fg='black')
        price.delete(0, END)
        price.configure(fg='black')
        quantity.delete(0, END)
        quantity.configure(fg='black')
        borrowFee.delete(0, END)
        borrowFee.configure(fg='black')

    def stock_operations(self, sales_window, item_name, item_idforSearch, author_name, item_price, item_borrowfee,
                         item_quantity,
                         rack_location, cal, local_centerText, item_TypeText, op_type, receiver_name, order_id,
                         sender_name):

        dateTimeObj = cal.get_date()

        receival_date = dateTimeObj.strftime("%Y-%m-%d")
        if op_type == OPERATION_ADD:
            item_id = self.generate_itemId(local_centerText.get())  # generates a unique item id
        elif op_type == OPERATION_EDIT:
            item_id = item_idforSearch.get()
        if item_name.get() == "" or author_name.get() == "" or item_price.get() == "" or item_quantity.get() == "" or item_borrowfee.get() == "":
            messagebox.showinfo("Data Entry Error", "All fields are mandatory !!!")

        else:
            bitemExists = self.validate_itemName(item_name.get(), local_centerText.get())
            print("bitemExists :", bitemExists)
            if bitemExists and op_type is OPERATION_ADD:
                messagebox.showwarning("Duplicate Entry Error !", "item already exists !!")
                item_name.configure(bd=2, fg='red')
                return
            else:
                conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()
                total_records = cursor.execute("SELECT * FROM inventory_stock")
                conn.close()

                if total_records is 0:
                    serial_no = 1
                else:
                    serial_no = total_records + 1

                # establishing the connection
                print("debug 1")
                conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')
                print("debug 2")
                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()
                print("debug 3")
                itemname = str(item_name.get())
                author = str(author_name.get())
                price = int(item_price.get())
                borrow_fee = int(item_borrowfee.get())
                quantity = int(item_quantity.get())
                location = rack_location.get()
                localcenter = local_centerText.get()
                stocktype = item_TypeText.get()
                receiver = receiver_name.get()
                orderid = order_id.get()
                sendername = sender_name.get()
                print("\n", serial_no, item_id, itemname, author, price, borrow_fee, quantity, location, receival_date,
                      localcenter, stocktype, stocktype, receiver, orderid, sendername)
                if op_type is OPERATION_ADD:
                    print("\n Add operation type")
                    sql = "INSERT INTO inventory_stock VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s,%s, %s, %s)"
                    values = (
                        serial_no, item_id, itemname, author, price, borrow_fee, quantity, location, receival_date,
                        localcenter, stocktype, receiver, orderid, sendername)
                    cursor.execute(sql, values)
                elif op_type is OPERATION_EDIT:
                    print("\n Edit operation type")
                    sql = "UPDATE inventory_stock set Item_name = %s, Author_Name = %s, Price = %s, Borrow_Fee = %s, " \
                          "Quantity = %s, Location = %s, Stock_Receival_Date = %s, Center_Name = %s, Stock_Type = %s " \
                          "where Item_Id = %s "
                    # sql = "UPDATE inventory_stock set Item_name = %s where Item_Id = %s"
                    values = (
                        itemname, author, price, borrow_fee, quantity, location, cal.get_date(), localcenter, stocktype,
                        item_id)
                    cursor.execute(sql, values)
                else:
                    '''do nothing'''

                # execute the query
                conn.commit()
                conn.close()
                print("Record inserted !!! ")

                self.btn_submit.configure(state=DISABLED, bg='light grey')
                self.clear_form(item_name, author_name, item_price, item_borrowfee, item_quantity)
                user_choice = messagebox.askquestion("Item insertion success", "Do you want to add another item ? ")
                # destroy the data entry form , if user do not want to add more records
                if user_choice == 'no':
                    print("Do nothing")

    def search_itemId(self, item_idforSearch, item_name, author_menu,
                      item_price,
                      item_author,
                      item_quantity, op_type):

        # search started -------------
        print("search_itemId--> Start for item name: ", item_idforSearch.get())
        itemId = item_idforSearch.get()
        bItemExists = self.validate_itemId(itemId)
        if bItemExists:
            conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

            # Creating a cursor object using the cursor() method
            cursor = conn.cursor()

            bItemExist = cursor.execute("SELECT * FROM inventory_stock WHERE Item_Id = %s", (itemId,))
            result = cursor.fetchone()
            print("result :", result)
            conn.close()
            if op_type == OPERATION_EDIT:
                item_name.delete(0, END)
                item_name.insert(0, result[2])
                item_price.delete(0, END)
                item_price.insert(0, result[4])
                item_author.delete(0, END)
                item_author.insert(0, result[3])
                item_quantity.delete(0, END)
                item_quantity.insert(0, result[6])
            elif op_type == OPERATION_SEARCH:
                item_name['text'] = result[2]
                author_menu['text'] = result[3]
                item_price['text'] = result[4]
                item_author['text'] = result[9]
                item_quantity['text'] = result[6]
            else:
                ''' do nothing '''
            self.btn_addToCart.configure(state=NORMAL, bg='RosyBrown1')
        else:
            messagebox.showwarning("Not Available", "Item doesn't exists!!!")

    def generate_itemId(self, local_centerText):
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        total_records = cursor.execute("SELECT * FROM inventory_stock")
        conn.close()
        stock_id = total_records + 100
        return "INV" + str(stock_id)  # CI- Commercial Inventory

    def validate_itemName(self, itemName, localCenterName):
        itemId = ""
        print("validate_itemName--> Start for item name: ", itemName)
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT EXISTS(SELECT * FROM inventory_stock WHERE Item_name = %s)", (itemName,))
        result = cursor.fetchone()
        print("result :", result[0])
        conn.close()
        return result[0]

    def isQuantityValid(self, itemdId, quantity_requested):
        print("isQuantityValid--> Start for item id: ", itemdId)
        b_QuantityValid = True
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT Quantity FROM inventory_stock WHERE Item_Id = %s", (itemdId,))

        result = cursor.fetchone()
        print("result of item_id:", result[0])
        conn.close()
        if int(result[0]) < int(quantity_requested):
            b_QuantityValid = False
        return b_QuantityValid

    def validate_itemId(self, itemId):
        print("validate_itemId--> Start for item Id : ", itemId)
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT EXISTS(SELECT * FROM inventory_stock WHERE Item_Id = %s)", (itemId,))
        result = cursor.fetchone()
        print("result of item_id:", result[0])
        conn.close()
        return result[0]

    def generate_authorId(self):
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        total_records = cursor.execute("SELECT * FROM author")
        conn.close()
        authorId = total_records + 100
        return "ATH" + str(authorId)  # Author Id

    def validate_author(self, name_text):
        print("validate_author--> validate for Name : ", name_text)
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT EXISTS(SELECT * FROM author WHERE author_Name = %s)", (name_text,))
        result = cursor.fetchone()
        print("result :", result[0])
        conn.close()
        return result[0]

    def register_author(self, sales_window, name_text, dor_text):
        """ register the author"""
        dateTimeObj = dor_text.get_date()

        dor_date = dateTimeObj.strftime("%Y-%m-%d")

        if name_text.get() == "":
            messagebox.showinfo("Data Entry Error", "All fields are mandatory !!!")
        else:
            item_id = self.generate_authorId()  # generates a unique item id
            bitemExists = self.validate_author(name_text.get())
            print("Author Exists :", bitemExists)
            if bitemExists:
                messagebox.showwarning("Duplicate Entry Error !", "Author already exists !!")
                name_text.configure(bd=2, fg='red')
                return
            else:
                conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()
                total_records = cursor.execute("SELECT * FROM author")
                conn.close()

                if total_records is 0:
                    serial_no = 1
                else:
                    serial_no = total_records + 1

                # establishing the connection
                print("debug 1")
                conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')
                print("debug 2")
                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()
                print("debug 3")
                authorname = str(name_text.get())

                print("\n", serial_no, item_id, name_text, dor_date)
                print("\n Add Author")
                sql = "INSERT INTO author VALUES(%s, %s, %s, %s)"
                values = (
                    serial_no, item_id, authorname, dor_date)
                cursor.execute(sql, values)

                conn.commit()
                conn.close()
                print("Author inserted !!! ")

                self.btn_submit.configure(state=DISABLED, bg='light grey')

                user_choice = messagebox.askquestion("Author registered", "Do you want to register new  ? ")
                # destroy the data entry form , if user do not want to add more records
                if user_choice == 'no':
                    print("Do nothing")

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

    def generate_StockPurchase_invoiceID(self):
        strInvId = datetime.now().strftime('%Y%m%d%H%M')
        finalId = "INV" + strInvId
        print("Generated Invoice Id : ", finalId)
        return finalId

    def get_currentStockQuantity(self, item_id):
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT Quantity FROM inventory_stock WHERE Item_Id = %s", (item_id,))
        result = cursor.fetchone()
        print("Current quantity :", result)
        conn.close()
        return int(result[0])
