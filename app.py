import streamlit as st
import streamlit_extras
from PIL import Image
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from C2 import nltk_summarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from C3 import text_rank

st. set_page_config(layout="wide") 

summarizer = pipeline("summarization")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')
with col2:
    image = Image.open("C:\\Users\\divya\\OneDrive\\Desktop\\Work\\Vintern\\App\\Logo.png")
    st.image(image)
with col3:
    st.write(' ')



st.title("  WELCOME TO SUMMERIZE ME")
st.markdown("------")


options = ["lexRank", "Nltk", "TextRank"]
selected_option = st.selectbox("Select an option", options)


if selected_option == "lexRank":
    st.write("You selected LexRankSummarizer!")
    text = st.text_area('Enter Text Below :', height=300)
    submit = st.button('Generate') 
    if submit:
            parser = PlaintextParser.from_string(text, Tokenizer("english"))
            summarizer = LexRankSummarizer()
            summary = summarizer(parser.document, sentences_count=10)
            summary = "\n".join(str(sentence) for sentence in summary)
            st.success(summary)


elif selected_option == "Nltk":
    st.write("You selected Nltk_Summarizer!")
    text3 = st.text_area('Enter Text Below :', height=900)
    submit = st.button('Generate') 
    if submit:
        st.subheader("Summary:")
        nltk_summary = nltk_summarizer([text3])
        st.success(nltk_summary[0])

elif selected_option == "TextRank":
    st.write("You selected Text_Rank!")
    text4 = st.text_area('Enter Text Below :', height=300)
    submit = st.button('Generate') 
    if submit: 
        st.subheader("Summary:")
        summary = text_rank(text4)
        st.success(summary)




    

        
        
        

