from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import random
import string
import time
import concurrent.futures
from clint.textui import progress

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
list_of_books=[]
list_of_urls=[]
specific=""
def main():
    print("Start")
    topic=input("TOPIC")
    specific=input("specific??")
    topic = topic+" "+"books"
    googleSearch(topic)
    find_books()

def find_books():
    try: 
     main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"extabar"))
     )
    
   
    #print(main.get_attribute("jsname"))
   
     books = main.find_elements_by_tag_name("a")
  

     for book in books:
      
       #print(book.get_attribute("title"))
       if(len(list_of_books)<5):
        list_of_books.append(book.get_attribute("title"))

    
     research()
     pass
    
    except : 
        print("oops")
     
    
    

       
   

def download(urll):
    name_books=''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
    print(urll)
  
  
   
    try:
        myfile = requests.get(urll, allow_redirects=True,stream=True)
        with open("C:/Users/Subodh Maharjan/Desktop/project/"+name_books+".pdf","wb")as Pypdf:

            total_length=int(myfile.headers.get('content-length'))
            name_books=''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
            for ch in progress.bar(myfile.iter_content(chunk_size=2391975),expected_size=(total_length/1024)+1):
                if ch:
                    Pypdf.write(ch)

    except:
        pass
   
def research():
    
    for book in list_of_books:
        download_pdf_books(book)
    
    print("jole")
    print(list_of_urls)
    for urle in list_of_urls:
        download(urle)
   

def download_pdf_books(book_name):

    
    pdf_name = book_name+"pdf"
    
    googleSearch(pdf_name)
    
    try: 
        urls_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"rso"))
         )
        get_url=urls_id.find_elements_by_tag_name("a")
        
     
        for uri in get_url:
           try: 
            divider=uri.get_attribute("href")
            pdf_filter=divider.split(".")
           
            if(pdf_filter[len(pdf_filter)-1]=="pdf"):
            
               list_of_urls.append(divider)
           except:
               pass  
               
              
              
    
                



    except:
            pass
     
    
    
def googleSearch(input_search):
    driver.get("https://www.google.com/")
    search = driver.find_element_by_name("q")
    search.send_keys(input_search)
    search.send_keys(Keys.RETURN)




if __name__=="__main__":
    main()





