from bs4 import BeautifulSoup
import requests
import smtplib

URL = 'https://www.amazon.com/SteelSeries-Arctis-Console-Playstation-Nintendo/dp/B09FTMB8R6/ref=sr_1_10?keywords=gaming+headsets&pd_rd_r=36f6edac-9152-4c47-8115-305576c90ddf&pd_rd_w=j1RUs&pd_rd_wg=8VANG&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=3VNZAYC6GMP17Q6P5ZWN&qid=1650172210&sr=8-10'
HEADERS = ({'User-Agent':
		        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
		    'Accept-Language': 'en-US, en;q=0.5'})
BUY_PRICE = 29.99
YOUR_SMTP_ADDRESS = 'XXX'
YOUR_EMAIL = 'xxx'
YOUR_PASSWORD = 'xxx'

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")
price = float(soup.find("span",class_="a-offscreen").text.split('$')[1])
title = soup.find(id="productTitle").text.strip()

if price <= BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode('utf-8')
        )