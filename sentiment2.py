from textblob import TextBlob


blob = TextBlob("More than 90% of road traffic deaths occur in low- and middle-income countries. Road traffic injury death rates are highest in the African region and lowest in the European region. Even within high-income countries, people from lower socioeconomic backgrounds are more likely to be involved in road traffic crashes.")
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)