
# music
@api.route('/music/<music_id>', methods=['GET'])
@allow_cross_domain
def music_detail(music_id):
    # 594e47b1d9f0920d10dfdf7e
    m_d = m.music_detail(music_id)
    return jsonify(m_d)

@api.route('/musicurl/<music_id>', methods=['GET'])
@allow_cross_domain
def music_url(music_id):
    # 594e47b1d9f0920d10dfdf7e
    m_u = m.music_url(music_id)
    return jsonify(m_u)

@api.route('/musiclist', methods=['GET'])
@allow_cross_domain
def music_list():
    m_l = m.music_list()
    return jsonify(m_l)
