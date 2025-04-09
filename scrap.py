import requests
from bs4 import BeautifulSoup
import pandas as pd
list=[]
for i in range(1,50):
    html=requests.get(f'https://books.toscrape.com/catalogue/category/books_1/page-{i}.html').text
    soup=BeautifulSoup(html,'lxml')
    books=soup.find('ol',class_='row').find_all('li',class_="col-xs-6")
    for book in books:
        dict={}
        link='https://books.toscrape.com/catalogue/'+book.find('h3').find('a')['href'].replace('../../','')
        bookhtml=requests.get(link).text
        booksoup=BeautifulSoup(bookhtml,'lxml')
        dict['title']=book.find("h3").text
        dict['discription']=booksoup.find('article',class_='product_page').find_all('p')[3].text
        dict['category']=booksoup.find('ul',class_='breadcrumb').find_all('li')[2].find('a').text
        dict['available']=booksoup.find('article',class_='product_page').find_all('p')[1].text.strip().replace('In stock (','').replace(' available)','')
        dict['img']='https://books.toscrape.com/'+book.find('article',class_="product_pod").find('div',class_='image_container').find('img')['src']
        dict['rating']=book.find('p')['class'][1]
        dict['price']=book.find('div',class_="product_price").find('p',class_="price_color").text
        dict['upc']=booksoup.find('table',class_="table table-striped").find('tr').find('td').text
        list.append(dict)
    print(f'page {i} scrapped')    
df=pd.DataFrame(list)
df.to_excel('books.xlsx',index=False)    
print('done')
