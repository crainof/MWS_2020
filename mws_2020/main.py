# -*- coding: utf-8 -*-

import sys
import tkinter
from tkinter import messagebox
from scraping import get_html
from extract_hit_word import extract_hit_word
from calc_info import is_tag, model_value

#チェックボックスに使うglobal変数
global cb_name_b
global cb_address_b,cb_pn_b,cb_cn_b
global rl_12_b,rl_13_b,rl_21_b,rl_33_b,rl_22_b,rl_31_b

#ウィンドウ作成
root = tkinter.Tk()
root.title("Personal Information Risk Checker")
root.geometry("380x420")

#チェックボックスに対する評価
def add_item():
    l = []
    if cb_name_b.get()==True:
        l.append("氏名")
    if cb_address_b.get()==True:
        l.append("住所")
    if cb_pn_b.get()==True:
        l.append("電話番号")
    if cb_cn_b.get()==True:
        l.append("会社名")
    if rl_12_b.get()==True:
        l.append("a(パスポート、口座番号のみ・クレジットカード番号のみ)")
    if rl_13_b.get()==True:
        l.append("b(口座番号+暗証番号、クレジットカード情報+有効期限)")
    if rl_33_b.get()==True:
        l.append("d(犯罪歴、前科前歴、与信ブラックリスト)")
    if rl_21_b.get()==True:
        l.append("c(身体・知的障がい情報、学歴、試験得点、趣味・特技、国籍)")
    if rl_31_b.get()==True:
        l.append("f(精神障害情報、介護度、政治的項目、病状)")
    if rl_22_b.get()==True:
        l.append("e(年収・年収区分、資産、残高、所得、給与・賞与額、借入、借金)")
    return l


#ボタンクリック実行

def button_click():

    text=" "


    input_value = input_box.get()

    html,driver = get_html(input_value)
    driver.close()

    print(html)
    hit_word_dict = extract_hit_word(html)
    score_dict = model_value(is_tag(hit_word_dict))
    word_list = is_tag(hit_word_dict)
    word_list.extend(add_item())
    print(word_list)
    score_dict = model_value(word_list)
    

    print(score_dict)
    connected_detail = ""
    connected_score =""
    for i, detail in enumerate(score_dict["detail"]):
        if not(i == (len(score_dict["detail"])-1)):
            connected_detail += detail + ", "
        else:
            connected_detail += detail

    for item, score in score_dict["model_par"].items():
        if(item=="basic"):
            connected_score+="\n基礎情報価値："
         
        if(item=="kibi"):
            connected_score+="\n機微情報度："
        if(item=="tokutei"):
            connected_score+="\n本人特定容易度："

        if(item=="syakai"):
            connected_score+="\n社会的責任度："
        
        connected_score += str(score)+" "
        



    messagebox.showinfo(input_value,"リスク：" +  score_dict["score"] +"\n"+ "\n詳細：" + connected_detail + "\n\nスコア："+str(score_dict["money"])+"\n"+connected_score)

    #if cb_name_b.get()==True:
    #    text+="名前"
    #if cb_address_b.get()==True:
    #    text+="住所"
    #if cb_pn_b.get()==True:
    #    text+="電話番号"
    #if cb_cn_b.get()==True:
    #    text+="会社名"
    #if rl_12_b.get()==True:
    #    l.append("a(パスポート、口座番号のみ・クレジットカード番号のみ)")
    #if rl_13_b.get()==True:
    #    l.append("a(パスポート、口座番号のみ・クレジットカード番号のみ)")
    #if rl_33_b.get()==True:
    #    l.append("c(身体・知的障がい情報、学歴、試験得点、趣味・特技、国籍)")
    #if rl_21_b.get()==True:
    #    l.append("c(身体・知的障がい情報、学歴、試験得点、趣味・特技、国籍)")
    #if rl_31_b.get()==True:
    #    l.append("c(身体・知的障がい情報、学歴、試験得点、趣味・特技、国籍)")
    #if rl_22_b.get()==True:
    #    l.append("c(身体・知的障がい情報、学歴、試験得点、趣味・特技、国籍)")
    #messagebox.showinfo(input_value,text)

def only_check():
    score_dict = model_value(add_item())
    print(score_dict)
    connected_detail = ""
    connected_score =""
    for i, detail in enumerate(score_dict["detail"]):
        if not(i == (len(score_dict["detail"])-1)):
            connected_detail += detail + ", "
        else:
            connected_detail += detail

    for item, score in score_dict["model_par"].items():
        if(item=="basic"):
            connected_score+="\n基礎情報価値："
         
        if(item=="kibi"):
            connected_score+="\n機微情報度："
        if(item=="tokutei"):
            connected_score+="\n本人特定容易度："

        if(item=="syakai"):
            connected_score+="\n社会的責任度："
        
        connected_score += str(score)+" "
        

    messagebox.showinfo("評価値","リスク：" +  score_dict["score"] +"\n"+ "\n詳細：" + connected_detail + "\n\nスコア："+str(score_dict["money"])+"\n"+connected_score)

    

    





#ラベル作成
page_label = tkinter.Label(text="---2ページ目以降に該当する項目があった場合チェックを入れる---")
page_label.place(x=10, y=80)

page_label = tkinter.Label(text="---チェックボックスの項目だけで評価---")
page_label.place(x=70, y=382)


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
rl_12 = tkinter.Checkbutton(root,variable=rl_12_b,text="a(パスポート、口座番号のみ・クレジットカード番号のみ)")
rl_12.place(x=10,y=140)




#1-3 口座番号+暗証番号、クレジットカード情報+有効期限
rl_13_b = tkinter.BooleanVar()
rl_13_b.set(False)
rl_13 = tkinter.Checkbutton(root,variable=rl_13_b,text="b(口座番号+暗証番号、クレジットカード情報+有効期限)")
rl_13.place(x=10,y=180)



#2-1 身体・知的障がい情報、学歴、試験得点、趣味・特技、国籍
rl_21_b = tkinter.BooleanVar()
rl_21_b.set(False)
rl_21 = tkinter.Checkbutton(root,variable=rl_21_b,text="c(身体・知的障がい情報、学歴、試験得点、趣味・特技、国籍)")
rl_21.place(x=10,y=220)


#3-3 犯罪歴、前科前歴、与信ブラックリスト
rl_33_b = tkinter.BooleanVar()
rl_33_b.set(False)
rl_33 = tkinter.Checkbutton(root,variable=rl_33_b,text="d(犯罪歴、前科前歴、与信ブラックリスト)")
rl_33.place(x=10,y=260)



#2-2 年収・年収区分、資産、残高、所得、給与・賞与額、借入、借金
rl_22_b = tkinter.BooleanVar()
rl_22_b.set(False)
rl_22 = tkinter.Checkbutton(root,variable=rl_22_b,text="e(年収・年収区分、資産、残高、所得、給与・賞与額、借入、借金)")
rl_22.place(x=10,y=300)



#3-1 精神障害情報、介護度、政治的項目、病状
rl_31_b = tkinter.BooleanVar()
rl_31_b.set(False)
rl_31= tkinter.Checkbutton(root,variable=rl_31_b,text="f(精神障害情報、介護度、政治的項目、病状)")
rl_31.place(x=10,y=340)

#チェックボックスだけで評価するボタン
button = tkinter.Button(text="Evaluate",command=only_check)
button.place(x=10,y=380)

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