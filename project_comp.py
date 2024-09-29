from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1350x690+1+1')
        self.root.title('School Manger')
        self.root.configure(background='silver')
        self.root.resizable(False, False)
        title = Label(self.root, text='Sign-UP System students',
                      font=('Semi Bold', 15),
                      bg='#212F3D',
                      fg='#D0D3D4')
        title.pack(fill=X)
        # -------------------- varible -------------------------
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.phon_var = StringVar()
        self.quali_var = StringVar()
        self.address_var = StringVar()
        self.gender_var = StringVar()
        self.sea_by = StringVar()
        self.search_var = StringVar()
        self.dell_var = StringVar()
        # -------------- Great frame -------------------------------
        fr = Frame(self.root, bg='#616A6B')
        fr.place(x=1137, y=30, width=210, height=400)
        #------------------------ Great Buttom ------------------------------

        # ------------ id student ------------------------
        l_id = Label(fr, text='ID Student', bg='#212F3D', font=('Bold', 12), fg='#F7F9F9')
        l_id.pack(fill=X)
        e_id = Entry(fr, font=('Bold', 10), bd=2, justify='center',textvariable=self.id_var)
        e_id.pack()
        # -------------------- name student ------------------------
        l_name = Label(fr, text='Name Student', bg='#212F3D', font=('Bold', 12), fg='#F7F9F9')
        l_name.pack(fill=X)
        e_name = Entry(fr, font=('Bold', 10), bd=2, justify='center',textvariable=self.name_var)
        e_name.pack()
        # ------------------- e-mail ---------------------
        l_mail = Label(fr, text='E-Mail ', bg='#212F3D', font=('Bold', 12), fg='#F7F9F9')
        l_mail.pack(fill=X)
        e_mail = Entry(fr, font=('Bold', 10), bd=2, justify='center',textvariable=self.email_var)
        e_mail.pack()
        # --------------- phone --------------------------------
        l_phone = Label(fr, text='Phone Student', bg='#212F3D', font=('Bold', 12), fg='#F7F9F9')
        l_phone.pack(fill=X)
        e_phone = Entry(fr, font=('Bold', 10), bd=2, justify='center',textvariable=self.phon_var)
        e_phone.pack()
        # ---------------- qualification -----------------------------
        l_qual = Label(fr, text='Qualification', bg='#212F3D', font=('Bold', 12), fg='#F7F9F9')
        l_qual.pack(fill=X)
        e_qual = Entry(fr, font=('Bold', 10), bd=2, justify='center',textvariable=self.quali_var)
        e_qual.pack()
        # --------------- gender ---------------------------------------
        l_gender = Label(fr, text='Gender', bg='#212F3D', font=('Bold', 12), fg='#F7F9F9')
        l_gender.pack(fill=X)
        com_gender = ttk.Combobox(fr,textvariable=self.gender_var,value=('Male', 'Femal', 'Other'),state='readonly')
        com_gender.pack()
        # --------------------------------- address ------------------------
        l_address = Label(fr, text='Address Student', bg='#212F3D', font=('Bold', 12), fg='#F7F9F9')
        l_address.pack(fill=X)
        e_address = Entry(fr, font=('Bold', 10), bd=2, justify='center',textvariable=self.address_var)
        e_address.pack()
        # ------------------------------ delete student ----------------------------
        l_delete = Label(fr, text='Delete Student', bg='#7b241C', font=('Blod', 12), fg='#F7F9F9')
        l_delete.pack(fill=X)
        e_delete = Entry(fr, font=('Blod', 10), bd=2, justify='center',textvariable=self.dell_var)
        e_delete.pack()
        # ------------------------Great frame 2 -------------------------------------------
        fr2 = Frame(self.root, bg='#616A6B')
        fr2.place(x=1137, y=435, width=210, height=253)
        # -------------- control table ---------------------
        l_control = Label(fr2, text='Control Table', font=('Semi Bold', 15), bg='#212F3D', fg='#D0D3D4')
        l_control.pack(fill=X)
        # --------- buttom add ------------------
        b_add = Button(fr2, text='Add Student', font=('Bold', 12), bg='#85929E', fg='#ECF0F1',command= self.add_student)
        b_add.place(x=25, y=30, width=150, height=30)
        # ----------------- updata ---------------------------
        b_udata = Button(fr2, text='Updata', font=('Bold', 12), bg='#85929E', fg='#ECF0F1',command=self.update)
        b_udata.place(x=25, y=70, width=150, height=30)
        # ------------------------- clear ----------------------
        b_clear = Button(fr2, text='Clear Data', font=('Bold', 12), bg='#85929E', fg='#ECF0F1',command=self.clear)
        b_clear.place(x=25, y=110, width=150, height=30)
        # --------------------------- delete -----------------------------
        b_delete = Button(fr2, text='Delete Data', font=('Bold', 12), bg='#85929E', fg='#ECF0F1',command= self.delet_stud)
        b_delete.place(x=25, y=150, width=150, height=30)
        # ------------------------------- about us----------------
        b_abut = Button(fr2, text='About us', font=('Bold', 12), bg='#85929E', fg='#ECF0F1',command=self.about)
        b_abut.place(x=25, y=190, width=150, height=30)
        # -------------------------- exit -----------------------------
        b_exit = Button(fr2, text='Exit', font=('Bold', 12), bg='#85929E', fg='#ECF0F1', command=self.root.quit)
        b_exit.place(x=25, y=230, width=150, height=30)
        # ----------------------------- tools search-----------------------------------------
        # ------------------ frame search --------------------
        fr_searsh = Frame(self.root, bg='#85929E')
        fr_searsh.place(x=1, y=30, width=1134, height=40)
        # ---------------- button search -------------------------------
        s = Label(fr_searsh, text='Search Info Student ', font=('Bold', 8), bg='#212F3D', fg='#ECF0F1')
        s.place(x=1034, y=20)
        # -------------- combobox ----------------------------
        com = ttk.Combobox(fr_searsh, values=(
        'ID Student', 'Name Student', 'Address', 'Phone', 'E-Mail', 'Qulafication', 'Gender'),
                           state='readyonly',textvariable=self.sea_by)
        com.place(x=880, y=20)
        # ----------------- entry search --------------------------
        e_search = Entry(fr_searsh, font=('Bold', 10), bd=2, justify='center',textvariable=self.search_var)
        e_search.place(x=700, y=20)
        l_s = Button(fr_searsh, text='Search 🔍', font=('Bold', 8), bg='#212F3D', fg='#ECF0F1',command=self.search)
        l_s.place(x=640, y=20)
        #-------------------- Deteiles ----------------------------------
        de_fram = Frame(self.root,bg='#95a5a6')
        de_fram.place(x=1,y=72,height=600,width=1134)

        #------------- scrolbar ----------------------------
        sc_x = Scrollbar(de_fram,orient=HORIZONTAL)
        sc_y = Scrollbar(de_fram,orient=VERTICAL)

        #------------ treeviwe ----------------------
        self.student_table = ttk.Treeview(de_fram,
        columns=('ID Student','Name Student','E-Mail','Phone Student','Qualification','Gender','Address'),
        xscrollcommand=sc_x.set , yscrollcommand=sc_y.set)
        self.student_table.place(x=18,y=1,width=1130,height=587)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y.pack(side=LEFT,fill=Y)
        sc_x.config(command=self.student_table.xview)
        sc_y.config(command=self.student_table.yview)

        self.student_table['show']='headings'
        self.student_table.heading('ID Student',text='ID Student')
        self.student_table.heading('Name Student', text='Name Student')
        self.student_table.heading('E-Mail', text='E-Mail')
        self.student_table.heading('Phone Student', text='Phone Student')
        self.student_table.heading('Qualification', text='Qualification')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Address', text='Address')


        self.student_table.column('ID Student', width=100)
        self.student_table.column('Name Student', width=100)
        self.student_table.column('E-Mail', width=30)
        self.student_table.column('Phone Student', width=100)
        self.student_table.column('Qualification', width=100)
        self.student_table.column('Gender', width=30)
        self.student_table.column('Address', width=30)
        self.student_table.bind("<ButtonRelease-1>",self.get_cur)
        #-------------- ad + con ------------------------

        self.update()
        self.fetch_all()
    def add_student(self):
        con = pymysql.connect(host='localhost',user='root', password='12345',database='stud')
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
            self.id_var.get(),
            self.name_var.get(),
            self.email_var.get(),
            self.phon_var.get(),
            self.quali_var.get(),
            self.gender_var.get(),
            self.address_var.get()

        ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
    def fetch_all(self ):
        con = pymysql.connect(host='localhost',user='root',password='12345',database='stud')
        cur = con.cursor()
        cur.execute("select  * from students")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
                con.commit()
        con.close()
    def delet_stud(self):
        con = pymysql.connect(host='localhost', user='root', password='12345', database='stud')
        cur = con.cursor()
        cur.execute('DELETE FROM students WHERE `Name Student` = %s',self.dell_var.get())
        con.commit()
        self.fetch_all()
        con.close()
    def clear(self):
        self.id_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.phon_var.set(""),
        self.quali_var.set(""),
        self.gender_var.set(""),
        self.address_var.set("")

    def get_cur(self,ev):
        cur_row = self.student_table.focus()
        cont = self.student_table.item(cur_row)
        row = cont['values']
        self.id_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.phon_var.set(row[3]),
        self.quali_var.set(row[4]),
        self.gender_var.set(row[5]),
        self.address_var.set(row[6])


    def update(self):
        con = pymysql.connect(host='localhost',user='root', password='12345',database='stud')
        cur = con.cursor()
        cur.execute("""
        UPDATE students 
        SET `Name Student`=%s, `E-Mail`=%s, `Phone Student`=%s, `Qualification`=%s, `Gender`=%s, `Address`=%s 
        WHERE `ID Student`=%s
        """,(

            self.name_var.get(),
            self.email_var.get(),
            self.phon_var.get(),
            self.quali_var.get(),
            self.gender_var.get(),
            self.address_var.get(),
            self.id_var.get()

        ))
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()


    # def search(self ):
    #     con = pymysql.connect(host='localhost',user='root',password='12345',database='stud')
    #     cur = con.cursor()
    #     cur.execute("select  * from students where " + str(self.sea_by.get()) + " LIKE '% " + str(self.search_var.get() + "%'"))
    #     rows = cur.fetchall()
    #     if len(rows)!=0:
    #         self.student_table.delete(*self.student_table.get_children())
    #         for row in rows:
    #             self.student_table.insert("",END,values=row)
    #             con.commit()
    #     con.close()
    def search(self):
        con = pymysql.connect(host='localhost', user='root', password='12345', database='stud')
        cur = con.cursor()

        search_by = str(self.sea_by.get()).strip()  # التأكد من عدم وجود مسافات زائدة
        search_value = "%" + str(self.search_var.get()).strip() + "%"  # إضافة الـ % بشكل صحيح حول القيمة المدخلة

        if not search_by:  # التأكد من عدم ترك اسم العمود فارغًا
            print("Error: Search column is empty.")
            return

        try:
            # استخدام علامات التنصيص الخلفية حول اسم العمود
            query = f"SELECT * FROM students WHERE `{search_by}` LIKE %s"
            print(f"Executing query: {query} with value: {search_value}")  # طباعة الاستعلام والقيم

            cur.execute(query, (search_value,))
            rows = cur.fetchall()

            self.student_table.delete(*self.student_table.get_children())  # حذف الصفوف الحالية في الجدول
            if len(rows) != 0:
                for row in rows:
                    self.student_table.insert("", END, values=row)
            else:
                # إدارة حالة عدم العثور على بيانات
                self.student_table.insert("", END, values=("No results found",))

        except pymysql.MySQLError as e:
            print(f"Error: {e}")

        finally:
            con.close()

    def about (self):
        messagebox.showinfo('frist GUI','devloper MO')


root = Tk()
ob = Student(root)

root.mainloop()