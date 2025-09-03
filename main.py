from database import Database
from models import Post
from sentiment_analysis import analyze_sentiment
from sentiment_analysis_score import analyze_sentiment_score
def main():
    db = Database('twitter3.db')

 #   text = "I dont like python!!!"
#    db.update_post(17, text, analyze_sentiment(text), 'false',analyze_sentiment_score(text) )
    db.delete_post(20)
    for post in db.read_posts():
        print(f"Post: {post[1]}, Categoria{post[2]}")

if __name__ == '__main__':
    main()



    