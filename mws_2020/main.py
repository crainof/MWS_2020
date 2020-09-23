# -*- coding: utf-8 -*-

import sys
import tkinter
import scraping
from tkinter import messagebox
from scraping import get_html
from extract_hit_word import extract_hit_word
from calc_info import is_tag, model_value


#ウィンドウ作成
root = tkinter.Tk()
root.title("Personal Information Risk Checker")
root.geometry("360x400")


#ボタンクリック実行

def button_click():
    global cb_name_b
    global cb_address_b,cb_pn_b,cb_cn_b
    global rl_12_b,rl_13_b,rl_21_b,rl_33_b,rl_22_b,rl_31_b
    text=" "


    input_value = input_box.get()

    html,driver = get_html(input_value)
    driver.close()

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


    if cb_name_b.get()==True:
        text+="名前"
    if cb_address_b.get()==True:
        text+="住所"
    if cb_pn_b.get()==True:
        text+="電話番号"
    if cb_cn_b.get()==True:
        text+="会社名"
    if rl_12_b.get()==True:
        text+="A"
    if rl_13_b.get()==True:
        text+="B"
    if rl_33_b.get()==True:
        text+="C"
    if rl_21_b.get()==True:
        text+="D"
    if rl_31_b.get()==True:
        text+="E"
    if rl_22_b.get()==True:
        text+="F"
    messagebox.showinfo(input_value,text)

    


#ラベル作成
page_label = tkinter.Label(text="---2ページ目以降に該当する項目があった場合チェックを入れる---")
page_label.place(x=10, y=80)


#氏名
cb_name_b = tkinter.BooleanVar()
cb_name_b.set(False)
cb_name = tkinter.Checkbutton(root,variable=cb_name_b,text="氏名")
cb_name.place(x=45,y=105)



#住所
cb_address_b = tkinter.BooleanVar()
cb_address_b.set(False)
cb_address = tkinter.Checkbutton(root, variable=cb_address_b, text="住所")
cb_address.place(x=105,y=105)



#電話番号
cb_pn_b = tkinter.BooleanVar()
cb_pn_b.set(False)
cb_pn = tkinter.Checkbutton(root,variable=cb_pn_b,text="電話番号")
cb_pn.place(x=155,y=105)





#会社名
cb_cn_b = tkinter.BooleanVar()
cb_cn_b.set(False)
cb_cn = tkinter.Checkbutton(root,variable=cb_cn_b,text="会社名")
cb_cn.place(x=225,y=105)



#1-2 パスポート、口座番号のみ・クレジットカード番号のみ
rl_12_b = tkinter.BooleanVar()
rl_12_b.set(False)
rl_12 = tkinter.Checkbutton(root,variable=rl_12_b,text="パスポート、口座番号のみ・クレジットカード番号のみ")
rl_12.place(x=10,y=140)




#1-3 口座番号+暗証番号、クレジットカード情報+有効期限
rl_13_b = tkinter.BooleanVar()
rl_13_b.set(False)
rl_13 = tkinter.Checkbutton(root,variable=rl_13_b,text="口座番号+暗証番号、クレジットカード情報+有効期限")
rl_13.place(x=10,y=180)



#2-1 身体・知的障がい情報、学歴、試験得点、趣味・特技、国籍
rl_21_b = tkinter.BooleanVar()
rl_21_b.set(False)
rl_21 = tkinter.Checkbutton(root,variable=rl_21_b,text="身体・知的障がい情報、学歴、試験得点、趣味・特技、国籍")
rl_21.place(x=10,y=220)


#3-3 犯罪歴、前科前歴、与信ブラックリスト
rl_33_b = tkinter.BooleanVar()
rl_33_b.set(False)
rl_33 = tkinter.Checkbutton(root,variable=rl_33_b,text="犯罪歴、前科前歴、与信ブラックリスト")
rl_33.place(x=10,y=260)



#2-2 年収・年収区分、資産、残高、所得、給与・賞与額、借入、借金
rl_22_b = tkinter.BooleanVar()
rl_22_b.set(False)
rl_22 = tkinter.Checkbutton(root,variable=rl_22_b,text="年収・年収区分、資産、残高、所得、給与・賞与額、借入、借金")
rl_22.place(x=10,y=300)



#3-1 精神障害情報、介護度、政治的項目、病状
rl_31_b = tkinter.BooleanVar()
rl_31_b.set(False)
rl_31= tkinter.Checkbutton(root,variable=rl_31_b,text="精神障害情報、介護度、政治的項目、病状")
rl_31.place(x=10,y=340)



#入力欄の作成
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=50)

#ラベル作成
input_label = tkinter.Label(text="Input URL")
input_label.place(x=10, y=20)

#ボタン作成
button = tkinter.Button(text="Analyze",command=button_click)
button.place(x=270, y=45)

#ウィンドウの描画
root.mainloop()