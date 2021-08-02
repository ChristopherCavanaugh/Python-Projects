import sqlite3

#creating database called databasedrill
conn = sqlite3.connect("databasedrill.db")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_drills( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, col_drilldata STRING)")
    # this creates a table called drills with a primary key and a column to
    #collect string data
    conn.commit()
conn.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


#this will print both the documents with the txt extention
for x in fileList:
  if ".txt" in x:
        print(x)

conn = sqlite3.connect("databasedrill.db")

with conn: #adding txt docs to table drills in column drill data
    cur = conn.cursor()
    if ".txt" in x:
        cur.execute("INSERT INTO tbl_drills(col_drilldata) VALUES")
    conn.commit()
conn.close()

conn = sqlite3.connect("databasedrill.db")

with conn: #querying database to show the txt files
    cur = conn.cursor()
    if ".txt" in x:
        cur.execute("SELECT col_drilldata FROM tbl_drills")
    varFiles = cur.fetchall()
    for item in varFiles:
        msg = "Text Files: {}".format(item[0])
        print(msg)


