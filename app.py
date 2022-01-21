from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging
import requests
import nltk
from bs4 import BeautifulSoup
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route('/getabstract/subject')
def getabstract(subject):
    """parameter"""
 
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
            'action': 'parse',
            'page': subject,
            'format': 'json',
            'prop':'text',
            'redirects':''
            }
 
    response = requests.get(url, params=params)
    data = response.json()
 
    raw_html = data['parse']['text']['*']
    soup = BeautifulSoup(raw_html,'html.parser')
    soup.find_all('p')
    text = ''
 
    for p in soup.find_all('p'):
      text += p.text
      pass
    
    return text  

  
  @app.route("/get_wiki_summary/subject")
  def get_wiki_summary(subject):
    text = getabstract(subject)
    stemmer = Stemmer('english') #Stemmer
    Tsummarizer=TextRankSummarizer(stemmer)#Initializing the TextRank Summarizer Object with stemmer
    Tsummarizer.stop_words = get_stop_words('english') #Removing the stopwords
    parser = PlaintextParser.from_string(text, Tokenizer('english')) #Parsing the text
    summary=Tsummarizer(parser.document, 10) #Creating the TextRank based Summary
    return summary
  
  @app.route("/")
  def home():
    html = "<h3>Wikipedia search: Use getabstract/subject to get the Wikipedia abstract of a subject and get_wiki_summary/subject to get 10 sentences that summarize the abstract.</h3>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
