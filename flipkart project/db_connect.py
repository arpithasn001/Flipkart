def create_db(cursor,dataBaseName):
    db=f"create database {dataBaseName}"
    cursor.execute(db)

def create_table(cursor,customer_comments):
    tb=f"CREATE TABLE IF NOT EXISTS {customer_comments} (Comment varchar(1000),Name varchar(100),Price varchar(30),Comment_H varchar(400),DateTime varchar(200),Name_P varchar(400));"
    cursor.execute(tb)

def insert_table(cursor,customer_comments,lst):
    insert_query=f"INSERT INTO {customer_comments}(Comment,Name,Price,Comment_H,DateTime,Name_P) VALUES (%(Comment)s, %(Name)s, %(Price)s, %(Comment_H)s, %(DateTime)s, %(Name_P)s);"  
    cursor.executemany(insert_query,lst) 