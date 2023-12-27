from tkinter import*
import tkinter.messagebox  
import registration_backend

class Registration():
       def __init__(self, master):
              self.master = master
              self.master.title('REGISTRATION')
              self.master.geometry('1350x750')
              self.master.config(bg = 'light blue')
              
              def information():
              #========================================================Variables=====================================================================
                     self.application_id = StringVar()
                     self.password = StringVar()
                     


               #==========================================================Functions====================================================================


                     def Exit():
                            Exit = tkinter.messagebox.askyesno("Registration System", "Confirm if you want to Exit")
                            if Exit > 0:
                                   self.master.destroy()
                                   return 


                     def Search_and_Update():
                            message=registration_backend.search(self.application_id.get())
                                   
                            if(len(self.password.get()) != 0):
                               registration_backend.update(self.password.get(),self.application_id.get())
                            if message[3]=='r':
                                tkinter.messagebox.showinfo("Registration System","You have successfully registered.\nYour password is: "+self.password.get()+"\n"+message)
                            else:
                                tkinter.messagebox.showinfo("Registration System", message)


                     


                     #============================================================Frames=====================================================================

                     self.Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial',20,'bold'), \
                                                  bg = 'light blue',bd = 15, relief = 'ridge')
                     self.Main_Frame.grid(row = 0, column = 0, padx = 10, pady = 20)

                     self.Frame_1 = LabelFrame(self.Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                                               relief = 'ridge', bd = 10, bg = 'light blue', text = 'REGISTER ')
                     self.Frame_1.grid(row = 1, column = 0, padx = 10)                 
                     
                     self.Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial',10,'bold'), \
                                               bg = 'light blue', relief = 'ridge', bd = 13)
                     self.Frame_3.grid(row = 2, column = 0, pady = 10)


                     
                     #========================================================Labels of Frame_1========================================================
                     self.Label_application_id = Label(self.Frame_1, text = 'Application ID', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_application_id.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                     self.Label_password = Label(self.Frame_1, text = 'Create New Password', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_password.grid(row = 1, column = 0, sticky = W, padx = 20)
 


                     #========================================================Entries of Frame_1========================================================
                     self.Entry_application_id = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.application_id)
                     self.Entry_application_id.grid(row = 0, column = 1, padx = 10, pady = 5)
                     self.Entry_password = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.password)
                     self.Entry_password.grid(row = 1, column = 1, padx = 10, pady = 5)






                     #========================================================Buttons of self.Frame_3=========================================================
                     self.btnSave = Button(self.Frame_3, text = 'REGISTER', font = ('arial',17,'bold'), width = 8, command = Search_and_Update)
                     self.btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
                     self.btnExit = Button(self.Frame_3, text = 'BACK', font = ('arial',17,'bold'), width = 8, command = Exit)
                     self.btnExit.grid(row = 0, column = 6, padx = 10, pady = 10)



                            
              information()
                     

root = Tk()
obj = Registration(root)
root.mainloop()
