#EDWARD LEONARDO
#TP058284

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#ROLE_SELECTION
def role_selection():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nPlease choose the role : "
            "\n1. Admin"
            "\n2. Student"
            "\n3. Guest"
            "\n4. Exit")
    RS_select = int(input("Please enter your role based on the number : "))

    while (RS_select >= 0):
        if(RS_select == 1):
            admin_login()
            break
        elif(RS_select == 2):
            reg_login()
            break
        elif(RS_select == 3):
            guest_main_menu()
            break
        elif(RS_select == 4):
            exit_menu()
            break
        else:
            while (RS_select > 4 or RS_select < 1):
                print("\nInvalid number!")
                RS_select = int(input("Please enter your role based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#EXIT_MENU
def exit_menu():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("Thankyou, Have a nice day!")
    exitmenu_des = str(input("Press '1' to go back to Role Selection, or enter any key to terminate the program"))
    if (exitmenu_des == "1"):
        role_selection()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#ADMIN_LOGIN
def admin_login():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Admin. Please enter your identification : ")
    admin_ID = str(input("ID NAME : "))
    admin_pass = str(input("PASSWORD : "))

    if(admin_ID == "edo14" and admin_pass == "test123"):
        admin_main_menu()
    else:
        admin_login_choice = str(input("Your ID or Password is incorrect, enter 1 to try again, or any other key to exit : "))
        if (admin_login_choice == "1"):
            admin_login()
        else:
            exit_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 
               
#ADMIN_MAIN_MENU
def admin_main_menu():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Admin, Please enter what records do you want to access : "
            "\n1. Add Records"
            "\n2. Display All Records"
            "\n3. Search Specific Records"
            "\n4. Sort and Display Records"
            "\n5. Modify Records"
            "\n6. Log Out"
            "\n7. Exit")
    adminmm_select = int(input("Please enter your choice based on the number : "))

    while (adminmm_select >= -100):
        if(adminmm_select == 1):
            add_main_menu()
            break
        elif(adminmm_select == 2):
            display_main_menu()
            break
        elif(adminmm_select == 3):
            search_main_menu()
            break
        elif(adminmm_select == 4):
            sort_main_menu()
            break
        elif(adminmm_select == 5):
            mod_main_menu()
            break
        elif(adminmm_select == 6):
            admin_login()
            break
        elif(adminmm_select == 7):
            exit_menu()
            break
        else:
            while (adminmm_select > 7 or adminmm_select < 1):
                print("\nInvalid number!")
                adminmm_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    
#ADD_MAIN_MENU
def add_main_menu():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Admin, Please enter what records do you want to add : "
            "\n1. Add Coach Records"
            "\n2. Add Sport Records"
            "\n3. Add Sport Schedule Records"
            "\n4. Back to Admin Main Menu"
            "\n5. Exit")
    addmm_select = int(input("Please enter your choice based on the number : "))

    while (addmm_select > -100):
        if(addmm_select == 1):
            add_coach()
            break
        elif(addmm_select == 2):
            add_sport()
            break
        elif(addmm_select == 3):
            add_schedule()
            break
        elif(addmm_select == 4):
            admin_main_menu()
            break
        elif(addmm_select == 5):
            exit_menu()
            break
        else:
            while (addmm_select > 5 or addmm_select < 1):
                print("\nInvalid number!")
                addmm_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#ADD_COACH
def add_coach():
    newcoach_list = []
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!\n")
    
    newcoach_IDcheck = ("ID")
    newcoach_ID = id_auto(newcoach_IDcheck)
    print("The New Coach's ID : "+newcoach_ID)
    newcoach_list.append(newcoach_ID)

    newcoach_name = str(input("Enter the new coach's name : "))
    newcoach_list.append(newcoach_name)

    newcoach_datej = str(input("Enter the new coach's Join Date (dd/mm/yyyy) : "))
    newcoach_list.append(newcoach_datej)

    newcoach_datet = str(input("Enter the new coach's Termination Date (If new, enter --/--/--) : "))
    newcoach_list.append(newcoach_datet)

    newcoach_pay = int(input("Enter the new coach's Hourly Rates in RM (Example : if 200 MYR/Hr, then enter '200')(Range of pay is 100-500RM per hr) : "))
    while(newcoach_pay>500 or newcoach_pay<100):
        print("Wrong Input! The pay is out of range")
        newcoach_pay = int(input("Enter the new coach's Hourly Rates in RM (Example : if 200 MYR/Hr, then enter '200')(Range of pay is 100-500RM per hr) : "))
    newcoach_pay = str(newcoach_pay)
    newcoach_list.append(newcoach_pay+" RM/Hr")

    newcoach_phone = str(input("Enter the new coach's Phone Number : "))
    newcoach_list.append(newcoach_phone)

    newcoach_address = str(input("Enter the new coach's Address : "))
    newcoach_list.append(newcoach_address)

    newcoach_loc = str(input("Enter the new coach Location's ID (Type 'help' if the Location ID list is needed) : "))
    while (newcoach_loc == "help" or newcoach_loc == "HELP" or newcoach_loc == "Help"):
        newcoach_help = open("help_locationID.txt","r")
        print (newcoach_help.read())
        newcoach_help.close()
        newcoach_loc = str(input("Enter the new coach Location's ID (Type 'help' if the Location ID list is needed) : "))

    newcoach_indicator = "0"
    while (newcoach_indicator == "0"):    
        if (newcoach_loc == "L001"):
            newcoach_indicator = "1"
            newcoach_list.append(newcoach_loc)
            newcoach_list.append("Surabaya")
        elif (newcoach_loc == "L002"):
            newcoach_indicator = "1"
            newcoach_list.append(newcoach_loc)
            newcoach_list.append("Malang")
        elif (newcoach_loc == "L003"):
            newcoach_indicator = "1"
            newcoach_list.append(newcoach_loc)
            newcoach_list.append("Lampung")
        else:
            print("Wrong Input!")
            newcoach_loc = str(input("Enter the new coach Location's ID (Type 'help' if the Location ID list is needed) : "))
            while (newcoach_loc == "help" or newcoach_loc == "HELP" or newcoach_loc == "Help"):
                newcoach_loc_help = open("help_locationID.txt","r")
                print (newcoach_loc_help.read())
                newcoach_loc_help.close()
                newcoach_loc = str(input("Enter the new coach Location's ID (Type 'help' if the Location ID list is needed) : "))    

    help_sport(newcoach_loc)

    newcoach_sport = str(input("Enter the new coach Sport's ID : "))
    newcoach_list.append(newcoach_sport)

    newcoach_sportn = str(sportname_search(newcoach_sport))
    newcoach_list.append(newcoach_sportn)

    newcoach_rating = float(input("Enter the new coach's Rating (Enter '0.0' if the coach is new) : "))
    newcoach_rating = str(newcoach_rating)
    newcoach_list.append(newcoach_rating)

    newcoach_norating = str("0")
    newcoach_list.append(newcoach_norating)

    recordscoach_display(newcoach_list)

    newcoach_locn = str(newcoach_list[8])
    newcoach_pay = str(newcoach_list[4])
    newcoach_rsum = str(0)
    newcoach_final = str(newcoach_ID+" | "+newcoach_name+" | "+newcoach_datej+" | "+newcoach_datet+" | "+newcoach_pay+" | "+newcoach_phone+" | "+newcoach_address+" | "+newcoach_loc+" | "+newcoach_locn+" | "+newcoach_sport+" | "+newcoach_sportn+" | "+"R"+newcoach_rating+" | "+newcoach_norating+" | "+newcoach_rsum+"\n")
    newcoach_des = str(input("Please enter '1' to enter the data into the database, or enter any key to quit back to Add Main Menu : "))
    if (newcoach_des == "1"):
        newcoach_save = open("allcoach.txt","a")
        newcoach_save.write(newcoach_final)
        newcoach_save.close()
        if (newcoach_loc == "L001"):
            newcoach_save = open("coach1surabaya.txt","a")
            newcoach_save.write(newcoach_final)
            newcoach_save.close()
        elif (newcoach_loc == "L002"):
            newcoach_save = open("coach2malang.txt","a")
            newcoach_save.write(newcoach_final)
            newcoach_save.close()
        elif (newcoach_loc == "L003"):
            newcoach_save = open("coach3lampung.txt","a")
            newcoach_save.write(newcoach_final)
            newcoach_save.close()
        input("Save Successful!"
        "\nPress anything to go back to Add Main Menu")
        add_main_menu()
    else:
        input("OK, press anything to go back to Add Main Menu")
        add_main_menu()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#ADD_SPORT
def add_sport():
    newsport_list =[]
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!\n")

    newsport_IDcheck = str("S")
    newsport_ID = id_auto(newsport_IDcheck)
    print("The New Sport's ID : "+newsport_ID)
    newsport_list.append(newsport_ID)

    newsport_name = str(input("Enter the new Sport's Name : "))
    newsport_list.append(newsport_name)

    newsport_loc = str(input("Enter the new Sport's Location ID (Type 'Help' if the location ID list is needed): "))
    while (newsport_loc == "help" or newsport_loc == "HELP" or newsport_loc == "Help"):
        newsport_help = open("help_locationID.txt","r")
        print (newsport_help.read())
        newsport_help.close()
        newsport_loc = str(input("Enter the new Sport's Location ID (Type 'Help' if the location ID list is needed): "))

    newsport_indicator = "0"
    while (newsport_indicator == "0"):    
        if (newsport_loc == "L001"):
            newsport_indicator = "1"
            newsport_list.append(newsport_loc)
            newsport_list.append("Surabaya")
        elif (newsport_loc == "L002"):
            newsport_indicator = "1"
            newsport_list.append(newsport_loc)
            newsport_list.append("Malang")
        elif (newsport_loc == "L003"):
            newsport_indicator = "1"
            newsport_list.append(newsport_loc)
            newsport_list.append("Lampung")
        else:
            print("Wrong Input!")
            newsport_loc = str(input("Enter the new Sport's Location ID (Type 'Help' if the location ID list is needed): "))
            while (newsport_loc == "help" or newsport_loc == "HELP" or newsport_loc == "Help"):
                newsport_help = open("help_locationID.txt","r")
                print (newsport_help.read())
                newsport_help.close()
                newsport_loc = str(input("Enter the new Sport's Location ID (Type 'Help' if the location ID list is needed): "))    

    recordssport_display(newsport_list)

    newsport_locn = str(newsport_list[3])
    newsport_final = str(newsport_ID+" | "+newsport_name+" | "+newsport_loc+" | "+newsport_locn+"\n")
    newsport_des = str(input("Please enter '1' to enter the data into the database, or enter any key to quit back to Add Main Menu : "))
    if (newsport_des == "1"):
        newsport_save = open("allsport.txt","a")
        newsport_save.write(newsport_final)
        newsport_save.close()
        if (newsport_loc == "L001"):
            newsport_save = open("sport1surabaya.txt","a")
            newsport_save.write(newsport_final)
            newsport_save.close()
        elif (newsport_loc == "L002"):
            newsport_save = open("sport2malang.txt","a")
            newsport_save.write(newsport_final)
            newsport_save.close()
        elif (newsport_loc == "L003"):
            newsport_save = open("sport3lampung.txt","a")
            newsport_save.write(newsport_final)
            newsport_save.close()
        input("Save Successful!"
        "\nPress anything to go back to Add Main Menu")
        add_main_menu()
    else:
        input("OK, press anything to go back to Add Main Menu")
        add_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#ADD_SCHEDULE
