"""
# Copyright 2020 by Vihangam Yoga Karnataka.
# All rights reserved.
# This file is part of the Vihangan Yoga Operations of Ashram Management Software Package(VYOAM),
# and is released under the "VY License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
# Vihangan Yoga Operations  of Ashram Management Software
# File Name : Inventory_Main.py
# Developer : Sant Anurag Deo
# Version : 1.0
"""

"""
# Import all necessary packages both system , and software defined
"""
from app_defines import *
from babel.numbers import *
import ctypes
# import for non commercial data operations
import MySQLdb as sql_db
from Inventory_Entry import *
from merchandise import *
from inventory_sales import *
from inventory_report import *
import sqlite3

"""
# Class definition starts here
"""


class Inventory:
    # constructor for Library class
    def __init__(self, master):
        self.list_InvoicePrint = []
        self.itemEntryInstance = False
        self.newItem_window = ""
        self.master = master
        self.print_button = ""
        # sets the configuration of main screen
        self.master.title("Inventory & Sales Management")
        self.main_menu()

    def createInventoryDatabase(self):
        # establishing the connection
        conn = sql_db.connect(user='root', host='192.168.1.109', port=3306)

        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS InventoryDB")
        print("Database Created !!! ")

        cursor.execute("USE InventoryDB")
        sql = '''CREATE TABLE IF NOT EXISTS inventory_stock(
            S_no int,
            Item_Id VARCHAR(255) NOT NULL PRIMARY KEY,
            Item_name VARCHAR(255) NOT NULL,
            Author_Name VARCHAR(255),
            Price int,
            Borrow_Fee int,
            Quantity int,
            Location VARCHAR(255),
            Stock_Receival_Date VARCHAR(255),
            Center_Name VARCHAR(255),
            Stock_Type VARCHAR(255),
            Receiver_name VARCHAR(255),
            order_id VARCHAR(255),
            sender_name VARCHAR(255)
        )'''
        cursor.execute(sql)

        sql = '''CREATE TABLE IF NOT EXISTS merchandise(
            S_no int,
            merchandise_Id VARCHAR(255) NOT NULL,
            merchandise_Name VARCHAR(255),
            merchandise_manager VARCHAR(255),
            merchandise_inaug_date DATE NOT NULL,
            merchandise_regis_no VARCHAR(255),
            merchandise_panno VARCHAR(255),
            merchandise_address VARCHAR(255)
        )'''
        cursor.execute(sql)

        sql = '''CREATE TABLE IF NOT EXISTS author(
            S_no int,
            author_Id VARCHAR(255) NOT NULL,
            author_Name VARCHAR(255),
            author_dor DATE NOT NULL
        )'''
        cursor.execute(sql)

        sql = '''CREATE TABLE IF NOT EXISTS invoice(
            S_no int,
            invoice_id VARCHAR(255) NOT NULL,
            author_date DATE NOT NULL
        )'''
        cursor.execute(sql)

        print("Tables Created !!! ")
        conn.close()

    def new_inventory_view(self):
        obj_newInventory = NewInventory(root)

    def new_center_registration(self):
        obj_newMchd = NewMerchandise(root)

    def sales_operations(self):
        obj_newMchd = InventorySales(root)

    def inventory_report(self):
        obj_newRept = InventoryReport(root)

    def designMainScreen(self, master, canvas):
        labelFrame = Label(master, text="Inventory & Sales Management", justify=CENTER,
                           font=XXL_FONT,
                           fg='black')
        # labelFrame.place(x=200, y=10)
        result_btnInv = partial(self.new_inventory_view)
        btn_inventory = Button(master, text="Inventory", fg="Black", command=result_btnInv,
                               font=XXL_FONT, width=20, state=NORMAL, bg='RosyBrown1')
        # button_load = Image.open('..//Images//Logos//button bg 2.jfif').resize((400, 110))
        # button_img = ImageTk.PhotoImage(button_load)
        # btn_inventory.config(image=button_img, text="Inventory")
        result_sales = partial(self.sales_operations)
        btn_sales = Button(master, text="Sales", fg="Black",command = result_sales,
                           font=XXL_FONT, width=20, state=NORMAL, bg='RosyBrown1')
        result_btnMchd = partial(self.new_center_registration)
        btn_merchandise = Button(master, text="Merchandise", fg="Black",command = result_btnMchd,
                                 font=XXL_FONT, width=20, state=NORMAL, bg='RosyBrown1')
        result_btnReport = partial(self.inventory_report)
        btn_reports = Button(master, text="Reports", fg="Black",command = result_btnReport,
                             font=XXL_FONT, width=20, state=NORMAL, bg='RosyBrown1')
        btn_exit = Button(master, text="Exit", fg="Black",command =master.destroy,
                          font=XXL_FONT, width=20, state=NORMAL, bg='RosyBrown1')
        btn_inventory.place(x=65, y=240)
        btn_sales.place(x=65, y=310)
        btn_merchandise.place(x=65, y=380)
        btn_reports.place(x=65, y=450)
        btn_exit.place(x=65, y=520)

        master.bind('<Escape>', lambda event=None: btn_exit.invoke())

        master.bind('<I>', lambda event=None: btn_inventory.invoke())
        master.bind('<i>', lambda event=None: btn_inventory.invoke())
        master.bind('<S>', lambda event=None: btn_sales.invoke())
        master.bind('<s>', lambda event=None: btn_sales.invoke())
        mainloop()

    def main_menu(self):
        width, height = pyautogui.size()
        self.master.geometry(
            '{}x{}+{}+{}'.format(int(width / 1.25), int(height / 1.25), int(width / 9), int(height / 12)))
        self.master.configure(bg='AntiqueWhite1')
        # canvas designed to display the library image on main screen

        canvas_width, canvas_height = width, height
        canvas = Canvas(self.master, width=canvas_width, height=canvas_height)
        myimage = ImageTk.PhotoImage(
            PIL.Image.open("..\\Images\\Logos\\Geometry-Header-1920x1080.jpg").resize((width, height)))
        canvas.create_image(0, 0, anchor=NW, image=myimage)
        canvas.pack()

        self.master.lift()
        # prevents the application been closed by alt + F4 etc.
        # self.master.overrideredirect(True)
        self.createInventoryDatabase()
        self.designMainScreen(self.master, canvas)
        self.master.mainloop()


# obj_animation = LoadingAnimation()
root = Tk()

# Query DPI Awareness (Windows 10 and 8)
awareness = ctypes.c_int()
errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
print(awareness.value)

# Set DPI Awareness  (Windows 10 and 8)
# errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)
# the argument is the awareness level, which can be 0, 1 or 2:
# for 1-to-1 pixel control I seem to need it to be non-zero (I'm using level 2)
dpi = root.winfo_fpixels('1i')
factor = dpi / 72
root.call('tk', 'scaling', factor)

libraryObj = Inventory(root)
