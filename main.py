import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
import os
matplotlib.use("QtAgg")


root = Tk()
root.title("Sound Speed/Attenuation/Density Auto Calculator")
root.config(bg="lightgrey")
# entering dx information
dx = Label(root, text="Δx", bg="lightgrey")
dx.grid(row=0, column=2, columnspan=1, padx=5, pady=5)

dx1 = Entry(root,width=5 ,bd=3)
dx1.grid(row=1, column=2, padx=5, pady=5)


dx2 = Entry(root,width=5 ,bd=3)
dx2.grid(row=2, column=2, padx=5, pady=5)

dx3 = Entry(root,width=5 ,bd=3)
dx3.grid(row=3, column=2, padx=5, pady=5)

dx4 = Entry(root,width=5 ,bd=3)
dx4.grid(row=4, column=2, padx=5, pady=5)

dx5 = Entry(root,width=5 ,bd=3)
dx5.grid(row=5, column=2, padx=5, pady=5)

dx6 = Entry(root,width=5 ,bd=3)
dx6.grid(row=6, column=2, padx=5, pady=5)

dx7 = Entry(root,width=5 ,bd=3)
dx7.grid(row=7, column=2, padx=5, pady=5)

dx8 = Entry(root,width=5 ,bd=3)
dx8.grid(row=8, column=2, padx=5, pady=5)

dx9 = Entry(root,width=5 ,bd=3)
dx9.grid(row=9, column=2, padx=5, pady=5)

dx10 = Entry(root,width=5 ,bd=3)
dx10.grid(row=10, column=2, padx=5, pady=5)

# entering dy information
dy = Label(root, text="Δy1", bg="lightgrey")
dy.grid(row=0, column=3, columnspan=1, padx=5, pady=5)

dy1 = Entry(root,width=5 ,bd=3)
dy1.grid(row=1, column=3, padx=5, pady=5)

dy2 = Entry(root,width=5 ,bd=3)
dy2.grid(row=2, column=3, padx=5, pady=5)

dy3 = Entry(root,width=5 ,bd=3)
dy3.grid(row=3, column=3, padx=5, pady=5)

dy4 = Entry(root,width=5 ,bd=3)
dy4.grid(row=4, column=3, padx=5, pady=5)

dy5 = Entry(root,width=5 ,bd=3)
dy5.grid(row=5, column=3, padx=5, pady=5)

dy6 = Entry(root,width=5 ,bd=3)
dy6.grid(row=6, column=3, padx=5, pady=5)

dy7 = Entry(root,width=5 ,bd=3)
dy7.grid(row=7, column=3, padx=5, pady=5)

dy8 = Entry(root,width=5 ,bd=3)
dy8.grid(row=8, column=3, padx=5, pady=5)

dy9 = Entry(root,width=5 ,bd=3)
dy9.grid(row=9, column=3, padx=5, pady=5)

dy10 = Entry(root,width=5 ,bd=3)
dy10.grid(row=10, column=3, padx=5, pady=5)

#dy222 = Label(root, text="Δy2", bg="lightgrey")
#dy222.grid(row=0, column=3, columnspan=9, padx=5, pady=5)

#dy21 = Entry(root,width=5 ,bd=3)
#dy21.grid(row=1, column=4, padx=5, pady=5)

#dy22 = Entry(root,width=5 ,bd=3)
#dy22.grid(row=2, column=4, padx=5, pady=5)

#dy23 = Entry(root,width=5 ,bd=3)
#dy23.grid(row=3, column=4, padx=5, pady=5)

#dy24 = Entry(root,width=5 ,bd=3)
#dy24.grid(row=4, column=4, padx=5, pady=5)

#dy25 = Entry(root,width=5 ,bd=3)
#dy25.grid(row=5, column=4, padx=5, pady=5)

#dy26 = Entry(root,width=5 ,bd=3)
#dy26.grid(row=6, column=4, padx=5, pady=5)

