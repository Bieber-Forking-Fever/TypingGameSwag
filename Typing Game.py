import random
from Tkinter import *

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


                labelList = [self.label1,self.label2,self.label3,self.label4,self.label5,self.label6,self.label7,self.label8,self.label9,self.label10,self.label11,self.label12,self.label13,self.label14,self.label15,self.label16,self.label17,self.label18,self.label19,self.label20,self.label21,self.label22,self.label23,self.label24,self.label25,self.label26,]


	
		
root = Tk()
myapp = MyApp(root)
root.mainloop()