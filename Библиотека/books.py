from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as mb
from sqlalchemy.orm import Session
import sys
sys.path.append("models.py")
from models import *


class Books(tk.Toplevel):    
    def __init__(self, parent):
        super().__init__(parent)
        self.resizable(0,0)
        self.iconbitmap('book.ico')
        self.title("Библиотека")      
        print(Enginer.database) 
        Label(self, height=1, text="Книги", font=("Times New Roman", 14),bg='white').grid(row=0,column=0,columnspan=3)
        
        Label(self,text="Книга: ").grid(row=1,column=0,padx=5,pady=5)
        self.entry_bookname=Entry(self)
        self.entry_bookname.grid(row=1,column=1,padx=5,pady=5)
        
        Label(self,text="Автор: ").grid(row=2,column=0,padx=5,pady=5)
        self.entry_author=Entry(self)
        self.entry_author.grid(row=2,column=1,padx=5,pady=5)
         
        
            
        Button(self,text="Добавить",command=self.add_row).grid(row=1,column=2,padx=5,pady=5)
        Button(self,text="Изменить",command=self.change_row).grid(row=3,column=2,padx=5,pady=5)
        Button(self,text="Удалить", command=self.delete_row).grid(row=4,column=2,padx=5,pady=5)
        
        column=("Book_id","Name","Author","State","Reader","Logbooks") 
        
        #scroll=Scrollbar(orient=VERTICAL,command=self.tree.yview).grid(row=0,column=3,rowspan=5)       
        self.tree=ttk.Treeview(self,columns=column,show="headings",selectmode="browse")
        #Вертикальная прокрутка
        #scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.tree.yview)
        #self.tree.configure(yscroll=scrollbar.set)
        #scrollbar.grid(self,row=0, column=4,rowspan=5,pady=5)
        
        self.tree.grid(row=0,column=3,rowspan=5,padx=5,pady=5)
        #Заголовки
        self.tree.heading("Book_id",text="Номер")
        self.tree.heading("Name",text="Название")
        self.tree.heading("Author",text="Автор")
        self.tree.heading("State",text="Состояние")
        self.tree.heading("Reader",text="Читатель") 
        self.tree.heading("Logbooks",text="Записи")
        #Добавление в таблицу
        with Session(autoflush=False, bind=Enginer.engine) as db:
            books=db.query(Books_table).all()
            print(books)
            db.commit()
            for b in books:
                self.tree.insert("",END,values=(b.Book_id,b.Name,b.Author,b.State,b.Reader,b.Logbooks))
                print(f"{b.Book_id}.{b.Name},{b.Author},{b.State}")
        self.tree.bind("<<TreeviewSelect>>",self.item_selected)
    def item_selected(self,event):
        item = self.tree.item(self.tree.selection())
        self.entry_bookname.delete(0,END)
        self.entry_author.delete(0,END)
        self.entry_bookname.insert(0,item['values'][1])
        self.entry_author.insert(0,item['values'][2])
    #Удалить книгу
    def delete_row(self):
        try:
            item = self.tree.item(self.tree.selection())            
            books_id=item['values'][0]
            print(item['values'])                       
            with Session(autoflush=False, bind=Enginer.engine) as db:
                book=db.get(Books_table,books_id)
                print(book)
                db.delete(book)
                db.commit()  
                self.tree.delete(self.tree.selection())              
            mb.showinfo("База данных","Данные удалены.")
        except:
            mb.showerror("Ошибка","Данные не удалены.")
    #Изменить книгу
    def change_row(self):
        try:
            item = self.tree.item(self.tree.selection())
            #Индекс
            selected_item=self.tree.selection()[0]
            print(selected_item)
            print(item)
            books_id,name,author,state=item['values']
            print(item['values'])                       
            with Session(autoflush=False, bind=Enginer.engine) as db:
                book=db.get(Books_table,books_id)
                print(book)
                book.Name=self.entry_bookname.get()
                book.Author=self.entry_author.get() 
                db.commit() 
                self.tree.item(selected_item,values=(books_id,book.Name,book.Author,book.State))            
            mb.showinfo("База данных","Данные изменены.")
        except:
            mb.showerror("Ошибка","Данные не изменены.")
    #Добавить книгу
    def add_row(self):
        try: 
            print(self.entry_bookname.get())
            print(self.entry_author.get())                
            with Session(autoflush=False, bind=Enginer.engine) as db:
                book=Books_table(Name=self.entry_bookname.get(),Author=self.entry_author.get(),State="На складе")
                books=db.query(Books_table).all()
                db.commit()
                for b in books:
                    if b.Name==book.Name and b.Author==book.Author:
                        raise Exception()
                db.add(book)
                db.commit()        
                print(books)
                self.tree.insert("",END,values=(book.Book_id,book.Name,book.Author,book.State)) 
                self.entry_bookname.delete(0,END)
                self.entry_author.delete(0,END)                  
            mb.showinfo("База данных","Данные добавлены.")
        except Exception: 
            mb.showwarning("Предупреждение", "Такая книга уже есть")
        except:
            mb.showerror("Ошибка","Данные не добавились")
              
    def open(self):
        self.grab_set()
        self.wait_window()
