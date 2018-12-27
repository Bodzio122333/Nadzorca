import os
import sys
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import _mysql
import sys
# from tkinter.ttk import *
from tkinter.ttk import Combobox

host="192.168.1.190"
user="bodzio"
passwd="bodzio123"
db="Gospodarstwo"


def pobranie_danych_db_k(host,user,passwd,db):
    try:
        conn = _mysql.connect(host, user, passwd, db)

        conn.query("SELECT * FROM Konie WHERE Archiwum = 0")
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
    root.attributes('-topmost', True)
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
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
        # ('John', 'Smith', 'PL1234567887866768678868'),
        # ('Larry', 'Black', 'PL1234567887866768678868'),
        # ('Walter', 'White', 'PL1234567887866768678868'),
        # ('Fred', 'Becker', 'PL1234567887866768678868'),
    # ]
    print(k_list)
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
    Button_1 = Button(tab1, text='Dodaj', command=lambda : Dodaj_button_k (okno_k, screen_width, screen_height))
    Button_1.place(x=680, y=10, height=40,width=90)
    Button_2 = Button(tab1, text='Usuń', command=Usun_button_k)
    Button_2.place(x=680, y=80, height=40,width=90)
    Button_3 = Button(tab1, text='Edytuj', command=Edytuj_button_k)
    Button_3.place(x=680, y=150, height=40,width=90)


    tresc2 = Label(tab2, text= 'opis 2', padx=65, pady=40)
    tresc2.grid(column=0, row=0)
    zakladki.pack(expand=1, fill='both')
    okno_k.mainloop()







