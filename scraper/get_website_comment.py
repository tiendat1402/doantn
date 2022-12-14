from scraper.website_crawler_source import TrafilaturaCrawlerConfig, TrafilaturaCrawlerSource
import pandas as pd
def get_website_comment(urls):

    source_config = TrafilaturaCrawlerConfig(urls=urls)
    source=TrafilaturaCrawlerSource()
    source_response_list=source.lookup(source_config)
    title = []
    raw_text = []
    for i in range(0, len(source_response_list)):
        source_response_list[i] = dict(source_response_list[i])
        #id.append(source_response_list[i]["meta"]["id"])
        #hostname.append(source_response_list[i]["meta"]["author"])
        title.append(source_response_list[i]["meta"]["title"])
        raw_text.append(source_response_list[i]["meta"]["raw_text"])
        #rating.append(None)
        #platform.append(source_response_list[i]["meta"]["source"])
    df = pd.DataFrame(list(zip(title, raw_text)), columns=['title','content'])
    return df