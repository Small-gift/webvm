from bs4 import BeautifulSoup
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edge/124.0.0.0"
}
for start_num in range(1,50,1):
    response = requests.get(f"http://books.toscrape.com/catalogue/page-{start_num}.html",headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"html.parser")
    all_ps = soup.findAll("p",attrs={"class": "price_color"})
    for ps in all_ps:
        ps_string = ps.string
        print(ps_string[1:])
print(response)            