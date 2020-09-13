import os,time,re
import setting
import emoji

from twitter import *

# settingファイルからapi keyなどを読み込む
CN = "ツイート収集API"
CK = setting.CONSUMER_KEY
CS = setting.CONSUMER_SECRET

TWITTER_CREDS = os.path.expanduser('.credentials') #過去に認証したときの情報
if not os.path.exists(TWITTER_CREDS):
  oauth_dance(CN, CK, CS, TWITTER_CREDS)
oauth_token, oauth_secret = read_token_file(TWITTER_CREDS)

twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CK, CS)) # 指定したkeywordでtweetを取得

#NG words
#ここでタプルに追加した単語（記号）を含むツイートは収集から除外される。
#今回は、URLやHashtag、【定期】のように使われるカッコなどを除外とした。
check_chara = ('http', '\\', '【', '】')

os.makedirs("TweetData", exist_ok=True)

# 正規表現パターンを構築
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
                           "]+", flags=re.UNICODE)

#禁止文字のチェックを行う
def check(text):
  for char in check_chara:
    if char in text:
      return False
  return True

#絵文字を除去
def remove_emoji(src_str):
  return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)

#改行を適当に置き換える
def trim(text):
  return text.replace('\r','-br-').replace('\n','-br-')

def show(_status, _tf):
  #禁止単語を含まないツイートの場合
  if check(_status['text']):
    _tf.write(remove_emoji(emoji_pattern.sub(r'@emoji', trim(_status['text']))))
    _tf.write('\n')

def main():
  keyword = "#バグ"
  tweet_data_list = os.listdir("TweetData")
  list_len = len(tweet_data_list)

  while True:
    with open("TweetData/" + str(list_len + 1) + ".txt", "w") as tf: #必ず新ファイルに書き込む
      try:
        tweet = twitter.search.tweets(q=keyword, lang="ja") #キーワードを含む，かつ，日本語
        for status in tweet["statuses"]:
          show(status, tf)
        break
      except TwitterHTTPError as twitter_http_error:
        if twitter_http_error.response_data["errors"][0]["code"] == 88: #15分間に180リクエスト以上要求した場合制限がかかる
          time.sleep(60 * 15) #15分待つ
      except Exception as e:
        print("新しいエラー")
        print(e)
        break

if __name__ == '__main__':
  main()
