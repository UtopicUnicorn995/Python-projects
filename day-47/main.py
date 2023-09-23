from bs4 import BeautifulSoup
import lxml
import requests
import smtplib 

my_email = "christianpy123@gmail.com"
password = "sdclnpccssmamibh"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
HEADERS = {
        "User-Agent": "Defined",
        "Accept-Language": "en-US,en;q=0.9",
    }

ROBOT_RESPONSE = "Sorry, we just need to make sure you're not a robot. For best results, please make sure your browser is accepting cookies."


robot_check = True

while robot_check == True:
    response = requests.get(url=URL, headers=HEADERS)
    response.raise_for_status()
    amazon_page = response.text
    
    soup = BeautifulSoup(amazon_page, "html.parser")
    test = soup.find(name="p").text
    if test != ROBOT_RESPONSE:
        robot_check = False
 
product_name = soup.select_one('#title #productTitle').getText().strip()
selected = soup.select_one('.a-price .a-offscreen').getText()
price = float(selected.strip("$"))
print(product_name)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="christian.degulacion@gmail.com", msg=f"{product_name}\n\nnow for ${price}".encode('utf-8'))