def add_schedule():
    newsch_list =[]
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!\n")

    newsch_IDcheck = str("SCH")
    newsch_ID = id_auto(newsch_IDcheck)
    print("The New Schedule's ID : "+newsch_ID)
    newsch_list.append(newsch_ID)

    newsch_LID = str(input("Enter the Location's ID of the lesson (Type 'help' if the Location ID list is needed)(Lxxx) : "))
    while (newsch_LID == "help" or newsch_LID == "HELP" or newsch_LID == "Help"):
        newsch_help = open("help_locationID.txt","r")
        print (newsch_help.read())
        newsch_help.close()
        newsch_LID = str(input("Enter the Location's ID of the lesson (Type 'help' if the Location ID list is needed)(Lxxx) : "))
        
    newsch_indicator = 0
    while (newsch_indicator == 0):    
        if (newsch_LID == "L001"):
            newsch_indicator = 1
            newsch_list.append(newsch_LID)
            newsch_list.append("Surabaya")
        elif (newsch_LID == "L002"):
            newsch_indicator = 1
            newsch_list.append(newsch_LID)
            newsch_list.append("Malang")
        elif (newsch_LID == "L003"):
            newsch_indicator = 1
            newsch_list.append(newsch_LID)
            newsch_list.append("Lampung")
        else:
            print("Wrong Input!")
            newsch_LID = str(input("Enter the Location's ID of the lesson (Type 'help' if the Location ID list is needed)(Lxxx) : "))
            while (newsch_LID == "help" or newsch_LID == "HELP" or newsch_LID == "Help"):
                newsch_help = open("help_locationID.txt","r")
                print (newsch_help.read())
                newsch_help.close()
                newsch_LID = str(input("Enter the Location's ID of the lesson (Type 'help' if the Location ID list is needed)(Lxxx) : "))

    help_sport(newsch_LID)
    newsch_SID = str(input("Enter the Sport's ID of the lesson(Sxxx) : "))
    newsch_list.append(newsch_SID)

    newsch_SIDn = str(sportname_search(newsch_SID))
    newsch_list.append(newsch_SIDn)
    
    help_coach(newsch_LID,newsch_SID)
    newsch_CID = str(input("Enter the Coach's ID of the lesson(IDxxx) : "))
    newsch_list.append(newsch_CID)

    newsch_CIDn = str(coachname_search(newsch_CID))
    newsch_list.append(newsch_CIDn)

    newsch_day = str(input("Enter the lesson day in number (Monday is 1) (Type 'help' if the number list is needed) : "))
    while (newsch_day == "help" or newsch_day == "HELP" or newsch_day == "Help"):
        print ("\nThe Day Number List : \nMonday\t\t= 1\nTuesday\t\t= 2\nWednesday\t= 3\nThursday\t= 4\nFriday\t\t= 5\nSaturday\t= 6\nSunday\t\t= 7")
        newsch_day = str(input("Enter the lesson day in number (Type 'help' if the number list is needed) : "))

    newsch_day = int(newsch_day)

    while (newsch_day>7 or newsch_day<1):
        print("Wrong Input!")
        newsch_day = str(input("Enter the lesson day in number (Monday is 1) (Type 'help' if the number list is needed) : "))
        while (newsch_day == "help" or newsch_day == "HELP" or newsch_day == "Help"):
            print ("\nThe Day Number List : \nMonday\t\t= 1\nTuesday\t\t= 2\nWednesday\t= 3\nThursday\t= 4\nFriday\t\t= 5\nSaturday\t= 6\nSunday\t\t= 7")
            newsch_day = str(input("Enter the lesson day in number (Type 'help' if the number list is needed) : "))    
        newsch_day = int(newsch_day)

    if(newsch_day == 1):
        newsch_list.append("Monday")
    elif(newsch_day == 2):
        newsch_list.append("Tuesday")
    elif(newsch_day == 3):
        newsch_list.append("Wednesday")
    elif(newsch_day == 4):
        newsch_list.append("Thursday")
    elif(newsch_day == 5):
        newsch_list.append("Friday")
    elif(newsch_day == 6):
        newsch_list.append("Saturday")
    elif(newsch_day == 7):
        newsch_list.append("Sunday")

    newsch_stime = str(input("Enter the lesson starting time in thousand (05.00 = 5 am, 17.00 = 5 pm)(Type 'help' if assistance is needed) : "))
    while (newsch_stime == "help" or newsch_stime == "HELP" or newsch_stime == "Help"):
        newsch_help = open("help_time.txt","r")
        print(newsch_help.read())
        newsch_help.close()
        newsch_stime = str(input("Enter the lesson starting time in thousand (Type 'help' if assistance is needed) : "))

    newsch_stimet = str(newsch_stime)
    newsch_stime = float(newsch_stime)

    while (newsch_stime<00.00 or newsch_stime>23.59):
        print("Wrong Input!")
        newsch_stime = str(input("Enter the lesson starting time in thousand (Type 'help' if assistance is needed) : "))
        while (newsch_stime == "help" or newsch_stime == "HELP" or newsch_stime == "Help"):
            newsch_help = open("help_time.txt","r")
            print(newsch_help.read())
            newsch_help.close()
            newsch_stime = str(input("Enter the lesson starting time in thousand (Type 'help' if assistance is needed) : "))
        newsch_stimet = str(newsch_stime)
        newsch_stime = float(newsch_stime)

    if (newsch_stime>= 00.00 and newsch_stime<=11.59):
        newsch_list.append(newsch_stimet+" AM")
    else:
        newsch_list.append(newsch_stimet+" PM")

    newsch_dura = int(input("Enter the lesson time duration in minutes (1 Hour = 60 Minutes)(Maximum Duration is 180 Minutes/3 Hours) : "))
    while (newsch_dura<0 or newsch_dura>180):
        print("Wrong Input!")
        newsch_dura = int(input("Enter the lesson time duration in minutes (1 Hour = 60 Minutes)(Maximum Duration is 180 Minutes/3 Hours) : "))
    newsch_dura = str(newsch_dura)
    newsch_list.append(newsch_dura+" Minutes")

    recordsschedule_display(newsch_list)
    newsch_schID = (newsch_list[0])
    newsch_LIDn = (newsch_list[2])
    newsch_day = (newsch_list[7])
    newsch_stimef = (newsch_list[8])
    newsch_duraf = (newsch_list[9])
    newsch_final = str(newsch_schID+" | "+newsch_LID+" | "+newsch_LIDn+" | "+newsch_SID+" | "+newsch_SIDn+" | "+newsch_CID+" | "+newsch_CIDn+" | "+newsch_day+" | "+newsch_stimef+" | "+newsch_duraf+"\n")
    newsch_des = str(input("Please enter '1' to enter the data into the database, or enter any key to quit back to Add Main Menu : "))
    if (newsch_des == "1"):
        newsch_save = open("allsportschedule.txt","a")
        newsch_save.write(newsch_final)
        newsch_save.close()
        if (newsch_LID == "L001"):
            newsch_save = open("sportschedule1surabaya.txt","a")
            newsch_save.write(newsch_final)
            newsch_save.close()
        elif (newsch_LID == "L002"):
            newsch_save = open("sportschedule2malang.txt","a")
            newsch_save.write(newsch_final)
            newsch_save.close()
        elif (newsch_LID == "L003"):
            newsch_save = open("sportschedule3lampung.txt","a")
            newsch_save.write(newsch_final)
            newsch_save.close()
        input("Save Successful!"
        "\nPress anything to go back to Add Main Menu")
        add_main_menu()
    else:
        input("OK, press anything to go back to Add Main Menu")
        add_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#DISPLAY_MAIN_MENU
def display_main_menu():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Admin, Please enter what records do you want to display : "
            "\n1. Display Coach Records"
            "\n2. Display Sport Records"
            "\n3. Display Registered Student Records"
            "\n4. Back to Admin Main Menu"
            "\n5. Exit")
    recordsmm_select = int(input("Please enter your choice based on the number : "))

    while (recordsmm_select > -100):
        if(recordsmm_select == 1):
            display_coach()
            break
        elif(recordsmm_select == 2):
            display_sport()
            break
        elif(recordsmm_select == 3):
            display_reg()
            break
        elif(recordsmm_select == 4):
            admin_main_menu()
            break
        elif(recordsmm_select == 5):
            exit_menu()
            break
        else:
            while (recordsmm_select > 5 or recordsmm_select < 1):
                print("\nInvalid number!")
                recordsmm_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#DISPLAY_COACH
def display_coach():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Admin, Please enter what records do you want to display : "
            "\n1. Coach in all Locations"
            "\n2. Coach in Surabaya"
            "\n3. Coach in Malang"
            "\n4. Coach in Lampung"
            "\n5. Back to Display Main Menu"
            "\n6. Exit")
    recordscoach_select = int(input("Please enter your choice based on the number : "))

    while (recordscoach_select > 0):
        if(recordscoach_select == 1):
            recordscoach_file = open("allcoach.txt","r")
            for line in recordscoach_file:
                recordscoach_list = str_to_list_convert(line)
                recordscoach_display(recordscoach_list)
            recordscoach_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordscoach_select == 2):
            recordscoach_file = open("coach1surabaya.txt","r")
            for line in recordscoach_file:
                recordscoach_list = str_to_list_convert(line)
                recordscoach_display(recordscoach_list)
            recordscoach_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordscoach_select == 3):
            recordscoach_file = open("coach2malang.txt","r")
            for line in recordscoach_file:
                recordscoach_list = str_to_list_convert(line)
                recordscoach_display(recordscoach_list)
            recordscoach_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordscoach_select == 4):
            recordscoach_file = open("coach3lampung.txt","r")
            for line in recordscoach_file:
                recordscoach_list = str_to_list_convert(line)
                recordscoach_display(recordscoach_list)
            recordscoach_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordscoach_select == 5):
            display_main_menu()
            break
        elif(recordscoach_select == 6):
            exit_menu()
            break
        else:
            while (recordscoach_select > 6 or recordscoach_select < 1):
                print("\nInvalid number!")
                recordscoach_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#DISPLAY_SPORT
def display_sport():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Admin, Please enter what records do you want to display : "
            "\n1. Sport in all Locations"
            "\n2. Sport in Surabaya"
            "\n3. Sport in Malang"
            "\n4. Sport in Lampung"
            "\n5. Back to Display Main Menu"
            "\n6. Exit")
    recordssport_select = int(input("Please enter your choice based on the number : "))

    while (recordssport_select > 0):
        if(recordssport_select == 1):
            recordssport_file = open("allsport.txt","r")
            for line in recordssport_file:
                recordssport_list = str_to_list_convert(line)
                recordssport_display(recordssport_list)
            recordssport_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordssport_select == 2):
            recordssport_file = open("sport1surabaya.txt","r")
            for line in recordssport_file:
                recordssport_list = str_to_list_convert(line)
                recordssport_display(recordssport_list)
            recordssport_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordssport_select == 3):
            recordssport_file = open("sport2malang.txt","r")
            for line in recordssport_file:
                recordssport_list = str_to_list_convert(line)
                recordssport_display(recordssport_list)
            recordssport_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordssport_select == 4):
            recordssport_file = open("sport3lampung.txt","r")
            for line in recordssport_file:
                recordssport_list = str_to_list_convert(line)
                recordssport_display(recordssport_list)
            recordssport_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordssport_select == 5):
            display_main_menu()
            break
        elif(recordssport_select == 6):
            exit_menu()
            break
        else:
            while (recordssport_select > 6 or recordssport_select < 1):
                print("\nInvalid number!")
                recordssport_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#DISPLAY_REG
