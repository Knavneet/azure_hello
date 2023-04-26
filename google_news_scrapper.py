URL_MAIN = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"

import requests
from bs4 import BeautifulSoup

# Make a request to the news website
#url = "https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pNbV9DckJ4RXlLNzlMa2lwRmdDZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
response = requests.get(URL_MAIN)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
print(soup.prettify())

# Find all links with the given pattern
links = soup.find_all('a', class_='jKHa4e', href=True)

# Extract the href attribute from each link
master_link = []
for link in links:
    xx = str("https://news.google.com")+link.get('href')
    master_link.append(xx)
master_link

import requests
from bs4 import BeautifulSoup

master_lk = []
for url in master_link[:20]:

# Make a request to the news website
#url = "https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pNbV9DckJ4RXlLNzlMa2lwRmdDZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup.prettify())

    import pandas as pd
    all_links = []
    for h4 in soup.find_all('h4'):
        for link in h4.find_all('a'):
            xx = str("https://news.google.com")+link.get('href')
            all_links.append(xx)
    pd.Series(all_links)



    series_list = []
    series_list_para = []
    series_list_body = []
    for links in all_links:
    # Make a request to the news website
        url = str(links)#"https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lReHZTbUJ4RlBwa0FrLUJESk55Z0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
        # print(links)
        # print("---")

        #print(soup.prettify())
        

        all_p_tags = soup.find_all("h1")
        all_p_tags_text = []
        for p_tag in all_p_tags:
            all_p_tags_text.append(p_tag.text)

        series_list.append(all_p_tags_text)

        all_p_tags = soup.find_all("p")
        all_p_tags_text_new = []
        for p_tag in all_p_tags:
            all_p_tags_text_new.append(p_tag.text)

        series_list_para.append(all_p_tags_text_new)
        


    master_lk.append(series_list)

display(pd.DataFrame(master_lk))
