from tool.mymongo import ssh


db = 'mynihongo2'
c_db = ssh(db,'sentences')

for x in c_db.find():
    words_list = x['words_list']
    w = [word['word_Nx'] for word in words_list if word['word_Nx'][0]=='N']
    # print(w)
    if w==[]:
        c_db.update({'_id':x['_id']},{'$set':{'sentence_Nx':'not in Nx'}})
    else:
        sentence_Nx = sorted(w)[0]
        c_db.update({'_id':x['_id']},{'$set':{'sentence_Nx':sentence_Nx}})
