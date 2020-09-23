import tag_list

#ful_name = ["名前","氏名","お名前","フルネーム","Full Name","おなまえ"]#氏名
#fst_name = ["First Name","名"]#名
#lst_name = ["Last Name","姓"]#姓
#red_name = ["ふりがな","フリガナ","カナ氏名"]#ふりがな
#mail_add = ["メールアドレス","Email","E-mail"]#メールアドレス
#paswd = ["パスワード","Password"]#パスワード
#usrid = ["ユーザID","ID","ユーザーネーム","Username"]#ユーザID
#country=["Country","Region","国","地域"]#国
#company=["Company","お勤め先"]#会社名
#gender =["性","性別"]#性別
#birth = ["生年月日","誕生日"] #生年月日
#tel = ["電話番号","連絡先"] #電話番号
#addr = ["お住まい","住所","都道府県","市区群", "町村"] #住所
#addr_area =["お住いの地域"] #地方区分 
#post_code = ["郵便番号"] #郵便番号
#card = ["クレジットカード"] #クレジットカード
#school=["学校種別","学校名","卒業"] #学歴

# 最大値を計算
def calc_max_score():
    score = 500 * (10**2 + 5**2) * 6 * 2 #基礎情報価値×機微情報度×本人特定容易度×社会的責任度
    # print(score)
    return score

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

    #空のリストが渡された時
    if (len(l)== 0):
        con["score"] = "-"
        con["money"] = 0
        con["detail"] = []
        con["model_par"] = model
        return con

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
        elif (tag =="国") or (tag == "学歴") or (tag == "a(パスポート、口座番号のみ・クレジットカード番号のみ)"):
            y=1
        elif (tag == "b(口座番号+暗証番号、クレジットカード情報+有効期限)"):
            y = 2
        elif tag == "c(身体・知的障がい情報、学歴、試験得点、趣味・特技、国籍)":
            x = 1
        elif tag == "d(犯罪歴、前科前歴、与信ブラックリスト)":
            x = 2
            y = 2
        elif tag == "e(年収・年収区分、資産、残高、所得、給与・賞与額、借入、借金)":
            x = 1
            y = 1
        elif tag == "f(精神障害情報、介護度、政治的項目、病状)":
            x = 2
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
    
    max_score = calc_max_score()
    score_threshold_list = []

    # 最大値から4つの閾値を求める
    score_threshold = 0
    for i in range(4):
        score_threshold += (max_score/4)
        score_threshold_list.append(score_threshold)
    # print(score_threshold_list)

    #金額計算
    money = 500 * tmp_ki * tmp_to * tmp_sy

    #score判定
    if money >= score_threshold_list[2]:
        score = "S"
    elif (money < score_threshold_list[2]) and (money >= score_threshold_list[1]):
        score = "A"
    elif (money < score_threshold_list[1]) and (money >= score_threshold_list[0]):
        score = "B"
    else:
        score = "C"
    con["score"] = score

    con["money"] = money
    con["detail"] = l
    con["model_par"] = model
    return con

#抽出されたタグ一覧のdictからlistを抜き出す

def is_tag(d):
    l = []
    for key,v in d.items():
        if(v==0):
            continue

        #氏名
        for item in tag_list.ful_name:
            if(key == item):
                l.append("氏名")
        #名
        if(key == "First Name" or key == "名"):
            l.append("名")
        #姓
        if(key == "Last Name" or key == "姓"):
            l.append("姓")
        #ふりがな
        if(key == "ふりがな" or key == "フリガナ" or key == "カナ氏名"):
            l.append("ふりがな")
        #メールアドレス
        if(key == "メールアドレス" or key == "Email" or key == "E-mail"):
            l.append("メールアドレス")
        #ユーザID
        if(key == "ユーザID" or key == "ID" or key == "ユーザーネーム" or key == "Username"):
            l.append("ユーザID")
        #国
        if(key == "Country" or key == "Region" or key == "国" or key == "地域"):
            l.append("国")
        #会社名
        if(key == "Company" or key == "お勤め先"):
            l.append("会社名")
        #性別
        if(key == "性" or key == "性別"):
            l.append("性別")
        #生年月日
        if(key == "生年月日" or key == "誕生日"):
            l.append("生年月日")
        #電話番号
        if(key == "電話番号" or key == "連絡先"):
            l.append("電話番号")
        #住所
        for item in tag_list.addr:
            if(key == item):
                l.append("住所")
        #地方区分
        for item in tag_list.addr_area:
            if(key == item):
                l.append("地方区分")
        #郵便番号
        if(key == "郵便番号"):
            l.append("郵便番号")
        #クレジットカード
        if(key == "クレジットカード"):
            l.append("クレジットカード")
        #学歴
        for item in tag_list.school:
            if(key == item):
                l.append("クレジットカード")
    return l

# max_score() #最大:750000        

#d = {"名前":4,"クレジットカード":3, "学校名":0, "国":1,"お勤め先":0}

#l = is_tag(d)
#con = model_value(l)
#print(con)