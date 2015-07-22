import os
from tornado import ioloop,web
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId

# Define MONGO DB connection url and DB name
# AWS_MONGODB_DB_URL =
#AWS_APP_NAME =
MONGODB_DB_URL = os.environ.get('AWS_MONGODB_DB_URL') if os.environ.get('AWS_MONGODB_DB_URL') else 'mongodb://localhost:27017/'
MONGODB_DB_NAME = os.environ.get('AWS_APP_NAME') if os.environ.get('AWS_APP_NAME') else 'app'
 
# Connect to MongoDB
client = MongoClient(MONGODB_DB_URL)
db = client[MONGODB_DB_NAME]
 

class IndexHandler(web.RequestHandler):
    def get(self):
        self.write("Remote Sensor Application!!")


# Responsible for persisting and finding users from MongoDB
class UsersHandler(web.RequestHandler):
    def get(self):
        users = db.users.find()
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(list(users),default=json_util.default))
 
    def post(self):
        user_data = json.loads(self.request.body)
        user_id = db.users.insert(user_data)
        print('user created with id ' + str(user_id))
        self.set_header("Content-Type", "application/json")
        self.set_status(201)


# Handler for individual Users
class UserHandler(web.RequestHandler):
    def get(self , story_id):
        user = db.users.find_one({"_id":ObjectId(str(story_id))})
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps((story),default=json_util.default))  
 
settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "/app/js"),
    "debug" : True
}

application = web.Application([
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
    (r'/api/v1/users',UsersHandler),
    (r'/api/v1/stories/(.*)', UserHandler)
],**settings)      
 
if __name__ == "__main__":
    port = 9515
    application.listen(port)
    print('server running on http://localhost:{}'.format(port))
    ioloop.IOLoop.instance().start()
