import requests

header_info = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://news.naver.com/'
site = requests.get(url, headers = header_info)
html_data = site.text

count = html_data.count('"cnf_news_title">')
sub_pos1_str = "nclk(event, 'home.editnfimg', '', '')"

for i in range(count):
    pos1 = html_data.find('"cnf_news_title">') + len('"cnf_news_title">')
    html_data = html_data[pos1:]

    pos2 = html_data.find('</strong>')
    extract_data = html_data[:pos2]    

    print(i + 1, extract_data)
    html_data = html_data[pos2 + 1:]

    sub_count = 3
    for j in range(sub_count):
        pos1 = html_data.find(sub_pos1_str) + len(sub_pos1_str) + 2
        html_data = html_data[pos1:]

        pos2 = html_data.find('</a>')
        extract_data = html_data[:pos2]

        html_data = html_data[pos2 + 1:]
        print("   ", f"{j + 1}. {extract_data}\n")


    if (i + 1) % 5 == 0:
        trigger = input("엔터 입력시 추가보기: ")
        if trigger != '':
            print("종료")
            break



