import requests
from bs4 import BeautifulSoup


page = requests.get('http://www.wordreference.com/definition/luck')
soup = BeautifulSoup(page.content, 'html.parser')
soup_children = soup.children
print(soup.html.body)

# for soup_child in soup_children:
#     if soup_child.find


# els = [type(item) for item in list(soup.children)]
# for el in els:
#     print(el)

# for soup_child in soup_children:
#     print(type(soup_child))

# print(len(soup_children[3]))

# print(type(soup.children)) iterator
# print(type(list(soup.children))) list