# -*- coding: utf-8 -*-

import tkinter
from tkinter import messagebox
from scraping import get_html
from extract_hit_word import extract_hit_word
from calc_info import is_tag, model_value

#ボタンクリック実行

def button_click():

    input_value = input_box.get()
    html = get_html(input_value)
    print(html)
    hit_word_dict = extract_hit_word(html)
    score_dict = model_value(is_tag(hit_word_dict))
    print(score_dict)
    connected_detail = ""
    for i, detail in enumerate(score_dict["detail"]):
        if not(i == (len(score_dict["detail"])-1)):
            connected_detail += detail + ","
        else:
            connected_detail += detail

    messagebox.showinfo(input_value,"リスク：" +  score_dict["score"] + "\n 詳細：" + connected_detail + "\n")


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