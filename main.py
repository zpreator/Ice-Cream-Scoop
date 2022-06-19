import requests
from bs4 import BeautifulSoup
import urllib
import cv2
from etext import send_sms_via_email, send_mms_via_email


def get_flavor_of_the_day():
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
    return text, 'temp.png'


def main():
    numbers = ["3039102797", "7202555850"]
    with open('key.txt', 'r') as file:
        key = file.readline()
    for number in numbers:
        try:
            message, file_path = get_flavor_of_the_day()
            provider = "T-Mobile"

            sender_credentials = ("zachary.preator@gmail.com", key)

            mime_maintype = "image"
            mime_subtype = "png"

            send_mms_via_email(
                number,
                message,
                file_path,
                mime_maintype,
                mime_subtype,
                provider,
                sender_credentials,
                subject="Today's Flavor is:"
            )
            print(f'Successfully sent message to: {number}')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()