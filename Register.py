import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("facedetect-1c5b3-firebase-adminsdk-cjkfa-a2c9e0777b.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def s_data(sid,fid):
    global db
    obj = {
        'Student id' : sid,
        'Fid' : fid
        }
    doc_ref = db.collection(u'User').document(obj['Student id'])
    doc_ref.set(obj)

def save_attendance(course,date,students):
    global db
    obj = {
        'Course':course,
        'Time' : date,
        'Students':students
    }
    doc_ref = db.collection(u'Attendance').document(obj['Time'])
    print(doc_ref.set(obj))




def g_data():
    obj_array = []
    doc_ref = db.collection(u'User')
    doc = doc_ref.get()
    for i in doc:
        obj_array.append(i.to_dict())
    print(obj_array)
    save_attendance("SE221","19-04-23",obj_array)
    return obj_array

if __name__ == "__main__":
    #s_data("Sourav","880")
    g_data()