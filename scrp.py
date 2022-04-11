import requests
from bs4 import BeautifulSoup

# セッションを開始
session = requests.session()

# submit時のパラメータ
odds_okasyo_info = {
    "cname":"pw151ou1009202202061120220410Z/52"
}
# action
url = "https://www.jra.go.jp/JRADB/accessO.html"
res = session.post(url, data=odds_okasyo_info)
res.encoding = res.apparent_encoding
res.raise_for_status() # エラーならここで例外を発生させる

soup = BeautifulSoup(res.text,"html.parser")
horse_name = soup.select("#odds_list .horse a")# isloginクラス要素内のaタグ

for i in horse_name:
  print(i.get_text())