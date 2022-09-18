import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import pandas as pd
import openpyxl

import my_func as mf
import my_graph as mgc

def startOperation(filename):
    sheet1 = pd.read_excel(filename, engine='openpyxl', sheet_name = 0)
    sheet2 = pd.read_excel(filename, engine='openpyxl', sheet_name = 1)

    attr_1 = ["Position number", "Index #", "First name", "Last name", "Current position level", "s/m preference 1", "s/m preference 2", "s/m preference 3", "HM recommended", "HM recommended.1", "HM recommended.2", "HM recommended.3", "HM recommended.4", "Scoring system (total)", "Division"]
    apply_data = sheet1[attr_1][:30]

    attr_2 = ["Position number", "Duty Station", "Level"]
    pos_data = sheet2[attr_2]

    pos2idx = mf.mk_pos2idx(apply_data)
    idx2pos = mf.to_idx2pos(pos2idx)

    mg = mgc.Graph(len(pos2idx), idx2pos, len(apply_data))
    mf.init_graph(mg, apply_data, pos2idx)
    mg.find_max_score_cycles()
    # mg.printResult()
    mg.saveExcel()

def selectFile():
    filetypes = (('text files', '*.xlsx'),)

    filename = fd.askopenfilename(
        title='Select a file',
        filetypes=filetypes
    )

    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )

    startOperation(filename)

def initWindow(window):
    window.title('Staff Mobility')
    window.resizable(False, False)
    window.geometry('300x150')

    openButton = tk.Button(
        window,
        text='Select a file',
        command=selectFile
    )

    openButton.pack(expand=True)



filename = ''
window = tk.Tk()
initWindow(window)
window.mainloop()