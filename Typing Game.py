import random
from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
alreadywon = False
speed = 1500
class MyApp:
	def __init__(self, parent):
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		self.scoreframe = Frame(parent)
		self.scoreframe.pack(side=BOTTOM)
		
                self.label1 = Label(root, text="a", bg='red')
                self.label1.pack(side = LEFT)

                self.label2 = Label(root, text="b", bg='red')
                self.label2.pack(side = LEFT)

                self.label3 = Label(root, text="c", bg='red')
                self.label3.pack(side = LEFT)

                self.label4 = Label(root, text="d", bg='red')
                self.label4.pack(side = LEFT)

                self.label5 = Label(root, text="e", bg='red')
                self.label5.pack(side = LEFT)

                self.label6 = Label(root, text="f", bg='red')
                self.label6.pack(side = LEFT)

                self.label7 = Label(root, text="g", bg='red')
                self.label7.pack(side = LEFT)

                self.label8 = Label(root, text="h", bg='red')
                self.label8.pack(side = LEFT)

                self.label9 = Label(root, text="i", bg='red')
                self.label9.pack(side = LEFT)

                self.label10 = Label(root, text="j", bg='red')
                self.label10.pack(side = LEFT)

                self.label11 = Label(root, text="k", bg='red')
                self.label11.pack(side = LEFT)

                self.label12 = Label(root, text="l", bg='red')
                self.label12.pack(side = LEFT)

                self.label13 = Label(root, text="m", bg='red')
                self.label13.pack(side = LEFT)

                self.label14 = Label(root, text="n", bg='red')
                self.label14.pack(side = LEFT)

                self.label15 = Label(root, text="o", bg='red')
                self.label15.pack(side = LEFT)

                self.label16 = Label(root, text="p", bg='red')
                self.label16.pack(side = LEFT)

                self.label17 = Label(root, text="q", bg='red')
                self.label17.pack(side = LEFT)

                self.label18 = Label(root, text="r", bg='red')
                self.label18.pack(side = LEFT)

                self.label19 = Label(root, text="s", bg='red')
                self.label19.pack(side = LEFT)

                self.label20 = Label(root, text="t", bg='red')
                self.label20.pack(side = LEFT)

                self.label21 = Label(root, text="u", bg='red')
                self.label21.pack(side = LEFT)

                self.label22 = Label(root, text="v", bg='red')
                self.label22.pack(side = LEFT)

                self.label23 = Label(root, text="w", bg='red')
                self.label23.pack(side = LEFT)

                self.label24 = Label(root, text="x", bg='red')
                self.label24.pack(side = LEFT)

                self.label25 = Label(root, text="y", bg='red')
                self.label25.pack(side = LEFT)

                self.label26 = Label(root, text="z", bg='red')
                self.label26.pack(side = LEFT)

                self.score = 0
        
                self.scoreTxt = Label(self.scoreframe, text=str(self.score), bg='green')
                self.scoreTxt.pack()


                self.labelList = [self.label1,self.label2,self.label3,self.label4,self.label5,self.label6,self.label7,self.label8,self.label9,self.label10,self.label11,self.label12,self.label13,self.label14,self.label15,self.label16,self.label17,self.label18,self.label19,self.label20,self.label21,self.label22,self.label23,self.label24,self.label25,self.label26,]
                self.loop()

                root.bind_all('<Key>', self.key)
        def loop(self):
                global drawpad
                global alreadywon
                global speed
                if alreadywon == False:
                    self.score = self.score - 10
                    self.scoreTxt.configure(text=self.score)
                alreadywon = False
                for x in self.labelList:
                    x.configure(bg = "Red")
                self.L = random.randint(0,25)
                self.labelList[self.L].configure(bg = "Green")
                self.currentLetter = self.labelList[self.L]
                speed = speed - 30
                if speed < 670:
                    speed = speed + 30
                drawpad.after(speed,self.loop)
                

        def key(self,event):
                global alreadywon

                if event.char == "a":
                    if self.currentLetter == self.labelList[0]:
                        if alreadywon == False:
                            self.labelList[0].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                    else:
                        self.score = self.score - 10
                        self.scoreTxt.configure(text=self.score)

                if event.char == "b":
                    if self.currentLetter == self.labelList[1]:
                        if alreadywon == False:
                            self.labelList[1].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                    else:
                        self.score = self.score - 10
                        self.scoreTxt.configure(text=self.score)

                if event.char == "c":
                        if alreadywon == False:
                            self.labelList[2].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)

                if event.char == "d":
                        if alreadywon == False:
                            self.labelList[3].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                
                if event.char == "e":
                    if self.currentLetter == self.labelList[4]:
                        if alreadywon == False:
                            self.labelList[4].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score) 
                 
                if event.char == "f":
                    if self.currentLetter == self.labelList[5]:
                        if alreadywon == False:
                            self.labelList[5].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                 
                if event.char == "g":
                    if self.currentLetter == self.labelList[6]:
                        if alreadywon == False:
                            self.labelList[6].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
               
                if event.char == "h":
                    if self.currentLetter == self.labelList[7]:
                        if alreadywon == False:
                            self.labelList[7].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                  
                if event.char == "i":
                    if self.currentLetter == self.labelList[8]:
                        if alreadywon == False:
                            self.labelList[8].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)

                if event.char == "j":
                    if self.currentLetter == self.labelList[9]:
                        if alreadywon == False:
                            self.labelList[9].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                            
                if event.char == "k":
                    if self.currentLetter == self.labelList[10]:
                        if alreadywon == False:
                            self.labelList[10].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                            
                if event.char == "l":
                    if self.currentLetter == self.labelList[11]:
                        if alreadywon == False:
                            self.labelList[11].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                            
                if event.char == "m":
                    if self.currentLetter == self.labelList[12]:
                        if alreadywon == False:
                            self.labelList[12].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score) 
                             
                if event.char == "n":
                    if self.currentLetter == self.labelList[13]:
                        if alreadywon == False:
                            self.labelList[13].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                            
                if event.char == "o":
                    if self.currentLetter == self.labelList[14]:
                        if alreadywon == False:
                            self.labelList[14].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score) 
                            
                if event.char == "p":
                    if self.currentLetter == self.labelList[15]:
                        if alreadywon == False:
                            self.labelList[15].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                         
                if event.char == "q":
                    if self.currentLetter == self.labelList[16]:
                        if alreadywon == False:
                            self.labelList[16].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score) 
                            
                if event.char == "r":
                    if self.currentLetter == self.labelList[17]:
                        if alreadywon == False:
                            self.labelList[17].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score) 
                           
                if event.char == "s":
                    if self.currentLetter == self.labelList[18]:
                        if alreadywon == False:
                            self.labelList[18].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                             
                if event.char == "t":
                    if self.currentLetter == self.labelList[19]:
                        if alreadywon == False:
                            self.labelList[19].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score) 
                             
                if event.char == "u":
                    if self.currentLetter == self.labelList[20]:
                        if alreadywon == False:
                            self.labelList[20].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score) 
                             
                if event.char == "v":
                    if self.currentLetter == self.labelList[21]:
                        if alreadywon == False:
                            self.labelList[21].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score) 
                              
                if event.char == "w":
                    if self.currentLetter == self.labelList[22]:
                        if alreadywon == False:
                            self.labelList[22].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                          
                if event.char == "x":
                    if self.currentLetter == self.labelList[23]:
                        if alreadywon == False:
                            self.labelList[23].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                           
                if event.char == "y":
                    if self.currentLetter == self.labelList[24]:
                        if alreadywon == False:
                            self.labelList[24].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)
                            
                if event.char == "z":
                    if self.currentLetter == self.labelList[25]:
                        if alreadywon == False:
                            self.labelList[25].configure(bg = "Red")
                            self.score = self.score + 10
                            self.scoreTxt.configure(text=self.score)
                            alreadywon = True
                        else:
                            self.score = self.score - 10
                            self.scoreTxt.configure(text=self.score)                        

        







myapp = MyApp(root)
root.mainloop()