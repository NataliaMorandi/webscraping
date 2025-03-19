import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com.br/FRISKIES-Filhotes-Carne-Molho-85g/dp/B08T1MQRG4"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
page = requests.get(url, headers=headers)

if page.status_code == 200:
    #print(page.text)
    #print(page.status_code)
    soup = BeautifulSoup(page.text, features="html.parser")
    div_preco = soup.find("div", class_="a-spacing-top-mini")
    print(f"div_preco", div_preco)
    if div_preco:
        span_preco = div_preco.find("span", class_="a-offscreen")
        print(f"span_preco", span_preco)
        if span_preco:
            print("Preço encontrado:", span_preco.text)
        else:
            print("Preço não encontrado dentro da div.")
    else:
        print("Div do preço não encontrada.")
else: 
    print("HTTP error", page.status_code)


#soup = BeautifulSoup(page.text, features="html.parser")

#print(soup.find_all("span", class_="a-offscreen"))

#print(soup)

