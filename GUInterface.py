# Program de citit ziare online
# de pe mai multe surse precum
# Adevarul
# Program realizat de catre:
# Olariu Alexandru-Razvan
# Contact: ufcolonel@gmail.com


#import Scraper 
#import Crawler
from tkinter import *
from tkinter import ttk


#   Graphical User Interface initialization
app = Tk()
screen_width = app.winfo_screenwidth()  # Lungime pentru rezolutia display
screen_height = app.winfo_screenheight()# Latime pentru rezolutie display
app.title('Ziare online de Olariu Alexandru-Razvan')
app.maxsize(screen_width,screen_height)


#   Top-down Menu setup
#   TODO: Prelungire comenzi
menu = Menu(app)
app.config(menu=menu)
helpmenu = Menu(menu)
menu.add_cascade(label='Ajutor', menu=helpmenu) 
helpmenu.add_command(label='Folosire software')
helpmenu.add_command(label='Contact') 

#   Search function
Label(app,text="Cautare dupa termeni:").pack()
search = Entry(app)
search.pack()

#   Variables initialization
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()


#   List of online newspapers
#   TODO: Custom ziar setat de catre utilizator.
ttk.Label(app, text = "Ziare din care vrei sa culegi informatiile:").pack()
ttk.Checkbutton(app, text="evz.ro",variable=var1).pack()
ttk.Checkbutton(app, text="adevarul.ro",variable=var2).pack()
ttk.Entry(app).pack()
ttk.Button(app,text="Verificare").pack()
ttk.Button(app,text="Cautare").pack()


####TEST:#################################
#https = 'https://www.adevarul.ro'       #
#search = 'elev mort curtea de arges'    #
##########################################


#   TODO: Output Box la ziare.
ttk.Label(app, text = "REZULTAT:").pack(pady=25)
address = Text(app)
address.pack()
#   Buton de Iesire din soft:
#   TODO: Buton sa distruga program.
Button(app, text='Iesire', command=app.quit, activebackground="red").pack()
app.mainloop()







#   Web crawler call:
#new_https = Crawler.crawl(f'{https}', f'{search}')
#print(new_https)

#   Web scraper call:
#results = Scraper.scraper('https://www.factual.ro/')
#content = Scraper.scraper(f'{new_https}')
#print(content)