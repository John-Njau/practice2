import urllib.request
import json
from .models import Articles,Source

# Articles = articles.Articles
# Sources = source.Source

api_key = None
BASE_SOURCE_URL = None
BASE_ARTICLES_URL = None

def configure_request(app):
    global api_key,BASE_SOURCE_URL,BASE_ARTICLES_URL
    BASE_SOURCE_URL = app.config['SOURCE_URL']
    BASE_ARTICLES_URL = app.config['ARTICLES_URL']
    api_key = app.config['NEWS_API_KEY']


def get_sources():
    source_url = BASE_SOURCE_URL.format(api_key)
    with urllib.request.urlopen(source_url) as news_source:
        source_data = news_source.read()
        source_data_dict = json.loads(source_data)
        
        source_results = None
        
        if source_data_dict['sources']:
            sources_list = source_data_dict['sources']
            source_results = process_sources(sources_list)
                
        return source_results
    

# id, name,description,url
def process_sources(sources):
    sources_list = []
    for source in sources:
        id = source['id']
        name = source['name']
        description = source['description']
        url = source['url']
        
        if url:
            source_object = Source(id, name, description, url)
            sources_list.append(source_object)
        
    return sources_list
    

def news_articles(id):
    news_url = BASE_ARTICLES_URL.format(id, api_key)
    with urllib.request.urlopen(news_url) as projectnews:
        projectnews_data = projectnews.read()
        projectnews_data_dict = json.loads(projectnews_data)

        articles_results = None

        if projectnews_data_dict['articles']:
            articles_list = projectnews_data_dict['articles']
            articles_results = process_results(articles_list)

        return articles_results


def process_results(results):
    articles_results = []
    for result in results:
        image = result['urlToImage']
        description = result['description']
        time = result['publishedAt']

        if image:
            articles_object = Articles(image, description, time)
            articles_results.append(articles_object)

    return articles_results
