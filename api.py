from flask import Flask, jsonify, make_response, request, abort,render_template
import pymongo
import requests
import json
import bson
import time
import random
import re

from tool.domain import allow_cross_domain
# 转移
# 静态文件的放置路径，可根据实际情况设置，这里设置为默认路径：'./static/'
api = Flask(__name__, static_url_path='')

# root
@api.route('/', methods=['GET'])
@allow_cross_domain
def root():
    return render_template('index.html')

# @api.route('/ppost', methods=['POST','OPTIONS'])
# @allow_cross_domain
# def text():
#     if request.json!=None:
#         print(request.json)
#         print(type(request.json))
#
#     return jsonify({'l': 'gkugku'})

from app.videos import videos
from app.sentences import sentences
from app.words import words
from app.ntext import ntext

api.register_blueprint(videos,url_prefix='/videos')
api.register_blueprint(sentences,url_prefix='/sentences')
api.register_blueprint(words,url_prefix='/words')
api.register_blueprint(ntext,url_prefix='/ntext')

if __name__ == '__main__':
    # api.run(debug=True,host='0.0.0.0',)
    api.run(host='0.0.0.0',port=8768)
    # api.run(host='0.0.0.0'),port=8888
