from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import registration_backend

class choice():
       def __init__(self, master):
              self.master = master
              self.master.title('USER HOME')
              self.master.geometry('1350x750')
              self.master.config(bg = 'light blue')
              
              def information():
              #========================================================Variables=====================================================================
                     self.registration_id = StringVar()
                     self.password = StringVar()
                     self.choice1 = StringVar()
                     self.choice2 = StringVar()
                     self.choice3 = StringVar()
                     self.choice4 = StringVar()
                     self.choice5 = StringVar()
                     self.choice6 = StringVar()
                     self.choice7 = StringVar()
                     self.choice8 = StringVar()
                     self.choice9 = StringVar()
                     self.choice10 = StringVar()
                     


               #==========================================================Functions====================================================================


                     def Exit():
                            Exit = tkinter.messagebox.askyesno("Choice Filling", "Confirm if you want to Exit")
                            if Exit > 0:
                                   self.master.destroy()
                                   return 


                     def Search():
                            Exit = tkinter.messagebox.askyesno("Choice Filling", "Are you sure you want to Submit?")                            
                            if Exit > 0:
                                   message=registration_backend.updatechoice(self.password.get(),self.registration_id.get(),self.choice1.get(),self.choice2.get(),self.choice3.get(),self.choice4.get(),self.choice5.get(),self.choice6.get(),self.choice7.get(),self.choice8.get(),self.choice9.get(),self.choice10.get())
                                   if message[0]!='1':
                                          tkinter.messagebox.showinfo("Choice Filling System",message)
                                   else:
                                          tkinter.messagebox.showinfo("Choice Filling System", "CHOICES SUBMITTED SUCCESSFULLY")
                                          self.master.destroy()
                                          return
                     
                     def result():
                            message=registration_backend.allotment(self.password.get(),self.registration_id.get())
                            if message[0]=='S':
                                   tkinter.messagebox.askyesnocancel("Allotment Result System",message)
                            else:
                                   tkinter.messagebox.showinfo("Allotment Result System",message)                          


                     


                     #============================================================Frames=====================================================================
                     self.Frame0 = LabelFrame(self.master, width = 1000, height = 150, font = ('arial',10,'bold'), \
                                                  bg = 'light blue',bd = 15, relief = 'ridge')
                     self.Frame0.place(x=185,y=80)

                     self.Main_Frame = LabelFrame(self.master, width = 1300, height = 500, font = ('arial',20,'bold'), \
                                                  bg = 'light blue',bd = 15, relief = 'ridge')
                     self.Main_Frame.grid(row = 0, column = 0, padx = 150, pady = 250)

                     self.Frame_1 = LabelFrame(self.Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                                               relief = 'ridge', bd = 10, bg = 'light blue', text = 'CHOICE FILLING')
                     self.Frame_1.grid(row = 1, column = 0, padx = 10)                 
                     
                     self.Frame_3 = LabelFrame(self.master, width = 1200, height = 100, font = ('arial',10,'bold'), \
                                               bg = 'light blue', relief = 'ridge', bd = 13)
                     self.Frame_3.place(x=300,y=600)
                     
                     #========================================================Labels of Frame_1========================================================
                     self.frame_0= Label(self.Frame0, text = 'CAP 2021-22 \n            Choice Filling Process has started                ', font = ('arial',30,'bold'), bg = '#00CCCC')
                     self.frame_0.place(x=10, y=10) 
                     self.Label_registration_id = Label(self.Frame_1, text = 'Registration ID', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_registration_id.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
                     self.Label_password = Label(self.Frame_1, text = 'Password', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_password.grid(row = 0, column = 2, sticky = W, padx = 20)
                     self.Label_choice1 = Label(self.Frame_1, text = 'Choice 1', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_choice1.grid(row = 2, column = 0, sticky = W, padx = 20) 
                     self.Label_choice2 = Label(self.Frame_1, text = 'Choice 2', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_choice2.grid(row = 2, column = 2, sticky = W, padx = 20)
                     self.Label_choice3 = Label(self.Frame_1, text = 'Choice 3', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_choice3.grid(row = 3, column = 0, sticky = W, padx = 20)
                     self.Label_choice4 = Label(self.Frame_1, text = 'Choice 4', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_choice4.grid(row = 3, column = 2, sticky = W, padx = 20)
                     self.Label_choice5 = Label(self.Frame_1, text = 'Choice 5', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_choice5.grid(row = 4, column = 0, sticky = W, padx = 20) 
                     self.Label_choice6 = Label(self.Frame_1, text = 'Choice 6', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_choice6.grid(row = 4, column = 2, sticky = W, padx = 20)
                     self.Label_choice7 = Label(self.Frame_1, text = 'Choice 7', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_choice7.grid(row = 5, column = 0, sticky = W, padx = 20)
                     self.Label_choice8 = Label(self.Frame_1, text = 'Choice 8', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_choice8.grid(row = 5, column = 2, sticky = W, padx = 20)
                     self.Label_choice9 = Label(self.Frame_1, text = 'Choice 9', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_choice9.grid(row = 6, column = 0, sticky = W, padx = 20)
                     self.Label_choice10 = Label(self.Frame_1, text = 'Choice 10', font = ('arial',20,'bold'),  bg = 'navajowhite')
                     self.Label_choice10.grid(row = 6, column = 2, sticky = W, padx = 20)

                     #========================================================Entries of Frame_1========================================================
                     self.Entry_registration_id = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.registration_id)
                     self.Entry_registration_id.grid(row = 0, column = 1, padx = 10, pady = 5)
                     self.Entry_password = Entry(self.Frame_1, font = ('arial',17,'bold'), textvariable = self.password)
                     self.Entry_password.grid(row = 0, column = 3, padx = 10, pady = 5)
                     self.Entry_choice1 = ttk.Combobox(self.Frame_1, values = ('VIT Pune-CS','COEP-CS','VJTI-CS','PICT-CS','SPIT-CS','VIT Pune-IT','COEP-IT','VJTI-IT','PICT-IT','SPIT-IT'), font = ('arial',13,'bold'), width = 23, textvariable = self.choice1 )
                     self.Entry_choice1.grid(row = 2, column = 1)                     
                     self.Entry_choice2 = ttk.Combobox(self.Frame_1, values = ('VIT Pune-CS','COEP-CS','VJTI-CS','PICT-CS','SPIT-CS','VIT Pune-IT','COEP-IT','VJTI-IT','PICT-IT','SPIT-IT'), font = ('arial',13,'bold'), width = 23, textvariable = self.choice2 )
                     self.Entry_choice2.grid(row = 2, column = 3)  
                     self.Entry_choice3 = ttk.Combobox(self.Frame_1, values = ('VIT Pune-CS','COEP-CS','VJTI-CS','PICT-CS','SPIT-CS','VIT Pune-IT','COEP-IT','VJTI-IT','PICT-IT','SPIT-IT'), font = ('arial',13,'bold'), width = 23, textvariable = self.choice3 )
                     self.Entry_choice3.grid(row = 3, column = 1)  
                     self.Entry_choice4 = ttk.Combobox(self.Frame_1, values = ('VIT Pune-CS','COEP-CS','VJTI-CS','PICT-CS','SPIT-CS','VIT Pune-IT','COEP-IT','VJTI-IT','PICT-IT','SPIT-IT'), font = ('arial',13,'bold'), width = 23, textvariable = self.choice4 )
                     self.Entry_choice4.grid(row = 3, column = 3)  
                     self.Entry_choice5 = ttk.Combobox(self.Frame_1, values = ('VIT Pune-CS','COEP-CS','VJTI-CS','PICT-CS','SPIT-CS','VIT Pune-IT','COEP-IT','VJTI-IT','PICT-IT','SPIT-IT'), font = ('arial',13,'bold'), width = 23, textvariable = self.choice5 )
                     self.Entry_choice5.grid(row = 4, column = 1)                    
                     self.Entry_choice6 = ttk.Combobox(self.Frame_1, values = ('VIT Pune-CS','COEP-CS','VJTI-CS','PICT-CS','SPIT-CS','VIT Pune-IT','COEP-IT','VJTI-IT','PICT-IT','SPIT-IT'), font = ('arial',13,'bold'), width = 23, textvariable = self.choice6 )
                     self.Entry_choice6.grid(row = 4, column = 3)  
                     self.Entry_choice7 = ttk.Combobox(self.Frame_1, values = ('VIT Pune-CS','COEP-CS','VJTI-CS','PICT-CS','SPIT-CS','VIT Pune-IT','COEP-IT','VJTI-IT','PICT-IT','SPIT-IT'), font = ('arial',13,'bold'), width = 23, textvariable = self.choice7 )
                     self.Entry_choice7.grid(row = 5, column = 1)  
                     self.Entry_choice8 = ttk.Combobox(self.Frame_1, values = ('VIT Pune-CS','COEP-CS','VJTI-CS','PICT-CS','SPIT-CS','VIT Pune-IT','COEP-IT','VJTI-IT','PICT-IT','SPIT-IT'), font = ('arial',13,'bold'), width = 23, textvariable = self.choice8 )
                     self.Entry_choice8.grid(row = 5, column = 3) 
                     self.Entry_choice9 = ttk.Combobox(self.Frame_1, values = ('VIT Pune-CS','COEP-CS','VJTI-CS','PICT-CS','SPIT-CS','VIT Pune-IT','COEP-IT','VJTI-IT','PICT-IT','SPIT-IT'), font = ('arial',13,'bold'), width = 23, textvariable = self.choice9 )
                     self.Entry_choice9.grid(row = 6, column = 1)
                     self.Entry_choice10 = ttk.Combobox(self.Frame_1, values = ('VIT Pune-CS','COEP-CS','VJTI-CS','PICT-CS','SPIT-CS','VIT Pune-IT','COEP-IT','VJTI-IT','PICT-IT','SPIT-IT'), font = ('arial',13,'bold'), width = 23, textvariable = self.choice10 )
                     self.Entry_choice10.grid(row = 6, column = 3) 




                     #========================================================Buttons of self.Frame_3=========================================================
                     self.btnSave = Button(self.Frame_3, text = 'SUBMIT', font = ('arial',17,'bold'), width = 8, command = Search)
                     self.btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
                     self.btnexit = Button( text = 'LOGOUT', font = ('arial',17,'bold'), width = 20, command = Exit, bg='#0000cc',fg='white')
                     self.btnexit.place(x=1000,y=25)                    
                     self.btnresult = Button( text = 'VIEW ALLOTMENT', font = ('arial',17,'bold'), width = 20, command = result, bg='#0000cc',fg='white')
                     self.btnresult.place(x=900,y=600) 

                            
              information()
                     

root = Tk()
obj = choice(root)
root.mainloop()