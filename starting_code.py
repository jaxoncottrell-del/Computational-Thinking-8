import random 

hidden_number = random.randint (2,4000)
#print (hidden_number)
number = int (input ("guess between 2 and 4000"))
if number == hidden_number:
     print ("yay! good job")
if number > hidden_number:
     print ("To high. :(")