from bs4 import BeautifulSoup
from requests import get as get_request
from re import compile as compile_regex
from argparse import ArgumentParser

import smtplib, ssl

# sends the accumulated list of postings to and from the emails defined in the credentials.env file
# for obvious reasons, .env file types are prevented from being committed to git
def send_message(message):
  with open("env_files/credentials.env", "r") as env_file:
    creds = env_file.read().strip().split()
    recipient = creds[0]
    sender = creds[1]
    password = creds[2]

  # default smtp port for GMail
  port = 465
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recipient, message)

# the OCH site has the Google Maps API integrated into it, which is great as it means we don't have to pay for it
# it does require interacting with the page, however
def get_commute(url):
  return "Not implemented yet"

# not implemented yet, need to create a DB of postings already found/viewed
def in_visited(property_name):
  return False

# checks the current posting against a blacklist of property managers that are dorm-style
# there is of course the chance of blacklisting posts that mention they are near these buildings...
# but as of right now, and based on the buildings' locations, the risk is worth it
def in_blacklist(property_name):
  black_list = ["UNIVERSITY VIEW", "COMMONS", "COURTYARDS", "LANDMARK", "TERRAPIN ROW", "VARSITY"]
  
  if any([org in property_name.upper() for org in black_list]):
    return True
  else:
    return False

# parses and accumulates all the information we need from the OCH site
def collect_information(posting):
  info = posting.find("div", class_="info")
  
  # name text formatted as "name \n address"
  name = info.find("div", class_="name").text.strip().split("\n")[0]

  if in_blacklist(name) or in_visited(name):
    return None

  # price text formatted as "price \n per X"
  price = " ".join(info.find("div", class_="price").text.strip().split())
  address = info.find("span", class_="address").text.strip()
  availability = info.find("div", class_="search--listing-extras").text.strip()
  link = "https://ochdatabase.umd.edu" + info.find("div", class_="name").find("a")["href"]

  commute_time = get_commute(link)

  return f"""
Posting name: {name}
Rent: {price}
Property address: {address}
Commute time: {commute_time}
Availability: {availability}
Link to page: {link}"""

if __name__ == "__main__":
  cli_parser = ArgumentParser()
  cli_parser.add_argument("--test", "-t", help="Send results to stdout", action="store_true")
  cli_args = cli_parser.parse_args()

  # sadly, https://ochdatabase.umd.edu/, doesn't have an API, but there is a degree of consistency to search queries and their matching URLs
  # the simplest way forward is to build a search manually and then copy/paste the URL below, as we have done
  url = "https://ochdatabase.umd.edu/property/search?view=grid&sort=default&b%5B0%5D=0&b%5B1%5D=1&per_bed=u&r%5Bmin%5D=600&r%5Bmax%5D=1000&page=1&search_all=&movein-start=0&movein-end=1&o=&distance%5B184%5D=3&distance%5B185%5D=&lastweek=on&has_photo=on&text_search="
  page = get_request(url)

  soup = BeautifulSoup(page.content, "html.parser")
  
  search_results = soup.find(id="expo")
  postings = search_results.find_all("article", class_=compile_regex(r"^ocp-property-search property-\d?.*"))

  parsed_posts = []
  for posting in postings:
    info = collect_information(posting)
    
    if info is not None:
      parsed_posts.append(info)

  if parsed_posts:
    final_message = "\n".join(parsed_posts)
  else:
    final_message = "No new postings found."

  if cli_args.test:
    print(final_message)
  else:
    send_message(final_message)