#dy27 = Entry(root,width=5 ,bd=3)
#dy27.grid(row=7, column=4, padx=5, pady=5)

#dy28 = Entry(root,width=5 ,bd=3)
#dy28.grid(row=8, column=4, padx=5, pady=5)

#dy29 = Entry(root,width=5 ,bd=3)
#dy29.grid(row=9, column=4, padx=5, pady=5)

#dy210 = Entry(root,width=5 ,bd=3)
#dy210.grid(row=10, column=4, padx=5, pady=5)

Thickness = Label(root, text="Thickness", bg="lightgrey")
Thickness.grid(row=0, column=5, columnspan=9, padx=5, pady=5)

Thickness1 = Entry(root,width=5 ,bd=3)
Thickness1.grid(row=1, column=5, padx=5, pady=5)

Thickness2 = Entry(root,width=5 ,bd=3)
Thickness2.grid(row=2, column=5, padx=5, pady=5)

Thickness3 = Entry(root,width=5 ,bd=3)
Thickness3.grid(row=3, column=5, padx=5, pady=5)

Thickness4 = Entry(root,width=5 ,bd=3)
Thickness4.grid(row=4, column=5, padx=5, pady=5)

mass = Label(root, text="Mass", bg="lightgrey")
mass.grid(row=0, column=20, columnspan=9, padx=5, pady=5)

mass1 = Entry(root,width=5 ,bd=3)
mass1.grid(row=1, column=20, padx=5, pady=5)

mass2 = Entry(root,width=5 ,bd=3)
mass2.grid(row=2, column=20, padx=5, pady=5)

mass3 = Entry(root,width=5 ,bd=3)
mass3.grid(row=3, column=20, padx=5, pady=5)

mass4 = Entry(root,width=5 ,bd=3)
mass4.grid(row=4, column=20, padx=5, pady=5)

mass5 = Entry(root,width=5 ,bd=3)
mass5.grid(row=5, column=20, padx=5, pady=5)

mass6 = Entry(root,width=5 ,bd=3)
mass6.grid(row=6, column=20, padx=5, pady=5)

mass7 = Entry(root,width=5 ,bd=3)
mass7.grid(row=7, column=20, padx=5, pady=5)

mass8 = Entry(root,width=5 ,bd=3)
mass8.grid(row=8, column=20, padx=5, pady=5)

mass9 = Entry(root,width=5 ,bd=3)
mass9.grid(row=9, column=20, padx=5, pady=5)

mass10 = Entry(root,width=5 ,bd=3)
mass10.grid(row=10, column=20, padx=5, pady=5)

Volume = Label(root, text="Volume", bg="lightgrey")
Volume.grid(row=0, column=30, columnspan=9, padx=5, pady=5)

volume1 = Entry(root,width=5 ,bd=3)
volume1.grid(row=1, column=30, padx=5, pady=5)

volume2 = Entry(root,width=5 ,bd=3)
volume2.grid(row=2, column=30, padx=5, pady=5)


volume3 = Entry(root,width=5 ,bd=3)
volume3.grid(row=3, column=30, padx=5, pady=5)


volume4 = Entry(root,width=5 ,bd=3)
volume4.grid(row=4, column=30, padx=5, pady=5)


volume5 = Entry(root,width=5 ,bd=3)
volume5.grid(row=5, column=30, padx=5, pady=5)
  

volume6 = Entry(root,width=5 ,bd=3)
volume6.grid(row=6, column=30, padx=5, pady=5)


volume7 = Entry(root,width=5 ,bd=3)
volume7.grid(row=7, column=30, padx=5, pady=5)


volume8 = Entry(root,width=5 ,bd=3)
volume8.grid(row=8, column=30, padx=5, pady=5)


volume9 = Entry(root,width=5 ,bd=3)
volume9.grid(row=9, column=30, padx=5, pady=5)


volume10 = Entry(root,width=5 ,bd=3)
volume10.grid(row=10, column=30, padx=5, pady=5)





