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
import os

from app_defines import *
from app_common import *
from app_thread import *
import MySQLdb as sql_db


class NewInventory:

    # constructor for Library class
    def __init__(self, master, loggeduser):
        self.currentuser = loggeduser
        self.obj_commonUtil = CommonUtil()
        self.dateTimeOp = DatetimeOperation()
        self.newItem_window = Toplevel(master)
        width, height = pyautogui.size()
        self.newItem_window.title("Inventory Operations")
        self.newItem_window.geometry(
            '{}x{}+{}+{}'.format(int('770'), int('450'), int(width / 2.82), int(height / 3.6)))

        self.newItem_window.configure(background='wheat')
        self.newItem_window.resizable(width=False, height=False)
        self.newItem_window.protocol('WM_DELETE_WINDOW', self.obj_commonUtil.donothing)

        canvas_width, canvas_height = 970, 750
        canvas = Canvas(self.newItem_window, width=canvas_width, height=canvas_height)
        myimage = ImageTk.PhotoImage(
            PIL.Image.open("..\\Images\\Logos\\Geometry-Header-1920x1080.jpg"))
        canvas.create_image(0, 0, anchor=NW, image=myimage)
        canvas.pack()

        self.mainMenuFrame = Frame(self.newItem_window, width=153, height=215, bd=4, relief='ridge',
                                   bg='wheat')
        self.opMenuFrame = Frame(self.newItem_window, width=153, height=215, bd=4, relief='ridge',
                                 bg='wheat')
        mainmenu_label = Label(self.mainMenuFrame, text="Main Menu", width=12, justify=CENTER,
                               font=L_FONT,
                               bg='wheat')
        opmenu_label = Label(self.opMenuFrame, text="Context Menu", width=12, justify=CENTER,
                             font=L_FONT,
                             bg='wheat')
        self.dataEntryFrame = Frame(self.newItem_window, width=600, height=440, bd=4, relief='ridge',
                                    bg='snow')
        self.dataEntryFrame.pack()
        self.dataModifyFrame = Frame(self.newItem_window, width=600, height=400, bd=4, relief='ridge',
                                     bg='snow')
        self.dataModifyFrame.pack()
        self.dataSearchFrame = Frame(self.newItem_window, width=800, height=500, bd=4, relief='ridge',
                                     bg='snow')
        self.dataSearchFrame.pack()

        self.authorFrame = Frame(self.newItem_window, width=800, height=500, bd=4, relief='ridge',
                                 bg='snow')
        self.authorFrame.pack()
        self.btn_submit = Button(self.opMenuFrame, text="Save", fg="Black",
                                 font=L_FONT, width=12, state=DISABLED, bg='RosyBrown1')
        self.btn_print = Button(self.opMenuFrame, text="Print", fg="Black",
                                font=L_FONT, width=12, state=DISABLED, bg='Light Grey')
        self.btn_reset = Button(self.opMenuFrame, text="Reset", fg="Black",
                                font=L_FONT, width=12, state=NORMAL, bg='RosyBrown1')
        self.btn_cancel = Button(self.opMenuFrame, text="Close", fg="Black",
                                 font=L_FONT, width=12, state=NORMAL, bg='RosyBrown1')
        self.btn_cancel.configure(command=self.newItem_window.destroy)

        # Side button panel - start
        author_result = partial(self.add_author, master)
        self.btn_author = Button(self.mainMenuFrame, text="Add Author", fg="Black", command=author_result,
                                 font=L_FONT, width=12, state=NORMAL, bg='RosyBrown1')
        search_result = partial(self.search_inventory_item, master)
        self.btn_search = Button(self.mainMenuFrame, text="Search Item", fg="Black", command=search_result,
                                 font=L_FONT, width=12, state=NORMAL, bg='RosyBrown1')

        edit_result = partial(self.edit_inventory_item, master)
        self.btn_modify = Button(self.mainMenuFrame, text="Modify Item", fg="Black", command=edit_result,
                                 font=L_FONT, width=12, state=NORMAL, bg='RosyBrown1')
        add_result = partial(self.add_inventory_item, master)
        self.btn_add = Button(self.mainMenuFrame, text="Add Item", fg="Black", command=add_result,
                              font=L_FONT, width=12, state=NORMAL, bg='RosyBrown1')
        # Side button panel - end
        self.mainMenuFrame.place(x=5, y=5)
        mainmenu_label.place(x=2, y=5)
        self.btn_add.place(x=1, y=40)
        self.btn_modify.place(x=1, y=80)
        self.btn_search.place(x=1, y=120)
        self.btn_author.place(x=1, y=160)

        self.opMenuFrame.place(x=5, y=230)
        opmenu_label.place(x=2, y=5)
        self.btn_submit.place(x=1, y=40)
        self.btn_print.place(x=1, y=80)
        self.btn_reset.place(x=1, y=120)
        self.btn_cancel.place(x=1, y=160)
        print("constructor called for newInventory Addition ")

        # default window is "Add New Inventor" when window opens
        self.add_inventory_item(master)

    def add_inventory_item(self, master):
        self.dataEntryFrame.destroy()
        self.dataModifyFrame.destroy()
        self.dataSearchFrame.destroy()
        self.authorFrame.destroy()

        self.dataEntryFrame = Frame(self.newItem_window, width=600, height=440, bd=4, relief='ridge',
                                    bg='snow')
        self.dataEntryFrame.pack()
        heading = Label(self.newItem_window, text="New item/Sukrit Product Entry", font=('ariel narrow', 15, 'bold'),
                        bg='wheat')
        self.default_text5 = StringVar(self.dataEntryFrame, value='0')
        self.default_text4 = StringVar(self.dataEntryFrame, value='')
        self.default_text3 = StringVar(self.dataEntryFrame, value='')
        self.default_text2 = StringVar(self.dataEntryFrame, value='')
        self.default_text1 = StringVar(self.dataEntryFrame, value='')
        self.default_text6 = StringVar(self.dataEntryFrame, value='')
        self.default_text7 = StringVar(self.dataEntryFrame, value='')
        self.default_text8 = StringVar(self.dataEntryFrame, value='')

        name = Label(self.dataEntryFrame, text="Item Name", width=11, anchor=W, justify=LEFT,
                     font=L_FONT,
                     bg='snow')

        # create a Author label
        author = Label(self.dataEntryFrame, text="Author", width=11, anchor=W, justify=LEFT,
                       font=L_FONT,
                       bg='snow')

        # create a Price label
        price = Label(self.dataEntryFrame, text="Price(Rs.)", width=13, anchor=W, justify=LEFT,
                      font=L_FONT, bg='snow')

        # create a Quantity label
        quantity = Label(self.dataEntryFrame, text="Quantity", width=13, anchor=W, justify=LEFT,
                         font=L_FONT, bg='snow')

        # create a borrow fee label
        borrowFee = Label(self.dataEntryFrame, text="Borrow Fee(Rs.)", width=13, anchor=W, justify=LEFT,
                          font=L_FONT, bg='snow')

        # create a borrow fee label
        rackNumber = Label(self.dataEntryFrame, text="Rack Number", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')

        # create a borrow fee label
        date_label = Label(self.dataEntryFrame, text="Received On", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')

        center_location = Label(self.dataEntryFrame, text="Center Name", width=13, anchor=W, justify=LEFT,
                                font=L_FONT, bg='snow')
        item_type = Label(self.dataEntryFrame, text="Item Type", width=13, anchor=W, justify=LEFT,
                          font=L_FONT, bg='snow')

        receivedBy = Label(self.dataEntryFrame, text="Received By", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')

        # create a Quantity label
        sendername = Label(self.dataEntryFrame, text="Sender Name", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')

        # create a borrow fee label
        orderId = Label(self.dataEntryFrame, text="Order/Inv No.", width=13, anchor=W, justify=LEFT,
                        font=L_FONT, bg='snow')

        self.dataEntryFrame.place(x=160, y=5)

        name.place(x=30, y=10)
        author.place(x=30, y=45)
        price.place(x=30, y=80)
        quantity.place(x=30, y=115)
        borrowFee.place(x=30, y=150)
        rackNumber.place(x=30, y=185)
        date_label.place(x=30, y=220)
        center_location.place(x=30, y=255)
        item_type.place(x=30, y=290)
        receivedBy.place(x=30, y=325)
        orderId.place(x=30, y=360)
        sendername.place(x=30, y=395)

        item_name = Entry(self.dataEntryFrame, width=35, font=NORM_FONT, bg='light cyan',
                          textvariable=self.default_text1)

        authorText = StringVar(self.dataEntryFrame)
        authorList = self.get_authorNames()  # self.obj_commonUtil.getAuthorNames()
        newAutorList = []
        iloop = 0
        for x in authorList:
            newAutorList.append(x[0])
            iloop = iloop + 1
        print("Author list  - ", newAutorList)
        authorText.set(newAutorList[0])
        author_menu = OptionMenu(self.dataEntryFrame, authorText, *newAutorList)
        author_menu.configure(width=31, font=NORM_FONT, bg='light cyan', anchor=W,
                              justify=LEFT)

        item_price = Entry(self.dataEntryFrame, width=35, font=NORM_FONT, bg='light cyan',
                           textvariable=self.default_text3)

        item_quantity = Entry(self.dataEntryFrame, width=35, font=NORM_FONT, bg='light cyan',
                              textvariable=self.default_text4)
        item_borrowfee = Entry(self.dataEntryFrame, width=35, text='0', state=DISABLED,
                               font=NORM_FONT,
                               bg='light grey', textvariable=self.default_text5)
        rack_location = Entry(self.dataEntryFrame, width=35, font=NORM_FONT, bg='light cyan')

        cal = DateEntry(self.dataEntryFrame, width=33, date_pattern='dd/MM/yyyy',
                        font=NORM_FONT,
                        bg='light cyan',
                        justify='left')
        local_centerText = StringVar(self.dataEntryFrame)

        localCenterList = self.get_centerNames()
        print("Center list  - ", localCenterList)
        newCenterList = []
        iloop = 0
        for x in localCenterList:
            newCenterList.append(x[0])
            iloop = iloop + 1
        print("Center list  - ", newCenterList)
        local_centerText.set(newCenterList[0])
        localcenter_menu = OptionMenu(self.dataEntryFrame, local_centerText, *newCenterList)
        localcenter_menu.configure(width=31, font=NORM_FONT, bg='light cyan', anchor=W,
                                   justify=LEFT)

        item_TypeText = StringVar(self.dataEntryFrame)
        itemtypeList = ['Commercial', 'Non-Commercial']
        print("Item Type list  - ", itemtypeList)
        item_TypeText.set(itemtypeList[0])
        item_Typemenu = OptionMenu(self.dataEntryFrame, item_TypeText, *itemtypeList)
        item_Typemenu.configure(width=31, font=NORM_FONT, bg='light cyan', anchor=W,
                                justify=LEFT)

        receiver_name = Entry(self.dataEntryFrame, width=35, font=NORM_FONT, bg='light cyan',
                              textvariable=self.default_text6)

        order_id = Entry(self.dataEntryFrame, width=35, font=NORM_FONT, bg='light cyan',
                         textvariable=self.default_text7)
        sender_name = Entry(self.dataEntryFrame, width=35, text='0',
                            font=NORM_FONT,
                            bg='light cyan', textvariable=self.default_text8)

        item_name.place(x=240, y=10)
        author_menu.place(x=240, y=40)
        item_price.place(x=240, y=80)
        item_quantity.place(x=240, y=115)
        item_borrowfee.place(x=240, y=150)
        rack_location.place(x=240, y=185)
        cal.place(x=240, y=220)
        localcenter_menu.place(x=240, y=255)
        item_Typemenu.place(x=240, y=290)
        receiver_name.place(x=240, y=325)
        order_id.place(x=240, y=360)
        sender_name.place(x=240, y=395)

        insert_result = partial(self.stock_operations, self.newItem_window, item_name, 'NA', authorText,
                                item_price,
                                item_borrowfee,
                                item_quantity, rack_location, cal, local_centerText, item_TypeText, OPERATION_ADD,
                                receiver_name, order_id, sender_name)

        # create a Save Button and place into the self.newItem_window window

        self.btn_submit.configure(state=NORMAL, bg='RosyBrown1', command=insert_result)

        self.default_text1.trace("w", self.check_SaveItemBtn_state)
        # self.default_text2.trace("w", self.check_SaveItemBtn_state)
        self.default_text3.trace("w", self.check_SaveItemBtn_state)
        self.default_text4.trace("w", self.check_SaveItemBtn_state)
        self.default_text5.trace("w", self.check_SaveItemBtn_state)
        clear_result = partial(self.clear_form_addInventory, item_name, authorText, item_price, item_borrowfee,
                               item_quantity, rack_location,
                               receiver_name, order_id, sender_name)

        self.btn_reset.configure(state=NORMAL, bg='RosyBrown1', command=clear_result)
        self.btn_cancel.configure(command=self.newItem_window.destroy)
        # cancel.grid(row=0, column=2)

        # ---------------------------------Button Frame End----------------------------------------

        self.newItem_window.bind('<Return>', lambda event=None: self.btn_submit.invoke())
        self.newItem_window.bind('<Escape>', lambda event=None: self.btn_cancel.invoke())
        self.newItem_window.bind('<Alt-r>', lambda event=None: self.btn_reset.invoke())

        self.newItem_window.focus()
        self.newItem_window.grab_set()
        mainloop()

    def edit_inventory_item(self, master):
        self.dataEntryFrame.destroy()
        self.dataModifyFrame.destroy()
        self.dataSearchFrame.destroy()
        self.authorFrame.destroy()

        self.dataModifyFrame = Frame(self.newItem_window, width=600, height=440, bd=4, relief='ridge',
                                     bg='snow')
        self.dataModifyFrame.pack()
        frameSearch = Frame(self.dataModifyFrame, width=580, height=40, bd=4, relief='ridge',
                            bg='snow')
        frameSearch.pack()
        framedisplay = Frame(self.dataModifyFrame, width=580, height=387, bd=4, relief='ridge',
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
                              font=L_FONT,
                              bg='snow')

        item_namelabel = Label(framedisplay, text="Item Name", width=11, anchor=W, justify=LEFT,
                               font=L_FONT,
                               bg='snow')

        author = Label(framedisplay, text="Author", width=11, anchor=W, justify=LEFT,
                       font=L_FONT,
                       bg='snow')

        # create a Price label
        price = Label(framedisplay, text="Price(Rs.)", width=13, anchor=W, justify=LEFT,
                      font=L_FONT, bg='snow')

        # create a Quantity label
        quantity = Label(framedisplay, text="Quantity", width=13, anchor=W, justify=LEFT,
                         font=L_FONT, bg='snow')

        # create a borrow fee label
        borrowFee = Label(framedisplay, text="Borrow Fee(Rs.)", width=13, anchor=W, justify=LEFT,
                          font=L_FONT, bg='snow')

        # create a borrow fee label
        rackNumber = Label(framedisplay, text="Rack Number", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')

        # create a borrow fee label
        date_label = Label(framedisplay, text="Received On", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')

        center_location = Label(framedisplay, text="Center Name", width=13, anchor=W, justify=LEFT,
                                font=L_FONT, bg='snow')
        item_type = Label(framedisplay, text="Item Type", width=13, anchor=W, justify=LEFT,
                          font=L_FONT, bg='snow')
        receivedBy = Label(framedisplay, text="Received By", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')
        sendername = Label(framedisplay, text="Sender Name", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')
        orderId = Label(framedisplay, text="Order/Inv No.", width=13, anchor=W, justify=LEFT,
                        font=L_FONT, bg='snow')

        self.dataModifyFrame.place(x=160, y=5)

        frameSearch.place(x=10, y=5)
        framedisplay.place(x=10, y=45)

        item_SearchId.place(x=30, y=2)

        item_namelabel.place(x=30, y=5)
        author.place(x=30, y=38)
        price.place(x=30, y=70)
        quantity.place(x=30, y=105)
        rackNumber.place(x=30, y=140)
        date_label.place(x=30, y=175)
        center_location.place(x=30, y=210)
        item_type.place(x=30, y=245)
        receivedBy.place(x=30, y=280)
        sendername.place(x=30, y=315)
        orderId.place(x=30, y=350)

        item_idforSearch = Entry(frameSearch, width=20, font=L_FONT, bg='light cyan')
        btn_search = Button(frameSearch)

        item_name = Entry(framedisplay, width=35, font=NORM_FONT, bg='light cyan',
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

        author_menu.configure(width=31, font=NORM_FONT, bg='light cyan', anchor=W,
                              justify=LEFT)

        item_price = Entry(framedisplay, width=35, font=NORM_FONT, bg='light cyan',
                           textvariable=self.default_text3)

        item_quantity = Entry(framedisplay, width=35, font=NORM_FONT, bg='light cyan',
                              textvariable=self.default_text4)
        item_borrowfee = Entry(framedisplay, width=35, text='0', state=DISABLED,
                               font=NORM_FONT,
                               bg='light grey', textvariable=self.default_text5)
        rack_location = Entry(framedisplay, width=35, font=NORM_FONT, bg='light cyan')

        cal = DateEntry(framedisplay, width=33, date_pattern='dd/MM/yyyy',
                        font=NORM_FONT,
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
        localcenter_menu.configure(width=31, font=NORM_FONT, bg='light cyan', anchor=W,
                                   justify=LEFT)

        item_TypeText = StringVar(framedisplay)
        itemtypeList = ['Commercial', 'Non-Commercial']
        print("Item Type list  - ", itemtypeList)
        item_TypeText.set(itemtypeList[0])
        item_Typemenu = OptionMenu(framedisplay, item_TypeText, *itemtypeList)
        item_Typemenu.configure(width=31, font=NORM_FONT, bg='light cyan', anchor=W,
                                justify=LEFT)
        receiver_name = Entry(framedisplay, width=35, font=NORM_FONT, bg='light cyan',
                              textvariable=self.default_text6)

        order_id = Entry(framedisplay, width=35, font=NORM_FONT, bg='light cyan',
                         textvariable=self.default_text7)
        sender_name = Entry(framedisplay, width=35, text='0', font=NORM_FONT,
                            bg='light cyan', textvariable=self.default_text8)

        item_idforSearch.place(x=200, y=5)
        item_name.place(x=200, y=5)
        author_menu.place(x=197, y=34)
        item_price.place(x=200, y=75)
        item_quantity.place(x=200, y=105)
        rack_location.place(x=200, y=138)
        cal.place(x=200, y=173)
        localcenter_menu.place(x=197, y=205)
        item_Typemenu.place(x=197, y=245)
        receiver_name.place(x=200, y=285)
        sender_name.place(x=200, y=318)
        order_id.place(x=200, y=353)

        search_result = partial(self.search_itemId, item_idforSearch, item_name, authorText,
                                item_price,
                                item_quantity, rack_location, cal, local_centerText, item_TypeText, receiver_name,
                                sender_name, order_id, OPERATION_EDIT)

        btn_search.configure(text="Search", fg="Black", command=search_result,
                             font=NORM_FONT, width=15, state=NORMAL, bg='RosyBrown1')
        btn_search.place(x=420, y=1)

        insert_result = partial(self.stock_operations, self.newItem_window, item_name, item_idforSearch, authorText,
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

        self.btn_reset.configure(state=DISABLED, bg='light grey')

        # ---------------------------------Button Frame End----------------------------------------

        self.newItem_window.bind('<Return>', lambda event=None: btn_search.invoke())
        self.newItem_window.bind('<Escape>', lambda event=None: self.btn_cancel.invoke())
        self.newItem_window.bind('<F9>', lambda event=None: self.btn_reset.invoke())

        self.newItem_window.focus()
        self.newItem_window.grab_set()
        mainloop()

    def search_inventory_item(self, master):
        self.dataEntryFrame.destroy()
        self.dataModifyFrame.destroy()
        self.dataSearchFrame.destroy()
        self.authorFrame.destroy()
        self.dataSearchFrame = Frame(self.newItem_window, width=600, height=440, bd=4, relief='ridge',
                                     bg='snow')
        self.dataSearchFrame.pack()
        frameSearch = Frame(self.dataSearchFrame, width=580, height=40, bd=4, relief='ridge',
                            bg='snow')
        frameSearch.pack()
        framedisplay = Frame(self.dataSearchFrame, width=580, height=387, bd=4, relief='ridge',
                             bg='snow')
        framedisplay.pack()

        # create a item Name label

        item_SearchId = Label(frameSearch, text="Search Item Id", width=11, anchor=W, justify=LEFT,
                              font=L_FONT,
                              bg='snow')

        item_namelabel = Label(framedisplay, text="Item Name", width=11, anchor=W, justify=LEFT,
                               font=L_FONT,
                               bg='snow')

        author = Label(framedisplay, text="Author", width=11, anchor=W, justify=LEFT,
                       font=L_FONT,
                       bg='snow')

        # create a Price label
        price = Label(framedisplay, text="Price(Rs.)", width=13, anchor=W, justify=LEFT,
                      font=L_FONT, bg='snow')

        # create a Quantity label
        quantity = Label(framedisplay, text="Quantity", width=13, anchor=W, justify=LEFT,
                         font=L_FONT, bg='snow')

        # create a borrow fee label
        rackNumber = Label(framedisplay, text="Rack Number", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')

        # create a borrow fee label
        date_label = Label(framedisplay, text="Received On", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')

        center_location = Label(framedisplay, text="Center Name", width=13, anchor=W, justify=LEFT,
                                font=L_FONT, bg='snow')
        item_type = Label(framedisplay, text="Item Type", width=13, anchor=W, justify=LEFT,
                          font=L_FONT, bg='snow')
        receivedBy = Label(framedisplay, text="Received By", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')
        sendername = Label(framedisplay, text="Sender Name", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')
        orderId = Label(framedisplay, text="Order/Inv No.", width=13, anchor=W, justify=LEFT,
                        font=L_FONT, bg='snow')

        self.dataSearchFrame.place(x=160, y=5)

        frameSearch.place(x=10, y=5)
        framedisplay.place(x=10, y=45)

        item_SearchId.place(x=30, y=2)
        item_namelabel.place(x=30, y=5)
        author.place(x=30, y=38)
        price.place(x=30, y=70)
        quantity.place(x=30, y=105)
        rackNumber.place(x=30, y=140)
        date_label.place(x=30, y=175)
        center_location.place(x=30, y=210)
        item_type.place(x=30, y=245)
        receivedBy.place(x=30, y=280)
        sendername.place(x=30, y=315)
        orderId.place(x=30, y=350)

        item_idforSearch = Entry(frameSearch, width=20, font=L_FONT, bg='light cyan')
        btn_search = Button(frameSearch)

        item_name = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                          font=NORM_FONT,
                          bg='light cyan')

        author_menu = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                            font=NORM_FONT,
                            bg='light cyan')

        item_price = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                           font=NORM_FONT,
                           bg='light cyan')

        item_quantity = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                              font=NORM_FONT,
                              bg='light cyan')

        rack_location = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                              font=NORM_FONT,
                              bg='light cyan')

        cal = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                    font=NORM_FONT,
                    bg='light cyan')

        localcenter_menu = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                                 font=NORM_FONT,
                                 bg='light cyan')

        item_Typemenu = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                              font=NORM_FONT,
                              bg='light cyan')
        receiver_name = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                              font=NORM_FONT,
                              bg='light cyan')

        order_id = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                         font=NORM_FONT,
                         bg='light cyan')
        sender_name = Label(framedisplay, width=32, anchor=W, justify=LEFT,
                            font=NORM_FONT,
                            bg='light cyan')

        item_idforSearch.place(x=200, y=5)
        item_name.place(x=200, y=7)
        author_menu.place(x=200, y=40)
        item_price.place(x=200, y=73)
        item_quantity.place(x=200, y=106)
        rack_location.place(x=200, y=139)
        cal.place(x=200, y=172)
        localcenter_menu.place(x=200, y=211)
        item_Typemenu.place(x=200, y=245)
        receiver_name.place(x=200, y=280)
        sender_name.place(x=200, y=313)
        order_id.place(x=200, y=347)

        search_result = partial(self.search_itemId, item_idforSearch, item_name, author_menu,
                                item_price,
                                item_quantity, rack_location, cal, localcenter_menu, item_Typemenu, receiver_name,
                                order_id, sender_name, OPERATION_SEARCH)

        btn_search.configure(text="Search", fg="Black", command=search_result,
                             font=NORM_FONT, width=15, state=NORMAL, bg='RosyBrown1')
        btn_search.place(x=420, y=1)

        self.btn_submit.configure(state=DISABLED, bg='light grey')

        self.newItem_window.bind('<Return>', lambda event=None: btn_search.invoke())
        self.newItem_window.bind('<Escape>', lambda event=None: self.btn_cancel.invoke())
        self.newItem_window.bind('<Alt-r>', lambda event=None: self.btn_reset.invoke())

        self.newItem_window.focus()
        self.newItem_window.grab_set()
        mainloop()

    def add_author(self, master):
        self.dataEntryFrame.destroy()
        self.dataModifyFrame.destroy()
        self.dataSearchFrame.destroy()
        self.authorFrame.destroy()

        self.authorFrame = Frame(self.newItem_window, width=600, height=440, bd=4, relief='ridge',
                                 bg='snow')
        self.authorFrame.pack()

        self.default_text1 = StringVar(self.authorFrame, value='')

        # create a item Name label

        name = Label(self.authorFrame, text="Author Name", width=11, anchor=W, justify=LEFT,
                     font=L_FONT,
                     bg='snow')

        # create a Author label
        dor = Label(self.authorFrame, text="DOR", width=9, anchor=W, justify=LEFT,
                    font=L_FONT,
                    bg='snow')

        self.authorFrame.place(x=160, y=5)

        name.place(x=30, y=10)
        dor.place(x=30, y=65)

        name_text = Entry(self.authorFrame, width=30, font=L_FONT, bg='light cyan',
                          textvariable=self.default_text1)

        dor_text = DateEntry(self.authorFrame, width=31, date_pattern='dd/MM/yyyy',
                             font=L_FONT,
                             bg='light cyan',
                             justify='left')

        name_text.place(x=240, y=10)
        dor_text.place(x=240, y=60)

        insert_result = partial(self.register_author, self.newItem_window, name_text, dor_text)

        self.btn_submit.configure(state=NORMAL, bg='RosyBrown1', command=insert_result)

        self.default_text1.trace("w", self.check_SaveItemBtn_author)

        clear_result = partial(self.clear_form_author, name_text)

        self.btn_reset.configure(command=clear_result)
        self.btn_cancel.configure(command=self.newItem_window.destroy)

        self.newItem_window.bind('<Return>', lambda event=None: self.btn_submit.invoke())
        self.newItem_window.bind('<Alt-c>', lambda event=None: self.btn_cancel.invoke())
        self.newItem_window.bind('<Alt-r>', lambda event=None: self.btn_reset.invoke())
        self.display_currentAuthorList(self.authorFrame, 5, 100, 550, 320)
        self.newItem_window.focus()
        self.newItem_window.grab_set()
        mainloop()

    def myfunction(self, xwidth, yheight, mycanvas, event):
        mycanvas.configure(scrollregion=mycanvas.bbox("all"), width=xwidth, height=yheight)

    def display_currentAuthorList(self, split_open_window, startx, starty, xwidth, xheight):
        myframe = Frame(split_open_window, relief=GROOVE, width=400, height=55, bd=4)
        myframe.place(x=startx, y=starty)

        mycanvas = Canvas(myframe)
        frame = Frame(mycanvas, width=200, height=100, bg='light yellow')
        myscrollbar = Scrollbar(myframe, orient="vertical", command=mycanvas.yview)
        mycanvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right", fill="y")
        mycanvas.pack(side="left")
        mycanvas.create_window((0, 0), window=frame, anchor='nw')

        result = partial(self.myfunction, xwidth, xheight, mycanvas)

        frame.bind("<Configure>", result)

        label_sno = Label(frame, text="S.No", width=5, height=1, anchor='center',
                          justify=CENTER,
                          font=('times new roman', 13, 'normal'),
                          bg='light yellow')

        label_authId = Label(frame, text="Author Id", width=10, height=1, anchor='center',
                             justify=CENTER,
                             font=('times new roman', 13, 'normal'),
                             bg='light yellow')

        label_AuthName = Label(frame, text="Author Name", width=30, height=1, anchor='center',
                               justify=CENTER,
                               font=('times new roman', 13, 'normal'),
                               bg='light yellow')

        label_dor = Label(frame, text="DOR", width=10, height=1,
                          anchor='center',
                          justify=CENTER,
                          font=('times new roman', 13, 'normal'),
                          bg='light yellow')

        label_sno.grid(row=0, column=1, padx=2, pady=5)
        label_authId.grid(row=0, column=2, padx=2, pady=5)
        label_AuthName.grid(row=0, column=3, padx=2, pady=5)
        label_dor.grid(row=0, column=4, padx=2, pady=5)

        # fetch the complete author table
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        result_query = cursor.execute("SELECT * FROM author")
        result = cursor.fetchall()
        print(result[0][1])
        print("Total records = ", result_query)
        conn.close()

        for row_index in range(0, result_query):
            # critical stock ->stock with quantity is 0 or 1
            for column_index in range(1, 5):
                if column_index == 1:
                    width_column = 5
                elif column_index == 2:
                    width_column = 10
                elif column_index == 3:
                    width_column = 35
                elif column_index == 4:
                    width_column = 10
                else:
                    print("Column doesn't exists")

                label_detail = Label(frame, text="No Data", width=width_column, height=1,
                                     anchor='center', justify=LEFT,
                                     font=('arial narrow', 13, 'normal'),
                                     bg='light yellow')
                label_detail.grid(row=row_index + 1, column=column_index, padx=2, pady=3, sticky=W)

                label_detail['text'] = result[row_index][column_index - 1]

    def check_SaveItemBtn_state(self, *args):
        print("Tracing  entry input")

        if self.default_text1.get() != "" and \
                self.default_text3.get() != "" and \
                self.default_text4.get() != "" and \
                self.default_text5.get() != "":

            self.btn_submit.configure(state=NORMAL, bg='RosyBrown1')
        else:
            self.btn_submit.configure(state=DISABLED, bg='light grey')

    def check_SaveItemBtn_author(self, *args):
        print("Tracing  entry input")

        if self.default_text1.get() != "":
            self.btn_submit.configure(state=NORMAL, bg='RosyBrown1')
        else:
            self.btn_submit.configure(state=DISABLED, bg='light grey')

    # Function for clearing the
    # contents of text entry boxes
    def clear_form_addInventory(self, name, author, price, quantity, borrowFee, rack_location,
                                receiver_name, order_id, sender_name):
        # clear the content of text entry box
        name.delete(0, END)
        name.configure(fg='black')
        price.delete(0, END)
        price.configure(fg='black')
        quantity.delete(0, END)
        quantity.configure(fg='black')
        borrowFee.delete(0, END)
        borrowFee.configure(fg='black')
        rack_location.delete(0, END)
        rack_location.configure(fg='black')
        receiver_name.delete(0, END)
        receiver_name.configure(fg='black')
        order_id.delete(0, END)
        order_id.configure(fg='black')
        sender_name.delete(0, END)
        sender_name.configure(fg='black')

    def clear_form_author(self, name):
        # clear the content of text entry box
        name.delete(0, END)
        name.configure(fg='black')

    def stock_operations(self, newItem_window, item_name, item_idforSearch, author_name, item_price, item_borrowfee,
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

                if total_records == 0:
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
                    logInfo = str(item_id) + " added" + " successfully"
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
                    logInfo = str(
                        item_id) + " modified" + " successfully" + " to " + itemname + " " + author + " " + str(
                        price) + " " + str(borrow_fee) + " " + str(quantity) + " " + location + " " + str(
                        cal.get_date()) + " " + localcenter + " " + stocktype
                else:
                    '''do nothing'''

                # execute the query
                conn.commit()
                conn.close()
                self.obj_commonUtil.logActivity(self.currentuser, logInfo)
                print("Record inserted !!! ")

                self.btn_submit.configure(state=DISABLED, bg='light grey')
                self.clear_form(item_name, author_name, item_price, item_borrowfee, item_quantity)
                user_choice = messagebox.askquestion("Item insertion success", "Do you want to add another item ? ")
                # destroy the data entry form , if user do not want to add more records
                if user_choice == 'no':
                    print("Do nothing")

    def search_itemId(self, item_idforSearch, item_name, authorText,
                      item_price,
                      item_quantity, rack_location, cal, local_centerText, item_TypeText, receiver_name, sender_name,
                      order_id, op_type):

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
                item_quantity['text'] = result[6]
                rack_location['text'] = result[7]
                local_centerText['text'] = result[9]
                cal['text'] = result[8]
                item_TypeText['text'] = result[10]
                receiver_name['text'] = result[11]
                order_id['text'] = result[13]
                sender_name['text'] = result[12]
                print_result = partial(self.print_item_description, result)
                self.btn_print.configure(state=NORMAL, bg='RosyBrown1', command=print_result)
            else:
                ''' do nothing '''

        else:
            messagebox.showwarning("Not Available", "Item doesn't exists!!!")

    def print_item_description(self, result):
        """ prints the item description to pdf form"""
        wb_template = openpyxl.load_workbook(PATH_ITEM_DETAILS_TEMPLATE)
        template_sheet = wb_template.active
        template_sheet.cell(row=1, column=3).value = result[1]
        template_sheet.cell(row=4, column=2).value = result[2]
        template_sheet.cell(row=6, column=2).value = result[3]
        template_sheet.cell(row=8, column=2).value = result[4]
        template_sheet.cell(row=10, column=2).value = result[6]
        template_sheet.cell(row=12, column=2).value = result[7]

        template_sheet.cell(row=4, column=3).value = result[9]
        template_sheet.cell(row=4, column=4).value = result[11]
        template_sheet.cell(row=6, column=3).value = result[10]
        template_sheet.cell(row=6, column=4).value = result[8]
        template_sheet.cell(row=8, column=3).value = result[12]
        template_sheet.cell(row=8, column=4).value = result[13]
        wb_template.save(PATH_ITEM_DETAILS_TEMPLATE)
        os.startfile(PATH_ITEM_DETAILS_TEMPLATE)  # prints the file on standard output printer

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

    def register_author(self, newItem_window, name_text, dor_text):
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

                if total_records == 0:
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
                self.display_currentAuthorList(self.authorFrame, 5, 100, 550, 320)
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
