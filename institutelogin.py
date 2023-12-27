from tkinter import*
import tkinter.messagebox  
import registration_backend
import os
import webbrowser

class Login():
       def __init__(self, master):
              self.master = master
              self.master.title('INSTITUTE LOGIN')
              self.master.geometry('1350x750')
              self.master.config(bg = 'light blue')
              
              def information():
              #========================================================Variables=====================================================================
                     self.username = StringVar()
                     self.password = StringVar()
                     


               #==========================================================Functions====================================================================


                     def Exit():
                            Exit = tkinter.messagebox.askyesno("Institute Login System", "Confirm if you want to Exit")
                            if Exit > 0:
                                   self.master.destroy()
                                   return 


                     def Search():
                            message=registration_backend.searchinstitutelogin(self.username.get(),self.password.get())
                            if message[0]!='h':
                                tkinter.messagebox.showinfo("Institute Login System",message)
                            else:
                                tkinter.messagebox.showinfo("Institute Login System", "LOGIN SUCCESSFUL")
                                webbrowser.open(message)
            
                    

                     def Forgot():
                        tkinter.messagebox.showinfo("Institute Login System","Please contact DTE helpline section.")


                     


                     #============================================================Frames=====================================================================

                     self.Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial',20,'bold'), \
                                                  bg = 'light blue',bd = 15, relief = 'ridge')
                     self.Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

                     self.Frame_1 = LabelFrame(self.Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                                               relief = 'ridge', bd = 10, bg = 'light blue', text = 'INSTITUTE LOGIN')
                     self.Frame_1.grid(row = 1, column = 0, padx = 10)                 
                     
                     self.Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial',10,'bold'), \
                                               bg = 'light blue', relief = 'ridge', bd = 13)
                     self.Frame_3.grid(row = 2, column = 0, pady = 10)


                     
                     #========================================================Labels of Frame_1========================================================
                     self.Label_username = Label(self.Frame_1, text = 'Username', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_username.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                     self.Label_password = Label(self.Frame_1, text = 'Password', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_password.grid(row = 1, column = 0, sticky = W, padx = 20)
 


                     #========================================================Entries of Frame_1========================================================
                     self.Entry_username = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.username)
                     self.Entry_username.grid(row = 0, column = 1, padx = 10, pady = 5)
                     self.Entry_password = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.password)
                     self.Entry_password.grid(row = 1, column = 1, padx = 10, pady = 5)






                     #========================================================Buttons of self.Frame_3=========================================================
                     self.btnSave = Button(self.Frame_3, text = 'VIEW ALLOTED STUDENTS', font = ('arial',17,'bold'), width = 32, command = Search)
                     self.btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
                     self.btnExit = Button(self.Frame_3, text = 'BACK', font = ('arial',17,'bold'), width = 8, command = Exit)
                     self.btnExit.grid(row = 0, column = 6, padx = 10, pady = 10)
                     self.btnForgot = Button(self.Frame_3, text = 'FORGOT PASSWORD/APPLICATION ID', font = ('arial',17,'bold'), width = 32, command = Forgot)
                     self.btnForgot.grid(row = 0, column = 12, padx = 10, pady = 10)                     



                            
              information()
                     

root = Tk()
obj = Login(root)
root.mainloop()