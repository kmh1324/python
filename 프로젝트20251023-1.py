import requests

header_info = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://https://news.naver.com/section/105/'
site = requests.get(url, headers = header_info)
html_data = site.text

count = html_data.count('"sa_text_strong">')
saved_news_list = []
category = {"AI": "", "보안": "", "에너지": "", "의료": "", "반도체": "", "기업": ""}

for i in range(count):
    pos1 = html_data.find('"sa_text_strong">') + len('"sa_text_strong">')
    html_data = html_data[pos1:]

    pos2 = html_data.find('</strong>')
    extract_data = html_data[:pos2]    

    saved_news_list[i] = extract_data
    html_data = html_data[pos2 + 1:]

for text in saved_news_list:
    if "AI" or "agi" or "초지능" in text:
        category["AI"] 

