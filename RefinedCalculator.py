from tkinter import *
from tkinter import messagebox

window=Tk()

symbols=["^","+","-","/","*","(",")"]
badsymbols1=["^","+","/","*",")"]
badsymbols2=["^","+","-","/","*","("]
nums=["0","1","2","3","4","5","6","7","8","9"]
wrong=["**","//","^^","..","*/","/*","/^,","^/","^*","*^","+*","*+","-*","+/","/+","-/","-^","^+","+^"]
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z","w","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def one():
    inputNum.insert(len(inputNum.get()),"1")

def two():
    inputNum.insert(len(inputNum.get()),"2")

def three():
    inputNum.insert(len(inputNum.get()),"3")

def four():
    inputNum.insert(len(inputNum.get()),"4")

def five():
    inputNum.insert(len(inputNum.get()),"5")

def six():
    inputNum.insert(len(inputNum.get()),"6")

def seven():
    inputNum.insert(len(inputNum.get()),"7")

def eight():
    inputNum.insert(len(inputNum.get()),"8")

def nine():
    inputNum.insert(len(inputNum.get()),"9")

def zero():
    inputNum.insert(len(inputNum.get()),"0")

def parenth1():
    inputNum.insert(len(inputNum.get()),"(")

def parenth2():
    inputNum.insert(len(inputNum.get()),")")

def dec():
    inputNum.insert(len(inputNum.get()),".")

def expo():
    inputNum.insert(len(inputNum.get()),"^")

def add():
    inputNum.insert(len(inputNum.get()),"+")

def sub():
    inputNum.insert(len(inputNum.get()),"-")

def mult():
    inputNum.insert(len(inputNum.get()),"*")

def div():
    inputNum.insert(len(inputNum.get()),"/")

def clear_text():
    inputNum.delete(0,'end')

def back():
    inputNum.delete((len(inputNum.get())-1),'end')

def multipleIndex(symbol,equation):
    multipleIndex=[]
    equation=list(equation)
    for x in range(len(equation)):
        if(symbol==equation[x]):
            multipleIndex.append(x)
    return multipleIndex

def enter():
    equation=inputNum.get()
    answer=str(solve(equation))
    if(answer[len(answer)-2:len(answer)]==(".0")):
        answer=answer.replace(".0","")
    inputNum.delete(0,'end')
    inputNum.insert(0,(answer))

