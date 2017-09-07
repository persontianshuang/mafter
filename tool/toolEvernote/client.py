
from evernote.api.client import EvernoteClient
# import evernote.edam.notestore.ttypes as Type

dev_token = "S=s1:U=93de4:E=164ada01725:C=15d55eee978:P=1cd:A=en-devtoken:V=2:H=d76e98edf6389e9b479302d27ecc8195"
client = EvernoteClient(token=dev_token)

# user的名字
userStore = client.get_user_store()
user = userStore.getUser()
print(user.username)
# 列出笔记本的名字
noteStore = client.get_note_store()
notebooks = noteStore.listNotebooks()
for n in notebooks:
    print(n.name)

# 创建笔记本
noteStore = client.get_note_store()
# notebook = Type.Notebook()
notebook.name = "My Notebook"
notebook = noteStore.createNotebook(notebook)
print(notebook.guid)
