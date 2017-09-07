# search
@api.route('/search', methods=['POST','GET'])
@allow_cross_domain
def search_api():
    rd = request.get_data().decode()
    print(rd)
    rd = json.loads(rd)
    searched = search.search_api(rd['sentence'])
    return jsonify(searched)
    # return jsonify(searched)

@api.route('/search/<s>', methods=['GET'])
@allow_cross_domain
def get_search_api(s):
    searched = search.search_api(s)
    return jsonify(searched)
