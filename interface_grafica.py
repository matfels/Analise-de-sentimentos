import customtkinter as ctk
import tkinter as tk

from database import Database
from sentiment_analysis import analyze_sentiment
from sentiment_analysis_score import analyze_sentiment_score



#======================Criação da Janela principal======================
ctk.set_appearance_mode('system')
interface = ctk.CTk()
interface.title("Twitter")
interface.iconbitmap("twitter.ico")
interface.geometry('300x300')

#================================funcao================================
def Botao_Enviar():
    db = Database('twitter3.db') #criação da DB
    texto = texto_interface.get()
    analise_post = analyze_sentiment(texto)
    if analise_post == "Negative":
        active = 'false'
        color1 = 'red'
    else:
        active = 'true'
        color1 = 'green'
    db.insert_post(texto, analise_post, active, analyze_sentiment_score(texto))
    retorno.configure(text = "Inserido com sucesso!")

    
    for post in db.read_posts():
        retorno_bd.configure(text = f'Post: "{post[1]}", categoria "{post[2]}"', text_color= color1)


    db.__del__    

    

    


#================================campos================================
legenda_interface = ctk.CTkLabel(interface, text= "Insira o seu tweet: ")
#texto_interface.place(x= 10, y=20)
#texto_interface.grid(row = 0, column = 0)
legenda_interface.pack(pady = 10)

texto_interface = ctk.CTkEntry(interface)
texto_interface.pack(pady = 10)


botao_interface = ctk.CTkButton(interface, text = "Enviar", command= Botao_Enviar)
#botao_interface.grid(row = 1, column = 1)
botao_interface.pack(pady = 10)

retorno = ctk.CTkLabel(interface, text = " ")
retorno.pack(pady = 10)

retorno_bd = ctk.CTkLabel(interface, text = " ")
retorno_bd.pack(pady = 10)


interface.mainloop()
