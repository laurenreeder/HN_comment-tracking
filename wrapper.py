import psycopg2, sys, mpld3, os
import matplotlib.pyplot as plt
from flask import Flask
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build


app = Flask(__name__)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.abspath('hn-comments-104e4b796685.json')
credentials = GoogleCredentials.get_application_default()
service = build('compute', 'v1', credentials=credentials)

@app.route('/')
def get_db_args():
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
    except:
      print "Could not run select command"

    rows = cur.fetchall()
    dates = tuple(x[0] for x in rows)
    visits = [1] * len(dates)
    cumv = np.cumsum(visits)

    plt.plot_date(x=dates, y=cumv, fmt="r-")

  mpld3.show()

  cur.close()
  conn.close()

if __name__ == '__main__':
    app.run()