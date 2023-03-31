import requests
from send_email import email_send
from os import getenv

topic = input("Enter a topic of the news: ")

api_key = getenv("NewsAPI")
url = "https://newsapi.org/v2/everything?" \
      "q=keyword&" \
      f"apiKey={api_key}&" \
      "language=en"

# Make request
url_request = requests.get(url)

# Turn the data into a dictionary
content = url_request.json()

# Get the title and description of the dictionary
body = ""
for article in content["articles"][:20]:
    # the news organised in a message
    if article["title"] is not None:
        body = "Subject: Today's news" + '\n' + \
                body + article["title"] + "\n" \
                + article["description"] \
                + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
# send the message to the email
email_send(message=body)

