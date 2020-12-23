import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles'

#opening a connection and grabbing a page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#arraying all the tables on the table-list based page
list_of_tables = page_soup.findAll("table",{"class":"wikitable"})

#title of each entry
#individual_entry_title = individual_entry.find("b").text.strip()

#full (clickable) link of each entry
#individual_entry_link = "https://en.wikipedia.org" + individual_entry.a.get("href")

#description of each entry
#individual_entry_description = individual_entry.findAll("td")[1].text.strip()

#creating a csv
filename= "wikipedia.csv"
f = open(filename, "w", encoding="utf-8")
#creating titles of each column, note the \n
headers= "Article Name,Description,Link\n"
f.write(headers)

for table_number in list_of_tables:
    table_entries = table_number.findAll("tr")
    for individual_entry in table_entries:
        individual_entry_title = individual_entry.find("b").text.strip()
        individual_entry_link = "https://en.wikipedia.org" + individual_entry.a.get("href")
        individual_entry_description = individual_entry.findAll("td")[1].text.strip() 
        print(individual_entry_title)
        f.write(individual_entry_title.replace(',', '') + "," + individual_entry_description.replace(',', '') + "," + individual_entry_link.replace(',', '') + "\n")

f.close()