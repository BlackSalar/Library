from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as mb
from datetime import datetime
from sqlalchemy.orm import Session
import sys
sys.path.append("models.py")
from models import *


class Logbook(tk.Toplevel):
    def __init__(self, parent):
        with Session(autoflush=False, bind=Enginer.engine) as db:
            super().__init__(parent)
            self.resizable(0,0)
            self.iconbitmap('book.ico')
            self.title("Библиотека")
            print(Enginer.database)
            #Журнал учета
            Label(self, height=1, text="Журнал учета", font=("Times New Roman", 14),bg='white').grid(row=0,column=0,columnspan=2)            
        
            Label(self,text="Дата (Год-месяц-день Час:минута:секунда): ").grid(row=1,column=0,padx=5,pady=5)
            self.entry_date=Entry(self)
            self.entry_date.grid(row=1,column=1,padx=5,pady=5)
        
            Label(self,text="Состояние: ").grid(row=2,column=0,padx=5,pady=5) 
            condition=["Взял","Принес"]  
            self.combobox_condition=ttk.Combobox(self,values=condition)
            self.combobox_condition.grid(row=2,column=1,padx=5,pady=5)
            #Книги, которые есть на складе
            Label(self, height=1, text="Книга", font=("Times New Roman", 14),bg='white').grid(row=0,column=2,columnspan=2)
            books=db.query(Books_table).filter(Books_table.State=="На складе").all() 
                           
            Label(self,text="Название:").grid(row=1,column=2,padx=5,pady=5)
            #Извлекаем имя                         
            self.book_name=[]
            for b in books:
                self.book_name.append(b.Name)                
            print(f"Имя книг: {self.book_name}")
            #Перебираем на повтор названий
            duplicates=[]
            book_name=[]
            for b in self.book_name:
                if self.book_name.count(b) > 1 and b not in duplicates:
                    duplicates.append(b)                    
                else:
                    book_name.append(b)                
            print(f"Имя книг: {book_name}")
            self.book_name=book_name
            print("Повторяющиеся элементы в названиях книг:", duplicates)            
            db.commit()
            self.combobox_book=ttk.Combobox(self,values=self.book_name) 
            self.combobox_book.grid(row=1,column=3,padx=5,pady=5)
            self.combobox_book.bind("<<ComboboxSelected>>",self.book)
            
            Label(self,text="Автор:").grid(row=2,column=2,padx=5,pady=5)
            #Извлекаем автора
            self.book_author=[]
            for b in books:
                self.book_author.append(b.Author)
            print(f"Имена авторов: {self.book_author}")
            #Перебираем на повтор названий
            duplicates=[]
            book_author=[]
            for b in self.book_author:
                if self.book_author.count(b) > 1 and b not in duplicates:
                    duplicates.append(b)                    
                else:
                    book_author.append(b)                
            print(f"Авторы: {book_author}")
            self.book_author=book_author
            print("Повторяющиеся элементы в названиях книг:", duplicates)
            db.commit()
            self.combobox_author=ttk.Combobox(self,values=self.book_author)
            self.combobox_author.grid(row=2,column=3,padx=5,pady=5)
            self.combobox_author.bind("<<ComboboxSelected>>",self.author)
            
            #Читатель
            Label(self, height=1, text="Читатель", font=("Times New Roman", 14),bg='white').grid(row=0,column=4,columnspan=2)
            readers=db.query(Readers_table).all()
            
            Label(self,text="Фамилия:").grid(row=1,column=4,padx=5,pady=5)
            self.reader_surname=[]
            for r in readers:
                self.reader_surname.append(r.Surname)
            print(f"Фамилии читателей: {self.reader_surname}")
            #Перебираем на повтор названий
            duplicates=[]
            reader_surname=[]
            for r in self.reader_surname:
                if self.reader_surname.count(r) > 1 and r not in duplicates:
                    duplicates.append(r)                    
                else:
                    reader_surname.append(r)                
            print(f"Фамилии читателей: {reader_surname}")
            self.reader_surname=reader_surname
            print("Повторяющиеся элементы в названиях книг:", duplicates)
            db.commit()
            self.combobox_surname=ttk.Combobox(self,values=self.reader_surname)
            self.combobox_surname.grid(row=1,column=5,padx=5,pady=5)            
            self.combobox_surname.bind("<<ComboboxSelected>>",self.surname)        
            
            Label(self,text="Имя:").grid(row=2,column=4,padx=5,pady=5)
            self.reader_name=[]
            for r in readers:
                self.reader_name.append(r.Name)
            print(f"Имена: {self.reader_name}")
            #Перебираем на повтор названий
            duplicates=[]
            reader_name=[]
            for r in self.reader_name:
                if self.reader_name.count(r) > 1 and r not in duplicates:
                    duplicates.append(r)                    
                else:
                    reader_name.append(r)                
            print(f"Имена: {reader_name}")
            self.reader_name=reader_name
            print("Повторяющиеся элементы в названиях книг:", duplicates)            
            db.commit()
            self.combobox_name=ttk.Combobox(self,values=self.reader_name)
            self.combobox_name.grid(row=2,column=5,padx=5,pady=5)
            self.combobox_name.bind("<<ComboboxSelected>>",self.name)
            
            Label(self,text="Отчество:").grid(row=3,column=4,padx=5,pady=5)
            self.reader_patronymic=[]
            for r in readers:
                self.reader_patronymic.append(r.Patronymic)
            print(f"Отчества: {self.reader_patronymic}")
            #Перебираем на повтор названий
            duplicates=[]
            reader_patronymic=[]
            for r in self.reader_patronymic:
                if self.reader_patronymic.count(r) > 1 and r not in duplicates:
                    duplicates.append(r)                    
                else:
                    reader_patronymic.append(r)                
            print(f"Отчества: {reader_patronymic}")
            self.reader_patronymic=reader_patronymic
            print("Повторяющиеся элементы в названиях книг:", duplicates)
            db.commit()
            self.combobox_patronymic=ttk.Combobox(self,values=self.reader_patronymic)
            self.combobox_patronymic.grid(row=3,column=5,padx=5,pady=5)
            self.combobox_patronymic.bind("<<ComboboxSelected>>",self.patronymic)
             
            Button(self,text="Добавить запись",command=self.add_row).grid(row=4,column=0,padx=5,pady=5)            
            Button(self,text="Изменить",command=self.change_row).grid(row=4,column=2,padx=5,pady=5)
            Button(self,text="Удалить", command=self.delete_row).grid(row=4,column=3,padx=5,pady=5)
        
            column=("Logbook_id","Date","Condition","Reader_id","Reader","Book_id","Book") 
        
            #scroll=Scrollbar(orient=VERTICAL,command=self.tree.yview).grid(row=0,column=3,rowspan=5)       
            self.tree=ttk.Treeview(self,columns=column,show="headings",selectmode="browse")
            #Вертикальная прокрутка
            #scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
            #self.tree.configure(yscroll=scrollbar.set)
            #scrollbar.grid(self,row=0, column=4,rowspan=5,pady=5)
        
            self.tree.grid(row=5,column=0,columnspan=6,padx=5,pady=5)
            #Заголовки
            self.tree.heading("Logbook_id",text="Номер")
            self.tree.heading("Date",text="Дата")
            self.tree.heading("Condition",text="Состояние")            
            self.tree.heading("Reader_id",text="Номер читателя")
            self.tree.heading("Reader",text="Читатель")
            self.tree.heading("Book_id",text="Номер книги")
            self.tree.heading("Book",text="Книга")
            #Добавление в таблицу
            logbooks=db.query(Logbook_table).all()
            print(logbooks)
            db.commit()
            for l in logbooks:
                self.tree.insert("",END,values=(l.Logbook_id,l.Date,l.Condition,l.Reader_id,l.Reader,l.Book_id,l.Book))
                print(f"{l.Logbook_id}.{l.Date},{l.Condition},{l.Reader_id},{l.Reader},{l.Book_id},{l.Book}")
            self.tree.bind("<<TreeviewSelect>>",self.item_selected)
    """
    def combobox_check(self,query):
        kortej=[]
        for q in query:
            kortej+=q
        query=kortej
        return query    
    """
    #Событие таблицы Журнал учета
    def item_selected(self,event):
        item = self.tree.item(self.tree.selection())
        self.entry_date.delete(0,END)
        self.combobox_condition.delete(0,END)
        self.combobox_book.delete(0,END)
        self.combobox_author.delete(0,END)
        self.combobox_surname.delete(0,END)
        self.combobox_name.delete(0,END)
        self.combobox_patronymic.delete(0,END)
        self.entry_date.insert(0,item['values'][1])
        self.combobox_condition.set(item['values'][2])
        with Session(autoflush=False,bind=Enginer.engine) as db:            
            book=db.get(Books_table,item['values'][5])
            reader=db.get(Readers_table,item['values'][3])
            self.combobox_book.set(book.Name)
            self.combobox_author.set(book.Author)
            self.combobox_surname.set(reader.Surname)
            self.combobox_name.set(reader.Name)
            self.combobox_patronymic.set(reader.Patronymic)
    #События по выбору ячеек. Книга
    def book(self,event):
        with Session(autoflush=False,bind=Enginer.engine) as db:                        
            if self.combobox_book.get()!="":
                self.combobox_book.configure(values=self.book_name)
                self.combobox_author.configure(values=self.book_author)
                books=db.query(Books_table).all()                       
                #Извлекаем по индексам книги с таким же названием                 
                index=[]
                for b in books:
                    if self.combobox_book.get()==b.Name:                                                    
                        index.append(b.Book_id)
                    print(f"Индекс книги: {index}")
                #Далее извлекаем по индексу авторов и меняем список в Combobox, если у нескольких авторов книга с одним названием
                authors=[]
                if len(index)>1:                    
                    self.combobox_author.delete(0,'end')
                    for i in index:
                        book=db.get(Books_table,i) 
                        authors.append(book.Author)
                    self.combobox_author.configure(values=authors)               
                else:
                    book=db.get(Books_table,index)
                    authors.append(book.Author)
                    self.combobox_author.set(book.Author)
    def author(self,event):
        with Session(autoflush=False,bind=Enginer.engine) as db: 
            if self.combobox_author.get()!="":
                self.combobox_book.configure(values=self.book_name)
                self.combobox_author.configure(values=self.book_author)
                books=db.query(Books_table).all()                                                  
                #Извлекаем по индексам книги с таким же автором                 
                index=[]
                for b in books:
                    if self.combobox_author.get()==b.Author:                                                    
                        index.append(b.Book_id)
                        print(f"Индекс книги: {index}")
                #Далее извлекаем по индексу названия книг и меняем список в Combobox, если у нескольких авторов книга с одним названием
                names=[]
                if len(index)>1:                    
                    
                    for i in index:
                        book=db.get(Books_table,i) 
                        names.append(book.Name)
                    #self.combobox_book.delete(0,'end')
                    self.combobox_book.configure(values=names)               
                else:
                    book=db.get(Books_table,index)
                    names.append(book.Name)
                    self.combobox_book.set(book.Name) 
    #События по выбору ячеек. Читатель
    def surname(self,event):
        with Session(autoflush=False,bind=Enginer.engine) as db:
            if self.combobox_surname.get()!="":
                self.combobox_name.configure(values=self.reader_name)
                self.combobox_patronymic.configure(values=self.reader_patronymic)
                readers=db.query(Readers_table).all()                                                  
                #Извлекаем по индексам читателей с такой же фамилией                 
                index=[]
                for r in readers:
                    if self.combobox_surname.get()==r.Surname:                                                    
                        index.append(r.Reader_id)
                        print(f"Индекс книги: {index}")
                #Далее извлекаем по индексу имена читателей и меняем список в Combobox, если у нескольких читателей одна фамилия
                names=[]
                if len(index)>1:                    
                    for i in index:
                        reader=db.get(Readers_table,i) 
                        names.append(reader.Name)       
                    self.combobox_name.delete(0,'end')
                    self.combobox_name.configure(values=names)               
                else:
                    reader=db.get(Readers_table,index)
                    names.append(reader.Name)
                    self.combobox_name.set(reader.Name)
                #Далее извлекаем по индексу отчества читателей и меняем список в Combobox, если у нескольких читателей одна фамилия
                patronymics=[]
                if len(index)>1:                    
                    for i in index:
                        reader=db.get(Readers_table,i) 
                        patronymics.append(reader.Patronymic)       
                    self.combobox_patronymic.delete(0,'end')
                    self.combobox_patronymic.configure(values=patronymics)               
                else:
                    reader=db.get(Readers_table,index)
                    names.append(reader.Patronymic)
                    self.combobox_patronymic.set(reader.Patronymic)                
    def name(self,event):
        with Session(autoflush=False,bind=Enginer.engine) as db:
            if self.combobox_name.get()!="":
                self.combobox_surname.configure(values=self.reader_surname)
                self.combobox_patronymic.configure(values=self.reader_patronymic)
                readers=db.query(Readers_table).all()                                                  
                #Извлекаем по индексам читателей с таким же именем                 
                index=[]
                for r in readers:
                    if self.combobox_name.get()==r.Name:                                                    
                        index.append(r.Reader_id)
                        print(f"Индекс книги: {index}")
                #Далее извлекаем по индексу имена читателей и меняем список в Combobox, если у нескольких читателей одна фамилия
                surnames=[]
                if len(index)>1:                    
                    for i in index:
                        reader=db.get(Readers_table,i) 
                        surnames.append(reader.Surname)       
                    self.combobox_surname.delete(0,'end')
                    self.combobox_surname.configure(values=surnames)               
                else:
                    reader=db.get(Readers_table,index)
                    surnames.append(reader.Surname)
                    self.combobox_surname.set(reader.Surname)
                #Далее извлекаем по индексу отчества читателей и меняем список в Combobox, если у нескольких читателей одна фамилия
                patronymics=[]
                if len(index)>1:                    
                    for i in index:
                        reader=db.get(Readers_table,i) 
                        patronymics.append(reader.Patronymic)       
                    self.combobox_patronymic.delete(0,'end')
                    self.combobox_patronymic.configure(values=patronymics)               
                else:
                    reader=db.get(Readers_table,index)
                    patronymics.append(reader.Patronymic)
                    self.combobox_patronymic.set(reader.Patronymic)
    def patronymic(self,event):
        with Session(autoflush=False,bind=Enginer.engine) as db: 
            if self.combobox_patronymic.get()!="":
                self.combobox_surname.configure(values=self.reader_surname)
                self.combobox_name.configure(values=self.reader_name)
                readers=db.query(Readers_table).all()                                                  
                #Извлекаем по индексам читателей с таким же именем                 
                index=[]
                for r in readers:
                    if self.combobox_patronymic.get()==r.Patronymic:                                                    
                        index.append(r.Reader_id)
                        print(f"Индекс книги: {index}")
                #Далее извлекаем по индексу имена читателей и меняем список в Combobox, если у нескольких читателей одна фамилия
                surnames=[]
                if len(index)>1:                    
                    for i in index:
                        reader=db.get(Readers_table,i) 
                        surnames.append(reader.Surname)       
                    self.combobox_surname.delete(0,'end')
                    self.combobox_surname.configure(values=surnames)               
                else:
                    reader=db.get(Readers_table,index)
                    surnames.append(reader.Surname)
                    self.combobox_surname.set(reader.Surname)
                #Далее извлекаем по индексу имена читателей и меняем список в Combobox, если у нескольких читателей одна фамилия
                names=[]
                if len(index)>1:                    
                    for i in index:
                        reader=db.get(Readers_table,i) 
                        names.append(reader.Name)       
                    self.combobox_name.delete(0,'end')
                    self.combobox_name.configure(values=names)               
                else:
                    reader=db.get(Readers_table,index)
                    names.append(reader.Name)
                    self.combobox_name.set(reader.Name)       
    #Удалить запись
    def delete_row(self):
        try:
            item = self.tree.item(self.tree.selection())            
            logbook_id=item['values'][0]
            print(item['values'])                       
            with Session(autoflush=False, bind=Enginer.engine) as db:
                logbook=db.get(Logbook_table,logbook_id)                
                print(logbook)
                db.delete(logbook)
                db.commit()  
                self.tree.delete(self.tree.selection())              
            mb.showinfo("База данных","Данные удалены.")
        except:
            mb.showerror("Ошибка","Данные не удалены.")
    #Изменить запись
    def change_row(self):
        try:
            item = self.tree.item(self.tree.selection())
            #Индекс
            selected_item=self.tree.selection()[0]
            print(selected_item)
            print(item)
            logbook_id=item['values'][0]
            reader_id=item['values'][3]
            book_id=item['values'][5]
            print(item['values'])                       
            with Session(autoflush=False, bind=Enginer.engine) as db:
                book=db.get(Books_table,book_id)                
                logbook=db.get(Logbook_table,logbook_id)                
                #Перерабатываем дату
                if self.entry_date.get()!="":                    
                    data=datetime.strptime(self.entry_date.get(),"%Y-%m-%d %H:%M:%S")
                else:
                    data=datetime.today()                
                logbook.Date=data                
                reader=db.get(Readers_table,reader_id)                
                #Извлекаем новых читателя и книгу
                newbooks=db.query(Books_table).filter(Books_table.Name==self.combobox_book.get(),Books_table.Author==self.combobox_author.get()).all()                                
                newreaders=db.query(Readers_table).filter(Readers_table.Surname==self.combobox_surname.get(),Readers_table.Name==self.combobox_name.get(),Readers_table.Patronymic==self.combobox_patronymic.get()).all()
                index_book=[]
                for b in newbooks:                    
                    newbook=db.get(Books_table,b.Book_id)
                    index_book.append(b.Book_id)
                    if len(index_book)>1:
                        raise Exception
                index_reader=[]
                for r in newreaders:
                    newreader=db.get(Readers_table,r.Reader_id)
                    index_reader.append(r.Reader_id)
                    if len(index_reader)>1:
                        raise Exception
                print(f"Новая книга: {newbook}")
                print(f"Новый читатель: {newreader}")
                
                #Проверяем читателей
                if reader!=newreader:
                    logbook.Reader=newreader
                else:
                    logbook.Reader=reader                
                if self.combobox_condition.get()=="Взял":                        
                    #Проверяем на равенство книги
                    if book!=newbook:
                        book.State="На складе"
                        newbook="У читателя"
                        #Привязка к созданной записи
                        logbook.Book=newbook
                    else:
                        logbook.Book=book    
                elif self.combobox_condition.get()=="Принес":
                    
                    #Ищем запись в таблице, что читатель брал эту книгу
                    logbooks=db.query(Logbook_table).all()
                    index=[]
                    for l in logbooks:
                        if l.Reader==logbook.Reader and l.Book==logbook.Book and l.Condition=="Взял":                        
                            index.append(l.Logbook_id)               
                    if len(index)>0:
                        #Проверяем на равенство книги
                        if book!=newbook:
                            book.State="На складе"
                            newbook="У читателя"
                            #Привязка к созданной записи
                            logbook.Book=newbook
                        else:
                            logbook.Book=book
                        db.commit()
                    else:
                        raise Exception
                else:
                    mb.showerror("Ошибка","Состояние книги указано неверно.")
                    book.State=""
                #Привязка книги читателю
                logbook.Book.Reader=logbook.Reader
                db.commit()                                
                self.tree.item(selected_item,values=(logbook.Logbook_id,logbook.Date,logbook.Condition,logbook.Reader_id,logbook.Reader,logbook.Book_id,logbook.Book))
                self.entry_date.delete(0,END)
                self.combobox_condition.delete(0,END)
                self.combobox_book.delete(0,END)
                self.combobox_author.delete(0,END)
                self.combobox_surname.delete(0,END)
                self.combobox_name.delete(0,END)
                self.combobox_patronymic.delete(0,END)            
            mb.showinfo("База данных","Данные изменены.")
        except Exception:
            mb.showerror("Ошибка","Данные не изменены.")
            self.entry_date.delete(0,END)
            self.combobox_condition.delete(0,END)
            self.combobox_book.delete(0,END)
            self.combobox_author.delete(0,END)
            self.combobox_surname.delete(0,END)
            self.combobox_name.delete(0,END)
            self.combobox_patronymic.delete(0,END)
    #Добавить запись
    def add_row(self):
        try: 
            print(self.entry_date.get())
            print(self.combobox_condition.get()) 
                          
            with Session(autoflush=False, bind=Enginer.engine) as db:                
                #Перерабатываем дату
                if self.entry_date.get()!="":                    
                    date=datetime.strptime(self.entry_date.get(),"%Y-%m-%d %H:%M:%S")
                else:
                    date=datetime.today()
                #date="{}-{}-{}".format(date.day,date.month,date.year)
                
                #Выбираем читателя                               
                readers=db.query(Readers_table).all()
                for r in readers:
                    if r.Surname==self.combobox_surname.get() and r.Name==self.combobox_name.get() and r.Patronymic==self.combobox_patronymic.get():
                        reader=db.get(Readers_table,r.Reader_id)
                        print(reader)                
                #Выбираем книгу
                books=db.query(Books_table).all()
                for b in books:
                    if b.Name==self.combobox_book.get() and b.Author==self.combobox_author.get():
                        book=db.get(Books_table,b.Book_id)
                        print(book)                
                #Создаем запись
                logbook=Logbook_table(Date=date,Condition=self.combobox_condition.get())
                #Привязка читателя и книги к записи
                logbook.Reader=reader
                logbook.Book=book                
                #Добавление записи о возвращении
                if logbook.Condition=="Принес":
                    #Ищем запись в таблице, что читатель брал эту книгу
                    logbooks=db.query(Logbook_table).all()
                    index=[]
                    for l in logbooks:
                        if l.Reader==reader and l.Book==book and l.Condition=="Взял":
                            index.append(l.Logbook_id)
                    if len(index)>0:
                        mb.showinfo("Запись","Читатель брал эту книгу.")
                        book.Reader=None
                        book.State="На складе"
                        db.add(logbook)
                        db.commit()
                        db.refresh(logbook)                    
                else:
                    #Привязка книги к читателю
                    book.Reader=reader                
                    book.State="У читателя"                
                    db.add(logbook)
                    db.commit()
                    db.refresh(logbook)
                self.tree.insert("",END,values=(logbook.Logbook_id,logbook.Date,logbook.Condition,logbook.Reader_id,logbook.Reader,logbook.Book_id,logbook.Book)) 
                self.entry_date.delete(0,END)
                self.combobox_condition.delete(0,END)
                self.combobox_book.delete(0,END)
                self.combobox_author.delete(0,END)
                self.combobox_surname.delete(0,END)
                self.combobox_name.delete(0,END)
                self.combobox_patronymic.delete(0,END)  
            mb.showinfo("База данных","Данные добавлены.")        
        except:
            mb.showerror("Ошибка","Данные не добавились")
    def open(self):
        self.grab_set()
        self.wait_window()
