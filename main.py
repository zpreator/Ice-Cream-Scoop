import requests
from bs4 import BeautifulSoup
import urllib
import cv2

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

url = r"https://www.culvers.com/restaurants/west-point-ut-n-2000-w"
# url = r"https://www.culvers.com"

# response = urllib.request.urlopen(url)
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
div = soup.find(class_='ModuleRestaurantDetail-fotd')
element = div.find_all('img')[0]
img_path = 'https:' + element['src']
text = element['alt']
response = requests.get(img_path)
print(response)
with open('temp.png', 'wb') as file:
    file.write(response.content)
image = cv2.imread('temp.png')
print(text)
cv2.imshow('', image)
cv2.waitKey(0)
