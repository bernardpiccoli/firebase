# pip install --upgrade firebase-admin
# pip install google-cloud-firestore

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'toll').document(u'QWE1234')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815,
    u'passagens': [
        {u'dia':u'12',u'hora':u'11:11'},
        {u'dia':u'12',u'hora':u'11:11'},
        ]
})

users_ref = db.collection(u'users')
docs = users_ref.get()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))