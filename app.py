from bs4 import BeautifulSoup
import requests

def crawler(website_link, link_class):
  # get and parse webpage content
  website_request = requests.get(website_link, timeout=5)
  website_content = BeautifulSoup(website_request.content, ‘html.parser’)
  
  # extract posting information
  jobs_link = website_content.find_all(class_ = link_class)
  return jobs_link

if __name__ == "__main__":
  url = "https://ochdatabase.umd.edu/property/search?view=grid&sort=default&b%5B0%5D=0&b%5B1%5D=1&per_bed=u&r%5Bmin%5D=600&r%5Bmax%5D=1000&page=1&search_all=&movein-start=0&movein-end=1&o=&distance%5B184%5D=3&distance%5B185%5D=&lastweek=on&has_photo=on&text_search="
  get = requests.get(url, timeout=5)

  print(get)
