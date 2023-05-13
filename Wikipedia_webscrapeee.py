from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles'

# opening a connection and grabbing a page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

#arraying all the tables on the table-list based page
list_of_tables = page_soup.findAll("table", {"class": "wikitable"})

#creating a csv
filename = 'wiki.csv'
with open(filename, "w", encoding="utf-8") as f:
    headers= "Article Name,Description,Link\n"
    f.write(headers)

    for table_number in list_of_tables:
        table_entries = table_number.findAll("tr")
        # loop then breaks down each table's entries even more
        for individual_entry in table_entries:
            individual_entry_title = individual_entry.find("b").text.strip().replace(',', '').replace('Ō', 'O')
            individual_entry_link = "https://en.wikipedia.org" + individual_entry.a.get("href")
            individual_entry_description_list = individual_entry.findAll("td")
            if len(individual_entry_description_list) > 1:
                individual_entry_description = individual_entry_description_list[1].text.strip().replace(',', '')
                print(individual_entry_title.encode('utf-8'))
                f.write(individual_entry_title + "," + individual_entry_description + "," + individual_entry_link + "\n")

# f.close()  # remove this line, the file is already closed when exiting the "with" block
