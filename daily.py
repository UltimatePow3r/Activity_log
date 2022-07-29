from datetime import datetime

class Dailyact():
    x = "no"
    n = 0
    storeon="yes"
    aclst = []
    thisday = datetime.now()
    day=thisday.strftime("%d/%m/%Y")
    time = thisday.strftime("%H:%M:%S")

    def outdatetime(self):
        print("Welcome you to your daily routine\n")
        print(f"Today's date is : {self.day}")
        print("Current Time is :" ,self.time , "\n")

    def acinp(self):
        while(self.x == "yes"):
            self.aclst.append(input("Enter the activity\n"))
            self.x = input("Do you want to add another activity: ")
            self.n+=1

    def prout(self):
        print("The activities you entered now are")
        for i in range(0,self.n):
            print(f"{i+1}.{self.aclst[i]}")

    def filout(self):
        '''
        To Store the output in a file 
        '''
        dlyfile = open('daily.txt','a')
        var=1
        with open("daily.txt", "r+") as dlyfile:
            for lines in dlyfile:
                if self.day in lines:
                    print("\nDate already exists!!!\nWriting only the editing time!!!")
                    var=0
            if(var == 1):
                dlyfile.write(f"\nDate:{self.day}\n")
                dlyfile.write(f"Time of editing:{self.time}\n")
            else:
                dlyfile.write(f"\nTime of editing:{self.time}\n")
            for i in range(0,self.n):
                dlyfile.write(f"{i+1}.{self.aclst[i]}\n")

dailyobj=Dailyact()
dailyobj.outdatetime()
dailyobj.x = input("Do you want to add a activity\n")
if(dailyobj.x == "yes"):
    dailyobj.acinp()
    dailyobj.prout()
    dailyobj.storeorn = input("Do you wanna store the output into a text file:  ")
    if(dailyobj.storeorn == "yes"):
        dailyobj.filout()
        print("\nOutput stored in text file successfully")
    else:
        print("Thank you!!")
print("Thankyou!!")
