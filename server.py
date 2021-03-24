from googleapiclient.discovery import build
import json
import time
import os
import mysql.connector
api_key = os.environ.get('youtube_api_key')
print(api_key)
youtube = build('youtube','v3',developerKey=api_key)
keyword = 'anime'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="youtubetask"
)
while True:
    print('while')

    request = youtube.search().list(
           part = 'snippet',
            q = keyword,
            order = 'date',
            type = 'video',
            maxResults	= 50
        )
    data = request.execute()
    mycursor = mydb.cursor()
    for i in range(len(data['items'])):
        try:
            argument = []
            argument.append(data['items'][i]['id']['videoId'])
            argument.append(data['items'][i]['snippet']['title'])
            argument.append(data['items'][i]['snippet']['description'])
            argument.append(data['items'][i]['snippet']['publishedAt'])
            argument.append(data['items'][i]['snippet']['channelId'])
            argument.append(data['items'][i]['snippet']['thumbnails']['default']['url'])
            argument.append(data['items'][i]['snippet']['thumbnails']['medium']['url'])
            argument.append(data['items'][i]['snippet']['thumbnails']['high']['url'])
            sql = "INSERT INTO videos  VALUES (%s, %s, %s, %s, %s, %s, %s ,%s)"
            mycursor.execute(sql,argument)
            print(i)
        except Exception as ex:
            print(ex)
        finally:
             mydb.commit()
    time.sleep(30)
    print('after sleep')