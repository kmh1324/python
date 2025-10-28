import requests

header_info = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://news.naver.com/section/105/'
site = requests.get(url, headers = header_info)
html_data = site.text

count = html_data.count('"sa_text_strong">')
saved_news_list = []
category = {"AI": [], "보안": [], "에너지": [], "반도체": [], "기업": []}

for i in range(count):
    pos1 = html_data.find('"sa_text_strong">') + len('"sa_text_strong">')
    html_data = html_data[pos1:]

    pos2 = html_data.find('</strong>')
    extract_data = html_data[:pos2]    

    saved_news_list[i].append(extract_data)
    html_data = html_data[pos2 + 1:]

for content in saved_news_list:
    if "AI" or "agi" or "초지능" or "챗GPT" or "GPU" or "양자" in text:
        category["AI"].append(content)
        
    if "해킹" or "블록체인" or "정보보호" or "정보" in text:
        category["보안"].append(content)
        
    if "에너지"  or "전력" or "원전" or "기후" or "온실" or "가스"  or "LNG" in text:
        category["에너지"].append(content)
        
    if "HBM" or "메모리" or "웨이퍼" or "고집적" or "디스플레이"  or "칩" in text:
        category["반도체"].append(content)
        
    if "카카오" or "네이버" or "삼성" or "구글" or "AWS" or "AMD" or "엔비디아" in text:
        category["기업"].append(content)

flag = 1
while flag:
    choice = input("분야를 선택하세요 \
    (1.AI  2.보안  3.에너지  4.반도체  5.기업 소식  0.종료 [숫자입력]): ")
    topic = ""
    if choice == '1':
        topic = "AI"
    elif choice == '2':
        topic = "보안"
    elif choice == '3':
        topic = "에너지"
    elif choice == '4':
        topic = "반도체"
    elif choice == '5':
        topic = "기업"

    count = 1
    for content in category[topic]:
        print(f"{count}. {category[topic]}")
        count += 1
        if count % 5 == 0:
            trigger = input("엔터 입력시 추가보기: ")
            if trigger != '':
                print("종료")
                break

    flag = input("더 찾으시겠습니까?(1.yes  2.no [숫자입력]): ")
        
    