def display_reg():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Admin, Please enter what records do you want to display : "
            "\n1. Registered Student in all Locations"
            "\n2. Registered Student in Surabaya"
            "\n3. Registered Student in Malang"
            "\n4. Registered Student in Lampung"
            "\n5. Back to Display Main Menu"
            "\n6. Exit")
    recordsreg_select = int(input("Please enter your choice based on the number : "))

    while (recordsreg_select > 0):
        if(recordsreg_select == 1):
            recordsreg_file = open("allregstudent.txt","r")
            for line in recordsreg_file:
                recordsreg_list = str_to_list_convert(line)
                recordsreg_display(recordsreg_list)
            recordsreg_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordsreg_select == 2):
            recordsreg_file = open("regstudent1surabaya.txt","r")
            for line in recordsreg_file:
                recordsreg_list = str_to_list_convert(line)
                recordsreg_display(recordsreg_list)
            recordsreg_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordsreg_select == 3):
            recordsreg_file = open("regstudent2malang.txt","r")
            for line in recordsreg_file:
                recordsreg_list = str_to_list_convert(line)
                recordsreg_display(recordsreg_list)
            recordsreg_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordsreg_select == 4):
            recordsreg_file = open("regstudent3lampung.txt","r")
            for line in recordsreg_file:
                recordsreg_list = str_to_list_convert(line)
                recordsreg_display(recordsreg_list)
            recordsreg_file.close()
            input("Press anything to go back to Records Main Menu")
            display_main_menu()
            break
        elif(recordsreg_select == 5):
            display_main_menu()
            break
        elif(recordsreg_select == 6):
            exit_menu()
            break
        else:
            while (recordsreg_select > 6 or recordsreg_select < 1):
                print("\nInvalid number!")
                recordsreg_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#SEARCH_MAIN_MENU
def search_main_menu():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Admin, Please enter what records do you want to search : "
            "\n1. Search Coach by Coach ID"
            "\n2. Search Coach by Overall Performance/Rating"
            "\n3. Sport by Sport ID"
            "\n4. Student by Student ID"
            "\n5. Back to Admin Main Menu"
            "\n6. Exit")
    searchmm_select = int(input("Please enter your choice based on the number : "))

    while (searchmm_select > -100):
        if(searchmm_select == 1):
            search_coach_id()
            break
        elif(searchmm_select == 2):
            search_coach_rating()
            break
        elif(searchmm_select == 3):
            search_sport_id()
            break
        elif(searchmm_select == 4):
            search_student_id()
            break
        elif(searchmm_select == 5):
            admin_main_menu()
            break
        elif(searchmm_select == 6):
            exit_menu()
            break
        else:
            while (searchmm_select > 5 or searchmm_select < 1):
                print("\nInvalid number!")
                searchmm_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#SEARCH_COACH_ID
def search_coach_id():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    search_coachID = str(input("Please Enter the ID of the Coach you want to search(IDxxx) : "))

    search_coachID_file = open("allcoach.txt","r")
    for line in search_coachID_file:
        if search_coachID in line:
            search_coachID_display = str_to_list_convert(line)
            recordscoach_display(search_coachID_display)
            break
    else:
        print("No Data Found!")
    input("Press any key to return back to Search Main Menu")
    search_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#SEARCH_COACH_RATING
def search_coach_rating():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    search_coachrate = str(input("Please Enter the rating of the Coach you want to search(Rx.x) : "))

    search_coachrate_file = open("allcoach.txt","r")
    for line in search_coachrate_file:
        if search_coachrate in line:
            search_coachrate_display = str_to_list_convert(line)
            recordscoach_display(search_coachrate_display)
            break
    else:
        print("No Data Found!")
    input("Press any key to return back to Search Main Menu")
    search_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#SEARCH_SPORT_ID
def search_sport_id():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    search_sportID = str(input("Please Enter the ID of the Sport you want to search(Sxxx) : "))

    search_sportID_file = open("allsport.txt","r")
    for line in search_sportID_file:
        if search_sportID in line:
            search_sportID_display = str_to_list_convert(line)
            recordssport_display(search_sportID_display)
            break
    else:
        print("No Data Found!")
    input("Press any key to return back to Search Main Menu")
    search_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#SEARCH_STUDENT_ID
def search_student_id():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    search_studentID = str(input("Please Enter the ID of the Student you want to search(STxxx) : "))

    search_studentID_file = open("allregstudent.txt","r")
    for line in search_studentID_file:
        if search_studentID in line:
            search_studentID_display = str_to_list_convert(line)
            recordsreg_display(search_studentID_display)
            break
    else:
        print("No Data Found!")
    input("Press any key to return back to Search Main Menu")
    search_main_menu()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#SORT_MAIN_MENU
def sort_main_menu():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Admin, Please enter what records do you want to sort in ascending order : "
            "\n1. Sort Coaches by Name"
            "\n2. Sort Coaches by Hourly Pay Rate"
            "\n3. Sort Coaches by Overall Performance/Rating"
            "\n4. Back to Admin Main Menu"
            "\n5. Exit")
    sortmm_select = int(input("Please enter your choice based on the number : "))

    while (sortmm_select > -100):
        if(sortmm_select == 1):
            sort_coach_name()
            break
        elif(sortmm_select == 2):
            sort_coach_pay()
            break
        elif(sortmm_select == 3):
            sort_coach_performance()
            break
        elif(sortmm_select == 4):
            admin_main_menu()
            break
        elif(sortmm_select == 5):
            exit_menu()
            break
        else:
            while (sortmm_select > 5 or sortmm_select < 1):
                print("\nInvalid number!")
                sortmm_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#SORT_COACH_NAMES
def sort_coach_name():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")

    sortname_datalist = []
    sortname_blist = []
    sortname_file = open("allcoach.txt","r")
    for line in sortname_file:
        sortname_datalist.append(line)
        sortname_namelist = str_to_list_convert(line)
        sortname_blist.append(sortname_namelist[1])

    sortname_length = len(sortname_blist)
    sortname_alist = bubble_sort(sortname_blist,sortname_length)

    sortname_finallist = []
    a = 0
    b = 0

    while (len(sortname_finallist) != sortname_length):
        if sortname_alist[a] in sortname_datalist[b]:
            sortname_finallist.append(sortname_datalist[b])
            sortname_datalist.pop(b)
            a += 1
            b = 0
        else:
            b += 1
    x = 0

    while (x != (len(sortname_finallist))):
        recordscoach_display(str_to_list_convert(sortname_finallist[x]))
        x += 1
    input("Press any key to return back to Sort Main Menu")
    sort_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#SORT_COACH_PAY
def sort_coach_pay():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")

    sortpay_datalist = []
    sortpay_blist = []
    sortpay_file = open("allcoach.txt","r")
    for line in sortpay_file:
        sortpay_datalist.append(line)
        sortpay_namelist = str_to_list_convert(line)
        sortpay_blist.append(sortpay_namelist[4])

    sortpay_length = len(sortpay_blist)
    sortpay_alist = bubble_sort(sortpay_blist,sortpay_length)

    sortpay_finallist = []
    a = 0
    b = 0

    while (len(sortpay_finallist) != sortpay_length):
        if sortpay_alist[a] in sortpay_datalist[b]:
            sortpay_finallist.append(sortpay_datalist[b])
            sortpay_datalist.pop(b)
            a += 1
            b = 0
        else:
            b += 1
    x = 0
    while (x != (len(sortpay_finallist))):
        recordscoach_display(str_to_list_convert(sortpay_finallist[x]))
        x += 1
    input("Press any key to return back to Sort Main Menu")
    sort_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#SORT_COACH_PERFORMANCE
def sort_coach_performance():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    sortperf_datalist = []
    sortperf_blist = []
    sortperf_file = open("allcoach.txt","r")
    for line in sortperf_file:
        sortperf_datalist.append(line)
        sortperf_namelist = str_to_list_convert(line)
        sortperf_blist.append(sortperf_namelist[11])

    sortperf_length = len(sortperf_blist)
    sortperf_alist = bubble_sort(sortperf_blist,sortperf_length)

    sortperf_finallist = []
    a = 0
    b = 0

    while (len(sortperf_finallist) != sortperf_length):
        if sortperf_alist[a] in sortperf_datalist[b]:
            sortperf_finallist.append(sortperf_datalist[b])
            sortperf_datalist.pop(b)
            a += 1
            b = 0
        else:
            b += 1
    x = 0
    while (x != (len(sortperf_finallist))):
        recordscoach_display(str_to_list_convert(sortperf_finallist[x]))
        x += 1
    input("Press any key to return back to Sort Main Menu")
    sort_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#MODIFY_MAIN_MENU
def mod_main_menu():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Admin, Please enter what records do you want to modify : "
            "\n1. Modify Coach Data"
            "\n2. Modify Sport Data"
            "\n3. Modify Sport Schedule Data"
            "\n4. Back to Admin Main Menu"
            "\n5. Exit")
    modmm_select = int(input("Please enter your choice based on the number : "))

    while (modmm_select > -100):
        if(modmm_select == 1):
            mod_coach()
            break
        elif(modmm_select == 2):
            mod_sport()
            break
        elif(modmm_select == 3):
            mod_schedule()
            break
        elif(modmm_select == 4):
            admin_main_menu()
            break
        elif(modmm_select == 5):
            exit_menu()
            break
        else:
            while (modmm_select > 5 or modmm_select < 1):
                print("\nInvalid number!")
                modmm_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#MODIFY_COACH
