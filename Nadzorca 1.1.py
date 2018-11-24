import os
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import _mysql
import sys
# from tkinter.ttk import *
host="192.168.1.190"
user="bodzio"
passwd="bodzio123"
db="Gospodarstwo"

Test

def pobranie_danych_db_k(host,user,passwd,db):
    try:
        conn = _mysql.connect(host, user, passwd, db)

        conn.query("SELECT * FROM Konie")
        result = conn.use_result()
        row = result.fetch_row()
        k_list=[]

        while len(row) > 0:
            # print(len(row))
            print(row[0][1], row[0][2], row[0][4], row[0][3], row[0][10])
            k = (row[0][1].decode("utf-8"), row[0][2].decode("utf-8"), row[0][4].decode("utf-8"), row[0][3], row[0][10])
            k_list.append(k)

            row = result.fetch_row()

    except _mysql.Error:
        print("Problem z polaczeniem do DB MySQL")

    finally:
        print(k_list)
        if conn:
            conn.close()
        return k_list



# pre-windows

def p1():
    root = Tk()
    root.title("Nadzorca 1.1")
    # root.geometry("500x500")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    screen_width1 = screen_width/2 -500
    screen_height1 = screen_height/2 -115
    geo = "1000x230+"+str(int(screen_width1))+"+"+ str(int(screen_height1))
    # print(geo)
    # Ukryj pasek przeciągania i przycisk zamykania okna głównego
    root.overrideredirect(True)
    # Ustaw okno główne zawsze na wierzchu
    # root.wm_attributes("- topmost", True)
    # Wyłącz cień okna
    # root.wm_attributes("- transparent", True)
    # Ustaw kolor tła okna głównego na kolor przezroczysty
    # root.config(bg='systemTransparent')
    root.geometry(geo)

    app = Frame(root)
    app.grid()
    photo1 = PhotoImage(file="ikony\\konie.png")
    photo2 = PhotoImage(file="ikony\\bydlo.png")

    MyButton1 = Button(text="BUTTON1", width=10, command = lambda: button_konie(root, screen_width, screen_height))
    MyButton1.config(image=photo1, width="500", height="230")
    MyButton1.grid(row=0, column=1)

    MyButton2 = Button(text="BUTTON2", width=10,  command=lambda: button_bydlo(root, screen_width, screen_height))
    MyButton2.config(image=photo2, width="500", height="230")
    MyButton2.grid(row=0, column=2)
    root.mainloop()

# def close_window(root):
#     root.destroy()  # destroying the main window


def button_konie(root, screen_width, screen_height):
    root.destroy()
    k_list=pobranie_danych_db_k(host, user, passwd, db)
    okno_k = Tk()
    k_tab1 = PhotoImage(file="ikony\\k_tab1.png")
    k_tab2 = PhotoImage(file="ikony\\k_tab2.png")
    k_tab3 = PhotoImage(file="ikony\\k_tab3.png")
    k_tab4 = PhotoImage(file="ikony\\k_tab4.png")
    k_tab5 = PhotoImage(file="ikony\\k_tab5.png")
    k_tab6 = PhotoImage(file="ikony\\k_tab6.png")
    k_tab7 = PhotoImage(file="ikony\\k_tab7.png")
    okno_k.title("Nadzorca")
    icon = PhotoImage(file="ikony\\ikona.png")
    okno_k.tk.call('wm', 'iconphoto', root._w, icon)
    # wyposrokowanie okna
    # print(screen_width)
    # print(screen_height)
    screen_width1 = screen_width / 2 - 400
    screen_height1 = screen_height / 2 - 300
    geo = "800x600+" + str(int(screen_width1)) + "+" + str(int(screen_height1))
    okno_k.geometry(geo)
    zakladki = ttk.Notebook(okno_k)
    tab1 = ttk.Frame(zakladki)
    tab2 = ttk.Frame(zakladki)
    tab3 = ttk.Frame(zakladki)
    tab4 = ttk.Frame(zakladki)
    tab5 = ttk.Frame(zakladki)
    tab6 = ttk.Frame(zakladki)
    tab7 = ttk.Frame(zakladki)


    zakladki.add(tab1, text='Stado', image = k_tab1, compound = "top")
    zakladki.add(tab2, text='Kalendarz rui i zaźrebień', image = k_tab2, compound = "top")
    zakladki.add(tab3, text='Baza potomstwa', image = k_tab3, compound = "top")
    zakladki.add(tab4, text='Baza zabiegów', image = k_tab4, compound = "top")
    zakladki.add(tab5, text='Geotracking', image = k_tab5, compound = "top")
    zakladki.add(tab6, text='Powiadomienia', image=k_tab6, compound="top")
    zakladki.add(tab7, text='Linki', image=k_tab7, compound="top")
    # k_list = [
    #     ('John', 'Smith', 'PL1234567887866768678868', '19-12-1992', '1'),
    #     ('Larry', 'Black', 'PL1234567887866768678868', '19-12-1992', '1,2'),
    #     ('Walter', 'White', 'PL1234567887866768678868', '19-12-1992', '5,4'),
    #     ('Fred', 'Becker','PL1234567887866768678868', '19-12-1992', '10'),
    #     ('John', 'Smith', 'PL1234567887866768678868', '19-12-1992', '20'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    #     # ('John', 'Smith', 'PL1234567887866768678868'),
    #     # ('Larry', 'Black', 'PL1234567887866768678868'),
    #     # ('Walter', 'White', 'PL1234567887866768678868'),
    #     # ('Fred', 'Becker', 'PL1234567887866768678868'),
    # ]
    # print(k_list)
    tree = ttk.Treeview(tab1, columns=('col1', 'col2', 'col3', 'col4', 'col5'), show="headings", height=22)


    tree.column('col1', width=150, anchor='center')
    tree.column('col2', width=100, anchor='center')
    tree.column('col3', width=200, anchor='center')
    tree.column('col4', width=100, anchor='center')
    tree.column('col5', width=100, anchor='center')
    tree.heading('col1', text='Imie konia')
    tree.heading('col2', text='Rasa')
    tree.heading('col3', text='Numer chipa')
    tree.heading('col4', text='Data urodzenia')
    tree.heading('col5', text='Wiek')
    vab = ttk.Scrollbar(tab1, orient="vertical", command=tree.yview)
    vab.place(x=650, y=0, height=480)
    # vab.pack(anchor='c')
    tree.configure(yscrollcommand=vab.set)

    def onDBClick(event):
        item = tree.selection()[0]
        print("you clicked on ", tree.item(item, "values"))

    for item in k_list:
        tree.insert('', 'end', values=item)
    tree.bind("<Double-1>", onDBClick)

    tree.pack(anchor='nw')
    Button_1 = Button(tab1, text='Dodaj', command=Dodaj_button_k)
    Button_1.place(x=680, y=10, height=40,width=90)
    Button_2 = Button(tab1, text='Usuń', command=Usun_button_k)
    Button_2.place(x=680, y=80, height=40,width=90)
    Button_2 = Button(tab1, text='Edytuj', command=Edytuj_button_k)
    Button_2.place(x=680, y=150, height=40,width=90)
    # Button_1.pack(anchor='ne')

    tresc2 = Label(tab2, text= 'opis 2', padx=65, pady=40)
    tresc2.grid(column=0, row=0)
    zakladki.pack(expand=1, fill='both')
    # db_pobieranie_danych_k(host, user, passwd, db)
    okno_k.mainloop()