def Dodaj_button_k(okno_k, screen_width, screen_height ):

    print("dodaje do db dane")
    # messagebox.showinfo('Dodaj', 'Tu bedzie GUI dodania konia')
    def SQL_dodaj_konia():
        print('Dodaje konia!!!')
        imie_k = E1.get()
        dp_k = E2.get()
        rasa_k = E3.get()
        du_k = E4.get()
        nch_k = E5.get()
        o_k = E6.get()
        m_k = E7.get()
        pl_k = S1.get()
        ip_k = E9.get()
        nt_k = E10.get()
        # oo_k = E11.get()
        query_dodaj ="INSERT INTO `Konie`(`id`, `Imie`, `Rasa`, `Data_urodzenia`, `Numer_chipa`, `Ojciec`, `Matka`, `Plec`, `Ilosc_potomstwa`,`Numer_trackera`, `Wiek`, `Ostatnie_odrobaczanie`, `Ostatni_mesz`, `Data_przybycia`, `Archiwum`)"
        query_dodaj = query_dodaj + "VALUES(NULL, '"+imie_k+"', '"+rasa_k+"', '"+du_k+"', '"+nch_k+"', '"+o_k+"', '"+m_k+"', '"+pl_k+"', '"+ip_k+"', '"+nt_k+"''', '', NULL, NULL,'"+dp_k+"', '0')"
        print(query_dodaj)

        try:
            conn = _mysql.connect(host, user, passwd, db)
            conn.query(query_dodaj)
            messagebox.showinfo('Informacja', 'Poprawnie dodano konia')
        except:
            print("problem z DB SQL")
            messagebox.showinfo('Informacja', 'Blad dodania do bazy SQL')

        finally:
            if conn:
                conn.close()
            okno_dodaj_k.destroy()
            button_konie(okno_k, screen_width, screen_height)
            # okno_k.destroy()




            # python = sys.executable
            # os.execl(python, python, *sys.argv)








    # INSERT
    # INTO
    # `Konie`(`id`, `Imie`, `Rasa`, `Data_urodzenia`, `Numer_chipa`, `Ojciec`, `Matka`, `Plec`, `Ilosc_potomstwa`,
    #         `Numer_trackera`, `Wiek`, `Ostatnie_odrobaczanie`, `Ostatni_mesz`, `Data_przybycia`, `Archiwum`)
    # VALUES(NULL, 'pucek', 'zajebista', '2018-12-03', '12345', 'dupek', 'algida', 'Klacz', '0', '123456', '', NULL, NULL,
    #        '2018-12-04', '0');


    okno_dodaj_k = Tk()
    okno_dodaj_k.iconbitmap("ikony\\ikona.ico")
    screen_width = okno_dodaj_k.winfo_screenwidth()
    screen_height = okno_dodaj_k.winfo_screenheight()
    screen_width1 = screen_width/2 -125
    screen_height1 = screen_height/2 -125
    geo = "300x310+"+str(int(screen_width1))+"+"+ str(int(screen_height1))
    okno_dodaj_k.geometry(geo)
    # okno_dodaj_k.attributes('-topmost', True)
    napis_NR = LabelFrame(okno_dodaj_k, text="DODAJ KONIA")
    napis_NR.pack(fill="both", expand="yes")
    okno_dodaj_k.title("Nadzorca")
    L1= Label(napis_NR, text="Imie konia ")
    L1.grid(row=0, column=0,sticky=W+E+N+S)
    E1= Entry(napis_NR)
    E1.grid(row=0, column=1,sticky=W+E+N+S)
    L2= Label(napis_NR, text="Data przybycia ")
    L2.grid(row=1, column=0, sticky=W+E+N+S)
    E2= Entry(napis_NR)
    E2.insert(END,"RRRR-mm-dd")
    E2.grid(row=1, column=1,sticky=W+E+N+S)
    L3= Label(napis_NR, text="Rasa ")
    L3.grid(row=2, column=0, sticky=W+E+N+S)
    E3= Entry(napis_NR)
    E3.grid(row=2, column=1,sticky=W+E+N+S)
    L4= Label(napis_NR, text="Data urodzenia ")
    L4.grid(row=3, column=0, sticky=W+E+N+S)
    E4= Entry(napis_NR)
    E4.insert(END,"RRRR-mm-dd")
    E4.grid(row=3, column=1,sticky=W+E+N+S)
    L5= Label(napis_NR, text="Numer chipa ")
    L5.grid(row=4, column=0, sticky=W+E+N+S)
    E5= Entry(napis_NR)
    E5.grid(row=4, column=1,sticky=W+E+N+S)
    L6= Label(napis_NR, text="Ojciec ")
    L6.grid(row=5, column=0, sticky=W+E+N+S)
    E6= Entry(napis_NR)
    E6.grid(row=5, column=1,sticky=W+E+N+S)
    L7= Label(napis_NR, text="Matka ")
    L7.grid(row=6, column=0, sticky=W+E+N+S)
    E7= Entry(napis_NR)
    E7.grid(row=6, column=1,sticky=W+E+N+S)
    L8 = Label(napis_NR, text="Plec ")
    L8.grid(row=7, column=0, sticky=W + E + N + S)
    S1= Combobox(napis_NR)
    S1['values'] = ("Klacz", "Ogier", "Walach")
    S1.current(0)  # ustawienie co ma być wartością domyślną
    S1.grid(row=7, column=1, sticky=W + E + N + S)
    L9= Label(napis_NR, text="Ilosc potomstwa ")
    L9.grid(row=8, column=0, sticky=W+E+N+S)
    E9= Entry(napis_NR)
    E9.insert(END, "0")
    E9.grid(row=8, column=1,sticky=W+E+N+S)
    L10= Label(napis_NR, text="Numer Trackera ")
    L10.grid(row=9, column=0, sticky=W+E+N+S)
    E10= Entry(napis_NR)
    E10.grid(row=9, column=1,sticky=W+E+N+S)
    # L11= Label(napis_NR, text="Ostatnie odrobaczanie ")
    # L11.grid(row=10, column=0, sticky=W+E+N+S)
    # E11= Entry(napis_NR)
    # E11.grid(row=10, column=1,sticky=W+E+N+S)
    # E11.insert(END, "RRRR-mm-dd")
    L11= Label(napis_NR, text=" ")
    L11.grid(row=11, column=0, sticky=W+E+N+S)
    Button_Dodaj = Button(napis_NR, text='Dodaj', command=SQL_dodaj_konia)
    Button_Dodaj.grid(row=12, column=1,sticky=W+E+N+S)
    okno_dodaj_k.mainloop()


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



