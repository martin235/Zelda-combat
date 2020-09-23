
import random as rd
from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Combat")
root.geometry("740x500+300+100")
root.resizable(width =False,height=False)
canv=Canvas(root,width=600,height=500)

link_image = Image.open("link.png")
image1 = ImageTk.PhotoImage(link_image,master=root)
item1 = canv.create_image(100, 300, image = image1)
ganon_image = Image.open("ganon.png")
image2 = ImageTk.PhotoImage(ganon_image,master=root)
item2 = canv.create_image(450, 300, image = image2)

Vie_link=canv.create_rectangle(30,150,150,160,width=3)
Vie_ganon=canv.create_rectangle(400,150,520,160,width=3)
Att_link=canv.create_rectangle(2,125,62,135,width=3)
Def_link=canv.create_rectangle(2,95,62,105,width=3)
Def_ganon=canv.create_rectangle(500,125,560,135,width=3)
L1=Label(root,text='Attaque:')
L1.place(x=6,y=123)
L2=Label(root,text='Defense:')
L2.place(x=6,y=92)
L3=Label(root,text="Defense:")
L3.place(x=502,y=123)
Vie_link_var=canv.create_rectangle(30,150,150,160,fill='green')
Vie_ganon_var=canv.create_rectangle(400,150,520,160,fill='green')
Att_link_var=canv.create_rectangle(2,125,2,135,fill='black')
Def_link_var=canv.create_rectangle(2,95,2,105,fill='black')
Def_ganon_var=canv.create_rectangle(500,125,500,135,fill='black')


level=1
roud=1

class Personnage:
    # Attributs
    def __init__(self, nombreDeVies=20):
        self.vie = nombreDeVies
        self.defense=0
        self.attaque=0

    # Méthodes
    def donneEtat(self):
        return self.vie

    def boirePotion(self,mini=1,maxi=3):
        bonus=rd.randint(mini,maxi)
        self.vie=self.vie+bonus

    def perdVie(self,mini=0,maxi=4):
        self.vie = self.vie -rd.randint(mini, maxi)
        self.defense+=1

def PointVie(point1,point2,LinkD,LinkA,GanonD):
    global Vie_link_var
    global Vie_ganon_var
    global Att_link_var
    global Def_link_var
    global Def_ganon_var
    if point1>25:
        point1=25
    if point1>13:
        couleur='green'
    if point1<=13 and point1>5:
        couleur='orange'
    if point1<=5:
        couleur='red'
    if point1<0:
        point1=0
    
    if point2>50:
        point2=50
    if point2>25:
        couleur1='green'
    if point2<=25 and point2>13:
        couleur1='orange'
    if point2<=13:
        couleur1='red'
    if point2<0:
        point2=0
    if LinkA>4:
        LinkA=4
    print(LinkA)
    canv.delete(Vie_ganon_var)
    canv.delete(Vie_link_var)
    canv.delete(Att_link_var)
    canv.delete(Def_link_var)
    canv.delete(Def_ganon_var)
    v1.set(point1)
    v2.set(point2)
    Def_link_var=canv.create_rectangle(2,95,2+LinkD*(60/4),105,fill='black')
    Att_link_var=canv.create_rectangle(2,125,2+LinkA*(60/4),135,fill='black')
    Vie_link_var=canv.create_rectangle(30,150,30+point1*(120/25),160,fill=couleur)
    Vie_ganon_var=canv.create_rectangle(400,150,400+point2*(120/50),160,fill=couleur1)
    Def_ganon_var=canv.create_rectangle(500,125,500+GanonD*(60/5),135,fill='black')


def match(vie1,vie2):
    if vie1>0 and vie2>0:
        return False
    else:
        if vie1>0:
            t=Label(root,text='Victoire de Link',fg='red')
            t.place(x=300,y=300)
        elif vie2>0:
            t=Label(root,text='Victoire de Ganon',fg='red')
            t.place(x=300,y=300)
        else:
            t=Label(root,text='Défaite des deux personnages',fg='red')
            t.place(x=250,y=300)
        return True
    
