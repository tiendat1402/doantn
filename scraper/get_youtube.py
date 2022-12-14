import pandas as pd
from scraper.youtube_scrapper import YoutubeScrapperSource, YoutubeScrapperConfig

#fuction start
def get_youtube_comment(url, max_count, lookup_period):
    try:
        text = []
        author = []
        id = []
        title = []
        rating = []
        platform = []
        ytb_config = YoutubeScrapperConfig(
           video_url = url,
           max_comments = max_count,
           lookup_period = lookup_period
        )
        ytb = YoutubeScrapperSource()
        ytb_response_list = ytb.lookup(ytb_config)
        for y in range (0, max_count):
          ytb_response_list[y] = dict(ytb_response_list[y])
          text.append(ytb_response_list[y]["meta"]["text"])
          author.append(ytb_response_list[y]["meta"]["author"])
          #id.append(ytb_response_list[y]["meta"]["comment_id"])
          #title.append(None)
          #rating.append(None)
          #platform.append('Youtube')
        df = pd.DataFrame(list(zip(author,text)), columns=['author','content'])
    except:
        raise ValueError("Your configuration is not valid!")
    return df