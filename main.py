from customtkinter import *
from random import randint as ran


def check_size():
    global cont
    global btn
    
    if cont <= 5:
        btn.configure(width=40, height=40)
    elif cont <=10:
        btn.configure(width=30, height=30)
    elif cont <=20:
        btn.configure(width=20, height=20)
    elif cont <=30:
        btn.configure(width=10, height=10)
    else:
        btn.configure(width=50, height=50)



def spawn_btn(not_destroy=False):
    global cont
    global btn    

    if not not_destroy:
        btn.destroy()
        cont += 1
    
        
    x = int(ran(50, 350))
    y = int(ran(50, 350))
    btn = CTkButton(body,width=50, height=50, text="", corner_radius=40, command=spawn_btn, fg_color="orange")
    check_size()
    btn.place(x=x, y=y)
    
    contador.configure(text=cont)
    app.update()

btn = None

bag = "black"
fog = "white"

app = CTk()
app.geometry("600x480")
app.configure(background=bag)
app.resizable(False, False)
app.title("Aim Trainner")



set_appearance_mode("dark")

header = CTkFrame(app)
header.pack(fill=X)


cont = 0
contador = CTkLabel(header, text=cont, text_color="#22dd22", font=("Arial", 20))
contador.pack(ipadx=20, ipady=5)

body = CTkFrame(app, width=400, height=400)
body.pack(fill=BOTH, pady=10)

spawn_btn(True)

app.mainloop()
