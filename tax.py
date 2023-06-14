'''sal=int(input("Enter monthly sal:"))
annual=sal*12
print(annual)
tax=0
if annual<=200000:
	tax=0
elif annual<=300000:
	tax=0.1*(annual-200000)
elif annual<=500000:
	tax=(0.2*(annual-300000))+(0.1*100000)
else:
	tax=(0.3*(annual-500000))+(0.2*200000)+(0.1*100000)
print("Income tax amount is:",tax)'''

class Pclass:
    def __init__(self):  
        self.a=a
        print("Parent-class Constructor");
        
class Cclass(Pclass):
	#pass;
	def __init__(self):    
		print("Child-class Constructor");
		#super().__init__();
	
obj = Cclass(10);