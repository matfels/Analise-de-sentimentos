import nltk
nltk.download('vader_lexicon')

from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment_score(texto):
    sia = SentimentIntensityAnalyzer() #Cria uma instância do SentimentIntensityAnalyzer
    pontuacao = sia.polarity_scores(texto)

    return pontuacao['compound']