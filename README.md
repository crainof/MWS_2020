Personal Information Risk Checker
====

## Overview
Webサイトの登録画面における個人の情報漏洩のリスクを通知するアプリケーション

## Description
 
 登録する情報を用いてモデル[(1)]()により、情報漏洩のリスクを確認することができる。

 次の機能が実装されています。
  - 入力されたURLの会員登録ページをスクレイピングし、情報漏洩のリスクを計算する


## Development Environment
- OS:Windows 10
- 言語:Python 3.7
- Visual Studio

## Install
Webスクレイピングのために、seleniumが必要である。

以下のコマンドでインストールする。

`pip install selenium`

さらに、seleniumの起動にはブラウザに応じたWebDriverが必要である。Firefoxを使用するためhttps://github.com/mozilla/geckodriver/releases
からダウンロードし、Driverのフォルダのパスを環境変数に追加する。

## Usage
1. `python3 main.py`を実行、Visual Studioではmain.pyをスタートアップファイルとして設定→`実行
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
