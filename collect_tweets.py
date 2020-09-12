from twitter import *
import setting
#import os,sys,time
#import re
#import emoji

#NG words
#ここでタプルに追加した単語（記号）を含むツイートは収集から除外される。
#今回は、URLやHashtag、【定期】のように使われるカッコなどを除外とした。
#check_chara = ('http', '#', '\\', '【', '】')

#Retry MAX
#retry_max = 15
#Retry time
#retry_time = 60

CN = "ツイート収集API" #CONSUMER_NAME
CK = setting.CK
CS = setting.CS

#過去に認証したときのTokenを探す。
TWITTER_CREDS = os.path.expanduser('.credentials')
if not os.path.exists(TWITTER_CREDS):
  #無ければ、OAuthで認証
  oauth_dance(CN, CK, CS, TWITTER_CREDS)
oauth_token, oauth_secret = read_token_file(TWITTER_CREDS)

# Tokenを用いて、Streaming APIで新着ツイートを見つけるstreamと、普通のTwitter APIで'in_reply_to_status_id'を参照するtwitterの2つを用意する。
#stream = TwitterStream(auth=OAuth(oauth_token, oauth_secret, CK, CS))
#twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CK, CS))

#count = 0
#twitter_number = 0

# 正規表現パターンを構築
#emoji_pattern = re.compile("["
#        u"\U0001F600-\U0001F64F"
#        u"\U0001F300-\U0001F5FF"
#        u"\U0001F680-\U0001F6FF"
#        u"\U0001F1E0-\U0001F1FF"
#                           "]+", flags=re.UNICODE)

#def remove_emoji(src_str):
#  return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)


#in_reply_to_status_idから宛先となるツイートを参照する。
#def show(_status):
#  global count
#  global twitter_number
  
#  tf = open('Data/' + str(twitter_number) + '_twitter_data.txt', 'a')
#  for r in range(retry_max):
  #言語が日本語、in_reply_to_status_idが明示されており、禁止単語を含まないツイートの場合
#    if 'in_reply_to_status_id' in _status and not _status['in_reply_to_status_id'] is None and 'text' in _status and check(_status['text']):
#      try:
      #ツイートを参照
#        status=twitter.statuses.show(id=_status['in_reply_to_status_id'])
#      except:
#        time.sleep(retry_time)
#        continue
      #宛先のツイートが日本語、in_reply_to_status_idが明示されており、禁止単語を含まないツイートの場合
#      if 'lang' in _status and _status['lang'] == 'ja' and 'text' in status and check(status['text']):
#        tf.write(remove_emoji(emoji_pattern.sub(r'@emoji', trim(status['text']))))
#        tf.write('\n')
#        tf.write(remove_emoji(emoji_pattern.sub(r'@emoji', trim(_status['text']))))
#        tf.write('\n')
#        count = count + 1
#        if count == 50000:
#          twitter_number = twitter_number + 1
#          count = 0
#        break
#      else:
#        break
#    else:
#      break
#  tf.close()

#改行を適当に置き換える
#def trim(text):
#  return text.replace('\r','-br-').replace('\n','-br-')

#禁止文字のチェックを行う
#def check(text):
#  for char in check_chara:
#    if char in text:
#      return False
#  return True

#def main():
 # while True:
 #   #with open('Data/twitter_data_' + twitter_number + '.txt', 'w') as tf:
 #   #ストリームに接続して適当にツイートを読み出す
 #   statuses = stream.statuses.sample()
 #   for status in statuses:
 #     #参照に送る
 #     show(status)

#if __name__ == '__main__':
#  main()
