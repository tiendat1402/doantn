import pandas as pd
from scraper.appstore_scrapper import AppStoreScrapperConfig, AppStoreScrapperSource

def get_appstore_comment(url, max_count, lookup_period):
    # initialize play store source config
    try:
        source_config = AppStoreScrapperConfig(
            app_url = url,
            lookup_period = lookup_period,
            max_count = max_count
        )
        # initialize app store reviews retriever
        source = AppStoreScrapperSource()
        source_data = source.lookup(source_config)
        # Extract information from data
        id = []
        author_name=[]
        title = []
        content = []
        rating = []
        platform = []
        for i in range(0,max_count):
            source_data[i]=dict(source_data[i])
            id.append(source_data[i]["meta"]["id"])
            author_name.append(source_data[i]["meta"]["author_name"])
            title.append(source_data[i]["meta"]["title"])
            content.append(source_data[i]["meta"]["content"])
            rating.append(source_data[i]["meta"]["rating"])
            platform.append('Appstore')
        df=pd.DataFrame(list(zip(id,author_name,title,content,rating,platform)),columns=['id','author','title','content','rating','source'])
    except:
        raise ValueError("Your configuration is not valid!")
    return df
