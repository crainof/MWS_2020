import subprocess
import re
import tag_list

# htmlのtagをそれぞれlistに保存および表示
# 入力: htmlの文字列
# 出力: なし
def print_tag():
    splited_html = re.findall(r"<.+>.+<.+>", curl_result) #タグごとの情報にスプリット
    for search_html in splited_html:
        print(search_html)

# htmlファイルからtag_listの単語に一致した単語を抽出し、カウントする
# 入力: htmlの文字列
# 出力: 辞書(tag_listの単語, カウント数)
# 備考: 現状,カウント数は必要ない.
#       入力欄以外の文も検索.
#       名前には名が含まれているため、名もカウント
def extract_hit_word(curl_result):
    hit_word_dict = {}
    for pattern in tag_list.all_tag:
        matched_list = re.findall(pattern, curl_result) # htmlをpatternで検索
        hit_word_dict[pattern] = len(matched_list)
    print(hit_word_dict)

    return hit_word_dict

def main():
    url = "https://grp01.id.rakuten.co.jp/rms/nid/registfwd?service_id=top" #楽天

    curl_result = subprocess.run(["curl ", url],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    curl_result = curl_result.stdout.decode("utf8")
    extract_hit_word(curl_result)

if __name__ == "__main__":
    main()