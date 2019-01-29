import time
from firebase import firebase
firebase = firebase.FirebaseApplication('https://autopark-alpr.firebaseio.com', None)
result = firebase.get('/placas', 'ABC1235')

ts = time.time()
print (ts)

data = {'bernard':'meunome'}
result = firebase.post('/users/teste', data)

print(result)