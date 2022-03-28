import os

try:
    file = open("UsersPoints.txt","x")
except:
    print()

def playerVerification(Player):
    while "=" in Player:
        Player = input("Enter a player name without punctiation!\n:")
    return Player    
def whatWasThePoint(Player):
    f =open("UsersPoints.txt","r")
    lines=f.readlines()
    f.close()
    for line in lines:
        if Player in line.split("=="):
            _list = line.split("==")
            Point = _list[1]
            
            return int(Point)
            #Password = line[2]
    
def isNameThere(Player):
    f =open("UsersPoints.txt","r")
    lines=f.readlines()
    f.close()
    
    for line in lines:
        if Player in line.split("==") :     
            return True
    return False
    
def ExistanceQuestion(NameExistance):
    while NameExistance !="y" and NameExistance !="n":
        NameExistance = input("Have you got account? Y or N. Not anything else.\nEnter : ")
        
    if NameExistance == "y" :
            return True        
    else:
            return False
def NewNameVerification(Player):#Why its happening none problem line 46
    NameThere = isNameThere(Player)
    while NameThere==True:
        print("this name already exist")
        Player=input("Enter a new name :")
        NameThere = isNameThere(Player)
    else:
        while len(Player)<3 or len(Player) > 7:
            print("This name too long or too short. The Name should be between 3-7 Characters.")
            Player=input("Enter a new name :")
            
        else:
            Point = 0
            savingNames(Player,Point)
           
            
            return Player            
def savingNames(Player,Point):
    Player = str(Player)
    Ufile = open("UsersPoints.txt","a")
    Ufile.write(Player)
    Ufile.write("==")
    Ufile.write(str(Point))
    Ufile.write("\n")
    Ufile.close()

  
  
  
  
  
  
  
   
NameExistance = "a"
ContinuetoAsking = True
while ContinuetoAsking == True:
    NameExistance = ExistanceQuestion(NameExistance)

    
    
    if NameExistance==True:    
        Player = input("Your hangman account : ")
        Player = playerVerification(Player)
        #password can come here
        NameThere=isNameThere(Player)     #player told us yes this name is exist but it can be lie, we check it here
    
        if NameThere == True:
            Point = whatWasThePoint(Player)
            NameExistance = False
            break
        if NameThere == False:
            print("we couldnt find your account ! ")

        
     
    elif NameExistance ==False:
        Player = input("Enter a name to create an account : ")
        Player = NewNameVerification(Player)
        Point = 0
        ContinuetoAsking = False
        break
    else:
        print("something goes wrong")



Player = str(Player)

print("Welcome ",Player)
print("Your score : ",Point)
