from db.config import _Db

from db.sentences.sentence import Sentences
from db.subFlow.flow import Flow
# for x in _Db['sentences'].find():
#     print(x)


# for x in Sentences.objects.all():
#     x.type = 'video'
#     x.save()

# for x in Flow.objects.all():
#     x.type = 'video'
#     x.save()

new_flow = Flow()
new_flow.name = '能力考N3'
new_flow.type = 'ntext'
new_flow.save()
