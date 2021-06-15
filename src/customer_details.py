"""
# Copyright 2020 by Vihangam Yoga Karnataka.
# All rights reserved.
# This file is part of the Vihangan Yoga Operations of Ashram Management Software Package(VYOAM),
# and is released under the "VY License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
# Vihangan Yoga Operations  of Ashram Management Software
# File Name : Customer_Entry.py
# Developer : Sant Anurag Deo
# Version : 1.0
"""
import os

from app_defines import *
from app_common import *
from app_thread import *


class Customer:

    # constructor for Library class
    def __init__(self, master):
        self.obj_commonUtil = CommonUtil()
        self.dateTimeOp = DatetimeOperation()
        self.newItem_window = Toplevel(master)
        width, height = pyautogui.size()
        self.newItem_window.title("Shopper Operations")
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

        self.mainMenuFrame = Frame(self.newItem_window, width=153, height=170, bd=4, relief='ridge',
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
        add_result = partial(self.add_Customer_item, master)
        self.btn_add = Button(self.mainMenuFrame, text="New Shopper", fg="Black", command=add_result,
                              font=L_FONT, width=12, state=NORMAL, bg='RosyBrown1')

        edit_result = partial(self.edit_Customer_item, master)
        self.btn_modify = Button(self.mainMenuFrame, text="Edit Shopper ", fg="Black", command=edit_result,
                                 font=L_FONT, width=12, state=NORMAL, bg='RosyBrown1')

        search_result = partial(self.search_Customer_item, master)
        self.btn_search = Button(self.mainMenuFrame, text="Search Shopper", fg="Black", command=search_result,
                                 font=L_FONT, width=12, state=NORMAL, bg='RosyBrown1')

        # Side button panel - end
        self.mainMenuFrame.place(x=5, y=5)
        mainmenu_label.place(x=2, y=5)
        self.btn_add.place(x=1, y=40)
        self.btn_modify.place(x=1, y=80)
        self.btn_search.place(x=1, y=120)

        self.opMenuFrame.place(x=5, y=175)
        opmenu_label.place(x=2, y=5)
        self.btn_submit.place(x=1, y=40)
        self.btn_print.place(x=1, y=80)
        self.btn_reset.place(x=1, y=120)
        self.btn_cancel.place(x=1, y=160)
        print("constructor called for newCustomer Addition ")

        # default window is "Add New Inventor" when window opens
        self.add_Customer_item(master)

    def add_Customer_item(self, master):
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

        name_label = Label(self.dataEntryFrame, text="Name", width=11, anchor=W, justify=LEFT,
                           font=L_FONT,
                           bg='snow')

        # create a Author label
        contact_label = Label(self.dataEntryFrame, text="Contact", width=11, anchor=W, justify=LEFT,
                              font=L_FONT,
                              bg='snow')

        # create a Price label
        gender_label = Label(self.dataEntryFrame, text="Gender", width=13, anchor=W, justify=LEFT,
                             font=L_FONT, bg='snow')

        date_label = Label(self.dataEntryFrame, text="Regis. Date", width=13, anchor=W, justify=LEFT,
                           font=L_FONT, bg='snow')

        address_label = Label(self.dataEntryFrame, text="Address", width=13, anchor=W, justify=LEFT,
                              font=L_FONT, bg='snow')

        self.dataEntryFrame.place(x=160, y=5)

        name_label.place(x=30, y=10)
        contact_label.place(x=30, y=45)
        gender_label.place(x=30, y=80)
        date_label.place(x=30, y=115)
        address_label.place(x=30, y=150)

        name_txt = Entry(self.dataEntryFrame, width=35, font=NORM_FONT, bg='light cyan',
                         textvariable=self.default_text1)

        contact_txt = Entry(self.dataEntryFrame, width=35, font=NORM_FONT, bg='light cyan',
                            textvariable=self.default_text2)
        authorText = StringVar(self.dataEntryFrame)
        authorList = ['Male', 'Female', 'Other']  # self.obj_commonUtil.getAuthorNames()
        newAutorList = []
        iloop = 0
        for x in authorList:
            newAutorList.append(x)
            iloop = iloop + 1
        print("Author list  - ", newAutorList)
        authorText.set(newAutorList[0])
        author_menu = OptionMenu(self.dataEntryFrame, authorText, *newAutorList)
        author_menu.configure(width=31, font=NORM_FONT, bg='light cyan', anchor=W,
                              justify=LEFT)

        cal = DateEntry(self.dataEntryFrame, width=33, date_pattern='dd/MM/yyyy',
                        font=NORM_FONT,
                        bg='light cyan',
                        justify='left')
        address_txt = Entry(self.dataEntryFrame, width=35, font=NORM_FONT, bg='light cyan',
                            textvariable=self.default_text3)

        name_txt.place(x=240, y=10)
        contact_txt.place(x=240, y=40)
        author_menu.place(x=238, y=70)
        cal.place(x=240, y=115)
        address_txt.place(x=240, y=150)

        insert_result = partial(self.shopper_operations, name_txt, contact_txt, authorText, cal,
                                address_txt, OPERATION_ADD)

        # create a Save Button and place into the self.newItem_window window

        self.btn_submit.configure(state=NORMAL, bg='RosyBrown1', command=insert_result)

        self.default_text1.trace("w", self.check_SaveItemBtn_state)
        self.default_text2.trace("w", self.check_SaveItemBtn_state)
        self.default_text3.trace("w", self.check_SaveItemBtn_state)

        clear_result = partial(self.clear_form_addCustomer, name_txt, authorText, contact_txt, address_txt)

        self.btn_reset.configure(state=NORMAL, bg='RosyBrown1', command=clear_result)
        self.btn_cancel.configure(command=self.newItem_window.destroy)
        # cancel.grid(row=0, column=2)

        # ---------------------------------Button Frame End----------------------------------------

        self.newItem_window.bind('<Return>', lambda event=None: self.btn_submit.invoke())
        self.newItem_window.bind('<Escape>', lambda event=None: self.btn_cancel.invoke())
        self.newItem_window.bind('<Alt-r>', lambda event=None: self.btn_reset.invoke())
        self.display_currentShopperList(self.dataEntryFrame, 5, 180, 550, 240)
        self.newItem_window.focus()
        self.newItem_window.grab_set()
        mainloop()

    def edit_Customer_item(self, master):
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

        insert_result = partial(self.shopper_operations, self.newItem_window, item_name, item_idforSearch, authorText,
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
        self.display_currentShopperList(self.authorFrame, 5, 100, 550, 320)
        self.newItem_window.focus()
        self.newItem_window.grab_set()
        mainloop()

    def search_Customer_item(self, master):
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
        self.display_currentShopperList(self.authorFrame, 5, 100, 550, 320)
        self.newItem_window.focus()
        self.newItem_window.grab_set()
        mainloop()

    def myfunction(self, xwidth, yheight, mycanvas, event):
        mycanvas.configure(scrollregion=mycanvas.bbox("all"), width=xwidth, height=yheight)

    def display_currentShopperList(self, split_open_window, startx, starty, xwidth, xheight):
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

        label_authId = Label(frame, text="Account No", width=10, height=1, anchor='center',
                             justify=CENTER,
                             font=('times new roman', 13, 'normal'),
                             bg='light yellow')

        label_AuthName = Label(frame, text="Shopper Name", width=30, height=1, anchor='center',
                               justify=CENTER,
                               font=('times new roman', 13, 'normal'),
                               bg='light yellow')

        label_dor = Label(frame, text="Contact No", width=10, height=1,
                          anchor='center',
                          justify=CENTER,
                          font=('times new roman', 13, 'normal'),
                          bg='light yellow')

        label_sno.grid(row=0, column=1, padx=2, pady=5)
        label_authId.grid(row=0, column=2, padx=2, pady=5)
        label_AuthName.grid(row=0, column=3, padx=2, pady=5)
        label_dor.grid(row=0, column=4, padx=2, pady=5)

        # fetch the complete author table
        conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        result_query = cursor.execute("SELECT * FROM customer_details")
        result = cursor.fetchall()
        print(result[0][1])
        print("Total records = ", result_query)
        conn.close()

        for row_index in range(0, result_query):
            # critical shopper ->shopper with quantity is 0 or 1
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
                self.default_text2.get() != "" and \
                self.default_text3.get() != "":
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
    def clear_form_addCustomer(self, name, author, price, quantity, borrowFee, rack_location,
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

    def shopper_operations(self, name_txt, contact_txt, authorText, cal, address_txt, op_type):

        dateTimeObj = cal.get_date()

        regis_date = dateTimeObj.strftime("%Y-%m-%d")
        if op_type == OPERATION_ADD:
            shopper_ActNo = self.generate_customerActNo()  # generates customer account number
        elif op_type == OPERATION_EDIT:
            pass;  # item_id = item_idforSearch.get()
        else:
            pass

        if name_txt.get() == "" or contact_txt.get() == "" or address_txt.get() == "":
            messagebox.showinfo("Data Entry Error", "Name, Contact No. and Address are mandatory !!!")

        else:
            bShopperExists = self.validate_customer(contact_txt.get())
            print("bShopperExists :", bShopperExists)
            if bShopperExists and op_type is OPERATION_ADD:
                messagebox.showwarning("Duplicate Entry Error !", "item already exists !!")
                name_txt.configure(bd=2, fg='red')
                return
            else:
                conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()
                total_records = cursor.execute("SELECT * FROM customer_details")
                conn.close()

                if total_records == 0:
                    serial_no = 1
                else:
                    serial_no = total_records + 1

                # establishing the connection
                print("debug 1")
                conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')
                print("debug 2")
                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()
                print("debug 3")
                shopper_name = str(name_txt.get())
                shopper_contact = str(contact_txt.get())
                shopper_address = str(address_txt.get())
                shopper_redeempt = '0'
                shopper_gender = authorText.get()

                print("\n", serial_no, shopper_ActNo, shopper_name, shopper_contact, shopper_address, shopper_redeempt,
                      shopper_gender)
                if op_type is OPERATION_ADD:
                    print("\n Add operation type")
                    sql = "INSERT INTO customer_details VALUES(%s, %s, %s, %s,%s, %s, %s, %s)"
                    values = (
                        serial_no, shopper_ActNo, shopper_name, shopper_contact, shopper_address, shopper_redeempt,
                        shopper_gender, regis_date)
                    cursor.execute(sql, values)
                    logInfo = str(shopper_ActNo) + " added" + " successfully"
                elif op_type is OPERATION_EDIT:
                    print("\n Edit operation type")
                    sql = "UPDATE customer_details set customer_actno = %s, customer_name = %s, customer_contact = " \
                          "%s, customer_address = %s,customer_redeempoints = %s, customer_gender = %s, customer_regisdate = %s where " \
                          "customer_contact = %s "
                    values = (
                        shopper_ActNo, shopper_name, shopper_contact, shopper_address, shopper_redeempt, shopper_gender,
                        regis_date, shopper_contact)
                    cursor.execute(sql, values)
                    logInfo = str(
                        shopper_ActNo) + " modified" + " successfully" + " to " + shopper_name + " " + shopper_contact + " " + str(
                        shopper_address) + " " + str(shopper_redeempt) + " " + str(shopper_gender) + str(cal.get_date())
                else:
                    '''do nothing'''

                # execute the query
                conn.commit()
                conn.close()
                self.obj_commonUtil.logActivity(logInfo)
                print("Record inserted !!! ")

                self.btn_submit.configure(state=DISABLED, bg='light grey')
                # self.clear_form(item_name, author_name, item_price, item_borrowfee, item_quantity)
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
            conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

            # Creating a cursor object using the cursor() method
            cursor = conn.cursor()

            bItemExist = cursor.execute("SELECT * FROM customer_details WHERE Item_Id = %s", (itemId,))
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

    def generate_customerActNo(self):
        conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        total_records = cursor.execute("SELECT * FROM customer_details")
        conn.close()
        shopper_id = total_records + 100
        return "SACT" + str(shopper_id)  # Shopper Account Number

    def validate_customer(self, contact_txt):
        itemId = ""
        print("validate_customer with contact no: ", contact_txt)
        conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT EXISTS(SELECT * FROM customer_details WHERE customer_contact = %s)",
                                    (contact_txt,))
        result = cursor.fetchone()
        print("result :", result[0])
        conn.close()
        return result[0]

    def validate_itemId(self, itemId):
        print("validate_itemId--> Start for item Id : ", itemId)
        conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        bItemExist = cursor.execute("SELECT EXISTS(SELECT * FROM customer_details WHERE Item_Id = %s)", (itemId,))
        result = cursor.fetchone()
        print("result :", result[0])
        conn.close()
        return result[0]

    def generate_authorId(self):
        conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        total_records = cursor.execute("SELECT * FROM author")
        conn.close()
        authorId = total_records + 100
        return "ATH" + str(authorId)  # Author Id

    def validate_author(self, name_text):
        print("validate_author--> validate for Name : ", name_text)
        conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

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
                conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

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
                conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')
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
                self.display_currentShopperList(self.authorFrame, 5, 100, 550, 320)
                # destroy the data entry form , if user do not want to add more records
                if user_choice == 'no':
                    print("Do nothing")

    def get_authorNames(self):
        print("get_authorNames--> Start for item name: ")
        conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        result_query = cursor.execute("SELECT author_Name FROM author")
        result = cursor.fetchall()
        conn.close()
        return result

    def get_centerNames(self):
        print("get_centerNames--> Start ")
        conn = sql_db.connect(user='root', host=SQL_SERVER, port=3306, database='inventorydb')

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        result_query = cursor.execute("SELECT merchandise_Name FROM merchandise")
        result = cursor.fetchall()
        conn.close()
        return result