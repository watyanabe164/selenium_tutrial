# 時間を計るライブラリをインポート
import time
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
driver.get('https://www.google.com/')

# 5秒待機する
time.sleep(5)

# ページ内でname属性がqの要素を指定する（検索ボックス）
search_box = driver.find_element(By.NAME,'q')
# 指定した要素（検索ボックス）にChromeDriverと入力する
search_box.send_keys('ChromeDriver')
# フォームを送信する（検索する）
search_box.submit()

# 検索結果のリストを取得する
#search_results = driver.find_elements(By.XPATH, '//div[@class="g"]')
search_results = driver.find_elements(By.CLASS_NAME, "g")

# CSVファイルに書き込む
with open('search_results.csv', mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for result in search_results:
        title = result.find_element(By.TAG_NAME, 'h3').text
        url = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
        writer.writerow([title, url])

# 次のページへのリンクを特定する
next_page_link = driver.find_element(By.XPATH, "//a[@id='pnnext']")

# リンクをクリックする
next_page_link.click()

search_results = driver.find_elements(By.CLASS_NAME, 'g')

# CSVファイルに書き込む
with open('search_results.csv', mode='a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for result in search_results:
        title = result.find_element(By.TAG_NAME, 'h3').text
        url = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
        writer.writerow([title, url])

# 画面を閉じる
driver.quit()