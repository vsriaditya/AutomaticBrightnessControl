from datetime import datetime
import screen_brightness_control as sbc
from tkinter import *
m=Tk()
m.title('Brightness Control')
def saver():
    print("Saving")
    global brit
    brit=e3.get()
    global frot
    frot=e1.get()
    global tot
    tot=e2.get()
    a=True
    while a==True:
        current_brightness=sbc.get_brightness()
        now=datetime.now().time()
        if now.hour>int(frot) and now.hour<int(tot) :
            sbc.set_brightness(brit)
        else:
            sbc.set_brightness(40)
'''  import sqlite3 as s
    con=s.connect('Brightness.db')
    cur=con.cursor()
    cur.execute("insert into brightness values (?,?,?)",(brit,frot,tot))
'''
Label(m, text='Brightness').grid(row=0,column=0) 
Label(m, text='From').grid(row=1,column=0) 
Label(m, text='To').grid(row=1,column=2) 

e1 = Entry(m)
e2 = Entry(m)
e3 = Entry(m)

e1.grid(row=1, column=1) 
e2.grid(row=1, column=3)
e3.grid(row=0, column=1) 
button = Button(m, text='Save', width=5,command=saver) 
button.grid(row=2,column=3)
m.mainloop()