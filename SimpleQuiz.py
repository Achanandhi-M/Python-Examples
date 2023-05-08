totalMark=0
def question():
	 global totalMark
	 print('This is Question No 1')
	 answer1=int(input('Python was founded in year 1989?  press 0 for False and 1 for True :'))
	 if answer1 == 1:
		 print('You are right!')
		 totalMark+=1
		 question1()
	 elif answer1 == 0:
	  print('Hard Luck')
	  question1()
	 else:
	  print('Invalid Option, Please Enter Correct Option')
	  question()

def question1():
	 global totalMark
	 print('This is Question No 2')
	 answer2=int(input('is Python can be used in web develpoment?  Type 0 for False and 1 for True :'))
	 if answer2 == 1:
		 print('You are right!')
		 totalMark+=1
		 question2()
	 elif answer2 == 0:
	  print('Hard Luck')
	  question2()
	 else:
	  print('Invalid Option, Please Enter Correct Option')
	  question1()

def question2():
	 global totalMark
	 print('This is Question No 3')
	 answer3=int(input('is Python is open source? Type 0 for False  and 1 for True : '))
	 if answer3 == 1:
		 print('You are right!')
		 totalMark+=1
		 mark()
		 

	 elif answer3 == 0:
	  print('Hard Luck')
	  mark()
	  

	 else:
	  print('Invalid Option, Please Enter Correct Option')
	  question2()	


def mark():
	 if totalMark == 0 :
		 print('Your mark is' ,totalMark)
		 print('Work Hard')
	 elif totalMark == 1:
		 print('Your mark is' ,totalMark)
		 print('Put some effort')
	 elif totalMark == 2:
		 print('Your mark is' ,totalMark)
		 print('Be patient')
	 else:
		 print('Your mark is' ,totalMark)
		 print('You are awesome')



Number=int(input('Enter your Enrollement Number: '))

question()