dx_avg_lb = Label(root, text="Avg Δx", bg="lightgrey")
dx_avg_lb.grid(row=11, column=1, columnspan=2, padx=5, pady=5)

dx_avg = StringVar()
ttk.Label(root, textvariable=dx_avg).grid(column=2, row=12)

density__lb = Label(root, text="Density (kg/L)", bg="lightgrey")
density__lb.grid(row=0, column=44, columnspan=3, padx=5, pady=5)

density1 = StringVar()
ttk.Label(root, textvariable=density1).grid(column=45, row=1)

density2 = StringVar()
ttk.Label(root, textvariable=density2).grid(column=45, row=2)


density3 = StringVar()
ttk.Label(root, textvariable=density3).grid(column=45, row=3)

density4 = StringVar()
ttk.Label(root, textvariable=density4).grid(column=45, row=4)

density5 = StringVar()
ttk.Label(root, textvariable=density5).grid(column=45, row=5)

density6 = StringVar()
ttk.Label(root, textvariable=density6).grid(column=45, row=6)

density7 = StringVar()
ttk.Label(root, textvariable=density7).grid(column=45, row=7)

density8 = StringVar()
ttk.Label(root, textvariable=density8).grid(column=45, row=8)

density9 = StringVar()
ttk.Label(root, textvariable=density9).grid(column=45, row=9)

density10 = StringVar()
ttk.Label(root, textvariable=density10).grid(column=45, row=10)

density_avg_lb = Label(root, text="Avg Density (kg/L)", bg="lightgrey")
density_avg_lb.grid(row=11, column=45, columnspan=1, padx=5, pady=5)

density_avg = StringVar()
ttk.Label(root, textvariable=density_avg).grid(column=45, row=12)

dy1_avg_lb = Label(root, text="Avg Δy1", bg="lightgrey")
dy1_avg_lb.grid(row=11, column=3, columnspan=1, padx=5, pady=5)

dy1_avg = StringVar()
ttk.Label(root, textvariable=dy1_avg).grid(column=3, row=12)

#dy2_avg_lb = Label(root, text="Avg Δy2", bg="lightgrey")
#dy2_avg_lb.grid(row=11, column=4, columnspan=1, padx=5, pady=5)

#dy2_avg = StringVar()
#ttk.Label(root, textvariable=dy2_avg).grid(column=4, row=12)

Thickness_avg_lb = Label(root, text="Avg Thickness", bg="lightgrey")
Thickness_avg_lb.grid(row=11, column=5, columnspan=2, padx=5, pady=5)

Thickness_avg = StringVar()
ttk.Label(root, textvariable=Thickness_avg).grid(column=5, row=12)


mass_avg_lb = Label(root, text="Avg M", bg="lightgrey")
mass_avg_lb.grid(row=11, column=20, columnspan=1, padx=5, pady=5)

mass_avg = StringVar()
ttk.Label(root, textvariable=mass_avg).grid(column=20, row=12)


volume_avg_lb = Label(root, text="Avg V", bg="lightgrey")
volume_avg_lb.grid(row=11, column=30, columnspan=2, padx=5, pady=5)

volume_avg = StringVar()
ttk.Label(root, textvariable=volume_avg).grid(column=30, row=12)


isim = Label(root, text="Mehmet Gökalp Köreken/TOBB ETU", bg="lightgrey", font=('Times', 22))
isim.grid(row=27, column=4, columnspan=2, padx=5, pady=5)