def mod_coach():
    modcoach_otherlist = []
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    modcoach_search = str(input("Please enter the Coach ID that you want to modify : "))
    modcoach_position = int(0)
    modcoach_file = open("allcoach.txt","r")
    for line in modcoach_file:
        modcoach_otherlist.append(line)
        if modcoach_search in line :
            del modcoach_otherlist[modcoach_position]
            modcoach_list = str_to_list_convert(line)
            modcoach_removeindicator = modcoach_list[7]
            recordscoach_display(modcoach_list)
            modcoach_des = str(input("Is this the right coach data? Enter '1' if correct, or any key to go back to Modify Main Menu : "))
            if (modcoach_des == "1"):
                modcoach_newlist = []
                modcoach_newlist.append(modcoach_list[0])

                modcoach_new = str(input("Enter the coach's name (If the data still the same, type 'same') : "))
                if (modcoach_new == "same" or modcoach_new == "Same" or modcoach_new == "SAME"):
                    modcoach_newlist.append(modcoach_list[1])
                else:
                    modcoach_newlist.append(modcoach_new)
                #modify coach date joined
                modcoach_new = str(input("Enter the coach's Date Joined (dd/mm/yyyy) (If the data still the same, type 'same') : "))
                if (modcoach_new == "same" or modcoach_new == "Same" or modcoach_new == "SAME"):
                    modcoach_newlist.append(modcoach_list[2])
                else:
                    modcoach_newlist.append(modcoach_new)
                #modify coach termination date
                modcoach_new = str(input("Enter the coach's Date of Termination (dd/mm/yyyy) (If the data still the same, type 'same') : "))
                if (modcoach_new == "same" or modcoach_new == "Same" or modcoach_new == "SAME"):
                    modcoach_newlist.append(modcoach_list[3])
                else:
                    modcoach_newlist.append(modcoach_new)

                modcoach_new = str(input("Enter the coach's hourly rate in MYR () (Example : if 200 MYR/Hr, then enter '200')(Range of pay is 100-500RM per hr) (If the data still the same, type 'same') : "))
                if (modcoach_new == "same" or modcoach_new == "Same" or modcoach_new == "SAME"):
                    modcoach_newlist.append(modcoach_list[4])
                else:
                    modcoach_new = int(modcoach_new)
                    while (modcoach_new > 500 or modcoach_new<100):
                        print("Value is out of range!")
                        modcoach_new = str(input("Enter the coach's hourly rate in MYR () (Example : if 200 MYR/Hr, then enter '200')(Range of pay is 100-500RM per hr) (If the data still the same, type 'same') : "))
                    modcoach_new = str(modcoach_new)
                    modcoach_newlist.append(modcoach_new+" RM/Hr")

                modcoach_new = str(input("Enter the coach's phone number (If the data still the same, type 'same') : "))
                if (modcoach_new == "same" or modcoach_new == "Same" or modcoach_new == "SAME"):
                    modcoach_newlist.append(modcoach_list[5])
                else:
                    modcoach_newlist.append(modcoach_new)
            
                modcoach_new = str(input("Enter the coach's address (If the data still the same, type 'same') : "))
                if (modcoach_new == "same" or modcoach_new == "Same" or modcoach_new == "SAME"):
                    modcoach_newlist.append(modcoach_list[6])
                else:
                    modcoach_newlist.append(modcoach_new)

                modcoach_new = str(input("Enter the coach's Location ID (Type 'Help' if the list of Location IDs is Needed) (If the data still the same, type 'same') : "))
                while (modcoach_new == "help" or modcoach_new == "Help" or modcoach_new == "HELP"):
                    modcoach_help = open("help_locationID.txt","r")
                    print (modcoach_help.read())
                    modcoach_help.close()
                    modcoach_new = str(input("Enter the coach's Location ID (Type 'Help' if the list of Location IDs is Needed) (If the data still the same, type 'same') : "))
                if (modcoach_new == "same" or modcoach_new == "Same" or modcoach_new == "SAME"):
                    modcoach_newlist.append(modcoach_list[7])
                    modcoach_newlist.append(modcoach_list[8])
                    modcoach_locindicator = modcoach_list[7]
                else:
                    modcoach_indicator = 0
                    while (modcoach_indicator == 0):    
                        if (modcoach_new == "L001"):
                            modcoach_indicator = 1
                            modcoach_newlist.append(modcoach_new)
                            modcoach_newlist.append("Surabaya")
                            modcoach_locindicator = "L001"
                        elif (modcoach_new == "L002"):
                            modcoach_indicator = 1
                            modcoach_newlist.append(modcoach_new)
                            modcoach_newlist.append("Malang")
                            modcoach_locindicator = "L002"
                        elif (modcoach_new == "L003"):
                            modcoach_indicator = 1
                            modcoach_newlist.append(modcoach_new)
                            modcoach_newlist.append("Lampung")
                            modcoach_locindicator = "L003"
                        else:
                            print("Wrong Input!")
                            modcoach_new = str(input("Enter the coach Location's ID (Type 'help' if the Location ID list is needed) (If the data still the same, type 'same') : "))
                            while (modcoach_new == "help" or modcoach_new == "HELP" or modcoach_new == "Help"):
                                modcoach_new_help = open("help_locationID.txt","r")
                                print (modcoach_new_help.read())
                                modcoach_new_help.close()
                                modcoach_new = str(input("Enter the coach Location's ID (Type 'help' if the Location ID list is needed) (If the data still the same, type 'same') : "))

                help_sport(modcoach_new)
                modcoach_new = str(input("Enter the coach's Sport ID (If the data still the same, type 'same') : "))
                if (modcoach_new == "same" or modcoach_new == "Same" or modcoach_new == "SAME"):
                    modcoach_newlist.append(modcoach_list[9])
                    modcoach_newlist.append(modcoach_list[10])
                else:
                    modcoach_newlist.append(modcoach_new)
                    modcoach_new = str(sportname_search(modcoach_new))
                    modcoach_newlist.append(modcoach_new)

                modcoach_newlist.append(modcoach_list[11])
                modcoach_newlist.append(modcoach_list[12])
                modcoach_newlist.append(modcoach_list[13])

                recordscoach_display(modcoach_newlist)
                modcoach_des = str(input("Please enter '1' to submit the modified the data, or enter any key to enter a new set of data : "))
                if (modcoach_des == "1"):
                    final = str(modcoach_newlist[0]+" | "+modcoach_newlist[1]+" | "+modcoach_newlist[2]+" | "+modcoach_newlist[3]+" | "+modcoach_newlist[4]+" | "+modcoach_newlist[5]+" | "+modcoach_newlist[6]+" | "+modcoach_newlist[7]+" | "+modcoach_newlist[8]+" | "+modcoach_newlist[9]+" | "+modcoach_newlist[10]+" | "+modcoach_newlist[11]+" | "+modcoach_newlist[12]+" | "+modcoach_newlist[13]+"\n")
                    modcoach_otherlist.insert(modcoach_position,final)
                else:
                    mod_coach()
            else:
                mod_main_menu()
        modcoach_position = (modcoach_position + 1)
    modcoach_file.close()

    modcoach_file = open("allcoach.txt","w")
    for x in range(modcoach_position):
        y = int(-modcoach_position+x)
        modcoach_add = modcoach_otherlist[y]
        modcoach_file.write(modcoach_add)
    modcoach_file.close()

    modcoach_otherlist = []
    modcoach_position = 0
    if (modcoach_removeindicator == "L001"):
        modcoach_file = open("coach1surabaya.txt","r")
        for line in modcoach_file:
            modcoach_otherlist.append(line)
            if modcoach_search in line:
                del modcoach_otherlist[modcoach_position]
                modcoach_position -= 1
            modcoach_position += 1
        modcoach_file.close()

        modcoach_file = open("coach1surabaya.txt","w")
        for x in range(modcoach_position):
            y = int(-modcoach_position+x)
            modcoach_add = modcoach_otherlist[y]
            modcoach_file.write(modcoach_add)
        modcoach_file.close()
        
    elif (modcoach_removeindicator == "L002"):
        modcoach_file = open("coach2malang.txt","r")
        for line in modcoach_file:
            modcoach_otherlist.append(line)
            if modcoach_search in line:
                del modcoach_otherlist[modcoach_position]
                modcoach_position -= 1
            modcoach_position += 1
        modcoach_file.close()

        modcoach_file = open("coach2malang.txt","w")
        for x in range(modcoach_position):
            y = int(-modcoach_position+x)
            modcoach_add = modcoach_otherlist[y]
            modcoach_file.write(modcoach_add)
        modcoach_file.close()
        
    elif (modcoach_removeindicator == "L003"):
        modcoach_file = open("coach3lampung.txt","r")
        for line in modcoach_file:
            modcoach_otherlist.append(line)
            if modcoach_search in line:
                del modcoach_otherlist[modcoach_position]
                modcoach_position -= 1
            modcoach_position += 1
        modcoach_file.close()

        modcoach_file = open("coach3lampung.txt","w")
        for x in range(modcoach_position):
            y = int(-modcoach_position+x)
            modcoach_add = modcoach_otherlist[y]
            modcoach_file.write(modcoach_add)
        modcoach_file.close()

    print("Done Deleting the data from old file, now printing the data into the new file")

    if (modcoach_locindicator == "L001"):
        modcoach_file = open("coach1surabaya.txt","a")
        modcoach_file.write(final)
        modcoach_file.close()
        
    elif (modcoach_locindicator == "L002"):
        modcoach_file = open("coach2malang.txt","a")
        modcoach_file.write(final)
        modcoach_file.close()
    
    elif (modcoach_locindicator == "L003"):
        modcoach_file = open("coach3lampung.txt","a")
        modcoach_file.write(final)
        modcoach_file.close()
    input("Done, Press any key to return to go back to Modify Main Menu")
    mod_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#MODIFY_SPORT
def mod_sport():
    modsport_otherlist = []
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    modsport_search = str(input("Please enter the Sport ID that you want to modify : "))
    modsport_position = int(0)
    modsport_file = open("allsport.txt","r")
    for line in modsport_file:
        modsport_otherlist.append(line)
        if modsport_search in line :
            del modsport_otherlist[modsport_position]
            modsport_list = str_to_list_convert(line)
            modsport_removeindicator = modsport_list[2]
            recordssport_display(modsport_list)
            modsport_des = str(input("Is this the right sport data? Enter '1' if correct, or any key to go back to Modify Main Menu : "))
            if (modsport_des == "1"):
                modsport_newlist = []
                modsport_newlist.append(modsport_list[0])

                modsport_new = str(input("Enter the sport's name (If the data still the same, type 'same') : "))
                if (modsport_new == "same" or modsport_new == "Same" or modsport_new == "SAME"):
                    modsport_newlist.append(modsport_list[1])
                else:
                    modsport_newlist.append(modsport_new)

                modsport_new = str(input("Enter the sport's Location ID (Type 'Help' if the list of Location IDs is Needed) (If the data still the same, type 'same') : "))
                while (modsport_new == "help" or modsport_new == "Help" or modsport_new == "HELP"):
                    modsport_help = open("help_locationID.txt","r")
                    print (modsport_help.read())
                    modsport_help.close()
                    modsport_new = str(input("Enter the coach's Location ID (Type 'Help' if the list of Location IDs is Needed) (If the data still the same, type 'same') : "))
                if (modsport_new == "same" or modsport_new == "Same" or modsport_new == "SAME"):
                    modsport_newlist.append(modsport_list[2])
                    modsport_newlist.append(modsport_list[3])
                    modsport_locindicator = (modsport_list[2])
                else:
                    modsport_indicator = 0
                    while (modsport_indicator == 0):    
                        if (modsport_new == "L001"):
                            modsport_indicator = 1
                            modsport_newlist.append(modsport_new)
                            modsport_newlist.append("Surabaya")
                            modsport_locindicator = "L001"
                        elif (modsport_new == "L002"):
                            modsport_indicator = 1
                            modsport_newlist.append(modsport_new)
                            modsport_newlist.append("Malang")
                            modsport_locindicator = "L002"
                        elif (modsport_new == "L003"):
                            modsport_indicator = 1
                            modsport_newlist.append(modsport_new)
                            modsport_newlist.append("Lampung")
                            modsport_locindicator = "L003"
                        else:
                            print("Wrong Input!")
                            modsport_new = str(input("Enter the coach Location's ID (Type 'help' if the Location ID list is needed) (If the data still the same, type 'same') : "))
                            while (modsport_new == "help" or modsport_new == "HELP" or modsport_new == "Help"):
                                modsport_new_help = open("help_locationID.txt","r")
                                print (modsport_new_help.read())
                                modsport_new_help.close()
                                modsport_new = str(input("Enter the coach Location's ID (Type 'help' if the Location ID list is needed) (If the data still the same, type 'same') : "))

                recordssport_display(modsport_newlist)
                modsport_des = str(input("Please enter '1' to submit the modified the data, or enter any key to enter a new set of data : "))
                if (modsport_des == "1"):
                    final = str(modsport_newlist[0]+" | "+modsport_newlist[1]+" | "+modsport_newlist[2]+" | "+modsport_newlist[3]+"\n")
                    modsport_otherlist.insert(modsport_position,final)
                else:
                    mod_sport()
            else:
                mod_main_menu()
        modsport_position = (modsport_position + 1)
    modsport_file.close()

    modsport_file = open("allsport.txt","w")
    for x in range(modsport_position):
        y = int(-modsport_position+x)
        modsport_add = modsport_otherlist[y]
        modsport_file.write(modsport_add)
    modsport_file.close()

    print("Deleting Old Data...")

    modsport_otherlist = []
    modsport_position = 0
    if (modsport_removeindicator == "L001"):
        modsport_file = open("sport1surabaya.txt","r")
        for line in modsport_file:
            modsport_otherlist.append(line)
            if modsport_search in line:
                del modsport_otherlist[modsport_position]
                modsport_position -= 1
            modsport_position += 1
        modsport_file.close()
        modsport_file = open("sport1surabaya.txt","w")
        for x in range(modsport_position):
            y = int(-modsport_position+x)
            print(y)
            modsport_add = modsport_otherlist[y]
            modsport_file.write(modsport_add)
        modsport_file.close()
        
    elif (modsport_removeindicator == "L002"):
        modsport_file = open("sport2malang.txt","r")
        for line in modsport_file:
            modsport_otherlist.append(line)
            if modsport_search in line:
                del modsport_otherlist[modsport_position]
                modsport_position -= 1
            modsport_position += 1
        modsport_file.close()

        modsport_file = open("sport2malang.txt","w")
        for x in range(modsport_position):
            y = int(-modsport_position+x)
            modsport_add = modsport_otherlist[y]
            modsport_file.write(modsport_add)
        modsport_file.close()
        
    elif (modsport_removeindicator == "L003"):
        modsport_file = open("sport3lampung.txt","r")
        for line in modsport_file:
            modsport_otherlist.append(line)
            if modsport_search in line:
                del modsport_otherlist[modsport_position]
                modsport_position -= 1
            modsport_position += 1
        modsport_file.close()

        modsport_file = open("sport3lampung.txt","w")
        for x in range(modsport_position):
            y = int(-modsport_position+x)
            modsport_add = modsport_otherlist[y]
            modsport_file.write(modsport_add)
        modsport_file.close()

    print("Done Deleting the data from old file, now printing the data into the new file...")

    if (modsport_locindicator == "L001"):
        modsport_file = open("sport1surabaya.txt","a")
        modsport_file.write(final)
        modsport_file.close()
        
    elif (modsport_locindicator == "L002"):
        modsport_file = open("sport2malang.txt","a")
        modsport_file.write(final)
        modsport_file.close()
    
    elif (modsport_locindicator == "L003"):
        modsport_file = open("sport3lampung.txt","a")
        modsport_file.write(final)
        modsport_file.close()
    input("Done, Press any key to return to go back to Modify Main Menu")
    mod_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#MODIFY_SCHEDULE
