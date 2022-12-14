import sys
sys.path.append(r"C:\Users\dat.nguyenvantien\Desktop\Workspace\datn")
from scraper.get_playstore_comment import get_playstore_comment
from scraper.get_youtube import get_youtube_comment
from scraper.get_appstore_comment import get_appstore_comment
from scraper.get_website_comment import get_website_comment
from scraper.get_google_news import get_google_news
import streamlit as st
st.set_page_config(page_title = 'SMA Demo', layout = 'wide')
#logo = "data:image/png;base64,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"
st.title('SMA Demo')

from summary.summarization import summarization
from sentiment_analyst.sentiment import sentiment_analyzer
col1, col2, col3 = st.columns(3)

# Column 1
with col1:
    st.header("Scrapper")
    scraper = st.selectbox(
        'CHOOSE YOUR PLATFORM',
        ('Playstore', 'Appstore', 'Youtube', 'Reddit', 'Google News', 'Website'))
    title1 = str(st.text_input('SOURCE'))
    title2 = int(st.slider('NUMBER',1,500))
    title3 = str(st.selectbox('CHOOSE PERIOD', ('5Y','365d','5m','10m','1Y','3Y','10d')))
    a = st.button('Get data')

def get_comment(scraper):
    if scraper == 'Playstore':
       data = get_playstore_comment(url=title1, max_count=title2, lookup_period=title3)
    elif scraper == 'Appstore':
         data = get_appstore_comment(url=title1, max_count=title2, lookup_period=title3)
    elif scraper == 'Youtube':
         data = get_youtube_comment(url=title1, max_count=title2, lookup_period=title3)
    elif scraper == 'Reddit':
         data = get_reddit_comment(url=title1, max_comment=title2, period=title3)
    elif scraper == 'Google News':
         data = get_google_news(query=title1, max_results=title2, lookup_period=title3, country='VN', language='vi')
    else:
        data = get_website_comment(urls=[title1])
    return data

if a:
   data = get_comment(scraper)
   st.dataframe(data)

# Column 2
with col2:
    st.header("Analyzer")
    analyzer = st.selectbox(
        'CHOOSE YOUR ANALYZER',
        ('None', 'Sentiment Analysis', 'Text Classification', 'Summarization', 'Keyword Extraction'))
    b = st.button('Analyze')

if b:
   if analyzer == 'None':
      data = get_comment(scraper)
      st.dataframe(data)

   elif analyzer == 'Sentiment Analysis':
      data = get_comment(scraper)
      sent = []
      label = sent.append(None)
      data['label'] = label
      for i in range(0, title2):
          sentiment = sentiment_analyzer(data["content"][i])
          if sentiment == 'Negative':
            data["label"][i]='Negative'
          elif sentiment == "Positive":
            data["label"][i]='Positive'
          else:
            data["label"][i]="Neural"
      st.dataframe(data)

   elif analyzer == 'Text Classification':
      data = get_comment(scraper)
      sent = []
      label = sent.append(None)
      data['label'] = label
      for i in range(0, title2):
          emotion = emotion_classification(data["content"][i])
          if emotion == 'Enjoyment':
              data["label"][i]='enjoyment'
          elif emotion == 'Disgust':
              data["label"][i]='disgust'
          elif emotion == 'Sadness':
              data["label"][i]='sadness'
          elif emotion == 'Anger':
              data["label"][i]='anger'
          elif emotion == 'Surprise':
              data["label"][i]='surprise'
          elif emotion == 'Fear':
              data["label"][i]='fear'
          else:
              data["label"][i]='other'
      st.dataframe(data)

   elif analyzer == 'Summarization':
      data = get_comment(scraper)
      sent = []
      label = sent.append(None)
      data['label'] = label
      for i in range(0, title2):
          summary = summarization(data["content"][i])
          data["label"][i] = summary
      st.dataframe(data)
