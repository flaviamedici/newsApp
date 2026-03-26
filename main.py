import requests
from send_email import send_email

topic = 'tesla'
api_key = "890603a55bfa47048e4490069ebee18c"
url = (f'https://newsapi.org/v2/everything?'
       f'q={topic}'
       '&sortBy=published'
       f'At&apiKey={api_key}'
       'langauge=en')

request = requests.get(url)
content = request.json()

body = ""
for article in content['articles'][:20]:
    body = "Subject: Today's news" + '\n' + body + article['title'] + '\n' + str(article['description']) + '\n' + article['url'] + '\n'

body = body.encode('utf-8')
send_email(message=body)