from tkinter import*
import os
import webbrowser
       
def registration():
       filename = 'python registration_frontend.py'
       os.system(filename)
       
def login():
       filename = 'python login.py'
       os.system(filename)

def video():
       webbrowser.open("https://www.youtube.com/watch?v=-I0LTAeOD-E")

def book():
       webbrowser.open("https://drive.google.com/file/d/1fwnTqh8v4moKHDN3K_Tty5gar82Vyc6r/view?usp=drivesdk")

def institutelogin():
       os.system('python institutelogin.py')       

def home():
       root = Tk()
       root.title('Menu')
       root.geometry('1350x750')
       root.config(bg = 'black')
       
       title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 1000, height = 200, bg = '#ffc300', relief = 'raise', bd = 13)
       title_Frame.place(x=185, y=50) 
       
       title_Label = Label(title_Frame, text = '        CAP 2021-22\n               ', font = ('arial',40,'bold'), bg = '#ffc300')
       title_Label.place(x=185, y=50) 


       #========================================================BUTTONS===================================================================
       Button_1 = Button( text = 'NEW CANDIDATE REGISTRATION', font = ('arial',16,'bold'), width = 30, command = registration, bg='red',fg='white')
       Button_1.place(x=230,y=330)
       Button_2 = Button( text = 'ALREADY REGISTERED CANDIDATE', font = ('arial',16,'bold'), width = 30, command = login, bg='#0000cc',fg='white')
       Button_2.place(x=750,y=330)
       Button_3 = Button( text = 'Click here:\nCandidate registration process video', font = ('arial',16,'bold'), width = 30,height=2, command = video, bg='#006400',fg='white')
       Button_3.place(x=150,y=600)
       Button_4 = Button( text = 'Click here:\nInformation Brochure', font = ('arial',16,'bold'), width = 30,height=2, command = book, bg='#006400',fg='white')
       Button_4.place(x=800,y=600)
       Button_5 = Button( text = 'INSTITUTE LOGIN', font = ('arial',16,'bold'), width = 20, command = institutelogin, bg='#006400',fg='white')
       Button_5.place(x=550,y=270)
       notice = Label(root, text="IMPORTANT NOTICE:\n\nChoice Filling Process for First Year Under Graduate Technical Courses has Started.\n Fill it before 21/01/2022",width=80,height=5, bg="teal", fg="white", font=("ariel", 20, "bold"))
       notice.place(x=0, y=400)           


       root.mainloop()
       
home()