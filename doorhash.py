from hashlib import md5
import csv
def checkGuest(guestId):
    dc={}
    with open('dc', newline='') as content_file:
        rc=csv.DictReader(content_file, delimiter=' ')
        dc=rc
        for row in rc:
            if row['id']==md5(str(guestId).encode()).hexdigest():
                return True;
        else:
            return False
def addGuest(guestName, guestId):
    with open('dc', 'a') as csvfile:
        fieldnames = ['name', 'id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=' ')
        writer.writerow({'name':guestName, 'id':md5(str(guestId).encode()).hexdigest()})


    

