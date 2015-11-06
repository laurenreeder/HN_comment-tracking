import psycopg2
import matplotlib.pyplot as plt
import sys

# Try to connect

try:
    conn = psycopg2.connect("dbname='hacker_news' user='postgres' host='localhost' password='1234'")
except:
    print "I am unable to connect to the database."

cur = conn.cursor()

input_var = raw_input("Enter search term: ")
input_var = "'%"+input_var+"%'"   # format SQL string

try:
  cur.execute("""SELECT DISTINCT ON(created_at) created_at, author FROM hn_comments WHERE comment_text LIKE %s ORDER BY created_at ASC""" % input_var)
except:
  print "Could not run select command"

rows = cur.fetchall()

for row in rows:
  print "r: ", row

