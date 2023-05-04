birthYear=0;#Assuming our initial age as 0 when we born

godChoice=int(input("The God choice is :")) #Assume you as a God and Enter the value,But in the real world we cannot know the value

while (birthYear<=godChoice):
    print("Your age is", birthYear)
    if(birthYear != godChoice):
        print("Enjoy your Life") 
    else:
        print("God decided to give rest to your soul ")    
    birthYear+=1 