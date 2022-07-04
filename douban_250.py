import requests
from bs4 import BeautifulSoup
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
f = open("data_top250.csv", mode="w", encoding="utf-8")
for i in range(0, 250, 25):
    url = "https://movie.douban.com/top250?start=" + str(i) +"&filter="
    resp = requests.get(url, headers=header)
    page_content = resp.text
    soup = BeautifulSoup(page_content)
    title_part = soup.select(".grid_view>li")
    for each in title_part:
        title = each.find(class_='title').string
        rating_num = each.find(class_='rating_num').string
        voting_num = each.find(string=re.compile("\d+人评价"))
        print(title,rating_num,voting_num)
 