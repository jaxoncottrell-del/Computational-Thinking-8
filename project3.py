sweet=0
sour=0
salty=0
answer1 = input ("Do you prefer A ice cream, B candy, C Popcorn")
if answer1 == "A":
    sweet += 1 
elif answer1 == "B":
    sour +=1 
elif answer1 == "C":
    salty += 1 
   
answer2 = input ("what do you prefer on a hot day A sweet, B sour, C salty")
if answer2 == "A" or answer1 == "a":
        sweet += 1
elif answer2 == "B":
        sour +=1 
elif answer2 == "C":
        salty +=1  
answer3 = input ("what are your favorite movie snack A skittles, B sour patch kids, C pretzel") 
if answer1 == "A":
     sweet += 1 
elif answer1 == "B":
    sour +=1 
elif answer1 == "C":
    salty += 1 
   
answer4 = input ("what is your favorite genre A hip hop, B pop, C rock and roll") 
if answer1 == "A":
         sweet += 1 
elif answer1 == "B":
        sour +=1 
elif answer1 == "C":
        salty += 1 
answer5 = input ("what your favoite sport A soccer, B baseball, C basketball")
if answer1 == "A":
      sweet +=1 
elif answer1 == "B":
     sour +=1
elif answer1 ==  "C":
    salty +=1
     # end of quiz 
if sweet  > sour  and sweet > salty:
            #you get this ending by doing sweet the most 
            print ("you loves sweet things")
elif sour > sweet and sour > salty:
            #you get this ending by doing  sour the most 
            print (" you are a sour person!")
elif salty  > sour  and salty > sweet:
           #you get this ending by doing salty the most 
          print ("I also love salty things")



