from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as mb
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys
sys.path.append("models.py")
from models import *

class Readers(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.resizable(0,0)
        self.iconbitmap('book.ico')
        self.title("Библиотека")      
        print(Enginer.database)
        
        Label(self, height=1, text="Читатели", font=("Times New Roman", 14),bg='white').grid(row=0,column=0,columnspan=3)
        
        Label(self,text="Фамилия: ").grid(row=1,column=0,padx=5,pady=5)
        self.entry_surname=Entry(self)
        self.entry_surname.grid(row=1,column=1,padx=5,pady=5)
        
        Label(self,text="Имя: ").grid(row=2,column=0,padx=5,pady=5)
        self.entry_name=Entry(self)
        self.entry_name.grid(row=2,column=1,padx=5,pady=5)
        
        Label(self,text="Отчество: ").grid(row=3,column=0,padx=5,pady=5)
        self.entry_patronymic=Entry(self)
        self.entry_patronymic.grid(row=3,column=1,padx=5,pady=5)
        
        Button(self,text="Добавить",command=self.add_row).grid(row=1,column=2,padx=5,pady=5)
        Button(self,text="Изменить",command=self.change_row).grid(row=3,column=2,padx=5,pady=5)
        Button(self,text="Удалить",command=self.delete_row).grid(row=4,column=2,padx=5,pady=5)
        
        column=("Reader_id","Surname","Name","Patronymic","Books","Logbooks")
        self.tree=ttk.Treeview(self,columns=column,show="headings",selectmode="browse")
        self.tree.grid(row=0,column=3,rowspan=5,padx=5,pady=5)
        #Заголовки
        self.tree.heading("Reader_id",text="Номер")
        self.tree.heading("Surname",text="Фамилия")
        self.tree.heading("Name",text="Имя")
        self.tree.heading("Patronymic",text="Отчество")
        self.tree.heading("Books",text="Книги")
        self.tree.heading("Logbooks",text="Записи")
        #Добавление в таблицу
        with Session(autoflush=False, bind=Enginer.engine) as db:
            readers=db.query(Readers_table).all()
            print(readers)
            db.commit()
            for b in readers:
                self.tree.insert("",END,values=(b.Reader_id,b.Surname,b.Name,b.Patronymic,b.Books,b.Logbooks))
                print(f"{b.Reader_id}.{b.Surname},{b.Name},{b.Patronymic}")
        self.tree.bind("<<TreeviewSelect>>",self.item_selected)
    def item_selected(self,event):
        item = self.tree.item(self.tree.selection())        
        self.entry_surname.delete(0,END)
        self.entry_name.delete(0,END)
        self.entry_patronymic.delete(0,END)
        self.entry_surname.insert(0,item['values'][1])
        self.entry_name.insert(0,item['values'][2])
        self.entry_patronymic.insert(0,item['values'][3])
    #Изменить читателя
    def change_row(self):
        try:
            item = self.tree.item(self.tree.selection())
            #Индекс
            selected_item=self.tree.selection()[0]
            print(selected_item)
            readers_id=item['values'][0]
            print(item['values'])                       
            with Session(autoflush=False, bind=Enginer.engine) as db:
                reader=db.get(Readers_table,readers_id)
                print(reader)
                reader.Surname=self.entry_surname.get()
                reader.Name=self.entry_name.get()
                reader.Patronymic=self.entry_patronymic.get()
                db.commit()  
                self.tree.item(selected_item,values=(readers_id,reader.Surname,reader.Name,reader.Patronymic))
                self.entry_surname.delete(0,END)
                self.entry_name.delete(0,END)
                self.entry_patronymic.delete(0,END)              
            mb.showinfo("База данных","Данные изменены.")
        except:
            mb.showerror("Ошибка","Данные не изменены.")
    #Удалить читателя
    def delete_row(self):
        try:
            item = self.tree.item(self.tree.selection())
            readers_id=item['values'][0]
            print(item['values'])                       
            with Session(autoflush=False, bind=Enginer.engine) as db:
                reader=db.get(Readers_table,readers_id)
                print(reader)
                db.delete(reader)
                db.commit()  
                self.tree.delete(self.tree.selection())              
            mb.showinfo("База данных","Данные удалены.")
        except:
            mb.showerror("Ошибка","Данные не удалены.")
    #Добавить читателя
    def add_row(self):
        try: 
            print(self.entry_surname.get())
            print(self.entry_name.get()) 
            print(self.entry_patronymic.get())               
            with Session(autoflush=False, bind=Enginer.engine) as db:
                reader=Readers_table(Surname=self.entry_surname.get(),Name=self.entry_name.get(),Patronymic=self.entry_patronymic.get())
                readers=db.query(Readers_table).all()
                db.commit()
                for r in readers:
                    if r.Surname==reader.Surname and r.Name==reader.Name and r.Patronymic==reader.Patronymic:
                        raise Exception()
                db.add(reader)
                db.commit()  
                self.tree.insert("",END,values=(reader.Reader_id,reader.Surname,reader.Name,reader.Patronymic))
                self.entry_surname.delete(0,END)
                self.entry_name.delete(0,END)
                self.entry_patronymic.delete(0,END)
            mb.showinfo("База данных","Данные добавлены.")
        except Exception: 
            mb.showwarning("Предупреждение","Такой читатель уже есть.")
        except:
            mb.showerror("Ошибка","Данные не добавились")
    def open(self):
        self.grab_set()
        self.wait_window()