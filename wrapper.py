import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys


# matplotlib.style.use('ggplot')

try:
    conn = psycopg2.connect("dbname='hacker_news' user='postgres' host='localhost' password='1234'")
except:
    print "Unable to connect to the database."

cur = conn.cursor()

input_var = raw_input("Enter single search term or phrase, separated by commas: ")
inputs = input_var.split(',')

for input_i in inputs:
  input_i = input_i.strip()
  input_i = "'%"+input_i+"%'"   # format SQL string
  try:
    cur.execute("""SELECT DISTINCT ON(created_at) created_at, author FROM hn_comments WHERE comment_text LIKE %s ORDER BY created_at ASC""" % input_i)
    # hardcoded for testing
    # cur.execute("""SELECT DISTINCT ON(created_at) created_at, author FROM hn_comments WHERE comment_text LIKE '%segment.io%' ORDER BY created_at ASC""")
  except:
    print "Could not run select command"

  rows = cur.fetchall()
  dates = tuple(x[0] for x in rows)
  visits = [1] * len(dates)
  cumv = np.cumsum(visits)

  plt.plot_date(x=dates, y=cumv, fmt="r-")

# messing with ticks
# x = range(len(dates))
# plt.xticks(x, dates)
# locs, labels = plt.xticks()
# plt.setp(labels, rotation=90)

plt.show()


cur.close()
conn.close()