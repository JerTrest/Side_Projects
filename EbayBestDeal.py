#This program searches Ebay to find the cheapest item you search for, as well as the best deals on that item
#Input the item you would like to search for (make sure spelling is correct) and the number of pages you would like to search through on Ebay
#Then open the links you would like to see 

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chrome_options=Options()
PATH="C:\Program Files (x86)\chromedriver.exe"
chrome_options.add_argument('--headless')
driver= webdriver.Chrome(options=chrome_options, executable_path=PATH)

def bestCashDiscount(current_prices,past_prices):
    if all(index==0 for index in past_prices):
        return False
    else:
        difference=0
        bestIndex=0
        for index in range(len(current_prices)):
            if ((past_prices[index])-(current_prices[index]))>difference:
                difference=past_prices[index]-current_prices[index]
                bestIndex=index
        return bestIndex

def bestPercentDiscount(current_prices,past_prices):
    if all(index==0 for index in past_prices):
        return False
    else:
        difference=0
        bestIndex=0
        for index in range(len(current_prices)):
            if past_prices[index]==0:
                pass
            elif (past_prices[index]-current_prices[index])/past_prices[index]>difference:
                difference=(past_prices[index]-current_prices[index])/past_prices[index]
                bestIndex=index
        return bestIndex

print("\n")
searchKey=str(input("What item are you looking for? "))

keyWords=searchKey.split(" ")
keyWords=[word.lower() for word in keyWords]

pagesToSearch=int(input("How many pages would you like to search? (Approx. 60-70 items per page) "))

past_prices=[]
current_prices=[]
links=[]
pageCounter=0
itemCounter=0
currentUrl="https://www.ebay.com/"

driver.get(currentUrl)
searchBar=driver.find_element_by_id("gh-ac")
searchBar.send_keys(searchKey)

searchBtn=driver.find_element_by_id("gh-btn")
searchBtn.click()


for count in range(pagesToSearch):
    currentUrl=driver.current_url
    webpage=requests.get(currentUrl)
    scr=webpage.content
    soup=BeautifulSoup(scr,'html.parser')

    for item in soup.findAll('div',{"class":"s-item__info clearfix"}):
        for title in item.findAll('h3',{"class":"s-item__title"}):
            itemCounter+=1
            if all(index in title.getText().lower() for index in keyWords):

                for link in item.findAll('a',{"class":"s-item__link"}):
                    links.append(link.attrs['href'])

                fixer=0
                for current_price in item.findAll("span",{"class":"s-item__price"}):
                    if fixer==0:
                        current_price=current_price.getText()
                        if "to" in current_price:
                            indexToCut=current_price.find("to")
                            current_price=current_price[:indexToCut-1]

                        if "," in current_price:
                            current_price=current_price.replace(",","")
                        current_price=float(current_price[1:])
                        current_prices.append(current_price)

                        for past_price in item.findAll("span",{"class":"STRIKETHROUGH"}):
                            past_price=past_price.getText()
                            if "," in past_price:
                                price_price=price_price.replace(",","")
                            past_price=float(past_price[1:])
                            past_prices.append(past_price)

                        if(len(current_prices)>len(past_prices)):
                            past_prices.append(0.0)
                        fixer+=1

                    else:
                        pass

    pageCounter+=1
    print("\n"+"\n")
    print("Page",pageCounter,"Completed")
    print("\n"+"\n")

    if(pageCounter==pagesToSearch):
        pass
    else:
        try:
            nextBtn = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pagination__next"))
            )
            nextBtn.click()
        except:
            print("\n"+"\n")
            print("*There are only",pageCounter,"pages of that item on Ebay*")
            break
    


print("Pages Searched:",pageCounter)
print("Items Searched:",itemCounter)
print("Items Found Matching Input:",len(links))
print("\n"+"\n")

print("Cheapest:")
print("Current Cost: $",min(current_prices))
print("Link:",links[current_prices.index(min(current_prices))])

print("\n"+"\n")

print("Best Discount Based On $ Reduction:")
cashIndex=bestCashDiscount(current_prices,past_prices)
if(cashIndex==False):
    print("There were no avaiable deals on the item listed")
else:
    print("Current Cost: $",current_prices[cashIndex])
    print("Past Cost: $",past_prices[cashIndex])
    print("Cash Reduction: $",round(past_prices[cashIndex]-current_prices[cashIndex],2))
    print("Link:",links[cashIndex])

print("\n"+"\n")

print("Best Discount Based On % Reduction:")
percentIndex=bestPercentDiscount(current_prices,past_prices)
if(percentIndex==False):
    print("There were no avaiable deals on the item listed")
else:
    print("Current Cost: $",current_prices[percentIndex])
    print("Past Cost: $",past_prices[percentIndex])
    print("Percent Reduction",round((past_prices[percentIndex]-current_prices[percentIndex])/past_prices[percentIndex],4)*100,"%")
    print("Link:",links[percentIndex])

print("\n"+"\n")
