from bs4 import BeautifulSoup

extract_a_hrefs = lambda content: [x["href"].strip("/") for x in
                                   BeautifulSoup(content, features="html5lib").findAll("a")]
