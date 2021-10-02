import time
import sqlite3
import datetime
import pandas as pd
from lxml import html
import requests
from requests_html import AsyncHTMLSession

asession = AsyncHTMLSession()

i=1
while i>0:
    try:        
        clock_start = time.time()
        start = datetime.datetime.today()+datetime.timedelta(days=-7)
        tmrw = datetime.datetime.today()+datetime.timedelta(days=1)
        startformd = start.strftime('%Y-%m-%d')
        tmrwformd = tmrw.strftime('%Y-%m-%d')
        conn = sqlite3.connect('headlines.sqlite')
        qry = "SELECT DISTINCT * FROM scrapes WHERE scrapes.url NOT IN(SELECT url from pulls) AND scrapes.url_scrape_time BETWEEN '"+startformd+"' AND '"+tmrwformd+"' LIMIT 10"
        linkdf = pd.read_sql_query(qry, conn)
        conn.close()
        linkdict = linkdf.to_dict(orient='records')

        header_dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
        }
        articlez = {}

        async def learn(site): 
            with await asession.get(site['url'], stream=False, headers=header_dict) as r:
                
                tree = html.fromstring(r.content)
                pagetexts = tree.xpath("//p")
                content = []
                for cont in pagetexts:
                    content.append(cont.text_content())

                url_scrape_time = site['url_scrape_time']
                news_source = site['news_source']
                url = site['url']
                headline = site['headline']
                content = " ".join(content)
                article_scrape_time = datetime.datetime.now()

                articlez[article_scrape_time] = [url_scrape_time, news_source, headline, url, content]

        asession.run(*[lambda link=link: learn(link) for link in linkdict])
        
        df = pd.DataFrame.from_dict(articlez, orient='index', columns=['url_scrape_time','news_source', 'headline', 'url', 'article'])
        df.index.name = "article_scrape_time"
        conn = sqlite3.connect('headlines.sqlite')
        df.to_sql('pulls', conn, if_exists='append')
        conn.close()

        end = time.time()
        print('took '+str(round(end-clock_start,2))+' seconds to grab '+str(len(linkdict))+' articles at ' +str(datetime.datetime.now().strftime("%Y-%m-%d %Hhr%Mm%Ss")))
        time.sleep(3)

        i = i+1
        
    except ValueError as e:
        time.sleep(10)
    except pd.io.sql.DatabaseError as err:
        print("Database Error: " + str(err))
        time.sleep(10)
    except requests.exceptions.ConnectionError as er:
        print("Rejected request")
        time.sleep(10)
    except requests.exceptions.ChunkedEncodingError as erro:
        print("Other rejected request")
        time.sleep(10)