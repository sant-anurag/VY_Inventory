"""
# Copyright 2020 by Vihangam Yoga Karnataka.
# All rights reserved.
# This file is part of the Vihangan Yoga Operations of Ashram Management Software Package(VYOAM),
# and is released under the "VY License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
# Vihangan Yoga Operations  of Ashram Management Software
# File Name : Inventory_Entry.py
# Developer : Sant Anurag Deo
# Version : 1.0
"""

from app_defines import *
from app_common import *
from app_thread import *
import MySQLdb as sql_db


class accountControl:

    # constructor for Library class
    def __init__(self, master, currentuser):
        self.currentuser = currentuser
        self.obj_commonUtil = CommonUtil()
        self.dateTimeOp = DatetimeOperation()
        self.account_control_window = Toplevel(master)
        self.account_control_window.title("User Control Operations")
        self.account_control_window.geometry('970x210+700+380')
        self.account_control_window.configure(background='wheat')
        self.account_control_window.resizable(width=False, height=False)
        self.account_control_window.protocol('WM_DELETE_WINDOW', self.obj_commonUtil.donothing)

        canvas_width, canvas_height = 970, 210
        canvas = Canvas(self.account_control_window, width=canvas_width, height=canvas_height)
        myimage = ImageTk.PhotoImage(
            PIL.Image.open("..\\Images\\Logos\\Geometry-Header-1920x1080.jpg"))
        canvas.create_image(0, 0, anchor=NW, image=myimage)
        canvas.pack()

        self.userInfoFrame = Frame(self.account_control_window, width=800, height=500, bd=4, relief='ridge',
                                   bg='snow')
        self.userInfoFrame.pack()
        self.newpasswordFrame = Frame(self.account_control_window, width=800, height=500, bd=4, relief='ridge',
                                     bg='snow')
        self.newpasswordFrame.pack()
        self.dataSearchFrame = Frame(self.account_control_window, width=800, height=500, bd=4, relief='ridge',
                                     bg='snow')
        self.dataSearchFrame.pack()

        self.new_authorFrame = Frame(self.account_control_window, width=800, height=500, bd=4, relief='ridge',
                                     bg='snow')
        self.new_authorFrame.pack()
        self.btn_submit = Button(self.account_control_window)
        # Bottom button panel - start

        self.btn_submit.configure(text="Save", fg="Black", font=L_FONT, width=14, state=NORMAL, bg='RosyBrown1')
        self.btn_cancel = Button(self.account_control_window, text="Close", fg="Black",
                                 font=L_FONT, width=14, state=NORMAL, bg='RosyBrown1')
        self.btn_cancel.configure(command=self.account_control_window.destroy)
        self.btn_clear = Button(self.account_control_window, text="Reset", fg="Black",
                                font=L_FONT, width=14, state=NORMAL, bg='RosyBrown1')

        # Bottom button panel - end

        # Side button panel - start
        author_result = partial(self.current_user_info_display, master)
        self.btn_userinfo = Button(self.account_control_window, text="User Info", fg="Black", command=author_result,
                                   font=L_FONT, width=13, state=NORMAL, bg='RosyBrown1')

        add_result = partial(self.add_new_account, master)
        self.btn_add = Button(self.account_control_window, text="New Account", fg="Black", command=add_result,
                              font=L_FONT, width=13, state=NORMAL, bg='RosyBrown1')
        self.btn_remove = Button(self.account_control_window, text="Remove Account", fg="Black", command=None,
                                 font=L_FONT, width=13, state=NORMAL, bg='RosyBrown1')
        edit_result = partial(self.set_new_password, master)
        self.btn_modify = Button(self.account_control_window, text="Edit Password", fg="Black", command=edit_result,
                                 font=L_FONT, width=13, state=NORMAL, bg='RosyBrown1')

        # Side button panel - end

        self.btn_userinfo.place(x=7, y=5)
        self.btn_add.place(x=7, y=45)
        self.btn_remove.place(x=7, y=85)
        self.btn_modify.place(x=7, y=125)

        self.btn_submit.place(x=280, y=165)
        self.btn_clear.place(x=440, y=165)
        self.btn_cancel.place(x=600, y=165)
        print("constructor called for User Account Display ")

        # default window is "Add New Inventor" when window opens
        self.current_user_info_display(master)

    def current_user_info_display(self, master):
        self.newpasswordFrame.destroy()
        self.dataSearchFrame.destroy()
        self.new_authorFrame.destroy()

        self.userInfoFrame = Frame(self.account_control_window, width=800, height=159, bd=4, relief='ridge',
                                   bg='wheat')
        self.userInfoFrame.pack()
        now = datetime.now()
        timeinfo = now.strftime("%H-%M-%S")
        date_info = now.strftime("%d-%b-%Y")
        info_text = "\nCurrent User :" + self.currentuser + "\n" + "Logged Date: " + date_info + "\n" + "At : " + timeinfo
        userInfo_label = Label(self.userInfoFrame, text=info_text, width=60, justify=CENTER,
                               font=('times new roman', 17, 'normal'),
                               bg='wheat')
        self.userInfoFrame.place(x=160, y=5)
        userInfo_label.place(x=5, y=5)
        self.account_control_window.focus()
        self.account_control_window.grab_set()
        mainloop()

    def add_new_account(self, master):
        self.newpasswordFrame.destroy()
        self.dataSearchFrame.destroy()
        self.userInfoFrame.destroy()

        self.newpasswordFrame = Frame(self.account_control_window, width=800, height=159, bd=4, relief='ridge',
                                     bg='wheat')
        self.newpasswordFrame.pack()

        self.default_text2 = StringVar(self.newpasswordFrame, value='')
        self.default_text1 = StringVar(self.newpasswordFrame, value='')
        self.newpasswordFrame.place(x=160, y=5)
        # create a item Name label

        username_label = Label(self.newpasswordFrame, text="Account Name", width=11, anchor=W, justify=LEFT,
                               font=L_FONT,
                               bg='wheat')

        # create a Author label
        password_label = Label(self.newpasswordFrame, text="Password", width=11, anchor=W, justify=LEFT,
                               font=L_FONT,
                               bg='wheat')

        role_label = Label(self.newpasswordFrame, text="Role", width=11, anchor=W, justify=LEFT,
                           font=L_FONT,
                           bg='wheat')

        username_label.place(x=30, y=10)
        password_label.place(x=30, y=65)
        role_label.place(x=30, y=115)

        username_text = Entry(self.newpasswordFrame, width=35, font=L_FONT, bg='light cyan',
                              textvariable=self.default_text1, justify=LEFT)

        password_text = Entry(self.newpasswordFrame, width=35, font=L_FONT, bg='light cyan',
                              textvariable=self.default_text2, justify=LEFT)

        roleText = StringVar(self.userInfoFrame)
        role_list = ['Admin', 'User']
        print("Role list  - ", role_list)
        roleText.set(role_list[0])
        role_TypeMenu = OptionMenu(self.newpasswordFrame, roleText, *role_list)
        role_TypeMenu.configure(width=41, font=L_FONT, bg='light cyan', anchor=W,
                                justify=LEFT)

        username_text.place(x=240, y=10)
        password_text.place(x=240, y=60)
        role_TypeMenu.place(x=240, y=110)

        insert_result = partial(self.register_account, username_text, password_text,
                                roleText)

        # create a Save Button and place into the self.account_control_window window

        self.btn_submit.configure(state=NORMAL, bg='RosyBrown1', command=insert_result)

        # self.default_text1.trace("w", self.check_SaveItemBtn_state)

        # clear_result = partial(self.clear_form, nam, authorText, item_price, item_borrowfee, item_quantity)

        # self.btn_clear.configure(command=clear_result)
        self.btn_cancel.configure(command=self.account_control_window.destroy)
        # cancel.grid(row=0, column=2)

        # ---------------------------------Button Frame End----------------------------------------

        self.account_control_window.bind('<Return>', lambda event=None: self.btn_submit.invoke())
        self.account_control_window.bind('<Alt-c>', lambda event=None: self.btn_cancel.invoke())
        self.account_control_window.bind('<Alt-r>', lambda event=None: self.btn_clear.invoke())

        self.account_control_window.focus()
        self.account_control_window.grab_set()
        mainloop()

    def set_new_password(self, master):
        self.newpasswordFrame.destroy()
        self.dataSearchFrame.destroy()
        self.userInfoFrame.destroy()

        self.newpasswordFrame = Frame(self.account_control_window, width=800, height=159, bd=4, relief='ridge',
                                     bg='wheat')
        self.newpasswordFrame.pack()

        self.default_text2 = StringVar(self.newpasswordFrame, value='')
        self.default_text1 = StringVar(self.newpasswordFrame, value='')
        self.newpasswordFrame.place(x=160, y=5)
        # create a item Name label

        username_label = Label(self.newpasswordFrame, text="Account Name", width=11, anchor=W, justify=LEFT,
                               font=L_FONT,
                               bg='wheat')

        # create a Author label
        password_label = Label(self.newpasswordFrame, text="New Password", width=11, anchor=W, justify=LEFT,
                               font=L_FONT,
                               bg='wheat')

        role_label = Label(self.newpasswordFrame, text="Role", width=11, anchor=W, justify=LEFT,
                           font=L_FONT,
                           bg='wheat')

        username_label.place(x=30, y=10)
        password_label.place(x=30, y=65)
        role_label.place(x=30, y=115)

        username_text = Entry(self.newpasswordFrame, width=35, font=L_FONT, bg='light cyan',
                              textvariable=self.default_text1, justify=LEFT)

        password_text = Entry(self.newpasswordFrame, width=35, font=L_FONT, bg='light cyan',
                              textvariable=self.default_text2, justify=LEFT)

        roleText = StringVar(self.newpasswordFrame)
        role_list = ['Admin', 'User']
        print("Role list  - ", role_list)
        roleText.set(role_list[0])
        role_TypeMenu = OptionMenu(self.newpasswordFrame, roleText, *role_list)
        role_TypeMenu.configure(width=41, font=L_FONT, bg='light cyan', anchor=W,
                                justify=LEFT)

        username_text.place(x=240, y=10)
        password_text.place(x=240, y=60)
        role_TypeMenu.place(x=240, y=110)

        insert_result = partial(self.edit_account_password, username_text, password_text,
                                roleText)

        # create a Save Button and place into the self.account_control_window window

        self.btn_submit.configure(state=NORMAL, bg='RosyBrown1', command=insert_result)

        # self.default_text1.trace("w", self.check_SaveItemBtn_state)

        # clear_result = partial(self.clear_form, nam, authorText, item_price, item_borrowfee, item_quantity)

        # self.btn_clear.configure(command=clear_result)
        self.btn_cancel.configure(command=self.account_control_window.destroy)
        # cancel.grid(row=0, column=2)

        # ---------------------------------Button Frame End----------------------------------------

        self.account_control_window.bind('<Return>', lambda event=None: self.btn_submit.invoke())
        self.account_control_window.bind('<Alt-c>', lambda event=None: self.btn_cancel.invoke())
        self.account_control_window.bind('<Alt-r>', lambda event=None: self.btn_clear.invoke())

        self.account_control_window.focus()
        self.account_control_window.grab_set()
        mainloop()

    def edit_inventory_item(self, master):
        self.userInfoFrame.destroy()
        self.newpasswordFrame = Frame(self.account_control_window, width=800, height=650, bd=4, relief='ridge',
                                     bg='snow')
        self.newpasswordFrame.pack()
        frameSearch = Frame(self.newpasswordFrame, width=780, height=50, bd=4, relief='ridge',
                            bg='snow')
        frameSearch.pack()
        framedisplay = Frame(self.newpasswordFrame, width=780, height=580, bd=4, relief='ridge',
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

        item_SearchId = Label(frameSearch, text="Item Id", width=11, anchor=W, justify=LEFT,
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
        borrowFee = Label(framedisplay, text="Borrow Fee(Rs.)", width=13, anchor=W, justify=LEFT,
                          font=('times new roman', 20, 'normal'), bg='snow')

        # create a borrow fee label
        rackNumber = Label(framedisplay, text="Rack Number", width=13, anchor=W, justify=LEFT,
                           font=('times new roman', 20, 'normal'), bg='snow')

        # create a borrow fee label
        date_label = Label(framedisplay, text="Received On", width=13, anchor=W, justify=LEFT,
                           font=('times new roman', 20, 'normal'), bg='snow')

        center_location = Label(framedisplay, text="Center Name", width=13, anchor=W, justify=LEFT,
                                font=('times new roman', 20, 'normal'), bg='snow')
        item_type = Label(framedisplay, text="Item Type", width=13, anchor=W, justify=LEFT,
                          font=('times new roman', 20, 'normal'), bg='snow')
        receivedBy = Label(framedisplay, text="Received By", width=13, anchor=W, justify=LEFT,
                           font=('times new roman', 20, 'normal'), bg='snow')
        sendername = Label(framedisplay, text="Sender Name", width=13, anchor=W, justify=LEFT,
                           font=('times new roman', 20, 'normal'), bg='snow')
        orderId = Label(framedisplay, text="Order/Inv No.", width=13, anchor=W, justify=LEFT,
                        font=('times new roman', 20, 'normal'), bg='snow')

        self.newpasswordFrame.place(x=150, y=20)

        frameSearch.place(x=10, y=5)
        framedisplay.place(x=10, y=60)

        item_SearchId.place(x=30, y=5)

        item_namelabel.place(x=30, y=5)
        author.place(x=30, y=50)
        price.place(x=30, y=100)
        quantity.place(x=30, y=140)
        borrowFee.place(x=30, y=185)
        rackNumber.place(x=30, y=230)
        date_label.place(x=30, y=285)
        center_location.place(x=30, y=330)
        item_type.place(x=30, y=380)
        receivedBy.place(x=30, y=430)
        sendername.place(x=30, y=480)
        orderId.place(x=30, y=530)

        item_idforSearch = Entry(frameSearch, width=20, font=('times new roman', 20, 'normal'), bg='light yellow')
        btn_search = Button(frameSearch)

        item_name = Entry(framedisplay, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                          textvariable=self.default_text1)

        authorText = StringVar(framedisplay)
        authorList = self.get_authorNames()  # self.obj_commonUtil.getAuthorNames()
        newAutorList = []
        iloop = 0
        for x in authorList:
            newAutorList.append(x[0])
            iloop = iloop + 1
        print("Author list  - ", newAutorList)
        authorText.set(newAutorList[0])
        author_menu = OptionMenu(framedisplay, authorText, *newAutorList)

        author_menu.configure(width=41, font=('times new roman', 17, 'normal'), bg='light cyan', anchor=W,
                              justify=LEFT)

        item_price = Entry(framedisplay, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                           textvariable=self.default_text3)

        item_quantity = Entry(framedisplay, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                              textvariable=self.default_text4)
        item_borrowfee = Entry(framedisplay, width=35, text='0', state=DISABLED,
                               font=('times new roman', 20, 'normal'),
                               bg='light grey', textvariable=self.default_text5)
        rack_location = Entry(framedisplay, width=35, font=('times new roman', 20, 'normal'), bg='light cyan')

        cal = DateEntry(framedisplay, width=39, date_pattern='dd/MM/yyyy',
                        font=('times new roman', 18, 'normal'),
                        bg='light cyanw',
                        justify='left')
        local_centerText = StringVar(framedisplay)
        localCenterList = self.get_centerNames()
        print("Center list  - ", localCenterList)
        newCenterList = []
        iloop = 0
        for x in localCenterList:
            newCenterList.append(x[0])
            iloop = iloop + 1
        print("Center list  - ", newCenterList)
        local_centerText.set(newCenterList[0])

        localcenter_menu = OptionMenu(framedisplay, local_centerText, *newCenterList)
        localcenter_menu.configure(width=41, font=('times new roman', 17, 'normal'), bg='light cyan', anchor=W,
                                   justify=LEFT)

        item_TypeText = StringVar(framedisplay)
        itemtypeList = ['Commercial', 'Non-Commercial']
        print("Item Type list  - ", itemtypeList)
        item_TypeText.set(itemtypeList[0])
        item_Typemenu = OptionMenu(framedisplay, item_TypeText, *itemtypeList)
        item_Typemenu.configure(width=41, font=('times new roman', 17, 'normal'), bg='light cyan', anchor=W,
                                justify=LEFT)
        item_idforSearch.place(x=240, y=5)

        receiver_name = Entry(framedisplay, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                              textvariable=self.default_text6)

        order_id = Entry(framedisplay, width=35, font=('times new roman', 20, 'normal'), bg='light cyan',
                         textvariable=self.default_text7)
        sender_name = Entry(framedisplay, width=35, text='0', font=('times new roman', 20, 'normal'),
                            bg='light cyan', textvariable=self.default_text8)
        item_name.place(x=240, y=5)
        author_menu.place(x=240, y=50)
        item_price.place(x=240, y=100)
        item_quantity.place(x=240, y=145)
        item_borrowfee.place(x=240, y=190)
        rack_location.place(x=240, y=235)
        cal.place(x=240, y=280)
        localcenter_menu.place(x=240, y=325)
        item_Typemenu.place(x=240, y=380)
        receiver_name.place(x=240, y=435)
        order_id.place(x=240, y=480)
        sender_name.place(x=240, y=525)

        search_result = partial(self.search_itemId, item_idforSearch, item_name, authorText,
                                item_price,
                                item_borrowfee,
                                item_quantity, rack_location, cal, local_centerText, item_TypeText, receiver_name,
                                order_id, sender_name, OPERATION_EDIT)

        btn_search.configure(text="Search", fg="Black", command=search_result,
                             font=('arial narrow', 14, 'normal'), width=19, state=NORMAL, bg='RosyBrown1')
        btn_search.place(x=540, y=2)

        insert_result = partial(self.stock_operations, self.account_control_window, item_name, item_idforSearch,
                                authorText,
                                item_price,
                                item_borrowfee,
                                item_quantity, rack_location, cal, local_centerText, item_TypeText, OPERATION_EDIT,
                                receiver_name,
                                order_id, sender_name)

        self.btn_submit.configure(state=NORMAL, bg='RosyBrown1', command=insert_result)

        self.default_text1.trace("w", self.check_SaveItemBtn_state)
        # self.default_text2.trace("w", self.check_SaveItemBtn_state)
        self.default_text3.trace("w", self.check_SaveItemBtn_state)
        self.default_text4.trace("w", self.check_SaveItemBtn_state)
        self.default_text5.trace("w", self.check_SaveItemBtn_state)
        clear_result = partial(self.clear_form, item_name, authorText, item_price, item_borrowfee, item_quantity)

        self.btn_clear.configure(command=clear_result)

        # ---------------------------------Button Frame End----------------------------------------

        self.account_control_window.bind('<Return>', lambda event=None: btn_search.invoke())
        self.account_control_window.bind('<Escape>', lambda event=None: self.btn_cancel.invoke())
        self.account_control_window.bind('<F9>', lambda event=None: self.btn_clear.invoke())

        self.account_control_window.focus()
        self.account_control_window.grab_set()
        mainloop()

    def search_inventory_item(self, master):
        self.userInfoFrame.destroy()
        self.newpasswordFrame.destroy()
        self.dataSearchFrame = Frame(self.account_control_window, width=800, height=650, bd=4, relief='ridge',
                                     bg='snow')
        self.dataSearchFrame.pack()
        frameSearch = Frame(self.dataSearchFrame, width=780, height=50, bd=4, relief='ridge',
                            bg='snow')
        frameSearch.pack()
        framedisplay = Frame(self.dataSearchFrame, width=780, height=580, bd=4, relief='ridge',
                             bg='snow')
        framedisplay.pack()

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
        borrowFee = Label(framedisplay, text="Borrow Fee(Rs.)", width=13, anchor=W, justify=LEFT,
                          font=('times new roman', 20, 'normal'), bg='snow')

        # create a borrow fee label
        rackNumber = Label(framedisplay, text="Rack Number", width=13, anchor=W, justify=LEFT,
                           font=('times new roman', 20, 'normal'), bg='snow')

        # create a borrow fee label
        date_label = Label(framedisplay, text="Received On", width=13, anchor=W, justify=LEFT,
                           font=('times new roman', 20, 'normal'), bg='snow')

        center_location = Label(framedisplay, text="Center Name", width=13, anchor=W, justify=LEFT,
                                font=('times new roman', 20, 'normal'), bg='snow')
        item_type = Label(framedisplay, text="Item Type", width=13, anchor=W, justify=LEFT,
                          font=('times new roman', 20, 'normal'), bg='snow')
        receivedBy = Label(framedisplay, text="Received By", width=13, anchor=W, justify=LEFT,
                           font=('times new roman', 20, 'normal'), bg='snow')
        sendername = Label(framedisplay, text="Sender Name", width=13, anchor=W, justify=LEFT,
                           font=('times new roman', 20, 'normal'), bg='snow')
        orderId = Label(framedisplay, text="Order/Inv No.", width=13, anchor=W, justify=LEFT,
                        font=('times new roman', 20, 'normal'), bg='snow')

        self.dataSearchFrame.place(x=150, y=20)

        frameSearch.place(x=10, y=5)
        framedisplay.place(x=10, y=60)

        item_SearchId.place(x=30, y=5)

        item_namelabel.place(x=30, y=5)
        author.place(x=30, y=50)
        price.place(x=30, y=100)
        quantity.place(x=30, y=140)
        borrowFee.place(x=30, y=185)
        rackNumber.place(x=30, y=230)
        date_label.place(x=30, y=285)
        center_location.place(x=30, y=330)
        item_type.place(x=30, y=380)
        receivedBy.place(x=30, y=430)
        sendername.place(x=30, y=480)
        orderId.place(x=30, y=530)

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
        rack_location = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'),
                              bg='light cyan')

        cal = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                    font=('times new roman', 20, 'normal'),
                    bg='light cyan')

        localcenter_menu = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                                 font=('times new roman', 20, 'normal'),
                                 bg='light cyan')

        item_Typemenu = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'),
                              bg='light cyan')

        item_idforSearch.place(x=240, y=5)

        receiver_name = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                              font=('times new roman', 20, 'normal'),
                              bg='light cyan')

        order_id = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                         font=('times new roman', 20, 'normal'),
                         bg='light cyan')
        sender_name = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                            font=('times new roman', 20, 'normal'),
                            bg='light cyan')
        item_name.place(x=240, y=5)
        author_menu.place(x=240, y=50)
        item_price.place(x=240, y=100)
        item_quantity.place(x=240, y=145)
        item_borrowfee.place(x=240, y=190)
        rack_location.place(x=240, y=235)
        cal.place(x=240, y=280)
        localcenter_menu.place(x=240, y=325)
        item_Typemenu.place(x=240, y=380)
        receiver_name.place(x=240, y=435)
        order_id.place(x=240, y=480)
        sender_name.place(x=240, y=525)

        search_result = partial(self.search_itemId, item_idforSearch, item_name, author_menu,
                                item_price,
                                item_borrowfee,
                                item_quantity, rack_location, cal, localcenter_menu, item_Typemenu, receiver_name,
                                order_id, sender_name, OPERATION_SEARCH)

        btn_search.configure(text="Search", fg="Black", command=search_result,
                             font=('arial narrow', 14, 'normal'), width=19, state=NORMAL, bg='RosyBrown1')
        btn_search.place(x=540, y=2)

        self.btn_submit.configure(state=DISABLED, bg='light grey')

        self.account_control_window.bind('<Return>', lambda event=None: btn_search.invoke())
        self.account_control_window.bind('<Escape>', lambda event=None: self.btn_cancel.invoke())
        self.account_control_window.bind('<Alt-r>', lambda event=None: self.btn_clear.invoke())

        self.account_control_window.focus()
        self.account_control_window.grab_set()
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

    def stock_operations(self, account_control_window, item_name, item_idforSearch, author_name, item_price,
                         item_borrowfee,
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

    def search_itemId(self, item_idforSearch, item_name, authorText,
                      item_price,
                      item_borrowfee,
                      item_quantity, rack_location, cal, local_centerText, item_TypeText, receiver_name, order_id,
                      sender_name, op_type):

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
                authorText.set(result[3])
                item_price.delete(0, END)
                item_price.insert(0, result[4])
                item_borrowfee.delete(0, END)
                item_borrowfee.insert(0, result[5])
                item_quantity.delete(0, END)
                item_quantity.insert(0, result[6])
                rack_location.delete(0, END)
                rack_location.insert(0, result[7])
                local_centerText.set(result[9])
                cal.delete(0, END)
                cal.insert(0, result[8])
                item_TypeText.set(result[10])
                receiver_name.delete(0, END)
                receiver_name.insert(0, result[11])
                order_id.delete(0, END)
                order_id.insert(0, result[12])
                sender_name.delete(0, END)
                sender_name.insert(0, result[13])
            elif op_type == OPERATION_SEARCH:
                item_name['text'] = result[2]
                authorText['text'] = result[3]
                item_price['text'] = result[4]
                item_borrowfee['text'] = result[5]
                item_quantity['text'] = result[6]
                rack_location['text'] = result[7]
                local_centerText['text'] = result[9]
                cal['text'] = result[8]
                item_TypeText['text'] = result[10]
                receiver_name['text'] = result[11]
                order_id['text'] = result[13]
                sender_name['text'] = result[12]
            else:
                ''' do nothing '''

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

    def validate_itemId(self, itemId):
        print("validate_itemId--> Start for item Id : ", itemId)
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT EXISTS(SELECT * FROM inventory_stock WHERE Item_Id = %s)", (itemId,))
        result = cursor.fetchone()
        print("result :", result[0])
        conn.close()
        return result[0]

    def validate_account(self, name_text):
        print("validate_author--> validate for Name : ", name_text)
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT EXISTS(SELECT * FROM userlogin WHERE username = %s)", (name_text,))
        result = cursor.fetchone()
        print("validate_account :", result[0])
        conn.close()
        return result[0]

    def register_account(self,username_text, password_text, roleText):
        """ register the author"""
        if username_text.get() == "" or password_text.get() == "":
            messagebox.showinfo("Data Entry Error", "All fields are mandatory !!!")
        else:
            bitemExists = self.validate_account(username_text.get())
            print("Account Exists :", bitemExists)
            if bitemExists:
                messagebox.showwarning("Duplicate Entry Error !", "Author already exists !!")
                username_text.configure(bd=2, fg='red')
                return
            else:
                conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()
                total_records = cursor.execute("SELECT * FROM userlogin")
                conn.close()

                if total_records is 0:
                    serial_no = 1
                else:
                    serial_no = total_records + 1

                # establishing the connection

                conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                username = str(username_text.get())

                sql = "INSERT INTO userlogin VALUES(%s, %s, %s, %s)"
                values = (
                    serial_no, username, password_text.get(), roleText.get())
                cursor.execute(sql, values)

                conn.commit()
                conn.close()
                print("Account created !!! ")

                self.btn_submit.configure(state=DISABLED, bg='light grey')

                user_choice = messagebox.askquestion("Success", "Want to create new ?")
                # destroy the data entry form , if user do not want to add more records
                if user_choice == 'no':
                    print("Do nothing")

    def edit_account_password(self, username_text, password_text, roleText):
        """ register the author"""
        if username_text.get() == "" or password_text.get() == "":
            messagebox.showinfo("Data Entry Error", "All fields are mandatory !!!")
        else:
            bitemExists = self.validate_account(username_text.get())
            print("Account Exists :", bitemExists)
            if not bitemExists:
                messagebox.showwarning("No Data !", "Account Unavailable !!")
                username_text.configure(bd=2, fg='red')
                return
            else:
                conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()
                total_records = cursor.execute("SELECT * FROM userlogin")
                conn.close()

                # establishing the connection

                conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                sql = "UPDATE userlogin set password = %s,category = %s where username = %s "
                values = (
                    password_text.get(),roleText.get(), username_text.get())
                cursor.execute(sql, values)

                conn.commit()
                conn.close()
                print("Password changed !!! ")

                self.btn_submit.configure(state=DISABLED, bg='light grey')
                messagebox.showinfo("Success", "Password change success")

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
