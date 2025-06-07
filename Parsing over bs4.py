from bs4 import BeautifulSoup
import requests

st_accept = 'text/html' # говорим веб-серверу, что хотим получить html, имитируем через бразузер Mozilla на Windows
st_useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.3.823 Yowser/2.5 Safari/537.36'
#формируем хеш заголовкой
headers = {
    'Accept': st_accept,
    'User-Agent': st_useragent
}
#  отправляем запрос с заголовками по нужному адресу
req = requests.get('https://uproger.com/', headers)
# считываем текст HTML- документа
src = req.text
#print(src)

#инициализируем html-код со страницы
soup = BeautifulSoup(src, 'html.parser')
#считываем заголовок страницы

#print(soup)
#print(soup.prettify())
#print(soup.title)

title = soup.title.string
#print(title)

counter_value = soup.find('div', class_= "post-views content-post post-8146 entry-meta")
#print(counter_value.text)

for count in soup.find_all('div', class_='post-views'):
    print(count.text)