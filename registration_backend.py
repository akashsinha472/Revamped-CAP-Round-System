import mysql.connector as c

def connect():
       con = c.connect(host="localhost", user="root", passwd="", database="sdp")
       db = con.cursor()
       db.execute("create table if not exists registered(Application_ID VARCHAR(20) UNIQUE KEY NOT NULL,Registration_ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,Password TEXT)")
       con.commit()
       con.close()                                                                        

def update(password='',application_id=''):
       con = c.connect(host="localhost", user="root", passwd="", database="sdp")
       db = con.cursor()

       db.execute("UPDATE registered SET password =%s where application_id=%s",(password,application_id))

       con.commit()
       con.close()

def search(application_id=''):
       con = c.connect(host="localhost", user="root", passwd="", database="sdp")
       db = con.cursor()

       db.execute("SELECT registration_id FROM registered WHERE application_id = %s and application_id = %s ", (application_id,application_id))
       rows = db.fetchall()
       if rows==[]:
           return ("You are not eligible to register as you didn't appear for the entrance exam")
       else:
           return("Your registration id is: "+str(rows[0][0])+"\nNote down for login purpose.")

def searchlogin(registration_id,password):
       con = c.connect(host="localhost", user="root", passwd="", database="sdp")
       db = con.cursor()

       db.execute("SELECT * FROM registered WHERE registration_id = %s and registration_id = %s ", (registration_id,registration_id))
       rows = db.fetchall()
       if len(rows)!=0:
              db.execute("SELECT * FROM registered WHERE registration_id = %s and password = %s ", (registration_id,password))
              r=db.fetchall()
              if len(r)!=0:
                     return ("1")
              else:
                     return("Incorrect password.")
       else:
              return(" You have not registered for the CAP Round process.Register first and then Login.")

def updatechoice(password='',registration_id='',choice1='',choice2='',choice3='',choice4='',choice5='',choice6='',choice7='',choice8='',choice9='',choice10=''):
       con = c.connect(host="localhost", user="root", passwd="", database="sdp")
       db = con.cursor()
       db.execute("SELECT * FROM registered WHERE registration_id = %s and registration_id = %s ", (registration_id,registration_id))
       rows = db.fetchall()
       if len(rows)!=0:
              db.execute("SELECT * FROM registered WHERE registration_id = %s and password = %s ", (registration_id,password))
              r=db.fetchall()
              if len(r)==0:
                     return("Incorrect password.")
              else:
                     db.execute("SELECT choice1 from registered where registration_id = %s and registration_id = %s ", (registration_id,registration_id))
                     r1=db.fetchall()
                     if(r1[0][0] is None):
                            db.execute("UPDATE registered SET choice1 =%s, choice2 =%s, choice3 =%s, choice4 =%s, choice5 =%s, choice6 =%s, choice7 =%s, choice8 =%s, choice9 =%s, choice10 =%s where registration_id=%s and choice1 is NULL",(choice1,choice2,choice3,choice4,choice5,choice6,choice7,choice8,choice9,choice10,registration_id))
                            con.commit()
                            con.close()
                            return("1")
                     else:
                            return("You have already submitted the choices. Can't submit again.")

       else:
              return("Incorrect Registration ID.")

def allotment(password='',registration_id=''):
       con = c.connect(host="localhost", user="root", passwd="", database="sdp")
       db = con.cursor()
       db.execute("SELECT * FROM registered WHERE registration_id = %s and registration_id = %s ", (registration_id,registration_id))
       rows = db.fetchall()
       if len(rows)!=0:
              db.execute("SELECT * FROM registered WHERE registration_id = %s and password = %s ", (registration_id,password))
              r=db.fetchall()
              if len(r)==0:
                     return("Incorrect password.")
              else:
                     db.execute("SELECT * from registered where registration_id = %s and registration_id = %s ", (registration_id,registration_id))
                     r1=db.fetchall()
                     if(r1[0][4] is None):
                            return("NO ALLOTMENT\nYou didn't submit the choices during choice filling period.")
                     else:
                            return("SEAT ALLOTEMENT STATUS:\nInstitute and Branch:"+str(r1[0][4])+"\nPlease select YES to accept the seat and report to institute before 25/01/2022\nSelect NO to reject\n\nIn case of query contact at: 9876543210")

       else:
              return("Incorrect Registration ID.")


def searchinstitutelogin(username,password):
       con = c.connect(host="localhost", user="root", passwd="", database="sdp")
       db = con.cursor()

       db.execute("SELECT * FROM institute WHERE username = %s and username = %s ", (username,username))
       rows = db.fetchall()
       if len(rows)!=0:
              db.execute("SELECT * FROM institute WHERE username = %s and password = %s ", (username,password))
              r=db.fetchall()
              if len(r)!=0:
                     return (r[0][2])
              else:
                     return("Incorrect password.")
       else:
              return("Your institute is not registered for the CAP Round process.")

connect()