import os
import logging
from flask import Flask
from flask_restplus import Api
from pymongo import MongoClient
from flask_mail import Mail

#Creates the flask object
application = Flask(__name__)

#Load configuration object for dev by default
application.config.from_object(os.getenv('FLASK_ENVIRONMENT', 'config.Development'))

#Create the mail object
mail = Mail(application)

#MongoDB connection
mongo_conn = MongoClient(application.config['MONGO_URI'])
mongo_db = mongo_conn[application.config['DB_NAME']]

#Basic Logger
FORMAT = '%(asctime)s %(module)s %(funcName)s %(message)s'
logging.basicConfig(filename="QD_app.log",
                    format=FORMAT,
                    filemode='w')
logger = logging.getLogger()

#api to setup flask restplus
api = Api(application, title='QuickDealz', description='QuickDealz', version=1.0)

