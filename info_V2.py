from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import json

search_url = "https://www.infobase.md/ro/search?page=1&q="
driver = webdriver.Firefox(executable_path="../geckodriver")

# enter the program, accesing web, looping it, writing it


def parse_idnos(idno_list):
    try:
        results = []
        for idno in idno_list:
            url = search_url + idno
            driver.get(url)
            print(url)
            clilck_dno()
            time.sleep(1)
            item = parse_individual_page()
            results.append(item)
        save_to_file(results)
    except:
        print("no element 1")
        # no_element()
        pass
    finally:
        pass


# entering link of idno


def clilck_dno():
    try:
        driver.implicitly_wait(10)
        search_engine = driver.find_element(
            By.XPATH, '//*[@id="index"]/div/main/div/div[3]/div[1]/div/div/div/h2/a'
        ).click()
    except:
        print("no element 2")
    finally:
        pass


# parsing web


def parse_individual_page():
    global soup

    html_code = driver.page_source
    soup = BeautifulSoup(html_code, "html.parser")

    try:
        founder_names = []
        director_names = []

        title = soup.select("title")[0]
        fields = soup.find_all(class_="MuiTableCell-root MuiTableCell-body")
        status = fields[3]
        registration_date = fields[5]
        phisical_adres = fields[7]
        jiridic_adres = fields[9]
        angajati = fields[11]

        # founders
        founders_title = soup.find(lambda x: x.text == "Fondatori")
        if founders_title:
            founders_container = founders_title.find_parent(
                class_="MuiPaper-root MuiCard-root MuiPaper-elevation1 MuiPaper-rounded"
            )
            founders_list = founders_container.find_all(
                "a",
                class_="MuiButtonBase-root MuiListItem-root MuiListItem-dense MuiListItem-gutters MuiListItem-button",
            )
            for founder in founders_list:
                founder_names.append(founder.text)

        # directors
        directors_title = soup.find(lambda x: x.text == "Directori")
        if directors_title:
            directors_container = directors_title.find_parent(
                class_="MuiPaper-root MuiCard-root MuiPaper-elevation1 MuiPaper-rounded"
            )
            directors_list = directors_container.find_all(
                "a",
                class_="MuiButtonBase-root MuiListItem-root MuiListItem-dense MuiListItem-gutters MuiListItem-button",
            )
            for director in directors_list:
                director_names.append(director.text)

        return {
            "title": title.text,
            "status": status.text,
            "registration_date": registration_date.text,
            "adres phisical": phisical_adres.text,
            "juridic adres": jiridic_adres.text,
            "angajati": angajati.text,
        }

    except Exception as e:
        print(e)
        pass
    finally:
        pass


# creating file, writin it


def save_to_file(py_dict):
    try:
        with open("test.json", "w") as f:
            f.write(json.dumps(py_dict, ensure_ascii=False))
            f.close()
    except Exception as e:
        print(e)


# program start

if __name__ == "__main__":

    try:
        input_str = input("Enter IDNO: ")
        input_list = input_str.split(",")
        parse_idnos(input_list)
        print(2)

    except Exception as e:
        print(e)
    finally:
        driver.quit()

# idno = ["1002600056626", "1003602004112", "1009600017846", "1013606000397"]
