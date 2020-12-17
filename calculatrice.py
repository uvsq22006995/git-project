from tkinter import *

main = Tk()
main.geometry("350x270+300+200")
nb1 = ""

def ajout(nb):
    global nb1
    nb1 += nb
    label["text"] = nb1

def num1():
    ajout("1")

def num2():
    ajout("2")

def num3():
    ajout('3')

def num4():
    ajout("4")

def num5():
    ajout("5")

def num6():
    ajout("6")

def num7():
    ajout("7")

def num8():
    ajout("8")

def num9():
    ajout("9")

def zero():
    ajout("0")

def point():
    ajout(".")

def clear():
    global nb1,nb2
    nb1 = ""
    nb2 = ""
    label["text"] = ""

def add():
    global nb1,op,nb2
    nb2 = float(nb1)
    nb1 = ""
    op = 1
    label["text"] = "+"

def sous():
    global nb1,op,nb2
    nb2 = float(nb1)
    nb1 = ""
    op = 2
    label['text'] = "-"

def fois():
    global nb1,op,nb2
    nb2 = float(nb1)
    nb1 = ""
    op = 3
    label['text'] = "x"

def div():
    global nb1,op,nb2
    nb2 = float(nb1)
    nb1 = ""
    op = 4
    label['text'] = "/"


def egal():
    global nb1
    nb1 = float(nb1)
    if(op == 1):
        result = round(nb2 + nb1,10)
    if(op == 2):
        result = round(nb2 - nb1,10)
    if(op == 3):
        result = round(nb2 * nb1,10)
    if(op == 4):
        result = round(nb2 / nb1,10)
    label["text"] = result
    nb1 = str(result)
    result = 0