def mod_schedule():
    modschedule_otherlist = []
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    modschedule_search = str(input("Please enter the Schedule ID that you want to modify : "))
    modschedule_position = int(0)
    modschedule_file = open("allsportschedule.txt","r")
    for line in modschedule_file:
        modschedule_otherlist.append(line)
        if modschedule_search in line :
            del modschedule_otherlist[modschedule_position]
            modschedule_list = str_to_list_convert(line)
            modschedule_removeindicator = modschedule_list[1]
            recordsschedule_display(modschedule_list)
            modschedule_des = str(input("Is this the right schedule data? Enter '1' if correct, or any key to go back to Modify Main Menu : "))
            if (modschedule_des == "1"):
                modschedule_newlist = []
                modschedule_newlist.append(modschedule_list[0])

                modschedule_new = str(input("Enter the Location's ID of the lesson (Type 'Help' if the list of Location IDs is Needed)(If the data still the same, type 'same') : "))
                while (modschedule_new == "help" or modschedule_new == "HELP" or modschedule_new == "Help"):
                    modschedule_help = open("help_locationID.txt","r")
                    print (modschedule_help.read())
                    modschedule_help.close()
                    modschedule_new = str(input("Enter the Location's ID of the lesson (Type 'help' if the Location ID list is needed)(Lxxx) : "))

                if (modschedule_new == "same" or modschedule_new == "Same" or modschedule_new == "SAME"):
                    modschedule_newlist.append(modschedule_list[1])
                    modschedule_newlist.append(modschedule_list[2])
                    modschedule_locindicator = modschedule_list[1]
                else:
                    modschedule_indicator = 0
                    while (modschedule_indicator == 0):    
                        if (modschedule_new == "L001"):
                            modschedule_indicator = 1
                            modschedule_newlist.append(modschedule_new)
                            modschedule_newlist.append("Surabaya")
                            modschedule_locindicator = "L001"
                        elif (modschedule_new == "L002"):
                            modschedule_indicator = 1
                            modschedule_newlist.append(modschedule_new)
                            modschedule_newlist.append("Malang")
                            modschedule_locindicator = "L002"
                        elif (modschedule_new == "L003"):
                            modschedule_indicator = 1
                            modschedule_newlist.append(modschedule_new)
                            modschedule_newlist.append("Lampung")
                            modschedule_locindicator = "L003"
                        else:
                            print("Wrong Input!")
                            modschedule_new = str(input("Enter the Location's ID of the lesson (Type 'help' if the Location ID list is needed) (If the data still the same, type 'same') : "))
                            while (modschedule_new == "help" or modschedule_new == "HELP" or modschedule_new == "Help"):
                                modschedule_new_help = open("help_locationID.txt","r")
                                print (modschedule_new_help.read())
                                modschedule_new_help.close()
                                modschedule_new = str(input("Enter the Location's ID of the lesson (Type 'help' if the Location ID list is needed) (If the data still the same, type 'same') : "))

                help_sport(modschedule_new)
                modschedule_new = str(input("Enter the Sport's ID of the lesson(If the data still the same, type 'same')(Sxxx) : "))
                if (modschedule_new == "same" or modschedule_new == "Same" or modschedule_new == "SAME"):
                    modschedule_newlist.append(modschedule_list[3])
                else:
                    modschedule_newlist.append(modschedule_new)

                modschedule_new = str(sportname_search(modschedule_new))
                modschedule_newlist.append(modschedule_new)

                help_coach(modschedule_newlist[1],modschedule_newlist[3])
                modschedule_new = str(input("Enter the Coach's ID of the lesson(IDxxx) : "))
                if (modschedule_new == "same" or modschedule_new == "Same" or modschedule_new == "SAME"):
                    modschedule_newlist.append(modschedule_list[5])
                else:
                    modschedule_newlist.append(modschedule_new)

                modschedule_new = str(coachname_search(modschedule_new))
                modschedule_newlist.append(modschedule_new)

                modschedule_new = str(input("Enter the lesson day in number (Monday is 1) (Type 'help' if the number list is needed) : "))
                while (modschedule_new == "help" or modschedule_new == "HELP" or modschedule_new == "Help"):
                    print ("\nThe Day Number List : \nMonday\t\t= 1\nTuesday\t\t= 2\nWednesday\t= 3\nThursday\t= 4\nFriday\t\t= 5\nSaturday\t= 6\nSunday\t\t= 7")
                    modschedule_new = str(input("Enter the lesson day in number (Type 'help' if the number list is needed) : "))
            
                modschedule_new = int(modschedule_new)

                while (modschedule_new>7 or modschedule_new<1):
                    print("Wrong Input!")
                    modschedule_new = str(input("Enter the lesson day in number (Monday is 1) (Type 'help' if the number list is needed) : "))
                    while (modschedule_new == "help" or modschedule_new == "HELP" or modschedule_new == "Help"):
                        print ("\nThe Day Number List : \nMonday\t\t= 1\nTuesday\t\t= 2\nWednesday\t= 3\nThursday\t= 4\nFriday\t\t= 5\nSaturday\t= 6\nSunday\t\t= 7")
                        modschedule_new = str(input("Enter the lesson day in number (Type 'help' if the number list is needed) : "))    
                    modschedule_new = int(modschedule_new)

                if(modschedule_new == 1):
                    modschedule_newlist.append("Monday")
                elif(modschedule_new == 2):
                    modschedule_newlist.append("Tuesday")
                elif(modschedule_new == 3):
                    modschedule_newlist.append("Wednesday")
                elif(modschedule_new == 4):
                    modschedule_newlist.append("Thursday")
                elif(modschedule_new == 5):
                    modschedule_newlist.append("Friday")
                elif(modschedule_new == 6):
                    modschedule_newlist.append("Saturday")
                elif(modschedule_new == 7):
                    modschedule_newlist.append("Sunday")

                modschedule_new = str(input("Enter the lesson starting time in thousand (05.00 = 5 am, 17.00 = 5 pm)(Type 'help' if assistance is needed) : "))
                while (modschedule_new == "help" or modschedule_new == "HELP" or modschedule_new == "Help"):
                    modschedule_help = open("help_time.txt","r")
                    print(modschedule_help.read())
                    modschedule_help.close()
                    modschedule_new = str(input("Enter the lesson starting time in thousand (Type 'help' if assistance is needed) : "))

                modschedule_temp = str(modschedule_new)
                modschedule_new = float(modschedule_new)

                while (modschedule_new<00.00 or modschedule_new>23.59):
                    print("Wrong Input!")
                    modschedule_new = str(input("Enter the lesson starting time in thousand (Type 'help' if assistance is needed) : "))
                    while (modschedule_new == "help" or modschedule_new == "HELP" or modschedule_new == "Help"):
                        modschedule_help = open("help_time.txt","r")
                        print(modschedule_help.read())
                        modschedule_help.close()
                        modschedule_new = str(input("Enter the lesson starting time in thousand (Type 'help' if assistance is needed) : "))
                    modschedule_temp = str(modschedule_new)
                    modschedule_new = float(modschedule_new)

                if (modschedule_new>= 00.00 and modschedule_new<=11.59):
                    modschedule_newlist.append(modschedule_temp+" AM")
                else:
                    modschedule_newlist.append(modschedule_temp+" PM")

                modschedule_new = int(input("Enter the lesson time duration in minutes (1 Hour = 60 Minutes)(Maximum Duration is 180 Minutes/3 Hours) : "))
                while (modschedule_new<0 or modschedule_new>180):
                    print("Wrong Input!")
                    modschedule_new = int(input("Enter the lesson time duration in minutes (1 Hour = 60 Minutes)(Maximum Duration is 180 Minutes/3 Hours) : "))
                modschedule_new = str(modschedule_new)
                modschedule_newlist.append(modschedule_new+" Minutes")    

                recordsschedule_display(modschedule_newlist)
                modschedule_des = str(input("Please enter '1' to submit the modified the data, or enter any key to enter a new set of data : "))
                if (modschedule_des == "1"):
                    final = str(modschedule_newlist[0]+" | "+modschedule_newlist[1]+" | "+modschedule_newlist[2]+" | "+modschedule_newlist[3]+" | "+modschedule_newlist[4]+" | "+modschedule_newlist[5]+" | "+modschedule_newlist[6]+" | "+modschedule_newlist[7]+" | "+modschedule_newlist[8]+" | "+modschedule_newlist[9]+"\n")
                    modschedule_otherlist.insert(modschedule_position,final)
                else:
                    mod_schedule()
            else:
                mod_main_menu()
        modschedule_position = (modschedule_position + 1)
    modschedule_file.close()

    modschedule_file = open("allsportschedule.txt","w")
    for x in range(modschedule_position):
        y = int(-modschedule_position+x)
        modschedule_add = modschedule_otherlist[y]
        modschedule_file.write(modschedule_add)
    modschedule_file.close()

    print("Deleting Old Data...")

    modschedule_otherlist = []
    modschedule_position = 0
    if (modschedule_removeindicator == "L001"):
        modschedule_file = open("sportschedule1surabaya.txt","r")
        for line in modschedule_file:
            modschedule_otherlist.append(line)
            if modschedule_search in line:
                del modschedule_otherlist[modschedule_position]
                modschedule_position -= 1
            modschedule_position += 1
        modschedule_file.close()

        modschedule_file = open("sportschedule1surabaya.txt","w")
        for x in range(modschedule_position):
            y = int(-modschedule_position+x)
            modschedule_add = modschedule_otherlist[y]
            modschedule_file.write(modschedule_add)
        modschedule_file.close()
        
    elif (modschedule_removeindicator == "L002"):
        modschedule_file = open("sportschedule2malang.txt","r")
        for line in modschedule_file:
            modschedule_otherlist.append(line)
            if modschedule_search in line:
                del modschedule_otherlist[modschedule_position]
                modschedule_position -= 1
            modschedule_position += 1
        modschedule_file.close()

        modschedule_file = open("sportschedule2malang.txt","w")
        for x in range(modschedule_position):
            y = int(-modschedule_position+x)
            modschedule_add = modschedule_otherlist[y]
            modschedule_file.write(modschedule_add)
        modschedule_file.close()
        
    elif (modschedule_removeindicator == "L003"):
        modschedule_file = open("sportschedule3lampung.txt","r")
        for line in modschedule_file:
            modschedule_otherlist.append(line)
            if modschedule_search in line:
                del modschedule_otherlist[modschedule_position]
                modschedule_position -= 1
            modschedule_position += 1
        modschedule_file.close()

        modschedule_file = open("sportschedule3lampung.txt","w")
        for x in range(modschedule_position):
            y = int(-modschedule_position+x)
            modschedule_add = modschedule_otherlist[y]
            modschedule_file.write(modschedule_add)
        modschedule_file.close()

    print("Done Deleting the data from old file, now printing the data into the new file...")

    if (modschedule_locindicator == "L001"):
        modschedule_file = open("sportschedule1surabaya.txt","a")
        modschedule_file.write(final)
        modschedule_file.close()
        
    elif (modschedule_locindicator == "L002"):
        modschedule_file = open("sportschedule2malang.txt","a")
        modschedule_file.write(final)
        modschedule_file.close()
    
    elif (modschedule_locindicator == "L003"):
        modschedule_file = open("sportschedule3lampung.txt","a")
        modschedule_file.write(final)
        modschedule_file.close()
    input("Done, Press any key to return to go back to Modify Main Menu")
    mod_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#GUEST_MAIN_MENU
