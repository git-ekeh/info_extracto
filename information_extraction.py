#!/usr/bin/env/python3



from bs4 import BeautifulSoup
import requests as rs 


def data_scrape():
    webpage_response = rs.get("https://www.toronto.ca/city-government/data-research-maps/open-data/open-data/open-data-catalogue/#5db8d9e0-1ef4-8bc9-5932-edf87a551163")
    webpage = webpage_response.content
    soup = BeautifulSoup(webpage, 'html.parser')
    page_links = soup.find_all("p")
    train = open("training_file.txt", "w+")
    for tag in page_links: 
        train.write(str(tag.get_text()))
    train.close()

data_scrape()

