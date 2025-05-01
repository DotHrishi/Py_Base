import requests
from twilio.rest import Client 

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "3DA43KU2KTGNLDNK"
NEWS_API_KEY = "your news api key"
TWILIO_SID = "your twilio sid"
TWILIO_AUTH_TOKEN = "your twilio auth token"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
    
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
uo_down=None
if difference>0:
    up_down='🔺'
else:
    up_down='🔻'

diff_percent = round((float(difference)/float(yesterday_closing_price))*100)
print(diff_percent)

if abs(diff_percent) > 0.01:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,

    }
    new_response = requests.get(NEWS_ENDPOINT, params=news_params)
    article = new_response.json()["articles"]
    
    three_articles = article[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles] 

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="sender's phone number",
            to="reciever's phone number"
        )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

