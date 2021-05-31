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

        self.deleteaccountfreme = Frame(self.account_control_window, width=800, height=500, bd=4, relief='ridge',
                                        bg='snow')
        self.deleteaccountfreme.pack()

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
        remove_result = partial(self.delete_useract_window, master)
        self.btn_remove = Button(self.account_control_window, text="Remove Account", fg="Black", command=remove_result,
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
        self.obj_commonUtil.logActivity(self.currentuser, "Viewed Current user info")
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

    def delete_useract_window(self, master):
        self.deleteaccountfreme.destroy()
        self.dataSearchFrame.destroy()
        self.userInfoFrame.destroy()

        self.deleteaccountfreme = Frame(self.account_control_window, width=800, height=159, bd=4, relief='ridge',
                                        bg='wheat')
        self.deleteaccountfreme.pack()

        self.default_text2 = StringVar(self.deleteaccountfreme, value='')
        self.default_text1 = StringVar(self.deleteaccountfreme, value='')
        self.deleteaccountfreme.place(x=160, y=5)
        # create a item Name label

        username_label = Label(self.deleteaccountfreme, text="Account Name", width=11, anchor=W, justify=LEFT,
                               font=L_FONT,
                               bg='wheat')

        username_label.place(x=30, y=65)

        username_text = Entry(self.deleteaccountfreme, width=35, font=L_FONT, bg='light cyan',
                              textvariable=self.default_text1, justify=LEFT)

        username_text.place(x=240, y=60)

        insert_result = partial(self.delete_account, username_text)

        self.btn_submit.configure(state=NORMAL, bg='RosyBrown1', command=insert_result)

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

    def register_account(self, username_text, password_text, roleText):
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
                infoText = "New Account created as: " + username
                self.obj_commonUtil.logActivity(self.currentUser, infoText)

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
                    password_text.get(), roleText.get(), username_text.get())
                cursor.execute(sql, values)

                conn.commit()
                conn.close()
                print("Password changed !!! ")

                self.btn_submit.configure(state=DISABLED, bg='light grey')
                messagebox.showinfo("Success", "Password change success")

    def delete_account(self, username_text):
        """ delete user account"""
        if username_text.get() == "":
            messagebox.showinfo("Data Entry Error", "All fields are mandatory !!!")
        else:
            bitemExists = self.validate_account(username_text.get())
            print("Account Exists :", bitemExists)
            if not bitemExists:
                messagebox.showwarning("No Data !", "Account Unavailable !!")
                username_text.configure(bd=2, fg='red')
                return
            else:
                # establishing the connection

                conn = sql_db.connect(user='root', host='192.168.1.109', port=3306, database='inventorydb')

                # Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                sql = "DELETE from userlogin where username = %s "
                values = (username_text.get(),)
                cursor.execute(sql, values)

                conn.commit()
                conn.close()
                print("User Account Deleted !!! ")

                self.btn_submit.configure(state=DISABLED, bg='light grey')
                messagebox.showinfo("Success", "Account Removal success")
                infoText = "Account deletion was success for: " + username_text.get()
                self.obj_commonUtil.logActivity(self.currentUser, infoText)

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
