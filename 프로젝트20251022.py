import requests

header_info = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1: WOW64: Trident/7.0: rv:11.0) like Gecko'}

url = 'https://news.naver.com/'
site = requests.get(url, headers = header_info)
html_data = site.text

count = html_data.count('"cnf_news_title">')

for i in range(count):
    pos1 = html_data.find('"cnf_news_title">') + len('"cnf_news_title">')
    html_data = html_data[pos1:]

    pos2 = html_data.find('</strong>')
    extract_data = html_data[:pos2]    

    print(i + 1, extract_data)

    sub_count = 3
    for j in range(sub_count):
        pos1 = html_data.find('"cnf_news_title">') + len('"cnf_news_title">')
        html_data = html_data[pos1:]

        pos2 = html_data.find('</strong>')
        extract_data = html_data[:pos2]

        html_data = html_data[pos2 + 1:]

    html_data = html_data[pos2 + 1:]
