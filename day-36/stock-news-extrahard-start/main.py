import requests
from twilio.rest import Client

account_sid = 'ACd4d9dd535ea5913fcb8171a5d5a38b74'
auth_token = '58272d50c9b1679e6203e5747d315173'



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCKS_API_KEY = "7D0R55H7K2AXJHI7"
NEWS_API_KEY = '957405cb19fe4b27852d7b8a473f8061'

stocks_parameters = {
    'function': "TIME_SERIES_DAILY",
    'symbol': 'IBM',
    'apikey': STOCKS_API_KEY
}

news_parameters = {
    'q': 'tesla',
    'apiKey': '957405cb19fe4b27852d7b8a473f8061'
}

stocks_response = requests.get('https://www.alphavantage.co/query?', stocks_parameters)
stocks_response.raise_for_status()
stocks = stocks_response.json()['Time Series (Daily)']

news_response = requests.get('https://newsapi.org/v2/everything?', news_parameters)
news_response.raise_for_status()
news = news_response.json()['articles'][:3]

closing_stocks = []

for stock in stocks:
    closing_stocks.append(float(stocks[stock]['4. close']))

result = ((closing_stocks[0] - closing_stocks[1]) / closing_stocks[1]) * 100

result = -5

def send_news(emoji):
    for single_news in news:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        from_='+18149149924',
        body=f"TESLA {emoji}{result}%\n\nHeadline: {single_news['title']}\n\nBrief: {single_news['description']}",
        to='+639615281824'
        )
        print(message.status)
    
if result >= 5:
    send_news('🔺')
elif result <= -5:
    send_news('🔻')
else:
    print('hoe')

    



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