def guest_main_menu():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Guest, Please enter what do you want to access : "
            "\n1. View details of the sports available"
            "\n2. View details of the sport schedules"
            "\n3. Register to become a new student"
            "\n4. Go back to Role Selection"
            "\n4. Exit")
    guestmm_select = int(input("Please enter your choice based on the number : "))

    while (guestmm_select >= 0):
        if(guestmm_select == 1):
            guest_display_sport()
            break
        elif(guestmm_select == 2):
            guest_display_schedule()
            break
        elif(guestmm_select == 3):
            guest_register()
            break
        elif(guestmm_select == 4):
            role_selection()
            break
        elif(guestmm_select == 5):
            exit_menu()
            break
        else:
            while (guestmm_select > 5 or guestmm_select < 1):
                print("\nInvalid number!")
                guestmm_select = int(input("Please enter your role based on the number : "))
                
#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#GUEST_DISPLAY_SPORT
def guest_display_sport():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Guest, Please enter what records do you want to display : "
            "\n1. Sport in all Locations"
            "\n2. Sport in Surabaya"
            "\n3. Sport in Malang"
            "\n4. Sport in Lampung"
            "\n5. Back to Guest Main Menu"
            "\n6. Exit")
    recordssport_select = int(input("Please enter your choice based on the number : "))

    while (recordssport_select > 0):
        if(recordssport_select == 1):
            recordssport_file = open("allsport.txt","r")
            recordssport_display(recordssport_file)
            recordssport_file.close()
            input("Press anything to go back to Main Menu")
            guest_main_menu()
            break
        elif(recordssport_select == 2):
            recordssport_file = open("sport1surabaya.txt","r")
            recordssport_display(recordssport_file)
            recordssport_file.close()
            input("Press anything to go back to Main Menu")
            guest_main_menu()
            break
        elif(recordssport_select == 3):
            recordssport_file = open("sport2malang.txt","r")
            recordssport_display(recordssport_file)
            recordssport_file.close()
            input("Press anything to go back to Main Menu")
            guest_main_menu()
            break
        elif(recordssport_select == 4):
            recordssport_file = open("sport3lampung.txt","r")
            recordssport_display(recordssport_file)
            recordssport_file.close()
            input("Press anything to go back to Main Menu")
            guest_main_menu()
            break
        elif(recordssport_select == 5):
            guest_main_menu()
            break
        elif(recordssport_select == 6):
            exit_menu()
            break
        else:
            while (recordssport_select > 6 or recordssport_select < 1):
                print("\nInvalid number!")
                recordssport_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#GUEST_DISPLAY_SCHEDULE
def guest_display_schedule():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Guest, Please enter what records do you want to display : "
            "\n1. Sport Schedule in all Locations"
            "\n2. Sport Schedule in Surabaya"
            "\n3. Sport Schedule in Malang"
            "\n4. Sport Schedule in Lampung"
            "\n5. Back to Guest Main Menu"
            "\n6. Exit")
    recordsschedule_select = int(input("Please enter your choice based on the number : "))

    while (recordsschedule_select > 0):
        if(recordsschedule_select == 1):
            recordsschedule_file = open("allsportschedule.txt","r")
            recordsschedule_display(recordsschedule_file)
            recordsschedule_file.close()
            input("Press anything to go back to Main Menu")
            guest_main_menu()
            break
        elif(recordsschedule_select == 2):
            recordsschedule_file = open("sportschedule1surabaya.txt","r")
            recordsschedule_display(recordsschedule_file)
            recordsschedule_file.close()
            input("Press anything to go back to Main Menu")
            guest_main_menu()
            break
        elif(recordsschedule_select == 3):
            recordsschedule_file = open("sportschedule2malang.txt","r")
            recordsschedule_display(recordsschedule_file)
            recordsschedule_file.close()
            input("Press anything to go back to Main Menu")
            guest_main_menu()
            break
        elif(recordsschedule_select == 4):
            recordsschedule_file = open("sportschedule3lampung.txt","r")
            recordsschedule_display(recordsschedule_file)
            recordsschedule_file.close()
            input("Press anything to go back to Main Menu")
            guest_main_menu()
            break
        elif(recordsschedule_select == 5):
            guest_main_menu()
            break
        elif(recordsschedule_select == 6):
            exit_menu()
            break
        else:
            while (recordsschedule_select > 6 or recordsschedule_select < 1):
                print("\nInvalid number!")
                recordsschedule_select = int(input("Please enter your choice based on the number : "))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#GUEST_REGISTER
def guest_register():
    guestreg_list = []
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("Hello new User!")
    guestreg_IDcheck = str("ST")
    guestreg_ID =  id_auto(guestreg_IDcheck)
    guestreg_list.append(guestreg_ID)
    print("Your new ID is : "+guestreg_ID)

    guestreg_username = str(input("Enter your Username : "))
    guestreg_file = open("allregstudent.txt","r")
    for line in guestreg_file:
        guestreg_checklist = str_to_list_convert(line)
        while (guestreg_username == guestreg_checklist[1]):
                print("Sorry, the username has been taken. Please try again!")
                guestreg_username = str(input("Enter your username : "))

    guestreg_list.append(guestreg_username)

    guestreg_pass = str(input("Enter your Password (Mininum 8 character long) : "))
    while (len(guestreg_pass) < 8):
        print("The Password is too short! Please enter a new one! ")
        guestreg_pass = str(input("Enter your Password (Mininum 8 character long) : "))
    guestreg_list.append(guestreg_pass)

    guestreg_name = str(input("Enter your Name : "))
    guestreg_list.append(guestreg_name)

    guestreg_age = str(input("Enter your Age : "))
    guestreg_list.append(guestreg_age)

    guestreg_address = str(input("Enter your Address : "))
    guestreg_list.append(guestreg_address)

    guestreg_phone = str(input("Enter your Phone Number : "))
    guestreg_list.append(guestreg_phone)

    guestreg_LID = str(input("Enter your Location ID (Type 'help' if the Location ID list is needed)(Lxxx) : "))
    while (guestreg_LID == "help" or guestreg_LID == "HELP" or guestreg_LID == "Help"):
        guestreg_help = open("help_locationID.txt","r")
        print (guestreg_help.read())
        guestreg_help.close()
        guestreg_LID = str(input("Enter your Location ID (Type 'help' if the Location ID list is needed)(Lxxx) : "))

    guestreg_indicator = 0
    while (guestreg_indicator == 0):    
        if (guestreg_LID == "L001"):
            guestreg_indicator = 1
            guestreg_list.append(guestreg_LID)
            guestreg_list.append("Surabaya")
        elif (guestreg_LID == "L002"):
            guestreg_indicator = 1
            guestreg_list.append(guestreg_LID)
            guestreg_list.append("Malang")
        elif (guestreg_LID == "L003"):
            guestreg_indicator = 1
            guestreg_list.append(guestreg_LID)
            guestreg_list.append("Lampung")
        else:
            print("Wrong Input!")
            guestreg_LID = str(input("Enter your Location ID (Type 'help' if the Location ID list is needed)(Lxxx) : "))
            while (guestreg_LID == "help" or guestreg_LID == "HELP" or guestreg_LID == "Help"):
                guestreg_help = open("help_locationID.txt","r")
                print (guestreg_help.read())
                guestreg_help.close()
                guestreg_LID = str(input("Enter your Location ID (Type 'help' if the Location ID list is needed)(Lxxx) : "))

    guestreg_LIDn = guestreg_list[8]

    help_sport(guestreg_LID)
    guestreg_SID = str(input("Enter your Sport ID(Sxxx) : "))
    guestreg_list.append(guestreg_SID)

    guestreg_SIDn = str(sportname_search(guestreg_SID))
    guestreg_list.append(guestreg_SIDn)

    recordsreg_display(guestreg_list)
    guestreg_final = str(guestreg_ID+" | "+guestreg_username+" | "+guestreg_pass+" | "+guestreg_name+" | "+guestreg_age+" | "+guestreg_address+" | "+guestreg_phone+" | "+guestreg_LID+" | "+guestreg_LIDn+" | "+guestreg_SID+" | "+guestreg_SIDn)
    guestreg_des = str(input("Please enter '1' to enter the data into the database, or enter any key to quit back to Guest Main Menu : "))
    if (guestreg_des == "1"):
        guestreg_save = open("allregstudent.txt","a")
        guestreg_save.write(guestreg_final)
        guestreg_save.close()
        if (guestreg_LID == "L001"):
            guestreg_save = open("regstudent1surabaya.txt","a")
            guestreg_save.write(guestreg_final+"\n")
            guestreg_save.close()
        elif (guestreg_LID == "L002"):
            guestreg_save = open("regstudent2malang.txt","a")
            guestreg_save.write(guestreg_final+"\n")
            guestreg_save.close()
        elif (guestreg_LID == "L003"):
            guestreg_save = open("regstudent3lampung.txt","a")
            guestreg_save.write(guestreg_final+"\n")
            guestreg_save.close()
        input("Save Successful! Now you can try login!"
        "\nPress anything to go back to Guest Main Menu")
        guest_main_menu()
    else:
        input("OK, press anything to go back to Guest Main Menu")
        guest_main_menu()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#REG_LOGIN
def reg_login():
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Student. Please enter your identification : ")
    reglogin_file = open("allregstudent.txt","r")
    reglogin_username = str(input("Username : "))
    reglogin_pass = str(input("Password : "))

    for line in reglogin_file:
        reglogin_list = str_to_list_convert(line)
        if (reglogin_username == reglogin_list[1] and reglogin_pass == reglogin_list[2]):
            input("Login Successful!")
            reglogin_file.close()
            reg_main_menu(reglogin_list[0],reglogin_list[9])
            break
    else:
        reglogin_des = str(input("Username or Password is wrong! Enter '1' to try again, or enter any other key to go back to role selection menu : "))
        if (reglogin_des == "1"):
            reg_login()
        else :
            role_selection()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#REG_MAIN_MENU
