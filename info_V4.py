from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from requests_html import AsyncHTMLSession
from requests import Request, Session

idno = ["1002600056626", "1003602004112", "1009600017846", "1013606000397"]

url = "https://www.infobase.md/ro/search?page=1&q="

def acces():
    global r
    for x in idno:
        r = requests.get(url + x)
        p = url + x
        print (p,'\n')
        # time.sleep(5)
        parser()
        print ('end====================')



def parser():
    global r
    # html_code = r.text
    try:
        html_code = r.content
        # html_code = driver.page_source 
        soup = BeautifulSoup(html_code, "lxml")

        x = soup.select("title")
        c = soup.find(class_="MuiTypography-root MuiTypography-h2")
        r = soup.find(class_="MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 MuiGrid-item MuiGrid-grid-xs-12")
        f = soup.find('a')
        p = soup.a

        h = soup.select('a[href]')
        # print(soup.get_text())
        print(x)
        print(r)
        print(c)
        print(h)
        print(f)
        print(p)
    except Exception as e:
        print(e)
    finally:
        pass

def second():
    pass



if __name__ == "__main__":
    
    try:
        acces()
        # parser()
    except Exception as e:
        print(e)
    finally:
        print('end')


