import random

#returns a string made from a list
def listToString(s):  
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1  

#returns a blank list with size of word
def wordToBlankList(word):
    blankList=list(word)
    for x in range(len(word)):
        blankList[x]="_"
    return blankList

#returns list of index that letter is in word
def multipleIndex(letter,word):
    multipleIndex=[]
    word=list(word)
    for x in range(len(word)):
        if(letter==word[x]):
            multipleIndex.append(x)
    return multipleIndex


words = ("cat","bat","dog","water","doodle","tire","music","computer","mirror")

word=random.choice(words)
wordLength=len(word)
count=0

solution=word
solutionList=wordToBlankList(solution)

incorrectGuesses=[]
vowel=["a","e","i","o","u"]

#images of hangman at different stages
wrong0="  ___  \n  |  | \n  | \n  | \n  | \n ===="
wrong1="  ___  \n  |  | \n  |  0\n  | \n  | \n ===="
wrong2="  ___  \n  |  | \n  |  0\n  |  |\n  | \n ===="
wrong3="  ___  \n  |  | \n  |  0\n  |  |/\n  | \n ===="
wrong4="  ___  \n  |  | \n  |  0\n  | \|/\n  | \n ===="
wrong5="  ___  \n  |  | \n  |  0\n  | \|/\n  |   \ \n ===="
wrong6="  ___  \n  |  | \n  |  0\n  |  /| \n  | /\ \n ===="
errors=[wrong0,wrong1,wrong2,wrong3,wrong4,wrong5,wrong6]

print("")
print("Word is ",wordLength," letters long")

while(True):

    #checks if you are out of guesses
    if(count==6):
        print("") 
        print("Out of guesses, you have lost!")
        print ("")
        print ("Correct word:",word)
        break 

    else:
        print("")
        guess=input("Enter guess: ")

        #checks if guessed letter is inside word
        if(guess in word):

           #creates list of indexes where the word contains the guessed letter
           indexes=multipleIndex(guess,word)

           #changes each index in solution to the guessed letter that corrisponds correctly within the word
           for x in range(len(indexes)):
               solutionList[indexes[x]]=guess
           print("")
           if(len(indexes)>1):
                print("This word contains",len(indexes),"'",guess,"'s")
           else:
                print("This word contains 1 '",guess,"'")
           print("")
           print("Gusses left:",(6-count))
           print("")
           print("Incorrect guesses:",incorrectGuesses)
           print("")
           print(solutionList)
           print(errors[count])

            #tells the player they have won if the solution string matches the orginal word string
           if(listToString(solutionList)==word):
               print("")
               print("Congrats! You have won!") 
               break

        #if the word does not contain the letter, the player loses a guess
        else:
            count+=1
            incorrectGuesses.append(guess)
            print("")
            if(guess in vowel):
                print("This word does not contain an '",guess,"'")
            else:
                print("This word does not contain a '",guess,"'")
            print("")
            print("Guesses left: ",(6-count))
            print("")
            print("Incorrect guesses:",incorrectGuesses)
            print("")
            print(solutionList)
            print(errors[count])
