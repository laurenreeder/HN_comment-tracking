import psycopg2

# Try to connect

try:
    conn = psycopg2.connect("dbname='hacker_news' user='postgres' host='localhost' password='1234'")
except:
    print "I am unable to connect to the database."

cur = conn.cursor()

try:
  cur.execute("""SELECT DISTINCT ON(created_at) created_at, author FROM hn_comments WHERE comment_text LIKE '%segment.com%' OR comment_text LIKE '%segment.io%' ORDER BY created_at ASC""")
  # cur.execute("""SELECT created_at, COUNT(*) from hn_comments WHERE comment_text LIKE '%segment.io%' ORDER BY created_at""")
  # cur.execute("""SELECT COUNT(*) from hn_comments""")
except:
  print "Could not run select command"

rows = cur.fetchall()

for row in rows:
  print "r: ", row