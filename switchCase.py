import datetime

now=datetime.datetime.now()

currentDay=now.strftime("%A")

match currentDay:
    case "Monday":
        print("Current Day is" ,currentDay)

    case "Tuesday":
        print("Current Day is" ,currentDay)

    case "Wednesday":
        print("Current Day is" ,currentDay)

    case "Thursday":
        print("Current Day is" ,currentDay)

    case "Friday":
        print("Current Day is" ,currentDay)

    case "Saturday":
        print("Current Day is" ,currentDay)

    case "Sunday":
        print("Current Day is" ,currentDay)