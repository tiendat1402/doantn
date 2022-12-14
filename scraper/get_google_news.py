from scraper.google_news_source import GoogleNewsConfig, GoogleNewsSource
import pandas as pd

# Fuction begin
def get_google_news(query, max_results, lookup_period, language, country):
   try:
      userName = []
      content = []
      rating = []
      id = []
      title = []
      platform = []
      source_config = GoogleNewsConfig(
      query=query,
      max_results=max_results, 
      lookup_period=lookup_period,
      language=language,
      country=country
      )  
      source = GoogleNewsSource()
      data = source.lookup(source_config)
      for i in range(0, max_results):
         data[i]=dict(data[i])
         #id.append(data[i]["meta"]["extracted_data"]["id"])
         #userName.append(data[i]["meta"]["extracted_data"]["author"])
         title.append(data[i]["meta"]["extracted_data"]["title"])
         content.append(data[i]["meta"]["extracted_data"]["raw_text"])
         #rating.append(None)
         platform.append(data[i]["meta"]["url"])
      df = pd.DataFrame(list(zip(title,content,platform)), columns=['title','content','source'])
   except:
        raise ValueError("Your configuration is not valid! Try increasing the period value.")
   return df
# Function end