def solve(equation):
    while(True):

        for index in range(len(wrong)):
            if(wrong[index] in equation):
                equation="ERROR: Incorrect Symbols"
                return equation

        for index in range(len(letters)):
            if(letters[index] in equation):
                    equation="ERROR: Letter in equation"
                    return equation 
    
        if(equation[0] in badsymbols1 or equation[len(equation)-1] in badsymbols2):
            return "ERROR"

        if("--" in equation) or ("+-" in equation) or ("-+" in equation) or ("++" in equation):
            if("--" in equation):
                equation=equation.replace("--","+")
            if("+-" in equation):
                equation=equation.replace("+-","-")
            if("--" in equation):
                equation=equation.replace("-+","-")
            if("++" in equation):
                equation=equation.replace("++","+")

        elif ("(" in equation) and (")" in equation):
            indexOfPar1=multipleIndex("(",equation)
            indexOfPar2=multipleIndex(")",equation)
            indexOfMatchingPar=0
            
            if(len(indexOfPar1)==len(indexOfPar2)):
                
                for index in range(len(indexOfPar1)):
                    if(indexOfPar1[index]!=0):
                        if(equation[indexOfPar1[index]-1] in nums):
                            equation=equation.replace(equation[indexOfPar1[index]],"*(")
                
                for index in range(len(indexOfPar2)):
                    if(indexOfPar2[index]!=len(equation)-1):
                        if(equation[indexOfPar1[index]+1] in nums):
                            equation=equation.replace(equation[indexOfPar2[index]],")*")  

                indexOfPar1=multipleIndex("(",equation)
                indexOfPar2=multipleIndex(")",equation)

                for index in range((len(indexOfPar2))):
                    if (indexOfPar2[index]>indexOfPar1[(len(indexOfPar1)-1)]):
                        indexOfMatchingPar=indexOfPar2[index]
                        break

                unsolved=equation[indexOfPar1[(len(indexOfPar1)-1)]:indexOfMatchingPar+1]
                answer=solve(equation[indexOfPar1[(len(indexOfPar1)-1)]+1:indexOfMatchingPar])
                equation=equation.replace(unsolved,(answer))
                
            else:
                equation="ERROR: Missing Parentheses"
                break


        elif("^" in equation):
            indexOfEx=[]
            indexOfEx=multipleIndex("^",equation)
            
            if(equation[indexBeforeSym(equation,indexOfEx[0])-1]=="-") and (equation[(indexOfEx[0])+1]=="-"):
                unsolved=equation[indexBeforeSym(equation,indexOfEx[0])-1:(indexAfterSym(equation,indexOfEx[0])+1)]
            elif(equation[indexBeforeSym(equation,indexOfEx[0])-1]=="-"):
                unsolved=equation[indexBeforeSym(equation,indexOfEx[0])-1:(indexAfterSym(equation,indexOfEx[0])+1)]
            elif(equation[(indexOfEx[0])+1]=="-"):
                unsolved=equation[indexBeforeSym(equation,indexOfEx[0]):(indexAfterSym(equation,indexOfEx[0])+1)]
            else:
                unsolved=equation[indexBeforeSym(equation,indexOfEx[0]):(indexAfterSym(equation,indexOfEx[0])+1)]
            
            answer=solveEquation(equation,indexOfEx[0],"exp")
            equation=equation.replace(unsolved,str(answer))

        elif(("/" in equation) or ("*" in equation)):
            indexOfMult=[]
            indexOfDiv=[]
            
            if("*" in equation):
                indexOfMult=multipleIndex("*",equation)
            
            if("/" in equation):
                indexOfDiv=multipleIndex("/",equation)
            
            if((len(indexOfMult)>0) and (len(indexOfDiv)>0)):
                if(indexOfMult[0]<indexOfDiv[0]):  
                    if(equation[indexBeforeSym(equation,indexOfMult[0])-1]=="-") and (equation[(indexOfMult[0])+1]=="-"):
                        unsolved=equation[indexBeforeSym(equation,indexOfMult[0])-1:(indexAfterSym(equation,indexOfMult[0])+1)]
                    elif(equation[indexBeforeSym(equation,indexOfMult[0])-1]=="-"):
                        unsolved=equation[indexBeforeSym(equation,indexOfMult[0])-1:(indexAfterSym(equation,indexOfMult[0])+1)]
                    elif(equation[(indexOfMult[0])+1]=="-"):
                        unsolved=equation[indexBeforeSym(equation,indexOfMult[0]):(indexAfterSym(equation,indexOfMult[0])+1)]
                    else:
                        unsolved=equation[indexBeforeSym(equation,indexOfMult[0]):(indexAfterSym(equation,indexOfMult[0])+1)]
                    
                    answer=solveEquation(equation,indexOfMult[0],"mult")
                    equation=equation.replace(unsolved,str(answer))
                else:           
                    if(equation[indexBeforeSym(equation,indexOfDiv[0])-1]=="-") and (equation[indexOfDiv[0]+1]=="-"):
                        unsolved=equation[indexBeforeSym(equation,indexOfDiv[0])-1:(indexAfteSym(equation,indexOfDiv[0])+1)]
                    elif(equation[indexBeforeSym(equation,indexOfDiv[0])-1]=="-"):
                        unsolved=equation[indexBeforeSym(equation,indexOfDiv[0])-1:(indexAfterSym(equation,indexOfDiv[0])+1)]
                    elif(equation[(indexOfDiv[0])+1]=="-"):
                        unsolved=equation[indexBeforeSym(equation,indexOfDiv[0]):(indexAfteSym(equation,indexOfDiv[0])+1)]
                    else:
                        unsolved=equation[indexBeforeSym(equation,indexOfDiv[0]):(indexAfterSym(equation,indexOfDiv[0])+1)]

                    answer=solveEquation(equation,indexOfDiv[0],"div")
                    if answer=="ERROR: Can't Divide By 0":
                        return answer
                   
                    else:
                        equation=equation.replace(unsolved,str(answer))
            elif(len(indexOfMult)>0):          
                if(equation[indexBeforeSym(equation,indexOfMult[0])-1]=="-") and (equation[(indexOfMult[0])+1]=="-"):
                    unsolved=equation[indexBeforeSym(equation,indexOfMult[0])-1:(indexAfterSym(equation,indexOfMult[0])+1)]
                elif(equation[indexBeforeSym(equation,indexOfMult[0])-1]=="-"):
                    unsolved=equation[indexBeforeSym(equation,indexOfMult[0])-1:(indexAfterSym(equation,indexOfMult[0])+1)]
                elif(equation[(indexOfMult[0])+1]=="-"):
                    unsolved=equation[indexBeforeSym(equation,indexOfMult[0]):(indexAfterSym(equation,indexOfMult[0])+1)]
                else:
                    unsolved=equation[indexBeforeSym(equation,indexOfMult[0]):(indexAfterSym(equation,indexOfMult[0]))+1]
                
                answer=solveEquation(equation,indexOfMult[0],"mult")
                equation=equation.replace(unsolved,str(answer))  

            elif(len(indexOfDiv)>0):
                if(equation[indexBeforeSym(equation,indexOfDiv[0])-1]=="-") and (equation[(indexOfDiv[0])+1]=="-"):
                    unsolved=equation[indexBeforeSym(equation,indexOfDiv[0])-1:(indexAfterSym(equation,indexOfDiv[0])+1)]
                elif(equation[indexBeforeSym(equation,indexOfDiv[0])-1]=="-"):
                    unsolved=equation[indexBeforeSym(equation,indexOfDiv[0])-1:(indexAfterSym(equation,indexOfDiv[0])+1)]
                elif(equation[(indexOfDiv[0])+1]=="-"):
                    unsolved=equation[indexBeforeSym(equation,indexOfDiv[0]):(indexAfterSym(equation,indexOfDiv[0])+1)]
                else:
                    unsolved=equation[indexBeforeSym(equation,indexOfDiv[0]):(indexAfterSym(equation,indexOfDiv[0])+1)]

                answer=solveEquation(equation,indexOfDiv[0],"div")
                if answer=="ERROR: Can't Divide By 0":
                    return answer
                
                else:
                    equation=equation.replace(unsolved,str(answer))

        elif(("+" in equation) or ("-" in equation)):
            indexOfAdd=[]
            indexOfSub=[]
            if("+" in equation):
                indexOfAdd=multipleIndex("+",equation)

            if("-" in equation):
                indexOfSub=multipleIndex("-",equation)
                if(indexOfSub[0]==0):
                    indexOfSub.pop(0)
                    
            if((len(indexOfAdd)==0) and (len(indexOfSub)==0)):
                return equation

            if((len(indexOfAdd)>0) and (len(indexOfSub)>0)):
                if(indexOfAdd[0]<indexOfSub[0]):
                    if(equation[indexBeforeSym(equation,indexOfAdd[0])-1]=="-"):
                        unsolved=equation[indexBeforeSym(equation,indexOfAdd[0])-1:(indexAfterSym(equation,indexOfAdd[0])+1)]
                    
                    else:
                        unsolved=equation[indexBeforeSym(equation,indexOfAdd[0]):(indexAfterSym(equation,indexOfAdd[0])+1)]
                    
                    answer=solveEquation(equation,indexOfAdd[0],"add")
                    equation=equation.replace(unsolved,str(answer))
                
                else:
                    if(equation[indexBeforeSym(equation,indexOfSub[0])-1]=="-"):
                        unsolved=equation[indexBeforeSym(equation,indexOfSub[0])-1:(indexAfterSym(equation,indexOfSub[0])+1)]

                    else:
                        unsolved=equation[indexBeforeSym(equation,indexOfSub[0]):(indexAfterSym(equation,indexOfSub[0])+1)]
                    answer=solveEquation(equation,indexOfSub[0],"sub")
                    equation=equation.replace(unsolved,str(answer))

            elif(len(indexOfAdd)>0):
                if(equation[indexBeforeSym(equation,indexOfAdd[0])-1]=="-"):
                    unsolved=equation[indexBeforeSym(equation,indexOfAdd[0])-1:(indexAfterSym(equation,indexOfAdd[0])+1)]

                else:
                    unsolved=equation[indexBeforeSym(equation,indexOfAdd[0]):(indexAfterSym(equation,indexOfAdd[0]))+1]
                answer=solveEquation(equation,indexOfAdd[0],"add")
                equation=equation.replace(unsolved,str(answer))  

            elif(len(indexOfSub)>0):
                if(equation[indexBeforeSym(equation,indexOfSub[0])-1]=="-"):
                    unsolved=equation[indexBeforeSym(equation,indexOfSub[0])-1:(indexAfterSym(equation,indexOfSub[0])+1)]

                else:
                    unsolved=equation[indexBeforeSym(equation,indexOfSub[0]):(indexAfterSym(equation,indexOfSub[0])+1)]
                answer=solveEquation(equation,indexOfSub[0],"sub")
                equation=equation.replace(unsolved,str(answer))
        
        else:
            break

    return equation

