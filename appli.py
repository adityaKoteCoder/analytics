import database as db

def c_add_internship():
    iname = input("Internship name:")
    company = input("Company name:")
    i_year = int(input("Conducted year:"))
    db.add_internship(iname, company, i_year)

def c_view_all_internships():
    db.view_all_internships()
    
def c_search_internship_by_name():
    name = input("enter the name")
    db.search_internship_by_name(name)

def c_change_status_internship():
    id = input("enter the id")
    status = input("enter the status")
    db.change_status_internship(id,status)

def c_delete_internship():
   i_id = int(input("enter the ID:"))
   db.delete_internship(i_id)



# Student oprations
def c_add_student(regno,name,sem,placed):
    usn = input("enter the usn")
    name = input("enter the name")
    sem = input("enter the sem")
    placed = input("enter the place")
    db.add_student(usn,name,sem,placed)

def c_view_all_student():
    db.view_all_students()

def c_search_student_by_name(name):
    name = input("enter the name : ")
    db.search_student(name) 

def c_update_student():
    usn = int("enter the usn")
    print("1.Name\n2.Sem\n3.Placed\n")
    ch = int(input("enter your choice"))
    if ch == 1:
        name = input("enter the name")
        db.update_student(usn,ch,name)
    if ch == 2:
        sem = input("enter the usn")
        db.update_student(usn,ch,sem) 
    if ch ==3:
        placed = input("enter the placed")
        db.update_student(usn,ch,placed)
    else:
        print("Enter choice from 1-3..")


def c_delete_student():
    usn = int(input("ente the usn"))
    db.delete_student(usn)
   

# Registrations and summary reports 
def c_company_ws_count():
    db.company_ws_count()
   
def c_student_ws_count():
    db.student_ws_count()

def c_ws_student_reports():
    db.ws_student_reports()

def c_reg_stu_internship():
    usn = int(input("enter the student usn:"))
    iid = int(input("enter the student ID:"))
    db.reg_student_internship(usn,iid)
    
def c_update_stu_intership_status():
   usn = int(input("Enter the usn : "))
   status = int(input("Enter the 1 for completed and 0 for not yet : "))
   db.update_stu_intership_status(usn,status)


while True:
    try:
        print("~"*10,"Welcome to IT Training Management System","~"*10,"\n1.Add Internship\n2.Student\n3.Reports\n4.Exit")
        mch = int(input("Enter you choice:"))
        
        if mch == 1:
            while True:
                try:
                    print("*"*50)
                    print("Internship programms conducted at MITE by Companies")
                    print("~"*50)
                    print("1.Add 2.View All 3.Search 4.Update 5.Delete 6.Main Menu")
                    print("*"*50)
                    ch = int(input("Enter your choice:"))
                    if ch == 1:
                        c_add_internship()
                    elif ch == 2:
                        c_view_all_internships()
                    elif ch == 3:
                        c_search_internship_by_name()
                    elif ch == 4:
                        c_change_status_internship()
                    elif ch == 5:
                        c_delete_internship()
                    elif ch == 6:
                        break
                    else:
                        raise Exception()
                except Exception as e:
                    print("Please provide valid input 1 - 6")
        elif mch == 2:
            while True:
                try:
                    print("*"*50)
                    print("Add Students to Internship programms")
                    print("1.Add 2.View All 3.Search 4.Update 5.Delete 6.Main Menu")
                    print("*"*50)
                    ch = int(input("Enter your choice:"))
                    if ch == 1:
                        c_add_student()
                    elif ch == 2:
                        c_view_all_student()
                    elif ch == 3:
                        c_search_student_by_name()
                    elif ch == 4:
                        c_update_student()
                    elif ch == 5:
                        c_delete_student()
                    elif ch == 6:
                        break
                    else:
                        raise Exception()
                except Exception as e:
                    print("Please provide valid input 1 - 6")
        elif mch == 3:
                while True:
                    try:
                        print("*"*50)
                        print("Internship programms conducted at MITE Reports")
                        print("1.Register Student 2.Update Status 3.Company ws count 4.Student ws count 5.Studen_ws_name_company_year 6.Main Menu")
                        ch = int(input("Enter your choice:"))
                        if ch == 1:
                            c_reg_stu_internship()
                        elif ch == 2:
                            c_update_stu_intership_status()                       
                        if ch == 3:
                            c_company_ws_count()
                        elif ch == 4:
                            c_student_ws_count()
                        elif ch == 5:
                            c_ws_student_reports()
                        elif ch == 6:
                            break
                        else:
                            raise Exception()
                    except Exception as e:
                        print("Please provide valid input 1 - 4")
        elif mch == 4:
            print("Thank you programming is going to terminate.....")
            exit()
        else:
            raise Exception()
    except Exception as e:
        print("Enter valid input (1 to 3) only...")