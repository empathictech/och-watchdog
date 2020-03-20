from bs4 import BeautifulSoup
from requests import get as get_request
from re import compile as compile_regex

if __name__ == "__main__":
  # sadly, https://ochdatabase.umd.edu/, doesn't have an API, but there is a degree of consistency to search queries and their matching URLs
  # the simplest way forward is to build a search manually and then copy/paste the URL below, as we have done
  URL = "https://ochdatabase.umd.edu/property/search?view=grid&sort=default&b%5B0%5D=0&b%5B1%5D=1&per_bed=u&r%5Bmin%5D=600&r%5Bmax%5D=1000&page=1&search_all=&movein-start=0&movein-end=1&o=&distance%5B184%5D=3&distance%5B185%5D=&lastweek=on&has_photo=on&text_search="
  page = get_request(URL)

  soup = BeautifulSoup(page.content, 'html.parser')
  
  search_results = soup.find(id='expo')
  listings = search_results.find_all('article', class_=compile_regex(r'^ocp-property-search property-\d?.*'))

  for posting in listings:
    print(posting.prettify())
