from bs4 import BeautifulSoup

soup = BeautifulSoup(open("word_list.html"), "html.parser")

# Get the paragraph element containing all the words
# Bad part is that each entry isn't its own element, 
# so I can't just select the entries from the BeautifulSoup tree

# This doesn't give me only the words
words = soup.find_all('p')