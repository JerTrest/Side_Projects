#Online adaptation of real game "Smart Mouth"

#First input the number of players/teams, scoring you are playing to, and name of each player/team
#The players/teams must then input words in the English dictionary that begin with the first letter and end with the second letter
#The player/team with the longest word that is in the English dictionary, begins with the first letter, and ends with the second letter will win the round and be given a point
#The submit button can be used to check if the given word is valid

#MAX PLAYERS: 8 
#This is due to the code in lines 122-137 (Code is written this way to prevent a problem I kept running into, still planning on working on this and fixing it in the future)

from tkinter import *
import random
import string
import enchant

dictionary=enchant.Dict("en_US")

def nextRound():
    lengths=[]
    for team in teamInputs:
        if statusCheck(team[0:len(team)-5]):
            lengths.append(len(teamInputs[team].get()))
        else:
            lengths.append(0)
    highestScore=max(lengths)

    count=0
    while count<len(lengths):
        if lengths[count]==highestScore:
            teamScores[count]+=1
            teamScoreLabels['{}ScoreLabel'.format(teamNames[count])].configure(text='Score: {}'.format(teamScores[count]))
        
        if teamScores[count]==maxScore:
            winningPopUp=Tk()
            winningMessage=Label(winningPopUp,text='{} WINS!'.format(teamNames[count]),font=('Verdana',40))
            winningMessage.pack()
            winningPopUp.mainloop()
            
        teamInputs['{}Input'.format(teamNames[count])].delete(0,'end')    
        wordLengthCounter['{}wordLength'.format(teamNames[count])].configure(text='Length: ')
        wordStatus["{}Status".format(teamNames[count])].configure(text='Word Status: ')
            
        count+=1

    randomLetter1.configure(text=random.choice(letters))
    randomLetter2.configure(text=random.choice(letters))
    

def submit(teamName):
    wordLengthCounter['{}wordLength'.format(teamName)].configure(text='Length: {}'.format(len(teamInputs['{}Input'.format(teamName)].get())))
    
    if not statusCheck(teamName):
            wordStatus["{}Status".format(teamName)].configure(text='Word Status: ✘')
    else:
        wordStatus["{}Status".format(teamName)].configure(text='Word Status: ✔')

def statusCheck(teamName):
    if len(teamInputs['{}Input'.format(teamName)].get())<2:
        return False
    elif randomLetter1.cget('text').lower()!=teamInputs['{}Input'.format(teamName)].get()[0] or randomLetter2.cget('text').lower()!=teamInputs['{}Input'.format(teamName)].get()[len(teamInputs['{}Input'.format(teamName)].get())-1]:
        return False
    elif not dictionary.check(teamInputs['{}Input'.format(teamName)].get()):
        return False
    else:
        return True

teamNames=[]
teamScores=[]
wordLength={}

maxScore=int(input('Playing to: '))
teamCount=int(input('Number of teams: '))

for count in range(teamCount):
    teamName=(input('Team {} name: '.format(count+1)))
    teamNames.append(teamName)
    wordLength[teamName]=0
    teamScores.append(0)
    
window=Tk()

letters=list(string.ascii_uppercase)

randomLetter1=Label(window,text=random.choice(letters),font=('Verdana',30))
randomLetter1.grid(row=0)

randomLetter2=Label(window,text=random.choice(letters),font=('Verdana',30))
randomLetter2.grid(row=0)


teamScoreLabels={}
count=0
while count<len(teamNames):
    teamScoreLabels['{}ScoreLabel'.format(teamNames[count])]=Label(window,text='Score: {}'.format(teamScores[count]))
    teamScoreLabels['{}ScoreLabel'.format(teamNames[count])].grid(row=2,column=count)
    count+=1


teamInputTitles={}
teamInputs={}    
submitBtns={}
wordLengthCounter={}
wordStatus={}

for team in teamNames:
    teamInputTitles['{}InputTitle'.format(team)]=Label(window,text=team,font=('Verdana',15))
    teamInputTitles['{}InputTitle'.format(team)].grid(row=1,column=teamNames.index(team))

    teamInputs['{}Input'.format(team)]=Entry(window)
    teamInputs['{}Input'.format(team)].grid(row=3,column=teamNames.index(team))

    submitBtns['{}SubmitBtn'.format(team)]=Button(window,text='Submit',command=lambda:submit(team))
    submitBtns['{}SubmitBtn'.format(team)].grid(row=4,column=teamNames.index(team))

    wordLengthCounter['{}wordLength'.format(team)]=Label(window,text='Length: {}'.format(wordLength[team]))
    wordLengthCounter['{}wordLength'.format(team)].grid(row=5,column=teamNames.index(team))

    wordStatus['{}Status'.format(team)]=Label(window,text='Word Status: ')
    wordStatus['{}Status'.format(team)].grid(row=6,column=teamNames.index(team))


#FIND SOLUTION TO SCALE:
if len(teamNames)>0:
    submitBtns['{}SubmitBtn'.format(teamNames[0])].configure(command=lambda:submit(teamNames[0]))
if len(teamNames)>1:
    submitBtns['{}SubmitBtn'.format(teamNames[1])].configure(command=lambda:submit(teamNames[1]))
if len(teamNames)>2:
    submitBtns['{}SubmitBtn'.format(teamNames[2])].configure(command=lambda:submit(teamNames[2]))
if len(teamNames)>3:
    submitBtns['{}SubmitBtn'.format(teamNames[3])].configure(command=lambda:submit(teamNames[3]))
if len(teamNames)>4:
    submitBtns['{}SubmitBtn'.format(teamNames[4])].configure(command=lambda:submit(teamNames[4]))
if len(teamNames)>5:
    submitBtns['{}SubmitBtn'.format(teamNames[5])].configure(command=lambda:submit(teamNames[5]))
if len(teamNames)>6:
    submitBtns['{}SubmitBtn'.format(teamNames[6])].configure(command=lambda:submit(teamNames[6]))
if len(teamNames)>7:
    submitBtns['{}SubmitBtn'.format(teamNames[7])].configure(command=lambda:submit(teamNames[7]))



nextRoundBtn=Button(window,text='Next Round',command=nextRound)
nextRoundBtn.grid(row=7)

colCount=window.grid_size()[0]
randomLetter1.grid(column=-1+colCount//2)
randomLetter2.grid(column=colCount//2)
if colCount%2==1:
    randomLetter1.grid(columnspan=2)
    randomLetter2.grid(columnspan=2)
    nextRoundBtn.grid(column=colCount//2)
else:
    nextRoundBtn.grid(column=-1+colCount//2,columnspan=2)

window.mainloop()