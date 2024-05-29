from textblob import TextBlob
from newspaper import Article


url = 'https://www.who.int/news-room/fact-sheets/detail/road-traffic-injuries'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)


