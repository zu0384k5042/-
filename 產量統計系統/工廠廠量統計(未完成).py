import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from PIL import ImageTk, Image
win = tk.Tk()

def fun1():


    global comboExample        #廠區
    global Tayouan          #廠區總產額
    global Zhongli         #廠區總產額
    global Taipei          #廠區總產額
    global today            #今日產量
    global t
    global t1
    global t2
    global TayouanSTR
    global ZhongliSTR
    global TaipeiSTR




    today=entry1.get()
    today=float(today)


    if(comboExample.get() =="桃園"):
        Tayouan=Tayouan+today

        TayouanSTR.set(str(Tayouan))




    elif (comboExample.get()  == "中壢"):
        Zhongli=Zhongli+today

        ZhongliSTR.set(str(Zhongli))




    elif(comboExample.get() =="台北"):
        Taipei= Taipei + int(entry1.get())

        TaipeiSTR.set(str(Taipei))

    return t,t1,t2


#視窗建立
win.wm_title("產量統計")
win.minsize(width=800, height=400)
win.maxsize(width=800, height=400)
win.resizable(width=False, height=False)

#背景
background_image = ImageTk.PhotoImage(Image.open("background.jpg"))
background_label = tk.Label(win, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#標題
label1=tk.Label(win,text="今日產量")
label1.place(x=0,y=0)

#日產能輸入
entry1=tk.Entry(win)
entry1.place(x=80,y=0)


#下拉式功能表
comboExample = ttk.Combobox(win,
                            values=[
                                    "桃園",
                                    "中壢",
                                    "台北"])
comboExample.place(x=20,y=120)
#combotext1=comboExample.get()

comboExample.current(1)

#按鍵設置
btn1 =tk.Button(win,text="輸入",command=fun1)
btn1.place(x=30,y=30)

#顯示產量

""""
label1 為顯示桃園產量
label2 為顯示中壢產量
label3 為顯示新竹產量
"""
label1Str=StringVar()
label1=tk.Label(win,text="桃園廠總產量為",textvariable=label1Str)
label1.place(x=20,y=150)
label1Str.set("")

label2Str=StringVar()
label2=tk.Label(win,text="中壢廠總產量為",textvariable=label1Str)
label2.place(x=20,y=150)
label2Str.set("")

label3Str=StringVar()
label3=tk.Label(win,text="台北廠總產量為",textvariable=label1Str)
label3.place(x=20,y=150)
label3Str.set("")



#廠區位置數量標題
label1=tk.Label(win,text="桃園產量")
label1.place(x=100,y=200)
label2=tk.Label(win,text="中壢產量")
label2.place(x=200,y=200)
label3=tk.Label(win,text="台北產量")
label3.place(x=300,y=200)

#顯示目前累加產量
""""
label5 為顯示桃園累加產量
label6 為顯示中壢累加產量
label7 為顯示新竹累加產量
"""
t=0
t1=0
t2=0

Taipei=0
Zhongli=0
Tayouan =0


TayouanSTR = StringVar()
label5=tk.Label(win,text=t,textvariable=TayouanSTR)
label5.place(x=100,y=250)

ZhongliSTR= StringVar()
label6=tk.Label(win,text=t1,textvariable=ZhongliSTR)
label6.place(x=200,y=250)

TaipeiSTR= StringVar()
label7=tk.Label(win,text=t2,textvariable=TaipeiSTR)
label7.place(x=300,y=250)
win.mainloop()
