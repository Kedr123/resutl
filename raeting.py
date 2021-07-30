import requests
import datetime
from bs4 import BeautifulSoup as BS

def reiting(a):

    if (a==1): r = requests.get("https://rgsu.net/abitur/ratings/pofamilnye-spiski.html?action=index&admin_mode=&level=&srchPat%5B0%5D=Москва&srchPat%5B5%5D=На+общих+основаниях&srchPat%5B1%5D=Программная+инженерия+%28бакалавриат%29&srchPat%5B7%5D=Разработка+корпоративной+информационной+системы&srchPat%5B2%5D=Очная&srchPat%5B3%5D=Федеральный+бюджет")
    if (a==2): r = requests.get("https://rgsu.net/abitur/ratings/pofamilnye-spiski.html?action=index&admin_mode=&level=&srchPat%5B0%5D=Москва&srchPat%5B5%5D=На+общих+основаниях&srchPat%5B1%5D=Информационные+системы+и+технологии+%28бакалавриат%29&srchPat%5B7%5D=Информационные+системы+и+технологии+в+экономической+сфере&srchPat%5B2%5D=Очная&srchPat%5B3%5D=Федеральный+бюджет")
    if (a==3): r = requests.get("https://rgsu.net/abitur/ratings/pofamilnye-spiski.html?action=index&admin_mode=&level=&srchPat%5B0%5D=Москва&srchPat%5B5%5D=На+общих+основаниях&srchPat%5B1%5D=Информатика+и+вычислительная+техника+%28бакалавриат%29&srchPat%5B7%5D=Программное+обеспечение+средств+вычислительной+техники+и+автоматизированных+систем&srchPat%5B2%5D=Очная&srchPat%5B3%5D=Федеральный+бюджет")
    if (a==4): r = requests.get("https://rgsu.net/abitur/ratings/pofamilnye-spiski.html?action=index&admin_mode=&level=&srchPat%5B0%5D=Москва&srchPat%5B5%5D=На+общих+основаниях&srchPat%5B1%5D=Информационная+безопасность+%28бакалавриат%29&srchPat%5B7%5D=Организация+и+технология+защиты+информации&srchPat%5B2%5D=Очная&srchPat%5B3%5D=Федеральный+бюджет")
    html = BS(r.content, 'html.parser')

    arr_itog=[]
    arr_string=[]

    for el in html.select('.ratings > tbody > tr'):
        for el2 in el.select('td'):
            arr_string.append(el2.text)
        arr_itog.append(arr_string)
        arr_string=[]


    count=0
    count_ige=0
    count_VI=0
    cvota=0
    arr_itog.sort(key = lambda x: x[2])
    for i in arr_itog:
        if(int(i[2])>=239 ):
            count +=1
            print(i)
            
        if(int(i[2])>=239 and i[5]=='В формате вуза'):
            count_VI +=1

        if(int(i[2])>=239 and i[5]=='ЕГЭ'):
            count_ige +=1
        if(i[8]!='На общих основаниях'):
            print(i)
            cvota +=1
    
            
        
    print("Всего : "+str(count))
    print("ЕГЭ : "+str(count_ige))
    print("В формате вуза : "+str(count_VI))
    print("Квота : "+str(cvota))
    data = datetime.datetime.now()
    print("Дата : "+str(data) )

reiting(1)

