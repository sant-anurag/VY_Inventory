# Python program demonstrating Multiple selection
# in Listbox widget with a scrollbar



from tkinter import *
from tkinter.ttk import *
from modules.tklistview import MultiListbox
from modules.tktoolbar import _init_toolbar
from models import Inventory_Product as Product

window = Tk()
window.title('Multiple selection')

# for scrolling vertically
yscrollbar = Scrollbar(window)
yscrollbar.pack(side=RIGHT, fill=Y)

label = Label(window,
              text="Select the languages below : ",
              font=("Times New Roman", 10),
              padx=10, pady=10)
label.pack()
list = MultiListbox(self.frame, (('id #',5),('Product', 20), ('Description', 32), ('UnitPrice', 15)))

# Widget expands horizontally and
# vertically by assigning both to
# fill option
list.pack(padx=10, pady=10,
          expand=YES, fill="both")

x = [("C","Dennis Ritche"), "C++", "C#", "Java", "Python",
     "R", "Go", "Ruby", "JavaScript", "Swift",
     "SQL", "Perl", "XML"]

for each_item in range(len(x)):
    list.insert(END, x[each_item])
    list.itemconfig(each_item, bg="lime")

# Attach listbox to vertical scrollbar
yscrollbar.config(command=list.yview)
window.mainloop()
