import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
import sys


# matplotlib.style.use('ggplot')

try:
    conn = psycopg2.connect("dbname='hacker_news' user='postgres' host='localhost' password='1234'")
except:
    print "Unable to connect to the database."

cur = conn.cursor()

# input_var = raw_input("Enter single search term or phrase: ")
# input_var = "'%"+input_var+"%'"   # format SQL string

try:
  # cur.execute("""SELECT DISTINCT ON(created_at) created_at, author FROM hn_comments WHERE comment_text LIKE %s ORDER BY created_at ASC""" % input_var)
  # hardcoded for testing
  cur.execute("""SELECT DISTINCT ON(created_at) created_at, author FROM hn_comments WHERE comment_text LIKE '%segment.io%' ORDER BY created_at ASC""")
except:
  print "Could not run select command"

rows = cur.fetchall()

# for row in rows:
#   print "r: ", row[0]
dates = tuple(x[0] for x in rows)

ts = pd.Series(dates)
ts.plot()

plt.show()


cur.close()
conn.close()