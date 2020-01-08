from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import pymysql
root=Tk()
root.title("Inventory")



USERNAME = StringVar()
PASSWORD = StringVar()
Component = StringVar()
Value = StringVar()
Quantity = IntVar()
SEARCH = StringVar()
DELETE = StringVar()






def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()
    
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Account Login", font=('arial', 20))
    lbl_text.pack()
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 20), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 20), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 20), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 20), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=15, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)

def Login(event=None):
 
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    elif (USERNAME.get() == "admin") and (PASSWORD.get() == "admin"):
        root.withdraw()
        Home()
        loginform.destroy()
    else:
        lbl_result.config(text="Invalid username or password", fg="red")
        USERNAME.set("")
        PASSWORD.set("")
    
   

def Exit():
    result = tkMessageBox.askquestion('Simple Inventory System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()
def Exit2():
    result = tkMessageBox.askquestion('Simple Inventory System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()
def Home():
    global Home
    Home = Tk()
    Home.title("Inventory System")
    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="Inventory System", font=('arial', 40))
    lbl_display.pack()
    lbl_acc=Label(Home, text="Account", font=('Times', 20,'bold'),bg="#99ff99")
    lbl_acc.place(x=370,y=180)
    logout=Button(Home,text="Logout",font=('Times',15),command=Logout)
    logout.place(x=380,y=240)
    ex1=Button(Home,text="Exit",font=('Times',15),command=Exit2)
    ex1.place(x=380,y=300)
    lbl_inven=Label(Home, text="Inventory", font=('Times', 20,'bold'),bg="#99ff99")
    lbl_inven.place(x=510,y=180)
    add=Button(Home,text="Add New",font=('Times',15),command=ShowAddNew)
    add.place(x=520,y=240)
    view=Button(Home,text="View",font=('Times',15),command=ShowView)
    view.place(x=520,y=300)
    Home.config(bg="#99ff99")


def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add new")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Component", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_productname = Label(MidAddNew, text="Component:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=0, sticky=W)
    lbl_qty = Label(MidAddNew, text="Value:", font=('arial', 25), bd=10)
    lbl_qty.grid(row=1, sticky=W)
    lbl_price = Label(MidAddNew, text="Quantity:", font=('arial', 25), bd=10)
    lbl_price.grid(row=2, sticky=W)
    productname = Entry(MidAddNew, textvariable=Component, font=('arial', 25), width=15)
    productname.grid(row=0, column=1)
    productqty = Entry(MidAddNew, textvariable=Value, font=('arial', 25), width=15)
    productqty.grid(row=1, column=1)
    productprice = Entry(MidAddNew, textvariable=Quantity, font=('arial', 25), width=15)
    productprice.grid(row=2, column=1)
    btn_add = Button(MidAddNew, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=3, columnspan=2, pady=20)

def AddNew():
    Database()
    cursor.execute("INSERT INTO `components` (Component, Value, Quantity) VALUES('{}', '{}', {})".format(Component.get(),Value.get(),Quantity.get()))
    conn.commit()
    Component.set("")
    Value.set("")
    Quantity.set("")
    cursor.close()
    conn.close()

def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("component_id","Component", "Value", "Quantity"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('component_id', text="component_id",anchor=W)
    tree.heading('Component', text="Component",anchor=W)
    tree.heading('Value', text="Value",anchor=W)
    tree.heading('Quantity', text="Quantity",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()

def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `components`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        #cursor.execute("SELECT * FROM `components` WHERE `Component` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        cursor.execute("SELECT * FROM `components` WHERE `Component` LIKE '{}'".format(SEARCH.get()))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")

def Delete():
    
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('Simple Inventory System', 'Are you sure you want to delete this record?', icon="warning")
    if result == 'yes':
        curItem = tree.focus()
        contents =(tree.item(curItem))
        selecteditem = contents['values']
        tree.delete(curItem)
        Database()
        
        cursor.execute("DELETE FROM `components` WHERE `component_id` = %d" % selecteditem[0])
        conn.commit()
        cursor.close()
        conn.close()
        


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("View Product")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()

def Logout():
    result = tkMessageBox.askquestion('Simple Inventory System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        
        root.deiconify()
        Home.destroy()
def Database():
    global conn, cursor
    conn = pymysql.connect("localhost","root","tiger","inventory")
    cursor = conn.cursor()
    

lab=Label(root, text="Inventory System", font=('Times', 25,'bold'))
lab.place(x=370,y=150)
width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#99ff99")
login=Button(root,text="Login",font=('Times',15),command=ShowLoginForm)
login.place(x=420,y=240)
ex=Button(root,text="Exit",font=('Times',15),command=Exit)
ex.place(x=520,y=240)
