from firebase import firebase
import time
import mysql.connector

# Initialize Firebase
firebase = firebase.FirebaseApplication('https://manhole-bc7a9-default-rtdb.firebaseio.com', None)


def read_firebase():
    # Read data from /sensor/dht
    result = firebase.get('/manhole', None)

    print("Data from Firebase:")
    print(result)

    # Access individual values
    if result:
        lmt = result.get('lmt')
        vib = result.get('vib')
        ir = result.get('ir')
        pitch = result.get('pitch')
        roll = result.get('roll')
        lat = result.get('lat')
        lan = result.get('lan')



        conn = mysql.connector.connect(user='root', password='', host='localhost', database='manhole')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO iotdata VALUES ('','" + str(lmt) + "','" + str(vib) + "','" + str(ir) + "','" + str(
                pitch) + "','" + str(roll) + "','" + str(lat) + "','"+str(lan)+"')")
        conn.commit()
        conn.close()


while True:
    read_firebase()

    time.sleep(5)