def reg_main_menu(studentid,studentsportid):
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    print("\nHello Student, Please enter what records do you want to access : "
            "\n1. View detail of coach for your sport"
            "\n2. View detail of your own Self Records"
            "\n3. View detail of registered sport schedule only"
            "\n4. Modify Self Record"
            "\n5. Provide feedback and Rating to your coach"
            "\n6. Log Out"
            "\n7. Exit")
    regmm_select = int(input("Please enter your choice based on the number : "))

    while (regmm_select >= -100):
        if(regmm_select == 1):
            reg_display_coach(studentid,studentsportid)
            break
        elif(regmm_select == 2):
            reg_display_selfrecord(studentid,studentsportid)
            break
        elif(regmm_select == 3):
            reg_display_schedule(studentid,studentsportid)
            break
        elif(regmm_select == 4):
            mod_selfrecord(studentid,studentsportid)
            break
        elif(regmm_select == 5):
            reg_feedback(studentid,studentsportid)
            break
        elif(regmm_select == 6):
            reg_login()
            break
        elif(regmm_select == 7):
            exit_menu()
            break
        else:
            while (regmm_select > 7 or regmm_select < 1):
                print("\nInvalid number!")
                regmm_select = int(input("Please enter your choice based on the number : ")) 

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#REG_DISPLAY_COACH
def reg_display_coach(studentid,studentsportid):
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    regdisplayc_file = open("allcoach.txt","r")
    regdisplayc_sportn = sportname_search(studentsportid)
    print("This is the Available Coach for "+regdisplayc_sportn+" : ")
    for line in regdisplayc_file:
        if studentsportid in line:
            regdisplayc_list = str_to_list_convert(line)
            remove = regdisplayc_list.pop(11)
            remove = remove.replace("R","")
            regdisplayc_list.insert(11,remove)
            print("\n\nCOACH ID\t\t: ",regdisplayc_list[0])
            print("COACH NAME\t\t: ",regdisplayc_list[1])
            print("LOCATION NAME\t\t: ",regdisplayc_list[8])
            print("SPORT NAME\t\t: ",regdisplayc_list[10])
            print("RATING\t\t\t: ",regdisplayc_list[11])
            print("NUMBER OF RATING\t: ",regdisplayc_list[12])
    regdisplayc_file.close()
    input("Press anything to go back to Main Menu")
    reg_main_menu(studentid,studentsportid)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 


#REG_DISPLAY_SELFRECORD
def reg_display_selfrecord(studentid,studentsportid):
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    regdisplaysr_file = open("allregstudent.txt","r")
    print("This is your personal record : ")
    for line in regdisplaysr_file :
        if studentid in line :
            regdisplaysr_list = str_to_list_convert(line)
            recordsreg_display(regdisplaysr_list)
    input("Press anything to go back to Main Menu")
    reg_main_menu(studentid,studentsportid)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#REG_DISPLAY_SCHEDULE
def reg_display_schedule(studentid,studentsportid):
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    regdisplaysch_file = open("allsportschedule.txt","r")
    print("This is your registered sport schedule : ")
    for line in regdisplaysch_file :
        if studentsportid in line :
            regdisplaysch_list = str_to_list_convert(line)
            recordsschedule_display(regdisplaysch_list)
    input("Press anything to go back to Main Menu")
    reg_main_menu(studentid,studentsportid)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#REG_MODIFY_SELFRECORD
def mod_selfrecord(studentid,studentsportid):
    modself_otherlist = []
    modself_position = int(0)
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    modself_file = open("allregstudent.txt","r")
    for line in modself_file:
        modself_otherlist.append(line)
        if studentid in line :
            del modself_otherlist[modself_position]
            modself_list = str_to_list_convert(line)
            modself_removeindicator = modself_list[7]
            recordsreg_display(modself_list)
            modself_des = str(input("Is this the your data? Enter '1' if correct, or any key to go back to your Main Menu : "))
            if (modself_des == "1"):
                modself_newlist = []
                modself_newlist.append(modself_list[0])

                modself_new = str(input("Enter your Username (If the data still the same, type 'same') : "))
                if (modself_new == "same" or modself_new == "Same" or modself_new == "SAME"):
                    modself_newlist.append(modself_list[1])
                else:
                    modself_newlist.append(modself_new)

                modself_new = str(input("Enter your Password (Minimum 8 Characters long)(If the password still the same, please enter it again) : "))
                while (len(modself_new)<8):
                    print("The Password is too short! Please enter a new one! ")
                    modself_new = str(input("Enter your Password (Minimum 8 Characters long)(If the password still the same, please enter it again) : "))
                modself_newlist.append(modself_new)

                modself_new = str(input("Enter your Name (If the data still the same, type 'same') : "))
                if (modself_new == "same" or modself_new == "Same" or modself_new == "SAME"):
                    modself_newlist.append(modself_list[3])
                else:
                    modself_newlist.append(modself_new)

                modself_new = str(input("Enter your age (If the data still the same, type 'same') : "))
                if (modself_new == "same" or modself_new == "Same" or modself_new == "SAME"):
                    modself_newlist.append(modself_list[4])
                else:
                    modself_newlist.append(modself_new)
            
                modself_new = str(input("Enter your address (If the data still the same, type 'same') : "))
                if (modself_new == "same" or modself_new == "Same" or modself_new == "SAME"):
                    modself_newlist.append(modself_list[5])
                else:
                    modself_newlist.append(modself_new)

                modself_new = str(input("Enter your phone number (If the data still the same, type 'same') : "))
                if (modself_new == "same" or modself_new == "Same" or modself_new == "SAME"):
                    modself_newlist.append(modself_list[6])
                else:
                    modself_newlist.append(modself_new)

                modself_new = str(input("Enter your Location ID (Type 'Help' if the list of Location IDs is Needed) (If the data still the same, type 'same') : "))
                modself_indicator = 0
                while (modself_indicator == 0):
                    if (modself_new == "same" or modself_new == "Same" or modself_new == "SAME"):
                        modself_newlist.append(modself_list[7])
                        modself_newlist.append(modself_list[8])
                        modself_locindicator = modself_list[7]
                        modself_indicator = 1
                    elif (modself_new == "Help" or modself_new == "HELP" or modself_new == "help"):
                        while (modself_new == "Help" or modself_new == "HELP" or modself_new == "help"):
                            modself_help = open("help_locationID.txt","r")
                            print (modself_help.read())
                            modself_help.close()
                            modself_new = str(input("Enter your Location ID (Type 'Help' if the list of Location IDs is Needed) (If the data still the same, type 'same') : "))
                    else:
                        if (modself_new == "L001"):
                            modself_indicator = 1
                            modself_newlist.append(modself_new)
                            modself_newlist.append("Surabaya")
                            modself_locindicator = "L001"
                        elif (modself_new == "L002"):
                            modself_indicator = 1
                            modself_newlist.append(modself_new)
                            modself_newlist.append("Malang")
                            modself_locindicator = "L002"
                        elif (modself_new == "L003"):
                            modself_indicator = 1
                            modself_newlist.append(modself_new)
                            modself_newlist.append("Lampung")
                            modself_locindicator = "L003"
                        else:
                            print("Wrong Input!")
                            modself_new = str(input("Enter your Location ID (Type 'Help' if the list of Location IDs is Needed) (If the data still the same, type 'same') : "))
                            while (modself_new == "help" or modself_new == "HELP" or modself_new == "Help"):
                                modself_help = open("help_locationID.txt","r")
                                print (modself_help.read())
                                modself_help.close()
                                modself_new = str(input("Enter your Location ID (Type 'Help' if the list of Location IDs is Needed) (If the data still the same, type 'same') : "))

                help_sport(modself_locindicator)
                modself_new = str(input("Enter your Sport ID (If the data still the same, type 'same') : "))
                if (modself_new == "same" or modself_new == "Same" or modself_new == "SAME"):
                    modself_newlist.append(modself_list[9])
                    modself_newlist.append(modself_list[10])
                else:
                    modself_newlist.append(modself_new)
                    modself_new = str(sportname_search(modself_new))
                    modself_newlist.append(modself_new)

                recordsreg_display(modself_newlist)
                modself_des = str(input("Please enter '1' to submit the modified the data, or enter any key to enter a new set of data : "))
                if (modself_des == "1"):
                    final = str(modself_newlist[0]+" | "+modself_newlist[1]+" | "+modself_newlist[2]+" | "+modself_newlist[3]+" | "+modself_newlist[4]+" | "+modself_newlist[5]+" | "+modself_newlist[6]+" | "+modself_newlist[7]+" | "+modself_newlist[8]+" | "+modself_newlist[9]+" | "+modself_newlist[10]+"\n")
                    modself_otherlist.insert(modself_position,final)
                else:
                    mod_selfrecord(studentid,studentsportid)
            else:
                reg_main_menu(studentid,studentsportid)
        modself_position = (modself_position + 1)
    modself_file.close()

    modself_file = open("allregstudent.txt","w")
    for x in range(modself_position):
        y = int(-modself_position+x)
        print(y)
        modself_add = modself_otherlist[y]
        modself_file.write(modself_add)
    modself_file.close()

    modself_otherlist = []
    modself_position = 0
    if (modself_removeindicator == "L001"):
        modself_file = open("regstudent1surabaya.txt","r")
        for line in modself_file:
            modself_otherlist.append(line)
            if studentid in line:
                del modself_otherlist[modself_position]
                modself_position -= 1
            modself_position += 1
        modself_file.close()
        print(modself_otherlist)

        modself_file = open("regstudent1surabaya.txt","w")
        for x in range(modself_position):
            y = int(-modself_position+x)
            print(y)
            modself_add = modself_otherlist[y]
            modself_file.write(modself_add)
        modself_file.close()
        
    elif (modself_removeindicator == "L002"):
        modself_file = open("regstudent2malang.txt","r")
        for line in modself_file:
            modself_otherlist.append(line)
            if studentid in line:
                del modself_otherlist[modself_position]
                modself_position -= 1
            modself_position += 1
        modself_file.close()

        modself_file = open("regstudent2malang.txt","w")
        for x in range(modself_position):
            y = int(-modself_position+x)
            print(y)
            modself_add = modself_otherlist[y]
            modself_file.write(modself_add)
        modself_file.close()
        
    elif (modself_removeindicator == "L003"):
        modself_file = open("regstudent3lampung.txt","r")
        for line in modself_file:
            modself_otherlist.append(line)
            if studentid in line:
                del modself_otherlist[modself_position]
                modself_position -= 1
            modself_position += 1
        modself_file.close()

        modself_file = open("regstudent3lampung.txt","w")
        for x in range(modself_position):
            y = int(-modself_position+x)
            print(y)
            modself_add = modself_otherlist[y]
            modself_file.write(modself_add)
        modself_file.close()

    print("Done Deleting the data from old file, now printing the data into the new file")

    if (modself_locindicator == "L001"):
        modself_file = open("regstudent1surabaya.txt","a")
        modself_file.write(final)
        modself_file.close()
        
    elif (modself_locindicator == "L002"):
        modself_file = open("regstudent2malang.txt","a")
        modself_file.write(final)
        modself_file.close()
    
    elif (modself_locindicator == "L003"):
        modself_file = open("regstudent3lampung.txt","a")
        modself_file.write(final)
        modself_file.close()
    input("Done, Press any key to return to go back to your Main Menu")
    reg_main_menu(studentid,studentsportid)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#REG_FEEDBACK
