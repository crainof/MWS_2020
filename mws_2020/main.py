# -*- coding: utf-8 -*-

import tkinter
from tkinter import messagebox

#ボタンクリック実行

def button_click():

    input_value = input_box.get()
    messagebox.showinfo(input_value,"リスク：〇〇\n 詳細：○○　\n")


#ウィンドウ作成
root = tkinter.Tk()
root.title("Personal Information Risk Checker")
root.geometry("360x120")


#入力欄の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=50)

#ラベル作成
input_label = tkinter.Label(text="Input URL")
input_label.place(x=10, y=20)

#ボタン作成
button = tkinter.Button(text="Analyze",command=button_click)
button.place(x=10, y=80)

#ウィンドウの描画
root.mainloop()