def solveEquation(equation,indexOfSym,sign):
    before=""
    after=""
    count=0
    for index in range((indexOfSym-1),-1,-1):
        if(equation[index] in symbols) and (equation[index]!="-"):
            break
        elif(equation[index]=="-"):
            before=equation[index]+before
            break
        else:
            before=equation[index]+before
    
    for index in range((indexOfSym+1),len(equation),1):
        if(equation[index] in symbols) and (equation[index]!="-"):
            break
        elif(equation[index]=="-"):
            if(count<1):
                count=1
                after=after+equation[index]
            else:
                break
        else:
            after=after+equation[index]
    
    count=0
    if sign=="exp":
        return(float(before)**float(after))
    elif sign=="mult":
        return(float(before)*float(after))
    elif sign=="div":
        if float(after)==0:
            return "ERROR: Can't Divide By 0"
        else:
            return(float(before)/float(after))
    elif sign=="add":
        return(float(before)+float(after))
    elif sign=="sub":
        return(float(before)-float(after))
    else:
        return "broke"

def indexBeforeSym(equation,indexOfSym):
    indexOfBeforeSym=0
    for index in range((indexOfSym-1),-1,-1):
        if(equation[index] in symbols):
            indexOfBeforeSym=index+1
            break
        if(index==0):
            indexOfBeforeSym=0
            break
    return(indexOfBeforeSym)

