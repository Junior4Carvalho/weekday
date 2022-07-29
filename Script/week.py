week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
ask = input("What day is today? ")
if ask.capitalize() in week:
    try:
        if ask.capitalize() != week[0] and ask.capitalize() != week[6]:
            print("Today is a Weekday!")

        else:
            print("Today is a Weekend!")

    except:
        print("Type only what's on this list: \n {} ".format(week))

else:
    print("Type only what's on this list: \n {} ".format(week))
    
 #Copyright-@Junior4Carvalho
