Personal Information Risk Checker
====

Overview
webサイトの登録画面における個人の情報漏洩のリスクを通知するアプリケーション

## Description
 近年、不正アクセスによる個人情報の漏洩事件が多発​している。
 過去5年間の上場企業による件数は平均して80件以上発生し(http://www.tsr-net.co.jp/news/analysis/20200123_01.html )、
 2018年には漏洩人数が約560万人、想定損害賠償総額は約2,680億円となっている(​https://www.jnsa.org/result/incident/2018.html )。
 
 そのような背景の一方で、アカウント登録を行うサービスやWebアプリは数多と存在している。
 アカウント登録の時、漏洩事件が多発しているにも関わらず、
 ユーザーは自身が登録する情報が漏洩した時のリスクを知る機会が少ない。
 そこで、漏洩した時のリスクを定性的に測定するために、このスクリプトが活用できる。

 登録する情報を用いて計算を行うモデルにより、情報漏洩のリスクを改めて確認することができる。

## Demo
1. main.pyを実行
2. 入力フォームが表示される

<img src = "https://user-images.githubusercontent.com/58422123/94141929-750d7b00-fea8-11ea-923e-da3176f9092c.png" width = 40%>

3. input URLに検証したいURLを入力する
4. チェックボックスを入力する
5. 実行ボタンを押す
- Analyze を押す　-> URLのサイトの情報とチェックボックスの情報の両方を加えて評価
- Evalute を押す　-> チェックボックスの情報のみで評価
6. 結果が出力される

<img src = "https://user-images.githubusercontent.com/58422123/94141930-763ea800-fea8-11ea-967a-f1bc7936cd2f.png" width = 80%>

	- リスク	: S,A,B,C の4段階評価 
	- 詳細		: URLから抽出された項目とチェックボックスで選択した項目
	- スコア	: モデルにより算出された値
	- 基礎情報価値	: 500(一定)
	- 機微情報度	: 項目が経済的、精神的に重要であるほど大きい
	- 本人特定容易度: 個人が特定できるほど大きい 
	- 社会的責任度	: 勤務先情報を登録する場合 2

## Development Environment
- OS:Windows
- 言語:Python 3.7
- Visual Studio

## Usage
- Visual Studio: main.pyをスタートアップファイルとして設定→`実行
- その他:`python3 main.py`

## Install
Webスクレイピングのために、seleniumをが必要である。

以下のコマンドでインストールする。

`pip install selenium`

さらに、seleniumの起動にはブラウザに応じたWebDriverが必要である。Firefoxを使用したためhttps://github.com/mozilla/geckodriver/releases
からダウンロードし、Driverのフォルダのパスを環境変数に追加する。