def dx_ort():
    dx_sum = []
    try:
        a = float((dx1.get()))
        dx_sum.append(a)
    except:
        print("")  
    try:
        a = float((dx2.get()))
        dx_sum.append(a)
    except:
        print("")  
    try:
        a = float((dx3.get()))
        dx_sum.append(a)
    except:
        print("")  
    try:
        a = float((dx4.get()))
        dx_sum.append(a)
    except:
        print("")  
    try:
        a = float((dx5.get()))
        dx_sum.append(a)
    except:
        print("")  
    try:
        a = float((dx6.get()))
        dx_sum.append(a)
    except:
        print("")  
    try:
        a = float((dx7.get()))
        dx_sum.append(a)
    except:
        print("")
    try:
        a = float((dx8.get()))
        dx_sum.append(a)
    except:
        print("")  
    try:
        a = float((dx9.get()))
        dx_sum.append(a)
    except:
        print("")
    try:
        a = float((dx10.get()))
        dx_sum.append(a)
    except:
        print("")    
    if(len(dx_sum)!= 0):
        b = sum(dx_sum) / len(dx_sum)
        dx_avg.set(float(b))
dx_avg_btn = Button(root, text ="Calculate Δx ", command = dx_ort)
dx_avg_btn.grid(column=2, row=13)
def dy_ort():
    dy_sum = []
    try:
        a = float((dy1.get()))
        dy_sum.append(a)
    except:
        print("")  
    try:
        a = float((dy2.get()))
        dy_sum.append(a)
    except:
        print("")  
    try:
        a = float((dy3.get()))
        dy_sum.append(a)
    except:
        print("")  
    try:
        a = float((dy4.get()))
        dy_sum.append(a)
    except:
        print("")  
    try:
        a = float((dy5.get()))
        dy_sum.append(a)
    except:
        print("")  
    try:
        a = float((dy6.get()))
        dy_sum.append(a)
    except:
        print("")  
    try:
        a = float((dy7.get()))
        dy_sum.append(a)
    except:
        print("")  
    try:
        a = float((dy8.get()))
        dy_sum.append(a)
    except:
        print("")  
    try:
        a = float((dy9.get()))
        dy_sum.append(a)
    except:
        print("")  
    try:
        a = float((dy10.get()))
        dy_sum.append(a)
    except:
        print("")    
    if(len(dy_sum)!= 0):
        b = sum(dy_sum) / len(dy_sum)
        dy1_avg.set(float(b))

dy_avg_btn = Button(root, text ="Calculate Δy1 ", command = dy_ort)
dy_avg_btn.grid(column=3, row=13)

#def dy2_ort():
 #   dy2_sum = []
   # try:
    #    a = float((dy21.get()))
 #       dy2_sum.append(a)
   # except:
 #       print("")  
   # try:
   #     a = float((dy22.get()))
  #      dy2_sum.append(a)
 #   except:
  #      print("")  
  #  try:
  #      a = float((dy23.get()))
   #     dy2_sum.append(a)
   # except:
   #     print("")  
   # try:
   ##     a = float((dy24.get()))
  #      dy2_sum.append(a)
  #  except:
 ##       print("")  
  #  try:
     #   a = float((dy25.get()))
      #  dy2_sum.append(a)
   ## except:
  #      print("")  
  #  try:
   #     a = float((dy26.get()))
   #     dy2_sum.append(a)
  #  except:
  #      print("")  
  #  try:
   #     a = float((dy27.get()))
   #     dy2_sum.append(a)
  #  except:
     #   print("")  
   # try:
    #    a = float((dy28.get()))
   #     dy2_sum.append(a)
   # except:
   #     print("")  
    #try:
    #    a = float((dy29.get()))
     #   dy2_sum.append(a)
   # except:
    #    print("")  
   # try:
    #    a = float((dy210.get()))
    #    dy2_sum.append(a)
    #except:
   #     print("")    
   # if(len(dy2_sum)!= 0):
   #     b = sum(dy2_sum) / len(dy2_sum)
     #   dy2_avg.set(float(b))

#dy_avg_btn = Button(root, text ="Calculate Δy2 ", command = dy2_ort)
#y_avg_btn.grid(column=4, row=13)

