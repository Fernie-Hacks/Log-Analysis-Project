# "Database code" for the DB Forum.

import psycopg2


def main():
    #Connect to Database & create cursor to query DB.
    dbConnection = psycopg2.connect("dbname=news")
    dbCursor = dbConnection.cursor()
        
    #1. What are the most  popular three articles of all time?
    #Join articles and log tables count based on articles.slug being a substring of log.path
    sqlMostPopularArticles = """
        select title, count(*) as views 
            from articles join log 
            on log.path like '%' || articles.slug 
            group by articles.title 
            order by views desc 
            limit 3;
    """
    dbCursor.execute(sqlMostPopularArticles)
    print("1. What are the most popular three articles of all time?")
    for (title, views) in dbCursor.fetchall():
        print("   {} - {} views".format(title, views))
    
    print("")
    
    #2. Who are the most popular article authors of all time?
    #Join articles,log and authors tables count appearance of authors.name when author id's match and the website was visited
    sqlMostPopularAuthors = """
        select authors.name, count(*) as views 
            from articles, authors, log 
            where articles.author = authors.id and log.path like '%' || articles.slug 
            group by authors.name order by views desc;
    """
    dbCursor.execute(sqlMostPopularAuthors)
    print("2. Who are the most popular article authors of all time?")
    for (name, views) in dbCursor.fetchall():
        print("   {} - {} views".format(name, views))
    
    print("")
    
    
    #3. On which days did more than 1% of requests lead to errors?
    #Join articles,log and authors tables count appearance of authors.name when author id's match and the website was visited
    #dbCursor.execute("")
    print("3. On which days did more than 1% of requests lead to errors?")
    #print(dbCursor.fetchall())



if __name__ == "__main__":
    main()