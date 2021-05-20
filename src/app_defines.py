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

from dateTime_operation import *


# constants defined for Application
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
BOOK_FIRST = 1
BOOK_SECOND = 2
BOOK_ID = 1
BOOK_NAME = 2
SEARCH_BY_MEMBERID = 1
SEARCH_BY_CONTACTNO = 2
TAX_ON_MRP = 0
ADMIN = "180"
MAX_ALLOWED_DONATION = 10000
CRITICAL_QUANTITY_LIMIT = 5
STOCK_OWNER_TYPE_ASHRAM = "Ashram"
STOCK_OWNER_TYPE_DONATED = "Donated"
VIHANGAM_YOGA_KARNATAKA_TRUST = 1
SADGURU_SADAFAL_AADARSH_GAUSHALA_TRUST = 2
OPERATION_ADD = 1
OPERATION_EDIT = 2
OPERATION_SEARCH = 3
REGULAR_STOCK = 1
CRITICAL_STOCK = 2

# defining fonts for usage in project
NORM_FONT = ('times new roman', 13, 'normal')
NORM_FONT_MEDIUM_HIGH = ('times new roman', 15, 'normal')
NORM_FONT_MEDIUM_LOW = ('times new roman', 14, 'normal')
TIMES_NEW_ROMAN_BIG = ('times new roman', 16, 'normal')
NORM_VERDANA_FONT = ('verdana', 10, 'normal')
BOLD_VERDANA_FONT = ('verdana', 11, 'normal')
LARGE_VERDANA_FONT = ('verdana', 13, 'normal')
XXL_FONT = ('times new roman', 25, 'normal')
XL_FONT = ('times new roman', 20, 'normal')
L_FONT = ('times new roman', 20, 'normal')

# Path for databases
PATH_STOCK = "..\\Library_Stock\\Commercial_stock\\Commercial_Stock.xlsx"
PATH_CRITICAL_STOCK = "..\\Library_Stock\\Critical_Stock\\Critical_Stock.xlsx"
PATH_STAFF = "..\\Staff_Data\\Staff.xlsx"
PATH_MEMBER = "..\\Member_Data\\Member.xlsx"
PATH_STAFF_CREDENTIALS = "..\\Staff_Data\\Staff_credentials.xlsx"
PATH_PURCHASE = "..\\Library_Stock\\Purchase_Transaction.xlsx"
PATH_NON_COMMERCIAL_STOCK = "..\\Library_Stock\\NonCommercial_Stock\\noncommercial_stock.xlsx"
PATH_STOCK_INFO_TEMPLATE = "..\\Library_Stock\\Stock_Statement\\Stock_inventory_template.xlsx"

PATH_TEMPLATE_MEMBERID_CARD = "..\\Member_Data\\ID_Card\\Template\\ID_Card_template.xlsx"
PATH_TEMPLATE_MEMBERID_DETAILS = "..\\Member_Data\\ID_Card\\Template\\Member_details_template.xlsx"
PATH_TEMPLATE_STAFFID_CARD = "..\\Staff_Data\\ID_Card\\Template\\ID_Card_template.xlsx"
PATH_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Monetary_Donation.xlsx"
PATH_SEVA_SHEET_TRIAL = "\\Seva_Rashi\\Donation\\Monetary_Donation.xlsx"
PATH_MONDONATION_STATEMENT_TEMPLATESHEET = "..\\Expanse_Data\\Seva_Rashi\\Template\\account_statement_template.xlsx"
PATH_EXPANSE_SHEET = "..\\Expanse_Data\\Expanse\\Expanse.xlsx"
PATH_ADVANCE_SHEET = "..\\Expanse_Data\\Expanse\\Advance.xlsx"
PATH_TRANSACTION_SHEET = "..\\Expanse_Data\\Transaction\\Transaction.xlsx"
PATH_ACCOUNT_STATEMENT_TEMPLATESHEET = "..\\Expanse_Data\\Account_Statement\\Template\\Transaction_template.xlsx"
PATH_NON_MONETARY_SHEET = "..\\Library_Stock\\NonMonetary_Donation\\NonMonetary_Donation.xlsx"
PATH_AKSHAY_PATRA_DATABASE = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Akshay_patra.xlsx"
PATH_MAGAZINE_SUBSCRIPTION_DATABASE = "..\\Expanse_Data\\Magazine_Subscription\\Subscription.xlsx"
PATH_GAUSHALA_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Gaushala_Donation.xlsx"
PATH_MONTHLY_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Monthly_Donation.xlsx"
PATH_HAWAN_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Hawan_Donation.xlsx"
PATH_EVENT_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Event_prachar_Donation.xlsx"
PATH_AARTI_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Aarti_Donation.xlsx"
PATH_ASHRAM_NIRMAAN_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Ashram_Nirmaan_Donation.xlsx"
PATH_YOGA_FEES_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Yoga_Fees_Donation.xlsx"
PATH_ASHRAM_GENERIC_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Ashram_Generic_Donation.xlsx"


PATH_SORTEDSEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Sorted_List\\Monetary_Donation.xlsx"
PATH_SORTEDAKSHAY_PATRA_DATABASE = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Sorted_List\\Akshay_patra.xlsx"
PATH_SORTEDGAUSHALA_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Sorted_List\\Gaushala_Donation.xlsx"
PATH_SORTEDMONTHLY_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Sorted_List\\Monthly_Donation.xlsx"
PATH_SORTEDHAWAN_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Sorted_List\\Hawan_Donation.xlsx"
PATH_SORTEDEVENT_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Sorted_List\\Event_prachar_Donation.xlsx"
PATH_SORTEDAARTI_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Sorted_List\\Aarti_Donation.xlsx"
PATH_SORTEDASHRAM_NIRMAAN_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Sorted_List\\Ashram_Nirmaan_Donation.xlsx"
PATH_SORTEDYOGA_FEES_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Sorted_List\\Yoga_Fees_Donation.xlsx"
PATH_SORTEDASHRAM_GENERIC_SEVA_SHEET = "..\\Expanse_Data\\Seva_Rashi\\Donation\\Sorted_List\\Ashram_Generic_Donation.xlsx"