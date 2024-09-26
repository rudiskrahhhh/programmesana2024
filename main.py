from cilveks import Cilveks, Sieviete
import tkinter as tk
from tkinter import ttk, END

#cilvēku saraksts

visi_cilveki = []


#Ekrāns

root = tk.Tk()
root.title("Cilvēku ražotne")
root.geometry("500x300")

frame = ttk.Frame(root)

# field options
options = {'padx': 5, 'pady': 5}

# vards label
vards_label = ttk.Label(frame, text='Vārds')
vards_label.grid(column=0, row=0, sticky='E', **options)

# dzimums label
dzimums_label = ttk.Label(frame, text='Dzimums')
dzimums_label.grid(column=0, row=1, sticky='E', **options)

# vecums label
vecums_label = ttk.Label(frame, text='Vecums')
vecums_label.grid(column=0, row=2, sticky='E', **options)

# vārds entry
vards = tk.StringVar()
vards_entry = ttk.Entry(frame, textvariable=vards)
vards_entry.grid(column=1, row=0, **options)
vards_entry.focus()

#dzimums entry
dzimums = tk.StringVar()
dzimums_entry = ttk.Entry(frame, textvariable=dzimums)
dzimums_entry.grid(column=1, row=1, **options)

#vecums entry
vecums = tk.IntVar()
vecums_entry = ttk.Entry(frame, textvariable=vecums)
vecums_entry.grid(column=1, row=2, **options)

#
def nomainit_sarakstu():
    listbox.delete(0,END)
    for cilveks in visi_cilveki:
        listbox.insert("end","{},{},{}".format(cilveks.vards,cilveks.dzimums,cilveks.vecums))

# ražošana button

def razot_button_clicked():
    cilveka_vards = vards.get()
    cilveka_dzimums = dzimums.get()
    cilveka_vecums = vecums.get()
    visi_cilveki.append(Cilveks(cilveka_vards,cilveka_dzimums,cilveka_vecums))
    result_label.config(text=visi_cilveki[-1].info())
    nomainit_sarakstu()
    # listbox.insert("end","{},{},{}".format(cilveka_vards,cilveka_dzimums,cilveka_vecums))



razot_button = ttk.Button(frame, text='Ražot')
razot_button.grid(column=2, row=0, sticky='W', **options)
razot_button.configure(command=razot_button_clicked)

def dzimsanas_diena():
    jaunais_teksts = ""
    for izveletais in listbox.curselection():
        visi_cilveki[izveletais].svinet_dz_d()
        jaunais_teksts += visi_cilveki[izveletais].info() + "\n"
    result_label.config(text=jaunais_teksts)
    nomainit_sarakstu()


dzimenes_button = ttk.Button(frame, text='Dzimšanas diena!')
dzimenes_button.grid(column=4, row=2, sticky='W', **options)
dzimenes_button.configure(command=dzimsanas_diena)


saturs=tk.Variable(value=tuple(visi_cilveki))

listbox = tk.Listbox(
    root,
    listvariable=saturs,
    height=6,
    selectmode=tk.EXTENDED
)

listbox.grid(row=3, columnspan=3, **options)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=3, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

# start the app
root.mainloop()