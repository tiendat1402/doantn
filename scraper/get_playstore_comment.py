from scraper.playstore_scrapper import PlayStoreScrapperConfig, PlayStoreScrapperSource
import pandas as pd

# Function start
def get_playstore_comment(url, max_count, lookup_period):
    try:
        userName = []
        content = []
        rating = []
        id = []
        title = []
        platform = []
        source_config = PlayStoreScrapperConfig(  
           app_url = url,
           max_count = max_count, 
           lookup_period = lookup_period
        )
        source = PlayStoreScrapperSource()
        data = source.lookup(source_config)    
        for h in range (0, max_count):
            data[h] = dict(data[h])
            userName.append(data[h]["meta"]["userName"])
            content.append(data[h]["meta"]["content"])
            rating.append(data[h]["meta"]["score"])
            id.append(data[h]["meta"]["reviewId"])
            title.append(None)
            platform.append('Playstore')
        df = pd.DataFrame(list(zip(id,userName,title,content,rating,platform)), columns=['id','author','title','content','rating','source'])
    except:
        raise ValueError("Your configuration is not valid!")
    return df
# Function end