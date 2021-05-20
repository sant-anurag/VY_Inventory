from app_defines import *
from app_common import *
from init_database import *
from app_thread import *
import MySQLdb as sql_db


class NewMerchandise:

    # constructor for Library class
    def __init__(self, master):
        self.obj_commonUtil = CommonUtil()
        self.dateTimeOp = DatetimeOperation()
        self.merchandise_window = Toplevel(master)
        self.merchandise_window.title("Inventory Operations")
        self.merchandise_window.geometry('970x470+700+260')
        self.merchandise_window.configure(background='wheat')
        self.merchandise_window.resizable(width=False, height=False)
        self.merchandise_window.protocol('WM_DELETE_WINDOW', self.obj_commonUtil.donothing)

        canvas_width, canvas_height = 970, 750
        canvas = Canvas(self.merchandise_window, width=canvas_width, height=canvas_height)
        myimage = ImageTk.PhotoImage(
            PIL.Image.open("..\\Images\\Logos\\Geometry-Header-1920x1080.jpg"))
        canvas.create_image(0, 0, anchor=NW, image=myimage)
        canvas.pack()

        self.dataEntryFrame = Frame(self.merchandise_window, width=800, height=500, bd=4, relief='ridge',
                                    bg='snow')
        self.dataEntryFrame.pack()
        self.dataModifyFrame = Frame(self.merchandise_window, width=800, height=500, bd=4, relief='ridge',
                                     bg='snow')
        self.dataModifyFrame.pack()
        self.dataSearchFrame = Frame(self.merchandise_window, width=800, height=500, bd=4, relief='ridge',
                                     bg='snow')
        self.dataSearchFrame.pack()

        self.btn_submit = Button(self.merchandise_window)

        self.btn_submit.configure(text="Save", fg="Black", font=XXL_FONT, width=14, state=NORMAL, bg='RosyBrown1')
        self.btn_cancel = Button(self.merchandise_window, text="Close", fg="Black",
                                 font=XXL_FONT, width=14, state=NORMAL, bg='RosyBrown1')
        self.btn_cancel.configure(command=self.merchandise_window.destroy)
        self.btn_clear = Button(self.merchandise_window, text="Reset", fg="Black",
                                font=XXL_FONT, width=14, state=NORMAL, bg='RosyBrown1')

        search_result = partial(self.search_merchandise_details, master)
        self.btn_search = Button(self.merchandise_window, text="Search", fg="Black", command=search_result,
                                 font=XXL_FONT, width=7, state=NORMAL, bg='RosyBrown1')

        edit_result = partial(self.edit_merchandise, master)
        self.btn_modify = Button(self.merchandise_window, text="Modify", fg="Black", command=edit_result,
                                 font=XXL_FONT, width=7, state=NORMAL, bg='RosyBrown1')
        add_result = partial(self.add_new_center, master)
        self.btn_add = Button(self.merchandise_window, text="Add", fg="Black", command=add_result,
                              font=XXL_FONT, width=7, state=NORMAL, bg='RosyBrown1')

        self.btn_add.place(x=7, y=100)
        self.btn_modify.place(x=7, y=170)
        self.btn_search.place(x=7, y=240)

        self.btn_submit.place(x=150, y=395)
        self.btn_clear.place(x=420, y=395)
        self.btn_cancel.place(x=690, y=395)
        print("constructor called for newInventory Addition ")

        # default window is "Add New Inventor" when window opens
        self.add_new_center(master)

    def add_new_center(self, master):
        self.dataModifyFrame.destroy()
        self.dataSearchFrame.destroy()
        self.dataEntryFrame = Frame(self.merchandise_window, width=800, height=370, bd=4, relief='ridge',
                                    bg='snow')
        self.dataEntryFrame.pack()

        self.default_text5 = StringVar(self.dataEntryFrame, value='0')
        self.default_text4 = StringVar(self.dataEntryFrame, value='')
        self.default_text3 = StringVar(self.dataEntryFrame, value='')
        self.default_text2 = StringVar(self.dataEntryFrame, value='')
        self.default_text1 = StringVar(self.dataEntryFrame, value='')
        self.default_text6 = StringVar(self.dataEntryFrame, value='')
        self.default_text7 = StringVar(self.dataEntryFrame, value='')
        self.default_text8 = StringVar(self.dataEntryFrame, value='')

        # create a item Name label

        name_label = Label(self.dataEntryFrame, text="Center Name", width=11, anchor=W, justify=LEFT,
                           font=('times new roman', 20, 'normal'),
                           bg='snow')

        # create a Author label
        manager_label = Label(self.dataEntryFrame, text="Manager", width=11, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'),
                              bg='snow')

        # create a Price label
        inaugdate_label = Label(self.dataEntryFrame, text="Opening Date", width=13, anchor=W, justify=LEFT,
                                font=('times new roman', 20, 'normal'), bg='snow')

        # create a Quantity label
        regisno_label = Label(self.dataEntryFrame, text="Regis. No", width=13, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'), bg='snow')

        # create a borrow fee label
        panNo_label = Label(self.dataEntryFrame, text="PAN No.", width=13, anchor=W, justify=LEFT,
                            font=('times new roman', 20, 'normal'), bg='snow')

        # create a borrow fee label
        address_label = Label(self.dataEntryFrame, text="Address", width=13, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'), bg='snow')

        self.dataEntryFrame.place(x=150, y=20)

        name_label.place(x=30, y=10)
        manager_label.place(x=30, y=65)
        inaugdate_label.place(x=30, y=115)
        regisno_label.place(x=30, y=170)
        panNo_label.place(x=30, y=225)
        address_label.place(x=30, y=275)

        center_name = Entry(self.dataEntryFrame, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                            textvariable=self.default_text1)

        manager_name = Entry(self.dataEntryFrame, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                             textvariable=self.default_text3)

        inaugdate = DateEntry(self.dataEntryFrame, width=39, date_pattern='dd/MM/yyyy',
                              font=('times new roman', 18, 'normal'),
                              bg='light cyan',
                              justify='left')

        regisno = Entry(self.dataEntryFrame, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                        textvariable=self.default_text4)

        panno = Entry(self.dataEntryFrame, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                      textvariable=self.default_text5)
        address = Entry(self.dataEntryFrame, width=35,
                        font=('times new roman', 20, 'normal'),
                        bg='light cyan', textvariable=self.default_text8)

        center_name.place(x=240, y=10)
        manager_name.place(x=240, y=60)
        inaugdate.place(x=240, y=120)
        regisno.place(x=240, y=170)
        panno.place(x=240, y=230)
        address.place(x=240, y=280)

        insert_result = partial(self.center_operations, 'NA', center_name, manager_name,
                                inaugdate,
                                regisno,
                                panno, address, OPERATION_ADD)

        # create a Save Button and place into the self.merchandise_window window

        self.btn_submit.configure(state=NORMAL, bg='RosyBrown1', command=insert_result)

        self.default_text1.trace("w", self.check_SaveItemBtn_state)
        # self.default_text2.trace("w", self.check_SaveItemBtn_state)
        self.default_text3.trace("w", self.check_SaveItemBtn_state)
        self.default_text4.trace("w", self.check_SaveItemBtn_state)
        self.default_text5.trace("w", self.check_SaveItemBtn_state)
        clear_result = partial(self.clear_form, center_name, manager_name, inaugdate, regisno,
                               panno, address)

        self.btn_clear.configure(command=clear_result)
        self.btn_cancel.configure(command=self.merchandise_window.destroy)
        # cancel.grid(row=0, column=2)

        # ---------------------------------Button Frame End----------------------------------------

        self.merchandise_window.bind('<F9>', lambda event=None: self.btn_clear.invoke())
        self.merchandise_window.bind('<Escape>', lambda event=None: self.btn_cancel.invoke())

        self.merchandise_window.bind('<Return>', lambda event=None: self.btn_submit.invoke())

        self.merchandise_window.focus()
        self.merchandise_window.grab_set()
        mainloop()

    def myfunction(self, mycanvas, frame, event):
        print("Scroll Encountered")
        mycanvas.configure(scrollregion=mycanvas.bbox("all"), width=722, height=400)

    def display_currentAuthorList(self, merchandise_window, authorFrame):
        author_listFrm = Frame(authorFrame, width=750, height=63, bd=4, relief='ridge',
                               bg='snow')
        author_listFrm.place(x=30, y=110)

        label_sno = Label(author_listFrm, text="S.No", width=10, height=2, borderwidth=1, relief="solid",
                          anchor='center',
                          justify=CENTER,
                          font=('times new roman', 16, 'normal'),
                          bg='light grey')

        label_authId = Label(author_listFrm, text="Author Id", width=12, height=2, borderwidth=1, relief="solid",
                             anchor='center',
                             justify=CENTER,
                             font=('times new roman', 16, 'normal'),
                             bg='light grey')

        label_AuthName = Label(author_listFrm, text="Author Name", width=28, height=2, borderwidth=1, relief="solid",
                               anchor='center',
                               justify=CENTER,
                               font=('times new roman', 16, 'normal'),
                               bg='light grey')

        label_dor = Label(author_listFrm, text="DOR", width=11, height=2, borderwidth=1, relief="solid",
                          anchor='center',
                          justify=CENTER,
                          font=('times new roman', 16, 'normal'),
                          bg='light grey')
        label_sno.place(x=5, y=5)
        label_authId.place(x=125, y=5)
        label_AuthName.place(x=255, y=5)
        label_dor.place(x=580, y=5)

        myframe = Frame(authorFrame, width=722, height=400, bd=4, relief='ridge',
                        bg='snow')
        myframe.place(x=30, y=170)

        mycanvas = Canvas(myframe)
        frame = Frame(mycanvas, width=722, height=900)
        myscrollbar = Scrollbar(myframe, orient="vertical")
        mycanvas.config(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right", fill="y")
        myscrollbar.config(command=mycanvas.yview)
        mycanvas.pack(side="left", fill='both', expand='yes')
        mycanvas.create_window((0, 0), window=frame, anchor='nw')

        result_scrll = partial(self.myfunction, mycanvas, frame)

        frame.bind("<Configure>", result_scrll)

        # fetch the complete author table
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        result_query = cursor.execute("SELECT * FROM author")
        result = cursor.fetchall()
        print(result[0][1])
        print("Total records = ", result_query)
        conn.close()

        y_pos = 3
        for row_count in range(0, result_query):
            for column_count in range(0, 4):
                if column_count == 0:
                    width_label = 10
                    start_pos = 5
                elif column_count == 1 or column_count == 3:
                    width_label = 12
                    start_pos = 125
                    if column_count == 3:
                        start_pos = 580
                        width_label = 11
                elif column_count == 2:
                    width_label = 28
                    start_pos = 255
                else:
                    '''Not possible'''
                label_display = Label(frame, width=width_label, height=2, borderwidth=1, relief="solid",
                                      anchor='center',
                                      justify=CENTER,
                                      font=('times new roman', 16, 'normal'),
                                      bg='light cyan')
                print("row_count : ", row_count, "column_count :", column_count)
                label_display['text'] = result[row_count][column_count]
                label_display.place(x=start_pos, y=y_pos)
            y_pos = y_pos + 51

    def edit_merchandise(self, master):
        self.dataEntryFrame.destroy()
        self.dataSearchFrame.destroy()
        self.dataModifyFrame = Frame(self.merchandise_window, width=800, height=370, bd=4, relief='ridge',
                                     bg='snow')
        self.dataModifyFrame.pack()
        frameSearch = Frame(self.dataModifyFrame, width=780, height=50, bd=4, relief='ridge',
                            bg='snow')
        frameSearch.pack()
        framedisplay = Frame(self.dataModifyFrame, width=780, height=290, bd=4, relief='ridge',
                             bg='snow')
        framedisplay.pack()

        self.default_text5 = StringVar(framedisplay, value='0')
        self.default_text4 = StringVar(framedisplay, value='')
        self.default_text3 = StringVar(framedisplay, value='')
        self.default_text2 = StringVar(framedisplay, value='')
        self.default_text1 = StringVar(framedisplay, value='')
        self.default_text6 = StringVar(framedisplay, value='')
        self.default_text7 = StringVar(framedisplay, value='')
        self.default_text8 = StringVar(framedisplay, value='')
        # create a item Name label

        mchd_SearchId = Label(frameSearch, text="Center Id", width=11, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'),
                              bg='snow')

        center_namelabel = Label(framedisplay, text="Center Name", width=11, anchor=W, justify=LEFT,
                                 font=('times new roman', 20, 'normal'),
                                 bg='snow')

        managerName_label = Label(framedisplay, text="Manager", width=11, anchor=W, justify=LEFT,
                                  font=('times new roman', 20, 'normal'),
                                  bg='snow')

        # create a Price label
        inaugDate_label = Label(framedisplay, text="Opening Date", width=13, anchor=W, justify=LEFT,
                                font=('times new roman', 20, 'normal'), bg='snow')

        # create a Quantity label
        regisNo_label = Label(framedisplay, text="Regis No.", width=13, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'), bg='snow')

        # create a borrow fee label
        panno_label = Label(framedisplay, text="PAN No.", width=13, anchor=W, justify=LEFT,
                            font=('times new roman', 20, 'normal'), bg='snow')

        # create a borrow fee label
        address_label = Label(framedisplay, text="Address", width=13, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'), bg='snow')

        self.dataModifyFrame.place(x=150, y=20)

        frameSearch.place(x=10, y=5)
        framedisplay.place(x=10, y=60)

        mchd_SearchId.place(x=30, y=5)

        center_namelabel.place(x=30, y=5)
        managerName_label.place(x=30, y=50)
        inaugDate_label.place(x=30, y=100)
        regisNo_label.place(x=30, y=140)
        panno_label.place(x=30, y=185)
        address_label.place(x=30, y=230)

        center_idforSearch = Entry(frameSearch, width=20, font=('times new roman', 20, 'normal'), bg='light yellow')
        center_idforSearch.place(x=240, y=5)

        btn_search = Button(frameSearch)

        center_name = Entry(framedisplay, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                            textvariable=self.default_text1)

        managerName = Entry(framedisplay, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                            textvariable=self.default_text3)
        cal = DateEntry(framedisplay, width=39, date_pattern='dd/MM/yyyy',
                        font=('times new roman', 18, 'normal'),
                        bg='light cyanw',
                        justify='left')
        regisNo = Entry(framedisplay, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                        textvariable=self.default_text7)
        panno = Entry(framedisplay, width=35, text='0', font=('times new roman', 20, 'normal'),
                      bg='light cyan', textvariable=self.default_text4)
        address = Entry(framedisplay, width=35, text='0', font=('times new roman', 20, 'normal'),
                        bg='light cyan', textvariable=self.default_text5)
        center_name.place(x=240, y=5)
        managerName.place(x=240, y=50)
        cal.place(x=240, y=100)
        regisNo.place(x=240, y=145)
        panno.place(x=240, y=190)
        address.place(x=240, y=235)

        search_result = partial(self.search_centerId, center_idforSearch, center_name, managerName,
                                cal, regisNo, panno, address, OPERATION_EDIT)

        btn_search.configure(text="Search", fg="Black", command=search_result,
                             font=('arial narrow', 14, 'normal'), width=19, state=NORMAL, bg='RosyBrown1')
        btn_search.place(x=540, y=2)

        insert_result = partial(self.center_operations, center_idforSearch, center_name,
                                managerName,
                                cal, regisNo, panno, address, OPERATION_EDIT)

        self.btn_submit.configure(state=NORMAL, bg='RosyBrown1', command=insert_result)

        self.default_text1.trace("w", self.check_SaveItemBtn_state)
        self.default_text3.trace("w", self.check_SaveItemBtn_state)
        self.default_text4.trace("w", self.check_SaveItemBtn_state)
        self.default_text5.trace("w", self.check_SaveItemBtn_state)
        clear_result = partial(self.clear_form, center_name, managerName,
                               cal,
                               regisNo,
                               panno, address)

        self.btn_clear.configure(command=clear_result)

        # ---------------------------------Button Frame End----------------------------------------

        self.merchandise_window.bind('<Return>', lambda event=None: btn_search.invoke())
        self.merchandise_window.bind('<Alt-c>', lambda event=None: self.btn_cancel.invoke())
        self.merchandise_window.bind('<Alt-r>', lambda event=None: self.btn_clear.invoke())

        self.merchandise_window.focus()
        self.merchandise_window.grab_set()
        mainloop()

    def search_merchandise_details(self, master):
        self.dataEntryFrame.destroy()
        self.dataModifyFrame.destroy()
        self.dataSearchFrame = Frame(self.merchandise_window, width=800, height=370, bd=4, relief='ridge',
                                     bg='snow')
        self.dataSearchFrame.pack()
        frameSearch = Frame(self.dataSearchFrame, width=780, height=50, bd=4, relief='ridge',
                            bg='snow')
        frameSearch.pack()
        framedisplay = Frame(self.dataSearchFrame, width=780, height=290, bd=4, relief='ridge',
                             bg='snow')
        framedisplay.pack()

        # create a item Name label

        mchd_SearchId = Label(frameSearch, text="center Id", width=11, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'),
                              bg='snow')

        centername_label = Label(framedisplay, text="Center Name", width=11, anchor=W, justify=LEFT,
                                 font=('times new roman', 20, 'normal'),
                                 bg='snow')

        managerName_label = Label(framedisplay, text="Manager Name", width=11, anchor=W, justify=LEFT,
                                  font=('times new roman', 20, 'normal'),
                                  bg='snow')

        inaug_label = Label(framedisplay, text="Opening Date", width=13, anchor=W, justify=LEFT,
                            font=('times new roman', 20, 'normal'), bg='snow')
        regisNo_label = Label(framedisplay, text="Regis. No.", width=13, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'), bg='snow')
        panno_label = Label(framedisplay, text="PAN No.", width=13, anchor=W, justify=LEFT,
                            font=('times new roman', 20, 'normal'), bg='snow')
        address_label = Label(framedisplay, text="Address", width=13, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'), bg='snow')

        self.dataSearchFrame.place(x=150, y=20)

        frameSearch.place(x=10, y=5)
        framedisplay.place(x=10, y=60)

        mchd_SearchId.place(x=30, y=5)

        centername_label.place(x=30, y=5)
        managerName_label.place(x=30, y=50)
        inaug_label.place(x=30, y=100)
        regisNo_label.place(x=30, y=140)
        panno_label.place(x=30, y=185)
        address_label.place(x=30, y=230)

        center_idforSearch = Entry(frameSearch, width=20, font=('times new roman', 20, 'normal'), bg='light cyan')
        center_idforSearch.place(x=240, y=5)

        btn_search = Button(frameSearch)

        center_name = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                            font=('times new roman', 20, 'normal'),
                            bg='light cyan')

        manager_name = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                             font=('times new roman', 20, 'normal'),
                             bg='light cyan')

        cal = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                    font=('times new roman', 20, 'normal'),
                    bg='light cyan')

        regisNo = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                        font=('times new roman', 20, 'normal'),
                        bg='light cyan')

        panno = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                      font=('times new roman', 20, 'normal'),
                      bg='light cyan')

        address = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                        font=('times new roman', 20, 'normal'),
                        bg='light cyan')

        center_name.place(x=240, y=5)
        manager_name.place(x=240, y=50)
        cal.place(x=240, y=100)
        regisNo.place(x=240, y=145)
        panno.place(x=240, y=190)
        address.place(x=240, y=235)

        search_result = partial(self.search_centerId, center_idforSearch, center_name, manager_name,
                                cal, regisNo, panno, address, OPERATION_SEARCH)

        btn_search.configure(text="Search", fg="Black", command=search_result,
                             font=('arial narrow', 14, 'normal'), width=19, state=NORMAL, bg='RosyBrown1')
        btn_search.place(x=540, y=2)

        self.btn_submit.configure(state=DISABLED, bg='light grey')

        self.merchandise_window.bind('<Return>', lambda event=None: btn_search.invoke())
        self.merchandise_window.bind('<Alt-c>', lambda event=None: self.btn_cancel.invoke())
        self.merchandise_window.bind('<Alt-r>', lambda event=None: self.btn_clear.invoke())

        self.merchandise_window.focus()
        self.merchandise_window.grab_set()
        mainloop()

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
    def clear_form(self, center_name, manager_name,
                   inaugdate,
                   regisno,
                   panno, address):
        # clear the content of text entry box
        center_name.delete(0, END)
        center_name.configure(fg='black')
        manager_name.delete(0, END)
        manager_name.configure(fg='black')
        regisno.delete(0, END)
        regisno.configure(fg='black')
        panno.delete(0, END)
        panno.configure(fg='black')
        address.delete(0, END)
        address.configure(fg='black')

    def center_operations(self, center_idforSearch, center_name, manager_name,
                          inaugdate,
                          regisno,
                          panno, address, op_type):

        dateTimeObj = inaugdate.get_date()

        inauguration_date = dateTimeObj.strftime("%Y-%m-%d")
        if op_type == OPERATION_ADD:
            center_id = self.generate_centerId()  # generates a unique item id
        elif op_type == OPERATION_EDIT:
            center_id = center_idforSearch.get()
        if center_name.get() == "" or manager_name.get() == "" or regisno.get() == "" or panno.get() == "" or address.get() == "":
            messagebox.showinfo("Data Entry Error", "All fields are mandatory !!!")

        else:
            bCenterExists = self.validate_centerName(center_name.get())
            print("bCenterExists :", bCenterExists)
            if bCenterExists and op_type is OPERATION_ADD:
                messagebox.showwarning("Duplicate Entry Error !", "center already exists !!")
                center_name.configure(bd=2, fg='red')
                return
            else:
                conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()
                total_records = cursor.execute("SELECT * FROM merchandise")
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
                centername = str(center_name.get())
                manager = str(manager_name.get())
                registration_no = str(regisno.get())
                pannumber = str(panno.get())
                addressofCenter = str(address.get())

                print("\n", serial_no, center_id, centername, manager, inauguration_date, registration_no, pannumber,
                      addressofCenter)
                if op_type is OPERATION_ADD:
                    print("\n Add operation type")
                    sql = "INSERT INTO merchandise VALUES(%s, %s, %s, %s,%s, %s, %s, %s)"
                    values = (
                        serial_no, center_id, centername, manager, inauguration_date, registration_no, pannumber,
                        addressofCenter)
                    cursor.execute(sql, values)
                elif op_type is OPERATION_EDIT:
                    print("\n Edit operation type")
                    sql = "UPDATE merchandise set merchandise_Name = %s, merchandise_manager = %s, " \
                          "merchandise_inaug_date = %s, merchandise_regis_no = %s, " \
                          "merchandise_panno = %s, merchandise_address = %s" \
                          "where merchandise_Id = %s "
                    values = (
                        centername, manager, inauguration_date, registration_no, pannumber, addressofCenter,
                        center_id)
                    cursor.execute(sql, values)
                else:
                    '''do nothing'''

                # execute the query
                conn.commit()
                conn.close()
                print("Merchandise registered !!! ")

                self.btn_submit.configure(state=DISABLED, bg='light grey')
                self.clear_form(center_name, manager_name, inaugdate, regisno,
                                panno, address)
                user_choice = messagebox.askquestion("Item insertion success", "Do you want to add another item ? ")
                # destroy the data entry form , if user do not want to add more records
                if user_choice == 'no':
                    print("Do nothing")

    def search_centerId(self, center_idforSearch, center_name, managerName,
                        cal, regisNo, panno, address, op_type):

        # search started -------------
        print("search_centerId--> Start for center name: ", center_idforSearch.get())
        centerId = center_idforSearch.get()
        bCenterExists = self.validate_centerId(centerId)
        if bCenterExists:
            conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

            # Creating a cursor object using the cursor() method
            cursor = conn.cursor()

            bItemExist = cursor.execute("SELECT * FROM merchandise WHERE merchandise_Id = %s", (centerId,))
            result = cursor.fetchone()
            print("result :", result)
            conn.close()
            if op_type == OPERATION_EDIT:
                center_name.delete(0, END)
                center_name.insert(0, result[2])
                managerName.delete(0, END)
                managerName.insert(0, result[3])
                cal.delete(0, END)
                cal.insert(0, result[4])
                regisNo.delete(0, END)
                regisNo.insert(0, result[5])
                panno.delete(0, END)
                panno.insert(0, result[6])
                address.delete(0, END)
                address.insert(0, result[7])
            elif op_type == OPERATION_SEARCH:
                center_name['text'] = result[2]
                managerName['text'] = result[3]
                cal['text'] = result[4]
                regisNo['text'] = result[5]
                panno['text'] = result[6]
                address['text'] = result[7]
            else:
                ''' do nothing '''

        else:
            messagebox.showwarning("Not Available", "Center Not Registered!!!")

    def generate_centerId(self):
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        total_records = cursor.execute("SELECT * FROM merchandise")
        conn.close()
        mchd_id = total_records + 100
        return "MCHD" + str(mchd_id)  # CI- Commercial Inventory

    def validate_centerName(self, centername):
        itemId = ""
        print("validate_centerName--> Start for item name: ", centername)
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT EXISTS(SELECT * FROM merchandise WHERE merchandise_Name = %s)",
                                    (centername,))
        result = cursor.fetchone()
        print("result :", result[0])
        conn.close()
        return result[0]

    def validate_centerId(self, itemId):
        print("validate_centerId--> Start for item Id : ", itemId)
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT EXISTS(SELECT * FROM merchandise WHERE merchandise_Id = %s)", (itemId,))
        result = cursor.fetchone()
        print("result :", result[0])
        conn.close()
        return result[0]

    def get_authorNames(self):
        print("get_authorNames--> Start for item name: ")
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        result_query = cursor.execute("SELECT author_Name FROM author")
        result = cursor.fetchall()
        conn.close()
        return result
