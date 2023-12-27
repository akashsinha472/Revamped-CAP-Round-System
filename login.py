from tkinter import*
import tkinter.messagebox  
import registration_backend
import os

class Login():
       def __init__(self, master):
              self.master = master
              self.master.title('LOGIN')
              self.master.geometry('1350x750')
              self.master.config(bg = 'light blue')
              
              def information():
              #========================================================Variables=====================================================================
                     self.registration_id = StringVar()
                     self.password = StringVar()
                     


               #==========================================================Functions====================================================================


                     def Exit():
                            Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
                            if Exit > 0:
                                   self.master.destroy()
                                   return 


                     def Search():
                            message=registration_backend.searchlogin(self.registration_id.get(),self.password.get())
                            if message[0]!='1':
                                tkinter.messagebox.showinfo("Login System",message)
                            else:
                                tkinter.messagebox.showinfo("Login System", "LOGIN SUCCESSFUL")
                                os.system('python choice.py')
                    

                     def Forgot():
                         os.system("python forgot.py")


                     


                     #============================================================Frames=====================================================================

                     self.Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial',20,'bold'), \
                                                  bg = 'light blue',bd = 15, relief = 'ridge')
                     self.Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

                     self.Frame_1 = LabelFrame(self.Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                                               relief = 'ridge', bd = 10, bg = 'light blue', text = 'LOGIN')
                     self.Frame_1.grid(row = 1, column = 0, padx = 10)                 
                     
                     self.Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial',10,'bold'), \
                                               bg = 'light blue', relief = 'ridge', bd = 13)
                     self.Frame_3.grid(row = 2, column = 0, pady = 10)


                     
                     #========================================================Labels of Frame_1========================================================
                     self.Label_registration_id = Label(self.Frame_1, text = 'Registration ID', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_registration_id.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                     self.Label_password = Label(self.Frame_1, text = 'Password', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_password.grid(row = 1, column = 0, sticky = W, padx = 20)
 


                     #========================================================Entries of Frame_1========================================================
                     self.Entry_registration_id = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.registration_id)
                     self.Entry_registration_id.grid(row = 0, column = 1, padx = 10, pady = 5)
                     self.Entry_password = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.password)
                     self.Entry_password.grid(row = 1, column = 1, padx = 10, pady = 5)






                     #========================================================Buttons of self.Frame_3=========================================================
                     self.btnSave = Button(self.Frame_3, text = 'LOGIN', font = ('arial',17,'bold'), width = 8, command = Search)
                     self.btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
                     self.btnExit = Button(self.Frame_3, text = 'BACK', font = ('arial',17,'bold'), width = 8, command = Exit)
                     self.btnExit.grid(row = 0, column = 6, padx = 10, pady = 10)
                     self.btnForgot = Button(self.Frame_3, text = 'FORGOT PASSWORD/APPLICATION ID', font = ('arial',17,'bold'), width = 32, command = Forgot)
                     self.btnForgot.grid(row = 0, column = 12, padx = 10, pady = 10)                     



                            
              information()
                     

root = Tk()
obj = Login(root)
root.mainloop()