def Thick_ort():
    Thick_sum = []
    try:
        a = float((Thickness1.get()))
        Thick_sum.append(a)
    except:
        print("")  
    try:
        a = float((Thickness2.get()))
        Thick_sum.append(a)
    except:
        print("")  
    try:
        a = float((Thickness3.get()))
        Thick_sum.append(a) 
    except:
        print("")  
    try:
        a = float((Thickness4.get()))
        Thick_sum.append(a) 
    except:
        print("")  
    if(len(Thick_sum)!= 0):
        b = sum(Thick_sum) / len(Thick_sum)
        Thickness_avg.set(float(b))

thick_btn = Button(root, text ="Calculate Thickness ", command = Thick_ort)
thick_btn.grid(column=5, row=13)

def mass_ort():
    mass_sum = []
    try:
        a = float((mass1.get()))
        mass_sum.append(a)
    except:
        print("")  
    try:
        a = float((mass2.get()))
        mass_sum.append(a)
    except:
        print("")  
    try:
        a = float((mass3.get()))
        mass_sum.append(a)
    except:
        print("")  
    try:
        a = float((mass4.get()))
        mass_sum.append(a)
    except:
        print("")  
    try:
        a = float((mass5.get()))
        mass_sum.append(a)
    except:
        print("")  
    try:
        a = float((mass6.get()))
        mass_sum.append(a)
    except:
        print("")  
    try:
        a = float((mass7.get()))
        mass_sum.append(a)
    except:
        print("")  
    try:
        a = float((mass8.get()))
        mass_sum.append(a)
    except:
        print("")  
    try:
        a = float((mass9.get()))
        mass_sum.append(a)
    except:
        print("")  
    try:
        a = float((mass10.get()))
        mass_sum.append(a)
    except:
        print("")    
    if(len(mass_sum)!= 0):
        b = sum(mass_sum) / len(mass_sum)
        mass_avg.set(float(b))

mass_btn = Button(root, text ="Calculate Mass ", command = mass_ort)
mass_btn.grid(column=20, row=13)

def volume_ort():
    volume_sum = []
    try:
        a = float((volume1.get()))
        volume_sum.append(a)
    except:
        print("")  
    try:
        a = float((volume2.get()))
        volume_sum.append(a)
    except:
        print("")  
    try:
        a = float((volume3.get()))
        volume_sum.append(a)
    except:
        print("")  
    try:
        a = float((volume4.get()))
        volume_sum.append(a)
    except:
        print("")  
    try:
        a = float((volume5.get()))
        volume_sum.append(a)
    except:
        print("")  
    try:
        a = float((volume6.get()))
        volume_sum.append(a)
    except:
        print("")  
    try:
        a = float(volume7.get())
        volume_sum.append(a)
    except:
        print("")  
    try:
        a = float((volume8.get()))
        volume_sum.append(a)
    except:
        print("")  
    try:
        a = float((volume9.get()))
        volume_sum.append(a)
    except:
        print("")  
    try:
        a = float((mass10.get()))
        volume_sum.append(a)
    except:
        print("")    
    if(len(volume_sum)!= 0):
        b = sum(volume_sum) / len(volume_sum)
        volume_avg.set(float(b))

volume_btn = Button(root, text ="Calculate Volume ", command = volume_ort)
volume_btn.grid(column=30, row=13)

def density():
    try:
        a = float((volume1.get()))
        b = float((mass1.get()))
        c=b/a
        density1.set(float(c))
    except:
        print("")  
    try:
        a = float((volume2.get()))
        b = float((mass2.get()))
        c=b/a
        density2.set(float(c))
    except:
        print("")  
    try:
        a = float((volume3.get()))
        b = float((mass3.get()))
        c=b/a
        density3.set(float(c))
    except:
        print("")  
    try:
        a = float((volume4.get()))
        b = float((mass4.get()))
        c=b/a
        density4.set(float(c))
    except:
        print("")  
    try:
        a = float((volume5.get()))
        b = float((mass5.get()))
        c=b/a
        density5.set(float(c))
    except:
        print("")  
    try:
        a = float((volume6.get()))
        b = float((mass6.get()))
        c=b/a
        density6.set(float(c))
    except:
        print("")  
    try:
        a = float((volume7.get()))
        b = float((mass7.get()))
        c=b/a
        density7.set(float(c))
    except:
        print("")  
    try:
        a = float((volume8.get()))
        b = float((mass8.get()))
        c=b/a
        density8.set(float(c))
    except:
        print("")  
    try:
        a = float((volume9.get()))
        b = float((mass9.get()))
        c=b/a
        density9.set(float(c))
    except:
        print("")  
    try:
        a = float((volume10.get()))
        b = float((mass10.get()))
        c=b/a
        density10.set(float(c))
    except:
        print("")    
    try:
        a = float((volume_avg.get()))
        b = float((mass_avg.get()))
        c=b/a
        density_avg.set(float(c))
    except:
        print("") 
