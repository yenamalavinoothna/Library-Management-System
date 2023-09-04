from tkinter import *
import tkinter as tk
import csv,operator
from tkinter import messagebox, ttk
from datetime import datetime

def LibraryManagementsystem():
    def show_frame(frame_faces):
        frame_faces.tkraise()

    win = Tk()
    win.geometry("1550x800+0+0")
    win.rowconfigure(0, weight=1)
    win.columnconfigure(0, weight=1)
    frame1 = Frame(win)
    frame2 = Frame(win)
    frame3 = Frame(win)
    frame4 = Frame(win)
    frame5 = Frame(win)
    frame6 = Frame(win)
    frame7 = Frame(win)
    frame8 = Frame(win)
    frame9 = Frame(win)
    frame10 = Frame(win)
    frame11 = Frame(win)
    frame12 = Frame(win)
    frame13 = Frame(win)
    frame14 = Frame(win)
    for frame in (frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12, frame13,
    frame14):
        frame.grid(row=0, column=0, sticky="nsew")

    student = tk.StringVar()
    book1 = tk.StringVar()

    # for Total booklist
    def booklist():
        win=Tk()
        win.title("Total Booklist")

        TableMargin = Frame(win, width=400)

        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("book", "author", "ROW", "column", "copies"), height=22,
                            selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('book', text="Book", anchor=W)
        tree.heading('author', text="Author", anchor=W)
        tree.heading('ROW', text="Row", anchor=W)
        tree.heading('column', text="Column", anchor=W)
        tree.heading('copies', text="Copies", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=250)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)
        tree.column('#4', stretch=NO, minwidth=0, width=200)
        tree.pack()
        with open('D:/python programs/bookinfo.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                book = row['book']
                author = row['author']
                ROW = row['ROW']
                column = row['column']
                copies = row['copies']
                tree.insert("", 0, values=(book, author, ROW, column, copies))
        win.mainloop()
    #For Issuebooks
    def fun5():
        def func3():
            window = Tk()
            window.title('Issue Books')
            window.geometry('500x500')

            label1 = tk.Label(window, text='Book')
            label1.grid(row=0, column=0)
            label2 = tk.Label(window, text='Student Username')
            label2.grid(row=1, column=0)
            #label3 = tk.Label(window, text='Issued date')
            #label3.grid(row=2, column=0)

            textbox1 = tk.Entry(window)
            textbox1.grid(row=0, column=1)
            textbox2 = tk.Entry(window)
            textbox2.grid(row=1, column=1)
            #textbox3 = tk.Entry(window)
            #textbox3.grid(row=2, column=1)

            def issue():
                issue_book = textbox1.get()
                issue_user = textbox2.get()
                issue_date = datetime.now()
                

                if (issue_book == '' or issue_user == ''):
                    messagebox.showerror('error', 'You forgot to enter something')

                else:
                    with open("D:/python programs/issue.csv", 'a') as file:
                        writer = csv.writer(file,delimiter=',')
                        writer.writerow([issue_book,issue_user,issue_date])
                        file.close()
            def reduce():
                r = csv.reader(open("D:/python programs/bookinfo.csv"))
                lines = list(r)
                issue_book = textbox1.get()

                for i in range(1, len(lines)):
                    if (issue_book == lines[i][0]):
                        lines[i][4] = int(lines[i][4]) - 1
                    # print(lines)
                with open("D:/python programs/bookinfo.csv", 'w', newline='') as w:
                    writer = csv.writer(w, delimiter=',')
                    writer.writerows(lines)
                    w.close()

            def combine():
                issue()
                reduce()



                #reduce()

            button1 = tk.Button(window, command=combine, text='Save',bg="gold",fg="black")
            button1.place(x=50, y=200)


            def delete():
                issue_book = textbox1.get()
                issue_user = textbox2.get()
                #issue_date = textbox3.get()

                textbox1.delete(0, END)
                textbox2.delete(0, END)
                #textbox3.delete(0, END)

            button2 = tk.Button(window, command=delete, text='Clear',bg="lightcyan",fg="black")
            button2.place(x=150, y=200)
            window.mainloop()

        func3()
    #for Searchbook
    def func():
        window = Tk()
        window.title('Search Books')
        window.geometry('500x500')
        window.config(highlightbackground='black')
        book = tk.StringVar()

        Label(window, text='Book').place(x=50, y=60)
        Label(window, text='Author').place(x=50, y=100)
        Label(window, text='Row').place(x=50, y=130)
        Label(window, text='Column').place(x=50, y=160)
        Label(window, text='Copies').place(x=50, y=190)

        book = Entry(window)
        book.place(x=250, y=60)
        author = Entry(window)
        author.place(x=250, y=100)
        ro = Entry(window)
        ro.place(x=250, y=130)
        column = Entry(window)
        column.place(x=250, y=160)
        copies = Entry(window)
        copies.place(x=250, y=190)

        author.configure(state=tk.DISABLED)
        ro.configure(state=tk.DISABLED)
        column.configure(state=tk.DISABLED)
        copies.configure(state=tk.DISABLED)

        def search():
            search_book = book.get()
            author.configure(state=tk.NORMAL)
            ro.configure(state=tk.NORMAL)
            column.configure(state=tk.NORMAL)
            copies.configure(state=tk.NORMAL)

            author.delete(0, 'end')
            ro.delete(0, 'end')
            column.delete(0, 'end')  # to clear previous displayed data
            copies.delete(0, 'end')

            file = csv.reader(open('D:/python programs/bookinfo.csv', 'r'))

            for row in file:
                if row[0] == str(search_book):
                    author.insert(0, row[1])
                    ro.insert(0, row[2])
                    column.insert(0, row[3])
                    copies.insert(0, row[4])

                    author.configure(state=tk.DISABLED)
                    ro.configure(state=tk.DISABLED)
                    column.configure(state=tk.DISABLED)
                    copies.configure(state=tk.DISABLED)

        Button(window, text='search', command=search,bg="gold", fg="black").place(x=100, y=300)
        Button(window, text='Issue book', command=fun5,bg="lightcyan", fg="black").place(x=350, y=300)
    #for Add books
    def fun6():
        def func3():
            window = Tk()
            window.title('Add Books')
            window.geometry('500x500')

            label1 = tk.Label(window, text='Book')
            label1.grid(row=0, column=0)
            label2 = tk.Label(window, text='Author')
            label2.grid(row=1, column=0)
            label3 = tk.Label(window, text='Row')
            label3.grid(row=2, column=0)
            label4 = tk.Label(window, text='Column')
            label4.grid(row=3, column=0)
            label5 = tk.Label(window, text='Copies')
            label5.grid(row=4, column=0)

            textbox1 = tk.Entry(window)
            textbox1.grid(row=0, column=1)
            textbox2 = tk.Entry(window)
            textbox2.grid(row=1, column=1)
            textbox3 = tk.Entry(window)
            textbox3.grid(row=2, column=1)
            textbox4 = tk.Entry(window)
            textbox4.grid(row=3, column=1)
            textbox5 = tk.Entry(window)
            textbox5.grid(row=4, column=1)

            def add():
                add_book = textbox1.get()
                add_author = textbox2.get()
                add_row = textbox3.get()
                add_column = textbox4.get()
                add_copies = textbox5.get()
                if (add_book == '' or add_author == '' or add_copies == ''):
                    messagebox.showerror('error', 'You forgot to enter something')

                else:
                    #messagebox.askyesno('conformation', 'Do you want save the details?')

                    with open('D:/python programs/bookinfo.csv','a',newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([add_book, add_author, add_row, add_column, add_copies])
                    file.close()

            def clear():
                add_book = textbox1.get()
                add_author = textbox2.get()
                add_row = textbox3.get()
                add_column = textbox4.get()
                add_copies = textbox5.get()

                textbox1.delete(0, END)
                textbox2.delete(0, END)
                textbox3.delete(0, END)
                textbox4.delete(0, END)
                textbox5.delete(0, END)

            button1 = tk.Button(window, command=add, text='Save',bg="gold", fg="black")
            button2 = tk.Button(window, command=clear, text='Clear All',bg="lightcyan", fg="black")
            button1.place(x=50, y=200)
            button2.place(x=150, y=200)
            window.mainloop()

        func3()

    def fun7():
        def funcs():
            window = Tk()
            window.title('STUDENT REGISTRATION')
            window.geometry('500x500')

            label1 = tk.Label(window, text='Admission Number')
            label1.grid(row=0, column=0)
            label2 = tk.Label(window, text='Student Name')
            label2.grid(row=1, column=0)
            label3= tk.Label(window, text='Mobile Number')
            label3.grid(row=2, column=0)
            label4 = tk.Label(window, text='Email ID')
            label4.grid(row=3, column=0)

            textbox1 = tk.Entry(window)
            textbox1.grid(row=0, column=1)
            textbox2 = tk.Entry(window)
            textbox2.grid(row=1, column=1)
            textbox3 = tk.Entry(window)
            textbox3.grid(row=2, column=1)
            textbox4 = tk.Entry(window)
            textbox4.grid(row=3, column=1)

            def add_student():
                add_admission = textbox1.get()
                add_name = textbox2.get()
                add_mobile = textbox3.get()
                add_mail = textbox4.get()

                if (add_admission == '' or add_name == '' or add_mobile == '' or add_mail == ''):
                    messagebox.showerror('error', 'You forgot to enter something')

                else:
                    messagebox.askyesno('conformation', 'Do you want save the details?')

                    with open('D:/python programs/stddetails.csv', 'a', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([add_admission, add_name, add_mobile, add_mail])
                    file.close()

            def sort():
                r1 = csv.reader(open("D:/python programs/stddetails.csv"))
                next(r1)
                lines1 = list(r1)

                lines1 = sorted(lines1, key=operator.itemgetter(0))
                lines1 = [['admissionnumber', 'name','mobile','mail']] + lines1

                with open("D:/python programs/stddetails.csv", 'w', newline='') as w:
                    writer = csv.writer(w, delimiter=',')
                    writer.writerows(lines1)
                    w.close()

            def combine2():
                add_student()
                sort()


            def clear():
                add_admission = textbox1.get()
                add_name = textbox2.get()
                add_mobile = textbox3.get()
                add_mail = textbox4.get()

                textbox1.delete(0, END)
                textbox2.delete(0, END)
                textbox3.delete(0, END)
                textbox4.delete(0, END)

            button1 = tk.Button(window, command=combine2, text='Save', bg="gold", fg="black")
            button2 = tk.Button(window, command=clear, text='Clear All', bg="lightcyan", fg="black")
            button1.place(x=50, y=200)
            button2.place(x=150, y=200)
            window.mainloop()

        funcs()

    #for student login
    def fun():
        def ok():
            username = e1.get()
            password = e2.get()

            csv_file = csv.reader(open("D:/python programs/stdlogin.csv", "r"))
            for line in csv_file:
                if username == line[0] and password == line[1]:
                    button3 = Button(win, text="Go to Next Pg", font=("Copperplate Gothic Bold", 17, "bold"), width=15,bg="lawngreen",fg="black", command=lambda: show_frame(frame6)).place(x=200, y=450)
                    #messagebox.showinfo("admin", "u have successfully logined")

        win = Tk()
        win.title("Student Login")
        win.config(bg="powder blue")
        win.geometry("500x500")
        global e1
        global e2
        Label(win, text="Username").place(x=10, y=10)
        Label(win, text="Password").place(x=10, y=40)
        e1 = Entry(win)
        e1.place(x=140, y=10)
        e2 = Entry(win)
        e2.place(x=140, y=40)
        e2.config(show="*")

        button1 = Button(win, text="Login", command=ok, bg="gold", fg="black")
        button1.place(x=100, y=100)
        button2 = Button(win, text="Click to exit", bg="red", fg="black", command=win.destroy)
        button2.place(x=200, y=100)
        win.mainloop()
    #for Admin Login
    def fun1():
        def ok():
            username = e1.get()
            password = e2.get()

            csv_file = csv.reader(
                open("D:/python programs/adminlogin.csv", "r"))
            for line in csv_file:
                if username == line[0] and password == line[1]:
                    button3 = Button(win, text="Go to Next Pg", font=("Copperplate Gothic Bold", 17, "bold"), width=15,
                                     bg="lawngreen",
                                     fg="black", command=lambda: show_frame(frame5)).place(x=200, y=450)
                    #messagebox.showinfo("admin", "u have successfully logined")

        win = Tk()
        win.title("Admin Login")
        win.config(bg="powder blue")
        win.geometry("500x500")
        global e1
        global e2
        Label(win, text="Username").place(x=10, y=10)
        Label(win, text="Password").place(x=10, y=40)
        e1 = Entry(win)
        e1.place(x=140, y=10)
        e2 = Entry(win)
        e2.place(x=140, y=40)
        e2.config(show="*")

        button1 = Button(win, text="Login", command=ok, bg="gold", fg="black")
        button1.place(x=100, y=100)
        button2 = Button(win, text="Click to exit", bg="red", fg="black", command=win.destroy)
        button2.place(x=200, y=100)
        win.mainloop()
    #for faculty Login
    def fun3():
        def ok():
            username = e1.get()
            password = e2.get()

            csv_file = csv.reader(open("D:/python programs/stafflogin.csv", "r"))
            for line in csv_file:
                if username == line[0] and password == line[1]:
                    button3 = Button(win, text="Go to Next Pg", font=("Copperplate Gothic Bold", 17, "bold"), width=15,
                                     bg="lawngreen",
                                     fg="black", command=lambda: show_frame(frame7)).place(x=200, y=450)
                    #messagebox.showinfo("admin", "u have successfully logined")

        win = Tk()
        win.title("Faculty Login")
        win.config(bg="powder blue")
        win.geometry("500x500")
        global e1
        global e2
        Label(win, text="Username").place(x=10, y=10)
        Label(win, text="Password").place(x=10, y=40)
        e1 = Entry(win)
        e1.place(x=140, y=10)
        e2 = Entry(win)
        e2.place(x=140, y=40)
        e2.config(show="*")

        button1 = Button(win, text="Login", command=ok, bg="gold", fg="black")
        button1.place(x=100, y=100)
        button2 = Button(win, text="Click to exit", bg="red", fg="black", command=win.destroy)
        button2.place(x=200, y=100)
        win.mainloop()
    #for delete books
    def delete_book():
        def deleting():
            Bookname = bookname.get()

            lines = list()
            # bookname=input("please enter the book name to be deleted")
            with open("D:/python programs/bookinfo.csv", 'r') as readfile:
                reader = csv.reader(readfile)
                for row in reader:
                    lines.append(row)
                    for field in row:
                        if field == Bookname:
                            lines.remove(row)
            with open("D:/python programs/bookinfo.csv", 'w',newline="") as writefile:
                writer = csv.writer(writefile)
                writer.writerows(lines)

        root = Tk()
        root.title("Delete Books")
        root.geometry("300x200")
        global bookname
        Label(root, text="book name").place(x=10, y=10)

        bookname = Entry(root)
        bookname.place(x=140, y=10)
        button = Button(root, text="Click to delete", command=deleting, bg="gold", fg="black")
        button.place(x=50, y=50)
        button1 = Button(root, text="Exit", command=root.destroy, bg="red", fg="black")
        button1.place(x=200, y=50)
        root.mainloop()
    #for return books
    def return_book():
        def deleting():
            Bookname = bookname.get()
            lines = list()
            with open("D:/python programs/issue.csv", 'r') as readfile:
                reader = csv.reader(readfile)
                for row in reader:
                    lines.append(row)
                    for field in row:
                        if field == Bookname:
                            lines.remove(row)
            with open("D:/python programs/issue.csv", 'w',newline='') as writefile:
                writer = csv.writer(writefile,delimiter=',')
                writer.writerows(lines)

        def increase():
            r = csv.reader(open("D:/python programs/bookinfo.csv"))
            lines = list(r)
            Bookname = bookname.get()
            for i in range(1, len(lines)):
                if ( Bookname== lines[i][0]):
                    lines[i][4] = int(lines[i][4]) + 1
                # print(lines)
            with open("D:/python programs/bookinfo.csv", 'w', newline='') as w:
                writer = csv.writer(w, delimiter=',')
                writer.writerows(lines)
                w.close()

        def combine1():
            deleting()
            increase()

        root = Tk()
        root.title("Return Books")
        root.geometry("300x200")
        global bookname
        Label(root, text="book name").place(x=10, y=10)

        bookname = Entry(root)
        bookname.place(x=140, y=10)
        button = Button(root, text="click to return", command=combine1, bg="gold", fg="black")
        button.place(x=50, y=50)
        button1 = Button(root, text="Exit", command=root.destroy, bg="red", fg="black")
        button1.place(x=200, y=50)
        root.mainloop()
    #for issue books
    def issued():
        win = Tk()
        win.title("Issued Booklist")
        win.geometry("500x500")
        TableMargin = Frame(win, width=400)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("book"), height=22, selectmode="extended",
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('book', text="Book", anchor=W)
        tree.column('#0', stretch=NO, minwidth=100, width=0)
        tree.pack()
        with open('D:/python programs/issue.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                book = row['book']
                tree.insert("", 0, values=(book))
        win.mainloop()
    #for Student anf faculty Total history
    def S_history():
        win = Tk()
        win.title("History")
        win.geometry("500x500")
        TableMargin = Frame(win, width=1000)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("book", "username", "date"), height=22, selectmode="extended",
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('book', text="Book", anchor=W)
        tree.heading('username', text="Username", anchor=W)
        tree.heading('date', text="Date of Issue", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.pack()
        with open('D:/python programs/issue.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                book = row['book']
                username = row['username']
                date = row['date']
                tree.insert("", 0, values=(book, username, date))
        win.mainloop()
    #for Faculty and Student Myhistory
    def Myhistory():
        win = tk.Tk()
        win.title("My History")
        win.geometry('700x500')
        label = Label(win, text='Username')
        label.place(x=150, y=100)
        textbox = Entry(win)
        textbox.place(x=250, y=100)
        #file = csv.reader(open('D:/python programs/history.csv', 'r'))
        #mylist = []
        #for row in file:
            #mylist.append(row)

        def history():
            new=[]
            username = textbox.get()
            r=csv.reader(open("D:\python programs\issue.csv"))
            lines=list(r)
        
            for i in range(0,len(lines)-1):
                if(username==lines[i][1]):
                    t=new.append(lines[i])
                else:
                    i=i+1
    #print(tuple(new))

    
            win1=Tk()
            win1.title("History")
            win1.geometry('700x1000')
            tv=ttk.Treeview(win1)
            tv['columns']=('book','username','date')
            tv.column('#0',width=0,stretch=NO)
            tv.column('book',anchor=CENTER,width=80)
            tv.column('username',anchor=CENTER,width=80)
            tv.column('date',anchor=CENTER,width=200)

            tv.heading('#0',text='',anchor=CENTER)
            tv.heading('book',text='Book',anchor=CENTER)
            tv.heading('username',text='Username',anchor=CENTER)
            tv.heading('date',text='Date of Issue',anchor=CENTER)

            for i in new:
                tv.insert(parent='',index=0,values=i)
            #tv.pack()
        #win.mainloop()

            tv.pack(side=TOP)
            scrollbar = ttk.Scrollbar(win1, orient=tk.VERTICAL, command=tv.yview)
            tv.configure(yscroll=scrollbar.set)
            scrollbar.pack(side=RIGHT, fill=Y)

        button = Button(win, bg="gold", fg="black", text="My History", command=history)
        button.place(x=200, y=200)

        win.mainloop()

    # Frame1 Home pg
    frame1_title = Label(frame1, text="JNTUA\nLIBRARY MANAGEMENT SYSTEM", bg="pink", fg="black", bd=20, relief=RIDGE,
                         font=("Footlight MT Light", 45, "bold"), padx=230, pady=8)
    frame1_title.pack(side=TOP, fill="x")
    frame1_bt1 = Button(frame1, text="ADMIN\nLOGIN", font=("Copperplate Gothic Bold", 20, "bold"), width=20,
                        bg="paleturquoise", fg="black", command=fun1)
    frame1_bt1.place(x=500, y=250)
    frame1_bt2 = Button(frame1, text="STUDENT\nLOGIN", font=("Copperplate Gothic Bold", 20, "bold"), width=20,
                        bg="paleturquoise", fg="black", command=fun)
    frame1_bt2.place(x=500, y=350)
    frame1_bt3 = Button(frame1, text="FACULTY\nLOGIN", font=("Copperplate Gothic Bold", 20, "bold"), width=20,
                        bg="paleturquoise", fg="black", command=fun3)
    frame1_bt3.place(x=500, y=450)
    frame1_bt4 = Button(frame1, text="Exit", bd=10, bg="purple", fg="white", font=("Footlight MT Light", 20, "bold"),
                        command=win.destroy)
    frame1_bt4.place(x=1230, y=590, width=100, height=75)
    frame1_bt5 = Button(frame1, text="Go Back", bd=10, bg="purple", fg="white", font=("Footlight MT Light", 20, "bold"),
                        command=lambda: show_frame(frame1))
    frame1_bt5.place(x=20, y=590, width=120, height=75)
    show_frame(frame1)

    e1 = Entry(frame3)
    e1.place(x=140, y=10)
    Password = StringVar()
    e2 = Entry(frame3)
    e2.place(x=600, y=300)


    # frame5 Admin dashboard

    frame5_title = Label(frame5, text="ADMIN DASHBOARD", bg="lightblue", fg="white", bd=20, relief=RIDGE,
                         font=("Footlight MT Light", 40, "bold"), padx=2, pady=6).pack()
    frame5_bt6 = Button(frame5, text="SHOW BOOKLIST", font=("Copperplate Gothic Bold", 20, "bold"), width=15, bg="pink",
                        fg="black", command=booklist).place(x=200, y=200)
    frame5_bt1 = Button(frame5, text="ADD BOOKS", font=("Copperplate Gothic Bold", 20, "bold"), width=15, bg="pink",
                        fg="black", command=fun6).place(x=200, y=300)
    frame5_bt10 = Button(frame5, text="STUDENT REGISTRATION", font=("Copperplate Gothic Bold", 20, "bold"), width=23, bg="pink",
                        fg="black", command=fun7).place(x=200, y=400)
    frame5_bt3 = Button(frame5, text="SEARCH BOOKS", font=("Copperplate Gothic Bold", 20, "bold"), width=15, bg="pink",
                        fg="black", command=func).place(x=200, y=500)
    frame5_bt4 = Button(frame5, text="ISSUED BOOKS", font=("Copperplate Gothic Bold", 20, "bold"), width=15, bg="pink",
                        fg="black", command=issued).place(x=800, y=300)
    frame5_bt5 = Button(frame5, text="RETURN BOOKS", font=("Copperplate Gothic Bold", 20, "bold"), width=15, bg="pink",
                        fg="black", command=return_book).place(x=800, y=200)
    frame5_bt7 = Button(frame5, text="DELETE BOOKS", font=("Copperplate Gothic Bold", 20, "bold"), width=15, bg="pink",
                        fg="black", command=delete_book).place(x=800, y=400)
    frame5_bt8 = Button(frame5, text="Log Out", font=("Copperplate Gothic Bold", 20, "bold"), width=15, bg="purple",
                        fg="white", command=lambda: show_frame(frame1)).place(x=800, y=500)
    frame5_bt9 = Button(frame5, text="Go Back", bd=10, bg="purple", fg="white", font=("Footlight MT Light", 20, "bold"),
                        command=lambda: show_frame(frame1))
    frame5_bt9.place(x=20, y=590, width=120, height=75)

    # frame6 student dashboard
    frame6_title = Label(frame6, text="STUDENT DASHBOARD", bg="lightblue", fg="white", bd=20, relief=RIDGE,
                         font=("Footlight MT Light", 40, "bold"), padx=2, pady=6, ).pack()
    frame6_bt1 = Button(frame6, text="VIEW TOTAL HISTORY", font=("Copperplate Gothic Bold", 20, "bold"), width=20, bg="pink",
                        fg="black", command=S_history).place(x=200, y=250)
    frame6_bt4 = Button(frame6, text="VIEW MY HISTORY", font=("Copperplate Gothic Bold", 20, "bold"), width=15, bg="pink",
                        fg="black",command=Myhistory).place(x=700, y=250)
    frame6_bt3 = Button(frame6, text="Go Back", bd=10, bg="purple", fg="white", font=("Footlight MT Light", 20, "bold"),
                        command=lambda: show_frame(frame1))
    frame6_bt3.place(x=20, y=590, width=120, height=75)
    frame6_bt2 = Button(frame6, text="Log Out", font=("Copperplate Gothic Bold", 20, "bold"), width=15, bg="purple",
                        fg="white", command=lambda: show_frame(frame1)).place(x=500, y=350)

    # frame7 faculty dashboard
    frame7_title = Label(frame7, text="FACULTY DASHBOARD", bg="lightblue", fg="white", bd=20, relief=RIDGE,
                         font=("Footlight MT Light", 40, "bold"), padx=2, pady=6, ).pack()
    frame6_bt1 = Button(frame7, text="VIEW TOTAL HISTORY", font=("Copperplate Gothic Bold", 20, "bold"), width=20,
                        bg="pink",
                        fg="black", command=S_history).place(x=200, y=250)
    frame6_bt4 = Button(frame7, text="VIEW MY HISTORY", font=("Copperplate Gothic Bold", 20, "bold"), width=15,
                        bg="pink",fg="black",command=Myhistory).place(x=700, y=250)
    frame7_bt3 = Button(frame7, text="Go Back", bd=10, bg="purple", fg="white", font=("Footlight MT Light", 20, "bold"),
                        command=lambda: show_frame(frame1))
    frame7_bt3.place(x=20, y=590, width=120, height=75)
    frame7_bt2 = Button(frame7, text="Log Out", font=("Copperplate Gothic Bold", 20, "bold"), width=15, bg="purple",
                        fg="white", command=lambda: show_frame(frame1)).place(x=500, y=350)



    """# frame 9 Booklist
    frame9_title = Label(frame9, text="Total BookList", bg="pink", fg="black", bd=20, relief=RIDGE,
                         font=("Copperplate Gothic Bold", 25, "bold"), padx=60, pady=10).pack()
    frame9_bt1 = Button(frame9, text="Go Back", bd=10, bg="purple", fg="white", font=("Footlight MT Light", 20, "bold"),
                        command=lambda: show_frame(frame5))
    frame9_bt1.place(x=20, y=590, width=120, height=75)"""

    """# for Total booklist

    TableMargin = Frame(frame9, width=400)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("book", "author", "ROW", "column", "copies"), height=22,selectmode="extended",yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('book', text="Book", anchor=W)
    tree.heading('author', text="Author", anchor=W)
    tree.heading('ROW', text="Row", anchor=W)
    tree.heading('column', text="Column", anchor=W)
    tree.heading('copies', text="Copies", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=250)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=200)
    tree.pack()
    with open('D:/python programs/bookinfo.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            book = row['book']
            author = row['author']
            ROW = row['ROW']
            column = row['column']
            copies = row['copies']
            tree.insert("", 0, values=(book, author, ROW ,column, copies))
    win.mainloop()"""
LibraryManagementsystem(
