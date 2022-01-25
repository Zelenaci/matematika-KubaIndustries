#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
from tkinter.constants import END
from xml.dom.minidom import Entity


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "EZ Matika"
    

    def __init__(self):
        super().__init__(className=self.name)
        
        self.title(self.name)
        
        self.bind("<Escape>", self.quit)
        
        self.lbl = tk.Label(self, text=" ")
        
        self.generovani()
        
        self.vysledekA = tk.Entry(self)
        
        self.vysledekA.grid(row=3, column=1)
        
        self.lbl_znamkujeme = tk.Label(self, text="")
        
        self.lbl_znamkujeme.grid(row=4,column=1)
        
        self.btn3 = tk.Button(self, text="Ověřit", command=self.overit)
        
        self.btn3.grid(row=5, column=1)


    def plus(self):
        
        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,100-self.cisloA)
        self.vysledek = self.cisloA + self.cisloB
        
        return str(self.cisloA)+"+"+str(self.cisloB)


    def minus(self):

        self.cisloA = random.randint(1,99)
        self.cisloB = random.randint(1,self.cisloA)
        self.vysledek = self.cisloA - self.cisloB

        return str(self.cisloA)+"-"+str(self.cisloB)


    def krat(self):

        self.cisloA = random.randint(1,10)
        self.cisloB = random.randint(1,10)
        self.vysledek = self.cisloA * self.cisloB
        
        return str(self.cisloA)+"*"+str(self.cisloB)


    def deleno(self):

        self.vysledek = random.randint(1,10)
        self.cisloB = random.randint(1,10)
        self.cisloA = self.vysledek * self.cisloB

        return str(self.cisloA)+ "/" +str(self.cisloB)



    def generovani(self):

        self.funkce = random.choice([self.plus,self.minus,self.krat,self.deleno])
        self.zadani = self.funkce()
        self.lbl.config(text= self.zadani)
        self.lbl.grid(row=1,column=1)
        



    def overit(self):

        if int(self.vysledekA.get()) == int(self.vysledek):
            self.lbl_znamkujeme.config(text="Dobře ty!")
        
        else:
            self.lbl_znamkujeme.config(text="Jejda špatně!")
        
        self.generovani()
        self.vysledekA.delete(0,END)
        

app = Application()
app.mainloop()
