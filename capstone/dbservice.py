from dbsettings import session, Article, Author, connection
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

session.add_all([
    Article(url="url1", title="title1",text="Some text1", publication_date="Sep 18, 2020", author_url="aurl1,aurl2", tags="tag1"),
    Article(url="url2", title="title2",text="Some text2", publication_date="Feb 4, 2020", author_url="aurl1,aurl2,aurl3", tags="tag2"),
    Article(url="url3", title="title1",text="Some text1", publication_date="Aug 13, 2019", author_url="aurl2", tags="tag1,tag2"),
    Author(url="aurl1", full_name="Name1", job_title="ML", linkedin_url="lurl1"),
    Author(url="aurl2", full_name="Name2", job_title="DS", linkedin_url="lurl2"),
    Author(url="aurl3", full_name="Name3", job_title="DevOps")
])

session.commit()

def add_new_articles(new_articles_data):
    max_date = get_max_date()
    for i in new_articles_data:
        if datetime.strptime(i["date"], '%b %d, %Y').date() > max_date:
            session.add(
                Article(url=i["link"], title=i["article_name"], text=i["text"], publication_date=i["date"],
                        author_url=i["author_url"], tags=i["tags"]))
    session.commit()

# def top_7_tags():
#     tags_list = []
#     pair = []
#     for each in session.query(Article):
#         tag = str(each.tags)
#         if tag.find(",") != -1:
#             tags_list.extend(tag.split(","))
#         else:
#             tags_list.append(tag)
#     tags_set = set(tags_list)
#     for i in tags_set:
#         pair.append((i, tags_list.count(i)))
#     pair.sort(reverse=True)
#     return pair[:7]
#
# def top_7_tags_plot(tags):
#     objects = tuple([i[0] for i in tags])
#     values = tuple([each[1] for each in tags])
#     y_pos = np.arange(len(objects))
#     plt.barh(y_pos, values, alpha=0.8)
#     plt.yticks(y_pos, objects)
#     plt.xlabel('quantity')
#     plt.title("Top 7 popular tags")
#     plt.show()

def articles_counter():
    articles = session.query(Article).all()
    authors = session.query(Author).all()
    for article in articles:
        urls = article.author_url.split(',')
        for aurl in urls:
            for author in authors:
                if author.url == aurl:
                    s = "UPDATE authors SET articles_counter = articles_counter + 1 WHERE url = '{}'".format(aurl)
                    session.execute(s)
                    session.commit()
                    break

def add_new_authors(new_authors_data):
    for each in new_authors_data:
                session.add(Author(url=each["url"], full_name=each["full_name"], job_title=each["job_title"],
                                   linkedin_url=each["linkedin_url"]))
    session.commit()

def get_max_date():
    first_date = session.query(Article.publication_date).first()
    max_date = datetime.strptime(*first_date, '%b %d, %Y').date()
    for each in session.query(Article.publication_date):
        current_date = datetime.strptime(*each, '%b %d, %Y').date()
        if max_date < current_date:
           max_date = current_date
    return max_date

def doublication_check(new_articles_data):
    new_authors = set()
    existed_authors = set()
    articles_to_add = []
    for author in session.query(Author.url):
        existed_authors.add(*author)
    max_date = get_max_date()
    for each in new_articles_data:
        if datetime.strptime(each["date"], '%b %d, %Y').date() > max_date:
            for i in each["author_url"].split(","):
                new_authors.add(i)
        articles_to_add.append(each)
    authors_to_add = new_authors.difference(existed_authors)
    return authors_to_add, articles_to_add