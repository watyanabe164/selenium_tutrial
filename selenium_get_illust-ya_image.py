# 時間を計るライブラリをインポート
import time
import requests
# WebDriverライブラリをインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# ChromeのWebDriverライブラリをインポート
import chromedriver_binary
import csv

# Chromeを指定する
driver = webdriver.Chrome()
# Chromeを開いてGoogleにアクセスする
driver.get('https://www.irasutoya.com/search/label/%E8%81%B7%E6%A5%AD')

# 5秒待機する
time.sleep(5)

# 画像一覧のリストを取得する
search_results = driver.find_elements(By.CLASS_NAME, "boxim")

# 画像リストの一覧CSVファイルに書き込んで、サムネイル画像をDLする
with open('search_results.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for result in search_results:
        title = result.find_element(By.TAG_NAME, 'img').get_attribute('alt')
        url = result.find_element(By.TAG_NAME, 'img').get_attribute('src')
        writer.writerow([title, url])

        # 画像のファイル名を取得する
        img_name = None
        if url:
            img_name = url.split('/')[-1]
        # 画像をダウンロードする
        response = None
        if url:
            response = requests.get(url)
        # ファイルを保存する
        if img_name and response:
            with open(img_name, 'wb') as f:
                f.write(response.content)

# 画面を閉じる
driver.quit()