from selenium import webdriver # Selenium WebDriverのインポート

def get_html(url):
    '''
    Overview: 与えられたurlからそのページのhtmlソースを返す関数
    params:
        url: URL(文字列)
    return:
        html: htmlソース(文字列)

    '''
    driver = webdriver.Firefox() # FirefoxのWebDriverの読み込み
    driver.get(url)              # Firefoxでurlのページを開く
    html = driver.page_source
    return html

if __name__ == '__main__':
    test_url = "https://www.shopjapan.co.jp/shop/customer/entry"
    #test_url = "https://www.uniqlo.com/jp/ja/account/registry"
    html = get_html(test_url)
    print(html)