from database import Database

from sentiment_analysis import analyze_sentiment
from sentiment_analysis_score import analyze_sentiment_score
def main():
    db = Database('twitter3.db')


#========================== TEXTO DO Tweet =========================================
    text = "Hate"

    analisepost =  analyze_sentiment(text)
    if analisepost == "Negative":
        active = 'false'
    else:
        active = 'true'



#========================== Inserir Tweet =========================================
    db.insert_post(text, analisepost, active, analyze_sentiment_score(text))



#========================== Corrigir Tweet ========================================
    db.update_post(5,text, analisepost, active, analyze_sentiment_score(text))


#========================== Deletar Tweet =========================================
#    db.delete_post(7)


#========================== Ler os posts Tweet ====================================
    for post in db.read_posts():
        print(f"Post: {post[1]}, Categoria {post[2]}")


    db.__del__

if __name__ == '__main__':
    main()



    