from dbservice import *

if (__name__ == "__main__"):

    #Scrapped new articles
    new_arts_data = [
        {"link":"url4", "article_name":"Article4", "text":"Some Text4", "date":"Feb 5, 2029", "author_url":"aurl1", "tags":"tags1"},
        {"link":"url5", "article_name":"Article5", "text":"Some Text5", "date":"Dec 31, 2030", "author_url":"aurl4,aurl5", "tags":"tags3"}
    ]

    authors_to_add, articles_to_add = doublication_check(new_arts_data)

    #Scrapped authours url
    new_auth_data = [
        {"url":"aurl4", "full_name":"Name4", "job_title":"Trainee", "linkedin_url": "lurl4"},
        {"url":"aurl5", "full_name":"Name5", "job_title":"SD", "linkedin_url": None}
    ]
    add_new_authors(new_auth_data)
    add_new_articles(articles_to_add)
    articles_counter()
