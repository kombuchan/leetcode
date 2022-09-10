


def temperatureFun(inp):
    x=0
    noMatch = 0
    temp = 0
    answers=[]
    loopnumber = 0
    while(True): 
        
 
        for loopnumber in range(len(inp)):
           
            temp = inp[x]
           

            if(loopnumber<x):
                continue
            else:
                if(inp[loopnumber]>temp):
                    
                    answers.append(loopnumber-x)
                    x+=1
                    noMatch=0
                    break

                else:
                    noMatch+=1
   
        
        if(noMatch >= (len(inp)-x)):
            answers.append(0)
            x+=1
            noMatch=0
        if((x-1)>=(len(inp)-1)):
            return(answers)
        
  
print(temperatureFun([30,60,90]))


#iterate through the list
#store item that is being compared in a temp variable
#compare item in the list with the temp variable
#if the item in the list is greater, do item in the list-temp to find the distance between the two values and append
#when items are done being compared, and no values are greater, append 0 to answers
#keep running this until the temp variables values is equal to the final value.