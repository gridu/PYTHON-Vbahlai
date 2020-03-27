from dbservice import *

if (__name__ == "__main__"):
    new_arts = [
        {"link":"url4", "article_name":"Article4", "text":"Some Text4", "date":"Feb 5, 2019", "author_url":"aurl1", "tags":"tags1"},
        {"link":"url5", "article_name":"Article5", "text":"Some Text5", "date":"Dec 31, 2020", "author_url":"aurl2,aurl3", "tags":"tags3"}
    ]

    new_auth = [
        {"url":"aurl4", "full_name":"Name4", "job_title":"Trainee", "linkedin_url":"lurl4"},
        {"url":"aurl5", "full_name":"Name5", "job_title":"SD", "linkedin_url":""}
    ]

    urls = add_new_articles(new_arts)
    add_new_authors(new_auth)
    top_7_tags_plot(top_7_tags())