def reg_feedback(studentid,studentsportid):
    regfeedback_otherlist = []
    regfeedback_position = int(0)
    print (60*"-")
    print ("\tWELCOME TO CHAMPION CLUB!")
    print("\tVIOLENCE, SPEED, MOMENTUM!")
    regfeedback_file = open("allcoach.txt","r")
    for line in regfeedback_file :
        if studentsportid in line :
            regfeedback_list = str_to_list_convert(line)
            remove = regfeedback_list.pop(11)
            remove = remove.replace("R","")
            regfeedback_list.insert(11,remove)
            print("\n\nCOACH ID\t\t: ",regfeedback_list[0])
            print("COACH NAME\t\t: ",regfeedback_list[1])
    regfeedback_coachid = str(input("Enter the coach's ID of the coach you want to give the rating and feedback on : "))
    regfeedback_file.close()

    regfeedback_file = open("allcoach.txt","r")
    for line in regfeedback_file :
        regfeedback_otherlist.append(line)
        if regfeedback_coachid in line :
            del regfeedback_otherlist[regfeedback_position] 
            regfeedback_list = str_to_list_convert(line)
            regfeedback_loc = regfeedback_list[7]
            brating = regfeedback_list.pop(11)
            brating = brating.replace("R","")
            regfeedback_list.insert(11,brating)
            regfeedback_list[11] = float(regfeedback_list[11])
            regfeedback_list[12] = int(regfeedback_list[12])
            regfeedback_list[13] = int(regfeedback_list[13])
            regfeedback_rating = int(input("Enter your Rating Between 1(Lowest) - 5(Highest) : "))
            while (regfeedback_rating>5 or regfeedback_rating<1):
                print("Invalid Value! Please try again!")
                regfeedback_rating = int(input("Enter your Rating Between 1(Lowest) - 5(Highest) : "))
            regfeedback_list[12] += 1
            regfeedback_list[13] = regfeedback_list[13]+regfeedback_rating
            regfeedback_list[11] = regfeedback_list[13]/regfeedback_list[12]
            regfeedback_list[11] = round(regfeedback_list[11],2)
            regfeedback_list[11],regfeedback_list[12],regfeedback_list[13] = str(regfeedback_list[11]),str(regfeedback_list[12]),str(regfeedback_list[13])
            regfeedback_cmt = str(input("Input comment, critique, or feedback for the coach : "))
            print("Okay, Submiting your Rating and Feedback...")
            final = str(regfeedback_list[0]+" | "+regfeedback_list[1]+" | "+regfeedback_list[2]+" | "+regfeedback_list[3]+" | "+regfeedback_list[4]+" | "+regfeedback_list[5]+" | "+regfeedback_list[6]+" | "+regfeedback_list[7]+" | "+regfeedback_list[8]+" | "+regfeedback_list[9]+" | "+regfeedback_list[10]+" | "+"R"+regfeedback_list[11]+" | "+regfeedback_list[12]+" | "+regfeedback_list[13]+"\n")
            str(regfeedback_list)
            regfeedback_otherlist.insert(regfeedback_position,final)
        regfeedback_position = (regfeedback_position + 1)
    regfeedback_file.close()

    regfeedback_file = open("coachfeedback.txt","a")
    regfeedback_file.write("For Coach "+regfeedback_list[1]+"\n\tCode "+regfeedback_list[0]+"\n\tFeedback : "+regfeedback_cmt+"\n")
    regfeedback_file.close()

    regfeedback_file = open("allcoach.txt","w")
    for x in range(regfeedback_position):
        y = int(-regfeedback_position+x)
        regfeedback_add = regfeedback_otherlist[y]
        regfeedback_file.write(regfeedback_add)
    regfeedback_file.close()

    regfeedback_otherlist = []
    regfeedback_position = 0

    if (regfeedback_loc == "L001"):
        regfeedback_file = open("coach1surabaya.txt","r")
        for line in regfeedback_file:
            regfeedback_otherlist.append(line)
            if regfeedback_coachid in line:
                del regfeedback_otherlist[regfeedback_position]
                regfeedback_otherlist.insert(regfeedback_position,final)
            regfeedback_position += 1
        regfeedback_file.close()

        regfeedback_file = open("coach1surabaya.txt","w")
        for x in range(regfeedback_position):
            y = int(-regfeedback_position+x)
            regfeedback_add = regfeedback_otherlist[y]
            regfeedback_file.write(regfeedback_add)
        regfeedback_file.close()
        
    elif (regfeedback_loc == "L002"):
        regfeedback_file = open("coach2malang.txt","r")
        for line in regfeedback_file:
            regfeedback_otherlist.append(line)
            if regfeedback_coachid in line:
                del regfeedback_otherlist[regfeedback_position]
                regfeedback_otherlist.insert(regfeedback_position,final)
            regfeedback_position += 1
        regfeedback_file.close()

        regfeedback_file = open("coach2malang.txt","w")
        for x in range(regfeedback_position):
            y = int(-regfeedback_position+x)
            regfeedback_add = regfeedback_otherlist[y]
            regfeedback_file.write(regfeedback_add)
        regfeedback_file.close()
        
    elif (regfeedback_loc == "L003"):
        regfeedback_file = open("coach3lampung.txt","r")
        for line in regfeedback_file:
            regfeedback_otherlist.append(line)
            if regfeedback_coachid in line:
                del regfeedback_otherlist[regfeedback_position]
                regfeedback_otherlist.insert(regfeedback_position,final)
            regfeedback_position += 1
        regfeedback_file.close()

        regfeedback_file = open("coach3lampung.txt","w")
        for x in range(regfeedback_position):
            y = int(-regfeedback_position+x)
            regfeedback_add = regfeedback_otherlist[y]
            regfeedback_file.write(regfeedback_add)
        regfeedback_file.close()
    input("Done, Press anything to go back to Main Menu")
    reg_main_menu(studentid,studentsportid)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------- 

#SPORTNAME_SEARCH
def sportname_search(x):
    myfile = open("allsport.txt","r")
    for line in myfile :
        if x in line:
            spl = line.split(" | ")
            name = spl[1]
            return name

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#COACHNAME_SEARCH
def coachname_search(x):
    myfile = open("allcoach.txt","r")
    for line in myfile :
        if x in line:
            spl = line.split(" | ")
            name = spl[1]
            return name

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#ID_AUTO
def id_auto(remover):
    if (remover == "ID"):
        myfile = open("allcoach.txt","r")
    elif (remover == "S"):
        myfile = open("allsport.txt","r")
    elif (remover == "ST"):
        myfile = open("allregstudent.txt","r")
    elif (remover == "SCH"):
        myfile = open("allsportschedule.txt","r")
    for line in myfile :
        spl = line.split(" | ")
        existID = spl[0]

    if remover == "ID":
        existID = existID.replace("ID","")
    elif remover == "S":
        existID = existID.replace("S","")
    elif remover == "ST":
        existID = existID.replace("ST","")
    elif remover == "SCH":
        existID = existID.replace("SCH","")
    existID = int(existID)
    existID = existID+1
    existID = str(existID)
    length = len(existID)
    
    if (length == 1 and remover == "ID"):
        newID = str("ID00"+existID)
    elif (length == 2 and remover == "ID"):
        newID = str("ID0"+existID)
    elif (length == 3 and remover == "ID"):
        newID = str("ID"+existID)
    elif (length == 1 and remover == "S"):
        newID = str("S00"+existID)
    elif (length == 2 and remover == "S"):
        newID = str("S0"+existID)
    elif (length == 3 and remover == "S"):
        newID = str("S"+existID)
    elif (length == 1 and remover == "ST"):
        newID = str("ST00"+existID)
    elif (length == 2 and remover == "ST"):
        newID = str("ST0"+existID)
    elif (length == 3 and remover == "ST"):
        newID = str("ST"+existID)
    elif (length == 1 and remover == "SCH"):
        newID = str("SCH00"+existID)
    elif (length == 2 and remover == "SCH"):
        newID = str("SCH0"+existID)
    elif (length == 3 and remover == "SCH"):
        newID = str("SCH"+existID)
    return newID

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#RECORDSCOACH_DISPLAY
def recordscoach_display(mylist):
    remove = mylist.pop(11)
    remove = remove.replace("R","")
    mylist.insert(11,remove)
    print("\n\nCOACH ID\t\t: ",mylist[0])
    print("COACH NAME\t\t: ",mylist[1])
    print("DATE JOINED\t\t: ",mylist[2])
    print("DATE TERMINATED\t\t: ",mylist[3])
    print("HOURLY RATE IN MYR\t: ",mylist[4])
    print("PHONE NUMBER\t\t: ",mylist[5])
    print("ADDRESS\t\t\t: ",mylist[6])
    print("LOCATION ID\t\t: ",mylist[7])
    print("LOCATION NAME\t\t: ",mylist[8])
    print("SPORT ID\t\t: ",mylist[9])
    print("SPORT NAME\t\t: ",mylist[10])
    print("RATING\t\t\t: ",mylist[11])
    print("NUMBER OF RATING\t: ",mylist[12])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#RECORDSSPORT_DISPLAY
def recordssport_display(mylist):
    print("\n\nSPORT ID\t\t: ",mylist[0])
    print("SPORTNAME\t\t: ",mylist[1])
    print("LOCATION ID\t\t: ",mylist[2])
    print("LOCATION NAME\t\t: ",mylist[3])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#RECORDSSCHEDULE_DISPLAY
def recordsschedule_display(mylist):
    print("\n\nSCHEDULE ID\t\t\t: ",mylist[0])
    print("LOCATION ID\t\t\t: ",mylist[1])
    print("LOCATION NAME\t\t\t: ",mylist[2])
    print("SPORT ID\t\t\t: ",mylist[3])
    print("SPORT NAME\t\t\t: ",mylist[4])
    print("COACH ID\t\t\t: ",mylist[5])
    print("COACH NAME\t\t\t: ",mylist[6])
    print("DAY \t\t\t\t: ",mylist[7])
    print("STARTING TIME BY THOUSAND\t: ",mylist[8])
    print("TIME DURATION IN MINUTES\t: ",mylist[9])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#RECORDSREG_DISPLAY
def recordsreg_display(mylist):
    print("\n\nSTUDENT ID\t\t: ",mylist[0])
    print("STUDENT USERNAME\t: ",mylist[1])
    print("STUDENT PASSWORD\t: ",mylist[2])
    print("STUDENT NAME\t\t: ",mylist[3])
    print("AGE\t\t\t: ",mylist[4])
    print("ADDRESS\t\t\t: ",mylist[5])
    print("PHONE NUMBER\t\t: ",mylist[6])
    print("LOCATION ID\t\t: ",mylist[7])
    print("LOCATION NAME\t\t: ",mylist[8])
    print("SPORT ID\t\t: ",mylist[9])
    print("SPORT NAME\t\t: ",mylist[10])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#STR_TO_LIST_CONVERT
def str_to_list_convert(line):
        mylist = line.split(" | ")
        remove = mylist.pop()
        remove = remove.replace("\n","")
        mylist.append(remove)
        return(mylist)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#BUBBLE_SORT
def bubble_sort(sort_list,length):
    flag = 0

    while (flag == 0):
        flag = 1
        for i in range(length-1):
            if sort_list[i] > sort_list[i+1]:
                flag = 0
                sort_list[i],sort_list[i+1] = sort_list[i+1],sort_list[i]
    
    return(sort_list)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#HELP_SPORT_ID
def help_sport(x):
    helpsport_file = open("allsport.txt","r")
    print("The Available Sports in location "+x+" are :")
    for line in helpsport_file:
        if x in line:
            helpsport_list = str_to_list_convert(line)
            print(helpsport_list[1]+" = "+helpsport_list[0])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

#HELP_COACH_ID
def help_coach(x,y):
    helpcoach_file = open("allcoach.txt","r")
    print("The Available Coach in for "+y+"and in "+x+" are :")
    for line in helpcoach_file:
        if (x and y) in line:
            helpcoach_list = str_to_list_convert(line)
            print(helpcoach_list[1]+" = "+helpcoach_list[0])

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

role_selection()