def att_ganon():
    if link.defense==4:
        var1=link.donneEtat()
        link.boirePotion(1,4)
        link.defense=0
        print("Link se regenere de ",str(link.donneEtat()-var1)," points")
    var1=link.donneEtat()
    link.perdVie(1,3)
    print("Link=",link.donneEtat())
    print("Link perd",str(var1-link.donneEtat())," points de vie")
    PointVie(link.donneEtat(),ganon.donneEtat(),link.defense,link.attaque,ganon.defense)
    match(link.donneEtat(),ganon.donneEtat())
    
    
def att():
    global roud
    var2=ganon.donneEtat()
    win=match(link.donneEtat(),var2)
    if win==False:
        print("ROUND ",roud)
        if ganon.defense==5:
            ganon.boirePotion(1,2+level)
            ganon.defense=0
            print("ganon=",ganon.donneEtat())
            print("Ganon se regenere de ",str(ganon.donneEtat()-var2)," points")
            
        if link.attaque>=4:
            ganon.perdVie(5-level,5-level)
            link.attaque=0
            print("ganon=",ganon.donneEtat())
            print("Ganon perd ",str(var2-ganon.donneEtat())," points de vie")
            
        else:
            ganon.perdVie(1,5-level)
            link.attaque+=1
            print("ganon=",ganon.donneEtat())
            print("Ganon perd ",str(var2-ganon.donneEtat())," points de vie")
        PointVie(link.donneEtat(),ganon.donneEtat(),link.defense,link.attaque,ganon.defense)
        att_ganon()
        roud+=1
    
    
def potion():
    global roud
    var1=link.donneEtat()
    win=match(var1,ganon.donneEtat())
    if win==False:
        print("ROUND ",roud)
        link.boirePotion(1,5-level)
        print("Link gagne ",str(link.donneEtat()-var1)," points de vie")
        print("Link=",link.donneEtat())
        PointVie(link.donneEtat(),ganon.donneEtat(),link.defense,link.attaque,ganon.defense)
        att_ganon()
        roud+=1
    
def selection(lvl):
    global level
    level=lvl   
    print(level)
    
def niveau():
    global level
    fen=Tk()
    fen.title("Paramètres")
    fen.geometry("500x300+400+150")
    fen.resizable(width =False,height=False)


    txt1=Label(fen,text='Choisissez votre niveau:')
    txt1.place(x=180,y=80)
    
    txt2=Label(fen,text="Niveau actuel: "+str(level))
    txt2.place(x=185,y=40)
    
    Nv1=Button(fen,width=8,height=3,text='Easy',bg='green',command=lambda:selection(1))
    Nv1.place(x=80,y=120)
    
    Nv2=Button(fen,width=8,height=3,text='Medium',bg='orange',command=lambda:selection(2))
    Nv2.place(x=220,y=120)
    
    Nv3=Button(fen,width=8,height=3,text='Hardcore',bg='red',command=lambda:selection(3))
    Nv3.place(x=360,y=120)
    
    fen.mainloop()

link = Personnage(25)
ganon = Personnage(50)

v1=StringVar()
v2=StringVar()
vie1=Label(root,textvariable=v1)
vie2=Label(root,textvariable=v2)
v1.set(link.donneEtat())
v2.set(ganon.donneEtat())
vie1.place(x=75,y=148)
vie2.place(x=598,y=148)

B_Attaque=Button(root,width=12,height=5,bg='red',text='Attaque',fg='black',command=att)
B_Attaque.place(x=250,y=50)
B_Potion=Button(root,width=12,height=5,bg='green',text='Potion',fg='black',command=potion)
B_Potion.place(x=370,y=50)

Para=Button(root,width=10,height=2,text='Paramètres',bg='grey',command=niveau)
Para.place(x=600,y=20)

canv.pack()
root.mainloop()