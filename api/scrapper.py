from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Optional
from scraper.get_playstore_comment import get_playstore_comment
from scraper.get_youtube import get_youtube_comment
from scraper.get_appstore_comment import get_appstore_comment
from scraper.get_website_comment import get_website_comment
from scraper.get_google_news import get_google_news


router = APIRouter(
    prefix='/scrapper-tasks',
    tags=['scrapper-tasks']
)

@router.post('/playstore-scrapper')
def read(url: str, max_count: int, lookup_period: Optional[str]='5Y'):
    df = get_playstore_comment(url, 
                               max_count, 
                               lookup_period)
    data = df.to_dict('records')
    return JSONResponse(content=data)



@router.post('/youtube-scrapper')
def read(url: str, max_count: int, lookup_period: Optional[str]='5Y'):
    df = get_youtube_comment(url, 
                             max_count, 
                             lookup_period)
    data = df.to_dict('records')
    return JSONResponse(content=data)


@router.post('/appstore-scrapper')
def read(url: str, max_count: int, lookup_period: Optional[str]='5Y'):
    df = get_appstore_comment(url, 
                              max_count, 
                              lookup_period)
    data = df.to_dict('records')
    return JSONResponse(content=data)


@router.post('/website-scrapper')
def read(urls: str):
    df = get_website_comment(urls=[urls])
    data = df.to_dict('records')
    return JSONResponse(content=data)

@router.post('/google-news-scrapper')
def read(query: str, max_results: int, lookup_period: Optional[str]='5Y', country: Optional[str]='VN', language: Optional[str]='vi'):
    df = get_google_news(query=query, 
                         max_results=max_results,
                         lookup_period=lookup_period,
                         country=country,
                         language=language)
    data = df.to_dict('records')
    return JSONResponse(content=data)