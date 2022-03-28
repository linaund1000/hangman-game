import os
from name import Player , Point
from difficulties import ListDependDifficulty , DifficultyVerification
import random
"""
Read ME    
    
    here program select a word and encrypt that word. 
    inside loop
        user gave a letter to program and if this letter was inside of word ,Letters in choosenWord and EncryptedWord would change(UpperLetter)
    if choosenword and encrypted word were same player won point as much as players tryingChance
    
    
    wrong trying = -1 chance
    correct trying +1 chance
    
    player point variables come from NAME and user play with that inputs
    
    every user store own data(all variables and points) on their computer -.txt-
    
    
    
    
    
"""



def ChoosingWord(ListDependDifficulty):
   
    length = len(ListDependDifficulty)
    random_numb = random.randint(0,length-1)
    
    ChoosenWord = str(ListDependDifficulty[random_numb])
    return ChoosenWord 
        
def WonOrNotTest(ChoosenWord,EncryptedWord,WordAward):   
    if ChoosenWord==EncryptedWord: #Here, player succeed in this word
        print("BRAVO")
        print("you won ",WordAward," point.")
        return True
    else:
       
        return "2"

def CharInputVerification(CharInput):
    CharInput = str(CharInput)
    CharInput = CharInput.lower()
    
    if len(CharInput) == 1 :         
        return CharInput
    else:
        CharInput=input("You didnt enter a char please use just a char..\nEnter char : ")
        CharInputVerification(CharInput)
#searching choosen letter in choosenword

#ListDependDifficulty and player are ready.  game engine can start here


#!!!!

# !!!!! problem was here  
def savenewPoint(Player,Point):
    f =open("UsersPoints.txt","r")
    lines=f.readlines()
    f.close()
    new_file = open("UsersPoints.txt","w")
    for line in lines:
        
        if  Player in line.split("=="):
            #program has to change point in players line :D BUT I COULDNT
            new_file.write(Player)
            new_file.write("==")
            new_file.write(str(Point))
            new_file.write("\n")
            
        else:        
            
            new_file.write(line)

    new_file.close()
    
    
    
            




"""                    
                
    logic       
            
"""
            
             


           



IwannaPlayGame = True

while IwannaPlayGame == True:            
    
    
    #
            
            # Under this line we expect ;
            # 
            # ChoosenWord will be Choosen
            # EncryptedWord will be prepared
            # CharInput has been taken 
            # CharInputExist is true
            
            
            # we change the word and look for that, will they be same or not in 8 trying  ?  
    
    #
    
    
    
    
      
    ChoosenWord = ChoosingWord(ListDependDifficulty)
    WordAward = len(ChoosenWord)  
    EncryptedWord = "*"*len(ChoosenWord)  
    WonOrNot = "will become True or false"     

    
    print("Your word is ",len(EncryptedWord),"characters !")

    while WordAward >0:
    
        print("you can try ",WordAward,"times")
        CharInput = input("Guess a char : ")
        CharInput = CharInputVerification(CharInput)
        
        
        while str(CharInput) in ChoosenWord:
            
            Char_Index = ChoosenWord.find(CharInput)
            CharUpper = CharInput.upper()
            WordAward += 1
        
            if CharInput in ChoosenWord[1:(len(ChoosenWord)-1)] :   #if target char in the middle of Word
                
                                
                ChoosenWord=ChoosenWord[:(Char_Index)] + CharUpper  + ChoosenWord[(Char_Index)+1:] 
                EncryptedWord = EncryptedWord[:(Char_Index)] + CharUpper  + EncryptedWord[(Char_Index)+1:] 
                
                
                print(EncryptedWord)
                WonOrNot = WonOrNotTest(ChoosenWord,EncryptedWord,WordAward)
            
            
            
            elif Char_Index == 0: #if target char is first char
            
                
                ChoosenWord= CharUpper + ChoosenWord[1:]
                EncryptedWord= CharUpper + EncryptedWord[1:]
                
                
                print(EncryptedWord)
                WonOrNot = WonOrNotTest(ChoosenWord,EncryptedWord,WordAward)
            
            
            
            elif Char_Index == (len(ChoosenWord)-1): # if target char at the end

                
                ChoosenWord= ChoosenWord[:(len(ChoosenWord)-1)]+CharUpper 
                EncryptedWord= EncryptedWord[:(len(ChoosenWord)-1)] + CharUpper
                
                
                print(EncryptedWord)
                WonOrNot = WonOrNotTest(ChoosenWord,EncryptedWord,WordAward)
            
            
            
            else:
                print("else part")

        WordAward -= 1

        if WonOrNot == False:
            
            
                        
            InputDifficulty = input("enter a difficulty. \nYou can add with words.\nE for easy , i for intermediate , A for Advenced , X for Expert mode. \n Enter please : ")
            ListDependDifficulty = DifficultyVerification(InputDifficulty)

            break
        elif WonOrNot == True:
            

            Point = Point +1 + WordAward
            savenewPoint(Player,Point)
            WordAward = False
            
            
            InputDifficulty = input("enter a difficulty. \nYou can add with words.\nE for easy , i for intermediate , A for Advenced , X for Expert mode. \n Enter please : ")
            ListDependDifficulty = DifficultyVerification(InputDifficulty)
            break
        else:
            
            continue  
    else:
        print("You lost! try again.")
        print("It was : " ,ChoosenWord)   
       
