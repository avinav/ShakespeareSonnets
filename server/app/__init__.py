from flask import Flask
from Query import query
queryIndex = query.getQueryIndex('../util/index_data.p')
app = Flask(__name__)
app.config.from_object('config')

from app import views


