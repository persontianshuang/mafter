from flask import Blueprint,jsonify

from tool.domain import allow_cross_domain

from db.subFlow.flow import Flow,MgFlow

videos = Blueprint('videos',__name__)



# 列出所有视频流
@videos.route('/', methods=['GET'])
@allow_cross_domain
def all_videos():
    all = MgFlow().all_videos()
    return jsonify(all)

# 获取某个指定的视频流的所有句子
@videos.route('/<id>/sentences', methods=['GET'])
@allow_cross_domain
def video_sentence_detail(id):
    v_d = MgFlow().a_video_sentences(id)
    return jsonify(v_d)





# 获取某个指定的视频的信息
@videos.route('/<id>', methods=['GET'])
@allow_cross_domain
def video_detail(id):
    v_a = MgFlow().a_video(id)
    return jsonify(v_a)

# # 新建一个视频流
# @videos.route('/', methods=['POST'])
# @allow_cross_domain
# def video_list():
#     v_l = v.video_list()
#     return jsonify({'succuss':'ok'})
#
# # 获取某个指定的视频流
# @videos.route('/<id>', methods=['GET'])
# @allow_cross_domain
# def video_detail(id):
#     # 594e47b1d9f0920d10dfdf7e
#     v_d = v.video_detail(video_id)
#     return jsonify(v_d)
#

