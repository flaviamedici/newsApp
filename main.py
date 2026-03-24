import requests
from send_email import send_email

api_key = "890603a55bfa47048e4490069ebee18c"
url = 'https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=890603a55bfa47048e4490069ebee18c'

request = requests.get(url)
content = request.json()

body = ""
for article in content['articles']:
    body = body + article['title'] + '\n' + str(article['description']) + '\n'

body = body.encode('utf-8')
send_email(message=body)