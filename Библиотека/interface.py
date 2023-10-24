from tkinter import *
from tkinter import ttk, font
import calendar,datetime
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import sys
sys.path.append("books.py")
sys.path.append("readers.py")
sys.path.append("models.py")
sys.path.append("logbook.py")
from books import *
from readers import *
from models import *
from logbook import *

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Библиотека")
        self.resizable(0,0)
        self.iconbitmap('book.ico')
        #Меню
        mainmenu=Menu(self)
        menu_db=Menu(self,tearoff=0)
        menu_db.add_command(label='Связать БД...', command=self.load_db)
        mainmenu.add_cascade(label='База данных', menu=menu_db)
        self.config(menu=mainmenu)        
        Label(self, height=1, text="Библиотека", font=("Times New Roman", 14),bg='white').grid(row=0,column=0,padx=5,pady=5)
        #Книги 
        Button(self,width=30, height=1,font=("Times New Roman", 14), text="Книги", command=self.open_books).grid(row=1,column=0,padx=5,pady=5)  
        #Читатели
        Button(self,width=30, height=1,font=("Times New Roman", 14), text="Читатели",command=self.open_readers).grid(row=2,column=0,padx=5,pady=5)
        #Журнал учета
        Button(self,width=30, height=1,font=("Times New Roman", 14), text="Журнал учета",command=self.open_logbook).grid(row=3,column=0,padx=5,pady=5)
            
    def load_db(self):
        #filetypes = (("SQLite-файл", "*.db"),("Любой", "*"))
        #self.database= fd.askopenfilename(title="Связать БД", initialdir="/", filetypes=filetypes) 
        #if self.database.endswith('.db'):                                                            
            Enginer.database="library.db"
            Enginer.engine=create_engine("sqlite:///"+Enginer.database,echo=True)
            Base.metadata.create_all(bind=Enginer.engine)
            mb.showinfo("Загрузка","База данных загружена и связана")            
        #else:
            #mb.showerror("Ошибка","Нужен файл формата .db")    
            
            
    def open_books(self):
        #if self.database != "":          
        book=Books(self)
            
            #print(self.database)            
        book.open()            
        #else:
           # mb.showerror("Ошибка","База данных не подключена")
    def open_readers(self):
        reader=Readers(self)
        reader.open()
    def open_logbook(self):
        logbook=Logbook(self)
        logbook.open()    
if __name__=="__main__":
    window=Window()    
    window.mainloop()