from googleapiclient.discovery import build
import json
import time
import os
import mysql.connector

api_key = os.environ.get('youtube_api_key')           # get youtube Data API key from the environment variables

keyword = 'anime'

youtube = build('youtube','v3',developerKey=api_key)  #Creating a YouTube service Object

mydb = mysql.connector.connect(  #Creating Mysql connection Object
  host="localhost",
  user="root",
  password="",
  database="youtubetask"
)

while True:
    request = youtube.search().list(  #creating a request object with 
           part = 'snippet',   
            q = keyword,
            order = 'date',
            type = 'video',
            publishedAfter = '2020-03-01T00:00:00Z', 
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
            sql = "INSERT INTO videos  VALUES (%s, %s, %s, %s, %s, %s, %s ,%s)"  #Necessary Details are added into the Database
            mycursor.execute(sql,argument)
        except Exception as ex:
            print(ex)
        finally:
             mydb.commit()
    time.sleep(30) #30 seconds gap between each API request