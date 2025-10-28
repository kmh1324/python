import requests

header_info = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://news.naver.com/section/105/'
site = requests.get(url, headers=header_info)
html_data = site.text

count = html_data.count('"sa_text_strong">')
saved_news_list = []
category = {"AI": ["AI", "AGI", "초지능", "챗GPT", "GPU", "양자"]\
            , "보안": ["해킹", "블록체인", "정보보호", "정보"]\
            , "에너지": ["에너지", "전력", "원전", "기후", "온실", "가스"]\
            , "반도체": ["HBM", "메모리", "웨이퍼", "고집적", "디스플레이", "칩"]\
            , "기업": ["카카오", "네이버", "삼성", "구글", "AWS", "AMD", "엔비디아"]
            }
topic_content = {"AI": [], "보안": [], "에너지": [], "반도체": [], "기업": []}

for i in range(count):
    pos1 = html_data.find('"sa_text_strong">') + len('"sa_text_strong">')
    html_data = html_data[pos1:]

    pos2 = html_data.find('</strong>')
    extract_data = html_data[:pos2]

    saved_news_list.append(extract_data)
    html_data = html_data[pos2 + 1:]

for content in saved_news_list:
    for keyword in category["AI"]:
        if keyword in content and content not in topic_content:
            topic_content["AI"].append(content)
            
    for keyword in category["보안"]:
        if keyword in content and content not in topic_content:
            topic_content["보안"].append(content)
        
    for keyword in category["에너지"]:
        if keyword in content and content not in topic_content:
            topic_content["에너지"].append(content)
        
    for keyword in category["반도체"]:
        if keyword in content and content not in topic_content:
            topic_content["반도체"].append(content)
        
    for keyword in category["기업"]:
        if keyword in content and content not in topic_content:
            topic_content["기업"].append(content)

flag = 1
while flag:
    choice = input("분야를 선택하세요 (1.AI  2.보안  3.에너지  4.반도체  5.기업 소식  0.종료 [숫자입력]): ")
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
    for content in topic_content[topic]:
        print(f"{count}. {content}")
        if count % 5 == 0:
            trigger = input("엔터 입력시 추가보기(다른 키 누르면 종료): ")
            if trigger != '':
                print("종료")
                break
        count += 1
        if count >= len([topic_content]):
            print("내용이 끝났습니다.")
            break

    flag = int(input("더 찾으시겠습니까?(1.yes  0.no [숫자입력]): "))
    
