from atproto import Client,models
import feedparser
import sqlite3
import sys
import time
import os 

def createdb(cur):
    cur.execute('''
CREATE TABLE shared_contents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_time TIMESTAMP,
    comment TEXT,
    success BOOLEAN,
    context TEXT,
    link TEXT
)
''')
    print("Table created succesfully")
    return True

def sendSkeetAndSave(cur,entry):
    client = Client()
    client.login(os.environ.get('BSKY_USERNAME'), os.environ.get('BSKY_PASSWORD'))
    skeet= entry['title']
    embed_external = models.AppBskyEmbedExternal.Main(
                external=models.AppBskyEmbedExternal.External(
                        title=entry['title'],
                        description=entry['description'],
                        uri=entry['link']
                       # thumb=models.blob_ref.BlobRef(
                       #     mime_type="image/jpeg",
                       #     size=1024,
                       #     ref=models.blob_ref.BlobRefLink(
                       #         link="https://www.bilimma.com/wp-content/uploads/2023/09/xcksnvm.jpg"
                       #         )
                       # )
                )
            )

    client.com.atproto.repo.create_record(
        models.ComAtprotoRepoCreateRecord.Data(
            repo=client.me.did,
            collection=models.ids.AppBskyFeedPost,
            record=models.AppBskyFeedPost.Main(
                created_at=client.get_current_time_iso(),
                text=skeet,
                #facets=facets
                embed=embed_external
                )
            )
        )

    print("Skeet posted!")
    ressa = cur.execute("INSERT INTO shared_contents(run_time,comment,success,context,link) VALUES('"+str(run_time)+"','"+title+"',true,'"+title+"','"+link+"');")
    print("Share saved!") 
    return True


db = sqlite3.connect('autoshare.db')
cur = db.cursor()

if(len(sys.argv)>1 and sys.argv[1] == "create-db"):
    createdb(cur)
    db.commit()

    print("Database created successfully!")

    exit()


newsFeed = feedparser.parse(os.environ.get('FEED_URL'));
entry = newsFeed.entries[1]


for entry in newsFeed.entries:
    curr = cur.execute("SELECT * FROM shared_contents WHERE link='"+entry['link']+"'")
    res = curr.fetchone()
    print(res)
    link = entry['link']
    title = entry['title']
    run_time = time.time()
    if(res == None):
        sendSkeetAndSave(cur,entry)
        break

db.commit()


print("bye")

