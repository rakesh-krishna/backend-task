from flask import Flask
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/youtubetask' #pymysql://[username]:[password]@[hostname]:[port]/[database]
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class Post(db.Model): # Creating DB Model
    __tablename__ = "videos"
    videoId = db.Column(db.String(12),primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    publishedAt = db.Column(db.String(50))
    channelId = db.Column(db.String(30))
    defaultThumbnail= db.Column(db.String(50))
    mediumThumbnail= db.Column(db.String(50))
    highThumbnail= db.Column(db.String(50))

    def __repr__(self):
        return '<Post %s>' % self.title


class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description","videoId","publishedAt","channelId","defaultThumbnail","mediumThumbnail","highThumbnail")

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()  # Fetching all the videos data from database
        return posts_schema.dump(posts)

api.add_resource(PostListResource, '/videos')
if __name__ == '__main__':
    app.run(debug=True)
