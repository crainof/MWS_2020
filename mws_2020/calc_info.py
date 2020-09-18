
#model_value()
#詳細
#   JNSAのモデルに基づいて計算するものです
#
#引数
#   l:代表タグが入ったリスト
#     #氏名,#名,#姓,#ふりがな, #メールアドレス,#パスワード, #ユーザID, 
#     #国, #会社名, #性別,#生年月日, #電話番号, #住所, 
#     #地方区分, #郵便番号, クレジットカード, 学歴
#
#返り値
#   con = {"score": "S-C",
#          "money": int(120000), #
#            "detail": ["名前",...],#入力を求められる項目
#       "model_par": {"basic": 500,... } }   


def model_value(l):

    con ={}
    model ={}

    #基礎情報価値
    model["basic"]=500

    #その他パラメータ
    x = 0
    y = 0
    flag_nam = 0
    flag_add = 0
    flag_tel = 0
    flag_com = 0


    for tag in l:
        if tag == "クレジットカード":
            x=1
        elif (tag =="国") or (tag == "学歴"):
            y=1
        elif tag== "氏名":
            flag_nam = 1
        elif tag == "住所":
            flag_add = 1
        elif tag == "電話番号":
            flag_tel = 1
        elif tag == "会社名":
            flag_com = 1

    #機微情報度
    tmp_ki = 10**x + 5**y
    model["kibi"]=tmp_ki

    #本人特定用意度
    tmp_to = 1
    if (flag_nam == 1):
        tmp_to = 3
    elif (flag_add==1)and(flag_tel==1):
        tmp_to = 3
    elif (flag_nam == 1)and(flag_add ==1):
        tmp_to = 6
    model["tokutei"]=tmp_to

    #社会責任度
    tmp_sy = 1
    if (flag_com==1):
        tmp_sy = 2
    model["syakai"] = tmp_sy
    
    #金額計算
    money = 500 * tmp_ki * tmp_to * tmp_sy

    #score判定
    if money >=15000:
        score = "S"
    elif (money <15000) and (money >= 12000):
        score = "A"
    elif (money <12000) and (money >= 6000):
        score = "B"
    else:
        score = "C"
    con["score"] = score

    con["money"] = money
    con["detail"] = l
    con["model_par"] = model
    return con

def is_tag(d):




#d = ["氏名","名","会社名","国","性別","郵便番号"]
#con = model_value(d)
#print(con)