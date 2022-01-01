from tkinter import *
from pymongo import *
import random, string 



class Password():

        
                
        def __init__ (self):


                self.long_line = '__________________________________________________________________________________'
                
                # Please replace <> in self.cluster with your own details in order for this to work
                
                self.cluster = MongoClient('mongodb+srv://<username>:<password>@<cluster_name>.mcpk2.mongodb.net/<database_name>?retryWrites=true&w=majority')
                self.db = self.cluster['db-project']
                self.col = self.db['password-storage']


        def Setup(self):


                        self.t = ('Calibri', 22 , 'bold')
                        self.f = ('Arial', 20, 'underline') 

                        self.root = Tk()

                        self.root.title('Passwords')
                        self.root.geometry('700x600')
                        self.root.resizable(False,False)

        
        def StartUp(self):


                                self.imageo = PhotoImage(file = '/Users/radix/Desktop/python macos /Python macos/junk/sea-edge-79ab30e2 Large.png')
                                self.imageLabel = Label(self.root, image  = self.imageo)
                                self.imageLabel.place(x=0,y=0)

                                self.generate_password_button = Button(self.root,command=lambda:password.Generate1(), font = self.t, text = 'Generate Password', highlightbackground = 'white', fg = 'black', width = 24, height =2)
                                self.generate_password_button.place(x=175,y= 120)

                                self.find_password_button = Button(self.root,command=lambda:password.Find_It(), font = self.t , highlightbackground = 'white', fg = 'black', width = 24, height =2, text = 'Find Password')
                                self.find_password_button.place(x=175, y = 250)

                                self.delete_password_button = Button(self.root,command=lambda:password.Delete_It(), highlightbackground = 'white', fg = 'black', width = 24, height= 2, text = 'Delete password', font = self.t)
                                self.delete_password_button.place(x=175,y=380)

                                self.root.mainloop()

                        
        def Generate1(self): 


                self.txtVar_password = StringVar()
                
                self.backround_label = Label(self.root, height = 50, width = 100, bg = 'black')
                self.backround_label.place(x=0,y=0)
                

                self.delete_password_button.destroy()
                self.generate_password_button.destroy()
                self.find_password_button.destroy()


                self.menustatus = Label(self.root, font = self.t, bg = 'black', fg = 'white', text = 'Passwords | Generate Password', width = 25)
                self.menustatus.place(x=160,y=0)
                

                return_button = Button(self.root,command=lambda:password.return_func('generate'), text = '<-', highlightbackground='black', fg= 'white',font = self.t,width = 1, border = False)
                return_button.place(x=0,y=0)
                

                self.barrier = Label(self.root, text=self.long_line, font = self.t,bg ='black', fg = 'white')
                self.barrier.place(x=0,y=30)
                

                self.password_label = Label(self.root, bg = 'black',fg = 'white', text = 'Password:', width =9 , font = self.t)
                self.password_label.place(x=5, y=80)
                

                self.generate_password_button =  Button(self.root,command=lambda:password.Generate2('generate'),border = False, highlightbackground='white', fg = 'black', text = 'Generate', width = 10,font = self.t )
                self.generate_password_button.place(x=200,y= 150)
                

                self.password_field = Entry(self.root,bg = 'black', fg = 'white', textvariable = self.txtVar_password, font = self.t, width = 18)
                self.password_field.place(x=200,y=80)
                

                self.app_name_label = Label(self.root, bg = 'black',fg = 'white', text = 'Website/App:', width =12 , font = self.t)
                self.app_name_label.place(x=0, y = 300)
                

                self.app_name_field = Entry(self.root,bg = 'black', fg = 'white', font = self.t, width = 18)
                self.app_name_field.place(x=200,y=300)
                

                self.barrier = Label(self.root, text=self.long_line, font = self.t,bg ='black', fg = 'white')
                self.barrier.place(x=0,y=420)
                

                self.save_label = Label(self.root, bg = 'black',fg = 'black', text = 'Save password:', width =12 , font = self.t)
                self.save_label.place(x=0,y= 485)
                

                self.save_button = Button(self.root, command=lambda: password.Generate3(),border = False, highlightbackground='white', fg = 'black', text = 'Save', width = 10,font = self.t )
                self.save_button.place(x=200, y =485)
                
        
        def Generate2(self, argument): 
                
                if argument == 'generate':
                        
                        uppercase_loc = random.randint(1,4)  
                        number_loc = random.randint(5, 6)  

                        number = random.randint(1,9)

                        lowercase_loc = random.randint(7,12)  

                        self.generated_password = ''  

                        pool = string.ascii_letters + string.punctuation  


                        for i in range(16):

                                if i == uppercase_loc: 
                                        self.generated_password += random.choice(string.ascii_uppercase)

                                elif i == lowercase_loc:  
                                        self.generated_password += random.choice(string.ascii_lowercase)

                                elif i == number_loc:
                                        self.generated_password += random.choice()

                                else: 
                                        self.generated_password += random.choice(pool)

                                
                        self.txtVar_password.set(self.generated_password)


        def Generate3(self):

                
                password = self.password_field.get()
                raw_name = self.app_name_field.get()

                name = raw_name.upper()


                self.col.insert_one({'App': name, 'Password': password})
                
                checkstatus = self.col.find_one({'App' : name})
                verify_connection = checkstatus['Password']

                if verify_connection == "": 

                        self.menustatus.config(text = 'No password provided')
                

                elif raw_name == '':

                        self.menustatus.config(text = 'No website provided')

                elif verify_connection != None : 

                        self.menustatus.config(text = 'Password Saved')


                




        def Find_It(self):

                self.password_var = StringVar()

                self.root.geometry('700x400')


                self.delete_password_button.destroy()
                self.generate_password_button.destroy()
                self.find_password_button.destroy()
        

                self.backround_label = Label(self.root, height =50, width = 100, bg = 'black')
                self.backround_label.place(x=0,y=0)


                self.menustatus = Label(self.root, font = self.t, bg='black', fg= 'white',  text = 'Passwords | Find Password', width = 25)
                self.menustatus.place(x=160,y=0)


                self.barrier = Label(self.root, text=self.long_line, font = self.t,bg ='black', fg = 'white')
                self.barrier.place(x=0,y=30)

                self.enter_app_label = Label(self.root,font=self.t, bg = 'black',fg = 'white', width = 12, text = 'App name :')
                self.enter_app_label.place(x=0,y=80)

                self.enter_app_field = Entry(self.root,textvariable = self.password_var,font=self.t, bg = 'black',fg = 'white', width = 23)
                self.enter_app_field.place(x=300,y=80)

                self.enter_app_button = Button(self.root, command=lambda: password.Find_It2(),border = False, highlightbackground='white', fg = 'black', text = 'Find', width = 21,font = self.t )
                self.enter_app_button.place(x=300, y = 140)




        def Find_It2(self):

                

                raw_app = self.enter_app_field.get()
                app = raw_app.upper()


                result = self.col.find_one({'App' : app })
                password = result['Password']

                        
                try :

                        if password == "":

                                self.menustatus.config(text = 'Password could not be located.')


                        
                        
                        else:
                                self.menustatus.config(text = 'Password successfully located.')

                                self.enter_app_label.config(text = 'Password :')

                                self.password_var.set(password)




                                   
                except TypeError : 

                        pass

        def Delete_It(self):


                self.password_var_del = StringVar()
                self.root.geometry('700x400')


                self.delete_password_button.destroy()
                self.generate_password_button.destroy()
                self.find_password_button.destroy()
        

                self.backround_label = Label(self.root, height =50, width = 100, bg = 'black')
                self.backround_label.place(x=0,y=0)


                self.menustatus = Label(self.root, font = self.t, bg = 'black', fg = 'white', text = 'Passwords | Delete Password', width = 25)
                self.menustatus.place(x=160,y=0)


                self.barrier = Label(self.root, text=self.long_line, font = self.t,bg ='black', fg = 'white')
                self.barrier.place(x=0,y=30)

                self.enter_app_label = Label(self.root,font=self.t, bg = 'black',fg = 'white', width = 12, text = 'App name :')
                self.enter_app_label.place(x=0,y=80)

                self.pas_to_del = Entry(self.root,textvariable = self.password_var_del, font=self.t, bg = 'black',fg = 'white', width = 23)
                self.pas_to_del.place(x=300,y=80)

                self.enter_app_button = Button(self.root, command=lambda: password.Delete_It2(),border = False, highlightbackground='white', fg = 'black', text = 'Delete', width = 21,font = self.t )
                self.enter_app_button.place(x=300, y = 140)


        def Delete_It2(self):

                

                raw_app = self.pas_to_del.get()
                app = raw_app.upper()

                        
                try :

                        if password == "":

                                self.menustatus.config(text = 'Password could not be located.')


                        
                        
                        else:
                                
                                self.col.delete_one({'App' : app })

                                self.menustatus.config(text = 'Password was successfully deleted.')

                                
                                
                               
                                   
                except TypeError : 

                        pass
                
password = Password()
password.Setup()
password.StartUp()



