# MWS_2020

# 環境
- Python 3.7

# インストール
- Twitter API関連

```
pip install twitter`(sixohsix) 
pip install emoji(絵文字除去のため)
```

# 問題点
- Twitter API
  - 180リクエスト/15分
  - 過去7日間分　[バグが多いみたいだけど，頑張れば過去7日以前も取得できるらしい．](https://qiita.com/jinto/items/60f23a6b5d9603836dab)
  - 自分のアカウントに紐づいていると凍結の可能性
  - 同じツイートが抽出されている？

# 留意点
  - 使用する場合はsetting.pyでkeyやtokenなどを記入してください