density_btn = Button(root, text ="Calculate Density ", command = density)
density_btn.grid(row=13, column=45, columnspan=2, padx=5, pady=5)

ses_hizi_lb = Label(root, text="Sound Speed(m/s)", bg="lightgrey")
ses_hizi_lb.grid(row=16, column=2, columnspan=1, padx=5, pady=5)

ses_hizi_lb2 = Label(root, text="Standart Deviasion", bg="lightgrey")
ses_hizi_lb2.grid(row=16, column=3, columnspan=1, padx=5, pady=5)

ses_hizi = StringVar()
ttk.Label(root, textvariable=ses_hizi).grid(column=2, row=17)

ses_hizi_std = StringVar()
ttk.Label(root, textvariable=ses_hizi_std).grid(column=3, row=17)

def ses_hizi_calc():
    ses_hizi.set(float(0))
    ses_hizi_arr = []
    try:
        a = float((dx_avg.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi.set(c)
    except:
        pass
    ses_hizi_arr = []
    try:
        a = float((dx1.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi_arr.append(c)
    except:
        pass  
    try:
        a = float((dx2.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi_arr.append(c)
    except:
        pass 
    try:
        a = float((dx3.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi_arr.append(c)
    except:
        pass
    try:
        a = float((dx4.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi_arr.append(c)
    except:
        pass 
    try:
        a = float((dx5.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi_arr.append(c)
    except:
        pass 
    try:
        a = float((dx6.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi_arr.append(c)
    except:
        pass 
    try:
        a = float((dx7.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi_arr.append(c)
    except:
        pass 
    try:
        a = float((dx8.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi_arr.append(c)
    
    except:
        pass 
    try:
        a = float((dx9.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi_arr.append(c)
    except:
        pass
    try:
        a = float((dx10.get()))
        k=a/10000000
        b = float((Thickness_avg.get()))
        o=b*2/1000
        c=o/k
        ses_hizi_arr.append(c)
    except:
        pass  

    try:
        s = np.std(ses_hizi_arr)
        ses_hizi_std.set(float(s))
    except:
        pass
    


SesHizi_btn = Button(root, text ="Calculate Speed", command = ses_hizi_calc)
SesHizi_btn.grid(row=18, column=1, columnspan=3, padx=5, pady=5) 



atunasyon_lb = Label(root, text="Attenuation Constant(dB/cm Mhz)", bg="lightgrey")
atunasyon_lb.grid(row=16, column=4, columnspan=1, padx=5, pady=5)

atunasyon_lb2 = Label(root, text="Standart Deviasion", bg="lightgrey")
atunasyon_lb2.grid(row=16, column=5, columnspan=4, padx=5, pady=5)

atunasyon_ort = StringVar()
ttk.Label(root, textvariable=atunasyon_ort).grid(column=4, row=17)

atunasyon_std = StringVar()
ttk.Label(root, textvariable=atunasyon_std).grid(column=5, row=17)


def atunasyon_calc():
    atunasyon_ort.set(float(0))
    try:
        a = float((dy1_avg.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float(-(1/p)*(k))
        atunasyon_ort.set(float(u))
    except:
        pass
    atunasyon_arr = []
    try:
        a = float((dy1.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float(-(1/p)*(k))
        atunasyon_arr.append(u)
    except:
        pass  
    try:
        a = float((dy2.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float(-(1/p)*(k))
        atunasyon_arr.append(u)
    except:
        pass 
    try:
        a = float((dy3.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float(-(1/p)*(k))
        atunasyon_arr.append(u)
    except:
        pass
    try:
        a = float((dy4.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float(-(1/p)*(k))
        atunasyon_arr.append(u)
    except:
        pass 
    try:
        a = float((dy5.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float(-(1/p)*(k))
        atunasyon_arr.append(u)
        atunasyon_arr.append(u)
    except:
        pass 
    try:
        a = float((dy6.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float(-(1/p)*(k))
        atunasyon_arr.append(u)
    except:
        pass 
    try:
        a = float((dy7.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float(-(1/p)*(k))
        atunasyon_arr.append(u)
    except:
        pass 
    try:
        a = float((dy8.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float(-(1/p)*(k))
        atunasyon_arr.append(u)
    except:
        pass 
    try:
        a = float((dy9.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float(-(1/p)*(k))
        atunasyon_arr.append(u)
    except:
        pass 
    try:
        a = float((dy10.get()))
        k = np.log(a)
        p = float((Thickness_avg.get()))/10
        u = float((1/p)*(k))
        atunasyon_arr.append(u)
    except:
        pass 
    try:
        s = np.std(atunasyon_arr)
        atunasyon_std.set(float(s))
    except:
        pass


Atunasyon_btn = Button(root, text ="Calculate Attenuation", command = atunasyon_calc)
Atunasyon_btn.grid(row=18, column=4, columnspan=4, padx=5, pady=5)



def AutomationX():
    files=os.listdir()
    nmbr=1
    for i in files:
        str1 = 'file' + str(nmbr)
        if i.endswith('.csv'):
            data=pd.read_csv(i)
            data['x-axis'].values[0]=data['x-axis'].values[2]
            data['1'].values[0]=data['x-axis'].values[2]
            data['x-axis'].values[1]=data['x-axis'].values[2]
            data['1'].values[1]=data['x-axis'].values[2]    
            data.to_excel('{}.xlsx'.format(str1) ,sheet_name='new_sheet_name')
    df = pd.read_excel('file1.xlsx')
    df['x-axis']=df['x-axis'].astype(float)
    df['1']=df['1'].astype(float)
    arr1 = df[['x-axis']].to_numpy()
    arr2 = df['1'].to_numpy()
    dx_raw_data=[]
    dx_proc_data=[]
    def mouse_event(event):
        dx_raw_data.append(event.xdata)
        if(len(dx_raw_data)%2==0):
            i1=(dx_raw_data[len(dx_raw_data)-1]-dx_raw_data[len(dx_raw_data)-2])*(1000000)
            dx_proc_data.append(i1)
            try:
                if(len(dx_proc_data)<=1):
                    dx1.insert(0,dx_proc_data[0])
            except:
                pass
            try:
                if(len(dx_proc_data)<=2):
                    dx2.insert(0,dx_proc_data[1])
            except:
                pass
            try:
                if(len(dx_proc_data)<=3):
                    dx3.insert(0,dx_proc_data[2])
            except:
                pass
            try:
                if(len(dx_proc_data)<=4):
                    dx4.insert(0,dx_proc_data[3])
            except:
                pass    
            try:
                if(len(dx_proc_data)<=5):
                    dx5.insert(0,dx_proc_data[4])
            except:
                pass
            try:
                if(len(dx_proc_data)<=6):
                    dx6.insert(0,dx_proc_data[5])
            except:
                pass
            try:
                if(len(dx_proc_data)<=7):
                    dx7.insert(0,dx_proc_data[6])
            except:
                pass
            try:
                if(len(dx_proc_data)<=8):
                    dx8.insert(0,dx_proc_data[7])
            except:
                pass
            try:
                if(len(dx_proc_data)<=9):
                    dx9.insert(0,dx_proc_data[8])
            except:
                pass
            try:
                if(len(dx_proc_data)<=10):
                    dx10.insert(0,dx_proc_data[9])
            except:
                pass
            if(len(dx_proc_data)==10):
                plt.close('all')
                
  


    fig = plt.figure()
    cid = fig.canvas.mpl_connect('button_press_event', mouse_event)
    plt.plot(arr1, arr2)
    plt.show()
    
            



def AutomationY():
    files=os.listdir()
    nmbr=1
    for i in files:
        str1 = 'file' + str(nmbr)
        if i.endswith('.csv'):
            data=pd.read_csv(i)
            data['x-axis'].values[0]=data['x-axis'].values[2]
            data['1'].values[0]=data['x-axis'].values[2]
            data['x-axis'].values[1]=data['x-axis'].values[2]
            data['1'].values[1]=data['x-axis'].values[2]    
            data.to_excel('{}.xlsx'.format(str1) ,sheet_name='new_sheet_name')
    df = pd.read_excel('file1.xlsx')
    df['x-axis']=df['x-axis'].astype(float)
    df['1']=df['1'].astype(float)
    arr1 = df[['x-axis']].to_numpy()
    arr2 = df['1'].to_numpy()
    dy_raw_data=[]
    dy_proc_data = []
    def mouse_event(event):
        dy_raw_data.append(event.ydata)
        if(len(dy_raw_data)%2==0):
            i1=(dy_raw_data[len(dy_raw_data)-1]-dy_raw_data[len(dy_raw_data)-2])
            dy_proc_data.append(i1)
            try:
                if(len(dy_proc_data)<=2):
                    dy1.insert(0,(dy_proc_data[1]-dy_proc_data[0]))
            except:
                pass
            try:
                if(len(dy_proc_data)<=4):
                    dy2.insert(0,(dy_proc_data[3]-dy_proc_data[2]))
            except:
                pass
            try:
                if(len(dy_proc_data)<=6):
                    dy3.insert(0,(dy_proc_data[5]-dy_proc_data[4]))
            except:
                pass
            try:
                if(len(dy_proc_data)<=8):
                    dy4.insert(0,(dy_proc_data[7]-dy_proc_data[6]))
            except:
                pass    
            try:
                if(len(dy_proc_data)<=10):
                    dy5.insert(0,(dy_proc_data[9]-dy_proc_data[8]))
            except:
                pass
            try:
                if(len(dy_proc_data)<=12):
                    dy6.insert(0,(dy_proc_data[11]-dy_proc_data[10]))
            except:
                pass
            try:
                if(len(dy_proc_data)<=14):
                    dy7.insert(0,(dy_proc_data[13]-dy_proc_data[12]))
            except:
                pass
            try:
                if(len(dy_proc_data)<=16):
                    dy8.insert(0,(dy_proc_data[15]-dy_proc_data[14]))
            except:
                pass
            try:
                if(len(dy_proc_data)<=18):
                    dy9.insert(0,(dy_proc_data[17]-dy_proc_data[16]))
            except:
                pass
            try:
                if(len(dy_proc_data)<=20):
                    dy10.insert(0,(dy_proc_data[19]-dy_proc_data[18]))
            except:
                pass
            if(len(dy_proc_data)==20):
                plt.close('all')
                
  


    fig = plt.figure()
    cid = fig.canvas.mpl_connect('button_press_event', mouse_event)
    plt.plot(arr1, arr2)
    plt.show()
    
            


AutomationX_btn = Button(root, text ="Auto insert ΔX values", command = AutomationX)
AutomationX_btn.grid(row=3, column=3, columnspan=4, padx=5, pady=5)


AutomationY_btn = Button(root, text ="Auto insert ΔY values", command = AutomationY)
AutomationY_btn.grid(row=2, column=3, columnspan=4, padx=5, pady=5)




mainloop()