def Dodaj_button_k():

    print("dodaje do db dane")
    messagebox.showinfo('Dodaj', 'Tu bedzie GUI dodania konia')

def Usun_button_k():

    print("usuwam do db dane")
    messagebox.showinfo('Usuń', 'Tu bedzie GUI usunięcia konia')

def Edytuj_button_k():

    print("edytuj do db dane")
    messagebox.showinfo('Edytuj', 'Tu bedzie GUI edycji konia')


def button_bydlo(root, screen_width, screen_height):

    root.destroy()
    okno_k = Tk()
    okno_k.title("Nadzorca 1.1")
    # wyposrokowanie okna
    # print(screen_width)
    # print(screen_height)
    screen_width1 = screen_width / 2 - 400
    screen_height1 = screen_height / 2 - 300
    geo = "800x600+" + str(int(screen_width1)) + "+" + str(int(screen_height1))
    okno_k.geometry(geo)
    zakladki = ttk.Notebook(okno_k)
    tab1 = ttk.Frame(zakladki)
    tab2 = ttk.Frame(zakladki)
    tab3 = ttk.Frame(zakladki)
    tab4 = ttk.Frame(zakladki)
    tab5 = ttk.Frame(zakladki)
    tab6 = ttk.Frame(zakladki)
    zakladki.add(tab1, text='Stado')
    zakladki.add(tab2, text='Krowy')
    zakladki.add(tab3, text='Młodzież')
    zakladki.add(tab4, text='Baza rozpłodowa')
    zakladki.add(tab5, text='Geotracking')
    zakladki.add(tab6, text='Powiadomienia')

    #treść1 = Label(tab1, text= 'opis 1') # może być taki prosty opis
    tresc1 = Label(tab1, text= 'opis 1', padx=25, pady=50)
    tresc1.grid(column=0, row=0)
    tresc2 = Label(tab2, text= 'opis 2', padx=65, pady=40)
    tresc2.grid(column=0, row=0)
    zakladki.pack(expand=1, fill='both')
    okno_k.mainloop()
p1()

# def mysql_try_conn(host,user,passwd,db):
#
#     try:
#         conn = _mysql.connect(host, user, passwd, db)
#
#         conn.query("SELECT * FROM Konie")
#         result = conn.use_result()
#         row = result.fetch_row()
#
#         while len(row) > 0:
#             print("Imię: %s \t Nazwisko: %s" % (row[0][1], row[0][2]))
#             row = result.fetch_row()
#
#
#
#     finally:
#         if conn:
#             conn.close()
#
#
# mysql_try_conn(host, user, passwd,
#                db)



