# Program de citit ziare online
# de pe mai multe surse precum
# Adevarul
# Program realizat de catre:
# Olariu Alexandru-Razvan
# Contact: ufcolonel@gmail.com


import Crawler,Scraper
from datetime import datetime
from tkinter import *
from tkinter import ttk



def save_status():
    global alegeri
    global interest
    alegeri = [option1.get(),option2.get(),option3.get(),
               option4.get(),option5.get(),option6.get(),
               option7.get(),option8.get(),option9.get()]
    interest = [search.get()]
    
def check():
    for source in range(len(alegeri)):
        https = alegeri[source]
        if https.startswith("https://"):
            try:
                https = Crawler.crawl(https,interest)
            except Exception as error:
                with open("Reports.txt","w") as f:
                    f.write(str(error))
            finally:
                interest = Scraper.scrape(https)


def save():
    alegeri = [option1.get(),option2.get(),option3.get(),
               option4.get(),option5.get(),option6.get(),
               option7.get(),option8.get(),option9.get()]
    for source in range(len(alegeri)):
        if alegeri[source].startswith("https://"):
            header = f"Date din sursa {alegeri[source]} :\n"
            with open("Salvate.txt","a") as g:
                g.write(datetime.now().strftime("\t%d/%m/%Y <---> %H:%M:%S\n"))
                g.write(header)
                g.write(interest)

            

# Graphical User Interface initialization - FINISHED
app = Tk()
app.title('Ziare online de Olariu Alexandru-Razvan')
app.geometry('900x500')
app.resizable(False,False)


# Search
ttk.Label(app,text="Căutare după termeni:").place(x=10,y=5)
search = ttk.Entry(app)
search.place(x=150,y=5,width=300,height=23)

# Online News Variables
option1, option2, option3 = StringVar(), StringVar(), StringVar()
option4, option5, option6 = StringVar(), StringVar(), StringVar() 
option7, option8, option9 = StringVar(), StringVar(), StringVar() 

# Online News

ttk.Checkbutton(app,text="Ziarul Libertatea",variable=option1,
                        onvalue='https://www.libertatea.ro/',
                        command=save_status).place(x=10,y=50)
ttk.Checkbutton(app,text="Ziarul Financiar",variable=option2,
                        onvalue='https://www.zf.ro/',
                        command=save_status).place(x=10,y=100)
ttk.Checkbutton(app,text="Mediafax",variable=option3,
                        onvalue='https://www.mediafax.ro/',
                        command=save_status).place(x=160,y=50)
ttk.Checkbutton(app,text="Evenimentul Zilei",variable=option4,
                        onvalue='https://evz.ro/',
                        command=save_status).place(x=160,y=100)
ttk.Checkbutton(app,text="Ziarul Adevarul",variable=option5,
                        onvalue='https://adevarul.ro/cauta',
                        command=save_status).place(x=310,y=50)
ttk.Checkbutton(app,text="Jurnalul Zilei",variable=option6,
                        onvalue='https://jurnalulnational.ro/',
                        command=save_status).place(x=310,y=100)
ttk.Checkbutton(app,text="Digi24",variable=option7,
                        onvalue='https://www.digi24.ro/',
                        command=save_status).place(x=470,y=50)
ttk.Checkbutton(app,text="Realitatea.NET",variable=option8,
                        onvalue='https://www.realitatea.net/',
                        command=save_status).place(x=470,y=100)


# Buttons
check_button = ttk.Button(app,text="Caută",command=check)
check_button.place(x=470,y=4)
save_button = ttk.Button(app,text="Salvare",command=save)
save_button.place(x=570,y=4)



# Output
output = ttk.Notebook(app)
ziar1, ziar2, ziar3 = Text(output), Text(output), Text(output)
ziar4, ziar5, ziar6 = Text(output), Text(output), Text(output)
ziar7, ziar8, ziar9 = Text(output), Text(output), Text(output)  
output.add(ziar1, text="Ziarul Libertatea")
output.add(ziar2, text="Ziarul Financiar")
output.add(ziar3, text="Gazeta Sporturilor")
output.add(ziar4, text="Romania Libera")
output.add(ziar5, text="Ziarul Adevarul")
output.add(ziar6, text="Jurnalul Zilei")
output.add(ziar7, text="Digi24")
output.add(ziar8, text="Realitatea.NET")
output.add(ziar9, text="Ajutor")
output.place(x=0,y=140,width=710,height=360)


# Progress TODO
progress_bar = ttk.Progressbar(app,orient=HORIZONTAL,length=185,mode='determinate')
progress_bar.place(x=711,y=477)

# ADS

ad1_image = PhotoImage(file="ad1.png")
ad1 = Label(app,image=ad1_image)
ad1.place(x=707,y=0)
ttk.Label(app,text="Reclama TA, AICI!").place(x=765,y=231)
ad2_image = PhotoImage(file="ad2.png")
ad2 = Label(app,image=ad2_image)
ad2.place(x=707,y=247)



app.mainloop()