from flask import Blueprint,jsonify,request

from tool.domain import allow_cross_domain

from db.ntext.create import Ntext,NewNtext


ntext = Blueprint('ntext',__name__)



# 获取某个指定的单词
@ntext.route('/create', methods=['POST','OPTIONS'])
@allow_cross_domain
def new_ntext():
    print(request.json)
    if request.json!=None and request.json['secret']=='sj':
        NewNtext(request.json).save_all()
        return 'win'
    else:
        return 'fail'

# 获取某个指定的试题
@ntext.route('/show/<id>', methods=['GET'])
@allow_cross_domain
def show_ntext(id):
    # print(NewNtext('s').show_ntext())
    return jsonify(NewNtext('s').show_ntext_dtails(id))


# 获取所有的试题
@ntext.route('/all', methods=['GET'])
@allow_cross_domain
def show_all_ntext():
    return jsonify(NewNtext('s').show_all())
