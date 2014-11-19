import random
from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')

class MyApp:
	def __init__(self, parent):
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
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


                self.labelList = [self.label1,self.label2,self.label3,self.label4,self.label5,self.label6,self.label7,self.label8,self.label9,self.label10,self.label11,self.label12,self.label13,self.label14,self.label15,self.label16,self.label17,self.label18,self.label19,self.label20,self.label21,self.label22,self.label23,self.label24,self.label25,self.label26,]
                self.loop()

                root.bind_all('<Key>', self.key)
        def loop(self):
                global drawpad
                self.L = random.randint(0,25)
                self.labelList[self.L].configure(bg = "Green")
                self.currentLetter = self.labelList[self.L]
            
                drawpad.after(1000,self.loop)

        def key(self,event):

                if event.char == "a":
                    if self.currentLetter == self.labelList[0]:
                        self.labelList[0].configure(bg = "Red")
                        print "a Worked"
                if event.char == "b":
                    if self.currentLetter == self.labelList[1]:
                        self.labelList[1].configure(bg = "Red")
                        print "b Worked"
                if event.char == "c":
                    if self.currentLetter == self.labelList[2]:
                        self.labelList[2].configure(bg = "Red")
                        print "c Worked"
                if event.char == "d":
                    if self.currentLetter == self.labelList[3]:
                        self.labelList[3].configure(bg = "Red")
                        print "d Worked"                  
                if event.char == "e":
                    if self.currentLetter == self.labelList[4]:
                        self.labelList[4].configure(bg = "Red")
                        print "e Worked"                   
                if event.char == "f":
                    if self.currentLetter == self.labelList[5]:
                        self.labelList[5].configure(bg = "Red")
                        print "f Worked"                   
                if event.char == "g":
                    if self.currentLetter == self.labelList[6]:
                        self.labelList[6].configure(bg = "Red")
                        print "g Worked"                  
                if event.char == "h":
                    if self.currentLetter == self.labelList[7]:
                        self.labelList[7].configure(bg = "Red")
                        print "h Worked"                   
                if event.char == "i":
                    if self.currentLetter == self.labelList[8]:
                        self.labelList[8].configure(bg = "Red")
                        print "i Worked"                  
                if event.char == "j":
                    if self.currentLetter == self.labelList[9]:
                        self.labelList[9].configure(bg = "Red")
                        print "j Worked"                             
                if event.char == "k":
                    if self.currentLetter == self.labelList[10]:
                        self.labelList[10].configure(bg = "Red")
                        print "k Worked"                             
                if event.char == "l":
                    if self.currentLetter == self.labelList[11]:
                        self.labelList[11].configure(bg = "Red")
                        print "l Worked"                             
                if event.char == "m":
                    if self.currentLetter == self.labelList[12]:
                        self.labelList[12].configure(bg = "Red")
                        print "m Worked"                               
                if event.char == "n":
                    if self.currentLetter == self.labelList[13]:
                        self.labelList[13].configure(bg = "Red")
                        print "n Worked"                              
                if event.char == "o":
                    if self.currentLetter == self.labelList[14]:
                        self.labelList[14].configure(bg = "Red")
                        print "o Worked"                               
                if event.char == "p":
                    if self.currentLetter == self.labelList[15]:
                        self.labelList[15].configure(bg = "Red")
                        print "p Worked"                           
                if event.char == "q":
                    if self.currentLetter == self.labelList[16]:
                        self.labelList[16].configure(bg = "Red")
                        print "q Worked"                              
                if event.char == "r":
                    if self.currentLetter == self.labelList[17]:
                        self.labelList[17].configure(bg = "Red")
                        print "r Worked"                               
                if event.char == "s":
                    if self.currentLetter == self.labelList[18]:
                        self.labelList[18].configure(bg = "Red")
                        print "s Worked"                              
                if event.char == "t":
                    if self.currentLetter == self.labelList[19]:
                        self.labelList[19].configure(bg = "Red")
                        print "t Worked"                               
                if event.char == "u":
                    if self.currentLetter == self.labelList[20]:
                        self.labelList[20].configure(bg = "Red")
                        print "u Worked"                               
                if event.char == "v":
                    if self.currentLetter == self.labelList[21]:
                        self.labelList[21].configure(bg = "Red")
                        print "v Worked"                               
                if event.char == "w":
                    if self.currentLetter == self.labelList[22]:
                        self.labelList[22].configure(bg = "Red")
                        print "w Worked"                             
                if event.char == "x":
                    if self.currentLetter == self.labelList[23]:
                        self.labelList[23].configure(bg = "Red")
                        print "x Worked"                              
                if event.char == "y":
                    if self.currentLetter == self.labelList[24]:
                        self.labelList[24].configure(bg = "Red")
                        print "y Worked"                              
                if event.char == "z":
                    if self.currentLetter == self.labelList[25]:
                        self.labelList[25].configure(bg = "Red")
                        print "z Worked"                           

        







myapp = MyApp(root)
root.mainloop()