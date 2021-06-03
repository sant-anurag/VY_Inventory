"""
# Copyright 2020 by Vihangam Yoga Karnataka.
# All rights reserved.
# This file is part of the Vihangan Yoga Operations of Ashram Management Software Package(VYOAM),
# and is released under the "VY License Agreement". Please see the LICENSE
# file that should have been included as part of this package.
# Vihangan Yoga Operations  of Ashram Management Software
# File Name : app_defines.py
# Developer : Sant Anurag Deo
# Version : 2.0
"""

from tkinter import *
from tkinter import messagebox
from random import randint
import os.path
import shutil
from functools import partial
from calendar import monthrange
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk, Image
import PIL.Image
import cv2
from tkinter import filedialog
from datetime import *
import re
import openpyxl
from tkinter import font
from openpyxl.styles import Font
from openpyxl.styles import Alignment
from shutil import copyfile
from win32com import client
import win32com.client
from pywintypes import com_error
import pandas as pd
import subprocess
import num2words
import time
import pyglet
import pyautogui
import MySQLdb as sql_db

from dateTime_operation import *

# constants defined for Application
SQL_SERVER = '192.168.1.109'
INDEX_ZERO = 0
MAX_RECORD_ENTRY = 29
DEFAULT = 1
FIELD_BLANK = -1
MAX_LEN_EXCEED = -2
MAX_ALLOWED_STOCK = 1500
MEMBER_ID_START = 1111
MEMBER_ID_END = 6111
LATE_PAYMENT_FEE = 5
DEFAULT_ITEM_ID = 999
MEMBER_STAFFID_START = 111
MEMBER_STAFFID_END = 500
ITEM_ENTRY = 1
BORROW_BOOK = 2
RETURN_BOOK = 3
DISPLAY_BOOK_INFO = 4
LIB_MEMBER_REGISTRATION = 5
DISPLAY_LIB_MEMBER_INFO = 6
REGISTRATION_STAFF = 7
DISPLAY_STAFF = 8
EXIT_APP = 9
TAX_ON_MRP = 0
ADMIN = "180"
MAX_ALLOWED_DONATION = 10000
CRITICAL_QUANTITY_LIMIT = 5
VIHANGAM_YOGA_KARNATAKA_TRUST = 1
SADGURU_SADAFAL_AADARSH_GAUSHALA_TRUST = 2
OPERATION_ADD = 1
OPERATION_EDIT = 2
OPERATION_SEARCH = 3
REGULAR_STOCK = 1
CRITICAL_STOCK = 2

# defining fonts for usage in project
MEDIUM_FONT = ('times new roman', 12, 'normal')
NORM_FONT = ('times new roman', 13, 'normal')
NORM_FONT_MEDIUM_HIGH = ('times new roman', 15, 'normal')
NORM_FONT_MEDIUM_LOW = ('times new roman', 14, 'normal')
TIMES_NEW_ROMAN_BIG = ('times new roman', 16, 'normal')
NORM_VERDANA_FONT = ('verdana', 10, 'normal')
BOLD_VERDANA_FONT = ('verdana', 11, 'normal')
LARGE_VERDANA_FONT = ('verdana', 13, 'normal')
XXL_FONT = ('times new roman', 25, 'normal')
XL_FONT = ('times new roman', 20, 'normal')
L_FONT = ('times new roman', 15, 'normal')

# Path for databases
PATH_PURCHASE = "..\\Library_Stock\\Purchase_Transaction.xlsx"
PATH_NON_COMMERCIAL_STOCK = "..\\Library_Stock\\NonCommercial_Stock\\noncommercial_stock.xlsx"
PATH_STOCK_INFO_TEMPLATE = "..\\Library_Stock\\Stock_Statement\\Stock_inventory_template.xlsx"
PATH_ITEM_DETAILS_TEMPLATE = "..\\Library_Stock\\Invoices\\Template\\Inventory_Details.xlsx"
PATH_CENTER_DETAILS_TEMPLATE = "..\\Library_Stock\\Invoices\\Template\\Center_details.xlsx"