def indexAfterSym(equation,indexOfSym):
    indexOfAfterSym=0
    count=0
    for index in range((indexOfSym+1),(len(equation)),1):
        if(equation[index] in symbols) and (equation[index]!="-") :
            indexOfAfterSym=index-1
            break
        elif(equation[index]=="-"):
            if count<1:
                count=1
            else:
                indexOfAfterSym=index-1
                break
        if(index==len(equation)-1):
            indexOfAfterSym=len(equation)-1
            break
    count=0
    return indexOfAfterSym


    
inputNum=Entry(window)
inputNum.grid(row=0,column=0,columnspan=3)

backBtn=Button(window,text="<--",command=back)
backBtn.grid(row=0,column=3,sticky=W)


OneBtn=Button(window,text="1",command=one)
OneBtn.grid(row=2,column=0,sticky=W)

TwoBtn=Button(window,text="2",command=two)
TwoBtn.grid(row=2,column=1,sticky=W)

ThreeBtn=Button(window,text="3",command=three)
ThreeBtn.grid(row=2,column=2,sticky=W)

FourBtn=Button(window,text="4",command=four)
FourBtn.grid(row=3,column=0,sticky=W)

FiveBtn=Button(window,text="5",command=five)
FiveBtn.grid(row=3,column=1,sticky=W)

SixBtn=Button(window,text="6",command=six)
SixBtn.grid(row=3,column=2,sticky=W)

SevenBtn=Button(window,text="7",command=seven)
SevenBtn.grid(row=4,column=0,sticky=W)

EightBtn=Button(window,text="8",command=eight)
EightBtn.grid(row=4,column=1,sticky=W)

NineBtn=Button(window,text="9",command=nine)
NineBtn.grid(row=4,column=2,sticky=W)

ZeroBtn=Button(window,text="0",command=zero)
ZeroBtn.grid(row=5,column=1,sticky=W)



par1Btn=Button(window,text="(",command=parenth1)
par1Btn.grid(row=1, column=1,sticky=W)

par2Btn=Button(window,text=")",command=parenth2)
par2Btn.grid(row=1, column=2,sticky=W)

decBtn=Button(window,text=".",command=dec)
decBtn.grid(row=5, column=2,sticky=W)

expoBtn=Button(window,text="^",command=expo)
expoBtn.grid(row=1, column=0,sticky=W)



addBtn=Button(window,text="+",command=add)
addBtn.grid(row=1,column=3,sticky=W)

subBtn=Button(window,text="-",command=sub)
subBtn.grid(row=2,column=3,sticky=W)

multBtn=Button(window,text="*",command=mult)
multBtn.grid(row=3,column=3,sticky=W)

divBtn=Button(window,text="/",command=div)
divBtn.grid(row=4,column=3,sticky=W)


clearBtn=Button(window,text="CE",command=clear_text)
clearBtn.grid(row=5,column=0,sticky=W)

enterBtn=Button(window,text="=",command=enter)
enterBtn.grid(row=5,column=3,sticky=W)

window.mainloop()