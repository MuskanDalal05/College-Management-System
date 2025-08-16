# database name College_Management_System
# table name New_Admission 
from tkinter import *
import tkinter as tk
import mysql.connector
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime


conn = mysql.connector.connect(
    user='root',
    password='12345',
    host='localhost',
    database='College_Management_System'
)
if (conn.is_connected):
    cursor = conn.cursor()

    width = 400
    height = 220
    window = Tk()
    system_width = window.winfo_screenwidth()
    system_height=window.winfo_screenheight()
    window.config(bg="#ccffcc")

    c_x = int(system_width/2-width/2)
    c_y = int(system_height/2-height/2)


    window.geometry(f"{width}x{height}+{c_x}+{c_y}")
    window.maxsize(width, height)
    window.minsize(width, height)
    window.title("College Management System")

    # New admission
    New_admission_window_first_name_var = StringVar(value='')
    New_admission_window_last_name_var = StringVar(value='')
    New_admission_window_Father_name_var = StringVar(value='')
    New_admission_window_gender_rd = StringVar()
    New_admission_window_mobile_number_var =IntVar(value='')
    New_admission_window_email_id_var= StringVar(value='')
    New_admission_window_dropdown_var=StringVar()
    New_admission_window_dropdown_var.set("Select a Course")
    New_admission_window_duration_var=StringVar(value='')
    New_admission_window_course_fees_var=IntVar(value='')
    New_admission_window_1st_semester_fees_var=IntVar(value='')

    # Student Details
    Student_details_mobile_number_var = IntVar(value='')
 
    # Student Fees
    Student_fees_mobile_number_var = IntVar(value='')
    Student_fees_update_mobile_number_var = IntVar(value='')
    Student_fees_update_paid_fees_var =IntVar(value='')
    Student_fees_update_last_payment_received_date_var = StringVar()
    Student_fees_update_pending_fees_var = IntVar(value='')
    
    # Remove student
    Remove_student_mobile_number_var = IntVar(value='')

    #upgrade semester
    upgrade_semester_mobile_number_var = IntVar(value='')
    upgrade_semester_first_name_var = StringVar(value='')
    upgrade_semester_last_name_var = StringVar(value='')
    upgrade_semester_Course_var = StringVar(value='')
    upgrade_semester_var = StringVar(value='')
    upgrade_semester_pending_fees_var = IntVar(value='')
    upgrade_semester_paid_fees_var = IntVar(value='')


    def main_window():
        width = 400
        height = 400
        main_Window = Toplevel()
        system_width = main_Window.winfo_screenwidth()
        system_height=main_Window.winfo_screenheight()
        main_Window.config(bg="#ccffcc")

        c_x = int(system_width/2-width/2)
        c_y = int(system_height/2-height/2)


        main_Window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        main_Window.maxsize(width, height)
        main_Window.minsize(width, height)

        # Main window main label
        main_window_main_label = Label(main_Window, text="Main Menu",font=12,bg="#ccffcc")
        main_window_main_label.pack(pady=12)

        # Main admission button
        main_window_new_admission_button = Button(main_Window,text="New Admission",padx=10,command=New_admission)
        main_window_new_admission_button.place(x=145,y=50)

        #Main Student Fees button
        main_window_student_fees_button = Button(main_Window,text="Student Fees",padx=10,command=Student_fees)
        main_window_student_fees_button.place(x=150,y=100)

        # Main Student Details button
        main_window_student_details = Button(main_Window,text="Student Details",padx=10,command=Student_details)
        main_window_student_details.place(x=145,y=150)

        # Main Remove Student button
        main_window_remove_student = Button(main_Window,text="Remove Student",padx=10,command=Remove_student)
        main_window_remove_student.place(x=145,y=200)

        # Main upgrade semester
        main_window_upgrade_semester = Button(main_Window,text="Upgrade Semester",padx=10,command=upgrade_semester)
        main_window_upgrade_semester.place(x=145,y=250)

        # Main Exit button
        main_window_exit_button = Button(main_Window,text="Exit",command=window.destroy,padx=15)
        main_window_exit_button.place(x=170,y=350)

    def New_admission():

        def on_change(value):

            if("B-Tech"==value):
                semester_fees = 18000
                course_fees = semester_fees*8
                New_admission_window_duration_var.set(4)
                New_admission_window_course_fees_var.set(course_fees)
                New_admission_window_1st_semester_fees_var.set(semester_fees)

            elif("M-Tech"==value):
                semester_fees = 22000
                course_fees = semester_fees*4
                New_admission_window_duration_var.set(2)
                New_admission_window_course_fees_var.set(course_fees)
                New_admission_window_1st_semester_fees_var.set(semester_fees)

            elif("BCA"==value):
                semester_fees = 14000
                course_fees = semester_fees*6
                New_admission_window_duration_var.set(3)
                New_admission_window_course_fees_var.set(course_fees)
                New_admission_window_1st_semester_fees_var.set(semester_fees)

            elif("MCA"==value):
                semester_fees = 16000
                course_fees = semester_fees*4
                New_admission_window_duration_var.set(2)
                New_admission_window_course_fees_var.set(course_fees)
                New_admission_window_1st_semester_fees_var.set(semester_fees)

            elif("BSc"==value):
                semester_fees = 15000
                course_fees = semester_fees*6
                New_admission_window_duration_var.set(3)
                New_admission_window_course_fees_var.set(course_fees)
                New_admission_window_1st_semester_fees_var.set(semester_fees)

            elif("MSc"==value):
                semester_fees = 17000
                course_fees = semester_fees*4
                New_admission_window_duration_var.set(2)
                New_admission_window_course_fees_var.set(course_fees)
                New_admission_window_1st_semester_fees_var.set(semester_fees)

        def Submit_function():
            New_admission_window_first_name = New_admission_window_first_name_var.get()
            New_admission_window_last_name = New_admission_window_last_name_var.get()
            New_admission_window_father_name = New_admission_window_Father_name_var.get()
            New_admission_window_mobile_number = New_admission_window_mobile_number_var.get()
            New_admission_window_gender = New_admission_window_gender_rd.get()
            New_admission_window_email_id = New_admission_window_email_id_var.get()
            New_admission_window_duration = New_admission_window_duration_var.get()
            New_admission_window_course_fees = New_admission_window_course_fees_var.get()
            New_admission_window_1st_semester_fees = New_admission_window_1st_semester_fees_var.get()
            New_admission_window_dob = New_admission_window_dob_input.get()
            New_admission_window_dropdown = New_admission_window_dropdown_var.get()
            New_admission_window_address = New_admission_window_address_input.get(1.0,"end")

            now = datetime.now()
            current_date = now.strftime('%Y-%m-%d')

            sql=f"SELECT * FROM New_Admission where MobileNumber={New_admission_window_mobile_number}"
            cursor.execute(sql)
            result = cursor.fetchone()

            if(result!=None):

                messagebox.showinfo("", "Mobile Number is already exist",parent=New_admission_window)
                New_admission_fees_alert.place_forget()

            else:
                sql1= f"insert into New_Admission values('{New_admission_window_first_name}','{New_admission_window_last_name}','{New_admission_window_father_name}',{New_admission_window_mobile_number},'{New_admission_window_gender}','{New_admission_window_email_id}','{New_admission_window_address}','{current_date}','{New_admission_window_dob}',NULL,'{New_admission_window_dropdown}','{New_admission_window_duration} Years','1st',{New_admission_window_course_fees},{New_admission_window_1st_semester_fees},{New_admission_window_1st_semester_fees},0)"
                cursor.execute(sql1)
                conn.commit()

                messagebox.showinfo("", "Admission successful",parent=New_admission_window)
                New_admission_fees_alert.place(x=430,y=420)

                New_admission_window_first_name_var.set(value='')
                New_admission_window_last_name_var.set(value='')
                New_admission_window_Father_name_var.set(value='')
                New_admission_window_mobile_number_var.set(value='')
                New_admission_window_gender_rd.set(value='')
                New_admission_window_email_id_var.set(value='')
                New_admission_window_duration_var.set(value='')
                New_admission_window_course_fees_var.set(value='')
                New_admission_window_1st_semester_fees_var.set(value='')
                New_admission_window_dob_input.set_date(datetime.now())
                New_admission_window_address_input.delete(1.0,"end")
                New_admission_window_dropdown_var.set("Select a Course")

        width = 750
        height = 550
        New_admission_window = Toplevel()
        system_width = New_admission_window.winfo_screenwidth()
        system_height=New_admission_window.winfo_screenheight()
        New_admission_window.config(bg="#ccffcc")

        c_x = int(system_width/2-width/2)
        c_y = int(system_height/2-height/2)


        New_admission_window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        New_admission_window.maxsize(width, height)
        New_admission_window.minsize(width, height)

        def on_closing():
            New_admission_window_first_name_var.set(value='')
            New_admission_window_last_name_var.set(value='')
            New_admission_window_Father_name_var.set(value='')
            New_admission_window_mobile_number_var.set(value='')
            New_admission_window_gender_rd.set(value='')
            New_admission_window_email_id_var.set(value='')
            New_admission_window_duration_var.set(value='')
            New_admission_window_course_fees_var.set(value='')
            New_admission_window_1st_semester_fees_var.set(value='')
            New_admission_window_dob_input.set_date(datetime.now())
            New_admission_window_address_input.delete(1.0,"end")
            New_admission_window_dropdown_var.set("Select a Course")
            New_admission_window.destroy()

        def back_function():
            New_admission_window_first_name_var.set(value='')
            New_admission_window_last_name_var.set(value='')
            New_admission_window_Father_name_var.set(value='')
            New_admission_window_mobile_number_var.set(value='')
            New_admission_window_gender_rd.set(value='')
            New_admission_window_email_id_var.set(value='')
            New_admission_window_duration_var.set(value='')
            New_admission_window_course_fees_var.set(value='')
            New_admission_window_1st_semester_fees_var.set(value='')
            New_admission_window_dob_input.set_date(datetime.now())
            New_admission_window_address_input.delete(1.0,"end")
            New_admission_window_dropdown_var.set("Select a Course")
            New_admission_window.destroy()

        New_admission_window.wm_protocol("WM_DELETE_WINDOW", on_closing)
        
        # New admission window main label
        New_admission_window_main_label = Label(New_admission_window,text="New Admission",font=12 ,bg="#ccffcc")
        New_admission_window_main_label.pack(pady=12)

        # New admission window first name label
        New_admission_window_first_name_label = Label(New_admission_window,text="First Name",font=6 ,bg="#ccffcc")
        New_admission_window_first_name_label.place(x=40,y=60)

        # New admission window first name input
        New_admission_window_first_name_input = Entry(New_admission_window,width=25,textvariable=New_admission_window_first_name_var)
        New_admission_window_first_name_input.place(x=140,y=60)

        # New admission window last name label
        New_admission_window_last_name_label = Label(New_admission_window,text="Last Name",font=6 ,bg="#ccffcc")
        New_admission_window_last_name_label.place(x=340,y=60)

        # New admission window last name input
        New_admission_window_last_name_input = Entry(New_admission_window,width=25,textvariable=New_admission_window_last_name_var)
        New_admission_window_last_name_input.place(x=440,y=60)

        # New admission window Father name label
        New_admission_window_father_name_label = Label(New_admission_window,text="Father Name",font=6,bg="#ccffcc")
        New_admission_window_father_name_label.place(x=30,y=110)

        # New admission window Father name input
        New_admission_window_Father_name_input = Entry(New_admission_window,width=25,textvariable=New_admission_window_Father_name_var)
        New_admission_window_Father_name_input.place(x=140,y=110)

        # New admission window gender label
        New_admission_window_gender_label = Label(New_admission_window,text="Gender",font=6,bg="#ccffcc")
        New_admission_window_gender_label.place(x=40,y=160)

        # New admission window gender Radio button
        New_admission_window_gender_radio_button1 = Radiobutton(New_admission_window, text="Male", variable=New_admission_window_gender_rd, value="Male" ,bg="#ccffcc")
        New_admission_window_gender_radio_button1.place(x=120,y=160)
        New_admission_window_gender_radio_button2 = Radiobutton(New_admission_window, text="Female", variable=New_admission_window_gender_rd, value="Female",bg="#ccffcc")
        New_admission_window_gender_radio_button2.place(x=200,y=160)

        # New admission window Date of Birth Label
        New_admission_window_dob_label = Label(New_admission_window,text="Date of Birth",font=6,bg="#ccffcc")
        New_admission_window_dob_label.place(x=30,y=210)

        # New admission window Date of Birth input
        New_admission_window_dob_input = DateEntry(New_admission_window,width=20,date_pattern='yyyy-mm-dd')
        New_admission_window_dob_input.place(x=140,y=210)

        # New admission window Mobile Number Label
        New_admission_window_mobile_number_label = Label(New_admission_window,text="Mobile Number",font=6,bg="#ccffcc")
        New_admission_window_mobile_number_label.place(x=20,y=260)

        # New admission window Mobile Number input
        New_admission_window_mobile_number_input  = Entry(New_admission_window,width=25,textvariable=New_admission_window_mobile_number_var)
        New_admission_window_mobile_number_input.place(x=140,y=260)

        # New admission window email Id label
        New_admission_window_email_id_label = Label(New_admission_window,text="Email Id",font=6,bg="#ccffcc")
        New_admission_window_email_id_label.place(x=40,y=310)

        # New admission window email Id input
        New_admission_window_email_id_input = Entry(New_admission_window,width=25,textvariable=New_admission_window_email_id_var)
        New_admission_window_email_id_input.place(x=140,y=310)

        New_admission_window_add_course_label = Label(New_admission_window,text="Add Course",font=6,bg="#ccffcc")
        New_admission_window_add_course_label.place(x=340,y=110)

        courses = ["BCA","MCA","BSc","MSc","B-Tech","M-Tech"]

        New_admission_window_add_course_dropdown = OptionMenu(New_admission_window , New_admission_window_dropdown_var, *courses, command=on_change)
        New_admission_window_add_course_dropdown.place(x=440,y=105)

        New_admission_window_duration_label = Label(New_admission_window,text="Duration (Year)",font=6,bg="#ccffcc")
        New_admission_window_duration_label.place(x=330,y=160)

        New_admission_window_duration_input = Entry(New_admission_window,width=25,textvariable=New_admission_window_duration_var)
        New_admission_window_duration_input.place(x=450,y=160)

        New_admission_window_course_fees_label = Label(New_admission_window,text="Course Fees",font=6,bg="#ccffcc")
        New_admission_window_course_fees_label.place(x=330,y=210)

        New_admission_window_course_fees_input = Entry(New_admission_window,width=25,textvariable=New_admission_window_course_fees_var)
        New_admission_window_course_fees_input.place(x=450,y=210)

        New_admission_window_1st_semester_fees_label = Label(New_admission_window,text="1st Semester Fees",font=6,bg="#ccffcc")
        New_admission_window_1st_semester_fees_label.place(x=310,y=260)

        New_admission_window_1st_semester_fees_input = Entry(New_admission_window,width=25,textvariable=New_admission_window_1st_semester_fees_var)
        New_admission_window_1st_semester_fees_input.place(x=450,y=260)

        New_admission_window_address_label = Label(New_admission_window,text="Address",font=6,bg="#ccffcc")
        New_admission_window_address_label.place(x=340,y=330)

        New_admission_window_address_input = Text(New_admission_window, height=5, width=25)
        New_admission_window_address_input.place(x=450,y=310)

        New_admission_fees_alert= Label(New_admission_window, text="Go back to the main menu and click student fees \n for submission of fees",bg="#ccffcc")

        New_admission_window_Submit_button = Button(New_admission_window,text="Submit",command=Submit_function)
        New_admission_window_Submit_button.place(x=300,y=470)

        New_admission_window_back_button = Button(New_admission_window,text="Back",command=back_function)
        New_admission_window_back_button.place(x=380,y=470)

    def Student_fees():

        def search(event):
            Student_fees_mobile_number = Student_fees_mobile_number_var.get()

            sql = f"select  First_Name, Last_Name, Course, Semester, Semester_Fees, Pending_Fees, Paid_Fees from New_Admission where MobileNumber={Student_fees_mobile_number}"
            cursor.execute(sql)

            record = cursor.fetchone()

            if(record!=None):
                
                Student_fees_first_name_label.config(
                    text="First Name"
                )
                Student_fees_first_name_value.config(
                    text=record[0]
                )
                Student_fees_last_name_label.config(
                    text="Last Name"
                )
                Student_fees_last_name_value.config(
                    text=record[1]
                )
                Student_fees_course_label.config(
                    text="Course"
                )
                Student_fees_course_value.config(
                    text=record[2]
                )
                Student_fees_semester_label.config(
                    text="Semester"
                )
                Student_fees_semester_value.config(
                    text=record[3]
                )
                Student_fees_semester_fees_label.config(
                    text="Semester Fees"
                )
                Student_fees_semester_fees_value.config(
                    text=record[4]
                )
                Student_fees_pending_fees_label.config(
                    text="Pending Fees"
                )
                Student_fees_pending_fees_value.config(
                    text=record[5]
                )
                Student_fees_paid_fees_label.config(
                    text="Paid Fees"
                )
                Student_fees_paid_fees_value.config(
                    text=record[6]
                )
                Student_fees_update_fees.config(
                    text="Update Fees"
                )
                Student_fees_update_fees_mobile_number_label.config(
                    text="Mobile Number"
                )

                Student_fees_update_mobile_number_input.place(x=520,y=140)

                Student_fees_update_mobile_number_var.set(Student_fees_mobile_number_var.get())

                Student_fees_update_paid_fees_var.set(value=" ")

                Student_fees_update_last_payment_received_date_var.set(value=" ")

                Student_fees_update_pending_fees_var.set(value=" ")

                Student_fees_update_paid_fees_label.config(
                    text="Paid Fees"
                )

                Student_fees_update_paid_fees_input.place(x=520,y=180)

                Student_fees_update_last_payment_received_date_label.config(
                    text="last Payment Received Date"
                )

                Student_fees_update_last_payment_received_date_input.place(x=520,y=220)

                Student_fees_update_pending_fees_label.config(
                    text="Pending Fees"
                )

                Student_fees_update_pending_fees_input.place(x=520,y=260)

                Student_fees_update_button.place(x=540,y=300)

                Student_fees_update_pending_fees_alert.place(x=480,y=380)

                Student_fees_alert_label.place_forget()
            else:
                Student_fees_first_name_label.config(
                    text=""
                )
                Student_fees_first_name_value.config(
                    text=""
                )
                Student_fees_last_name_label.config(
                    text=""
                )
                Student_fees_last_name_value.config(
                    text=""
                )
                Student_fees_course_label.config(
                    text=""
                )
                Student_fees_course_value.config(
                    text=""
                )
                Student_fees_semester_label.config(
                    text=""
                )
                Student_fees_semester_value.config(
                    text=""
                )
                Student_fees_semester_fees_label.config(
                    text=""
                )
                Student_fees_semester_fees_value.config(
                    text=""
                )
                Student_fees_pending_fees_label.config(
                    text=""
                )
                Student_fees_pending_fees_value.config(
                    text=""
                )
                Student_fees_paid_fees_label.config(
                    text=""
                )
                Student_fees_paid_fees_value.config(
                    text=""
                )
                Student_fees_update_fees.config(
                    text=""
                )
                Student_fees_update_fees_mobile_number_label.config(
                    text=""
                )

                Student_fees_update_mobile_number_input.place_forget()

                Student_fees_update_mobile_number_var.set(value='')

                Student_fees_update_paid_fees_label.config(
                    text=""
                )
                Student_fees_update_paid_fees_input.place_forget()

                Student_fees_update_last_payment_received_date_label.config(
                    text=""
                )

                Student_fees_update_last_payment_received_date_input.place_forget()

                Student_fees_update_pending_fees_label.config(
                    text=""
                )

                Student_fees_update_pending_fees_input.place_forget()

                Student_fees_update_button.place_forget()

                Student_fees_update_pending_fees_alert.place_forget()

                Student_fees_alert_label.place(x=220,y=80)
                
        def update_fees():
            Student_fees_update_mobile_number = Student_fees_update_mobile_number_var.get()
            Student_fees_update_paid_fees = Student_fees_update_paid_fees_var.get()
            Student_fees_update_last_payment_received_date = Student_fees_update_last_payment_received_date_var.get()

            sql = f"select Pending_Fees from New_Admission where MobileNumber={Student_fees_update_mobile_number}"
            cursor.execute(sql)

            record = cursor.fetchone()

            if(record !=None):
                if(record[0]>=Student_fees_update_paid_fees):
                    sql1 = f"update New_Admission set Paid_Fees=Paid_Fees+{Student_fees_update_paid_fees},Pending_Fees=Pending_Fees-{Student_fees_update_paid_fees},Last_Payment_Received_Date='{Student_fees_update_last_payment_received_date}'where MobileNumber={Student_fees_update_mobile_number}" 
                    cursor.execute(sql1)
                    conn.commit()

                    sql2 = f"select Pending_Fees, Paid_Fees from New_Admission where MobileNumber={Student_fees_update_mobile_number}"
                    cursor.execute(sql2)

                    record2=cursor.fetchone()

                    Student_fees_update_pending_fees_var.set(record2[0])

                    Student_fees_pending_fees_value.config(
                        text=record2[0]
                    )
                    Student_fees_paid_fees_value.config(
                        text=record2[1]
                    )
                    Student_fees_Paid_Amount_alert.config(
                        text=""
                    )
                else:
                    Student_fees_Paid_Amount_alert.config(
                        text="Paid Fees is greater than Pending Fees"
                    )

        def on_closing():
            Student_fees_mobile_number_var.set(value='')
            Student_fees_update_mobile_number_var.set(value='')
            Student_fees_update_paid_fees_var.set(value='')
            Student_fees_update_last_payment_received_date_var.set(value='')
            Student_fees_update_pending_fees_var.set(value='')
            Student_Fees_Window.destroy()
        
        def back_function():
            Student_fees_mobile_number_var.set(value='')
            Student_fees_update_mobile_number_var.set(value='')
            Student_fees_update_paid_fees_var.set(value='')
            Student_fees_update_last_payment_received_date_var.set(value='')
            Student_fees_update_pending_fees_var.set(value='')
            Student_Fees_Window.destroy()
        
        width = 850
        height = 500
        Student_Fees_Window = Toplevel()
        system_width = Student_Fees_Window.winfo_screenwidth()
        system_height=Student_Fees_Window.winfo_screenheight()
        Student_Fees_Window.config(bg="#ccffcc")
        
        Student_Fees_Window.wm_protocol("WM_DELETE_WINDOW", on_closing)

        c_x = int(system_width/2-width/2)
        c_y = int(system_height/2-height/2)


        Student_Fees_Window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        Student_Fees_Window.maxsize(width, height)
        Student_Fees_Window.minsize(width, height)

        Student_fees_main_label = Label(Student_Fees_Window,text="Student Fees",font=10,bg="#ccffcc")
        Student_fees_main_label.pack(pady=7)

        # Student fees mobile number label
        Student_fees_mobile_number_label = Label(Student_Fees_Window,text="Mobile Number",bg="#ccffcc")
        Student_fees_mobile_number_label.place(x=140,y=50)

        # Student Fees mobile number input
        Student_fees_mobile_number_input = Entry(Student_Fees_Window, width=25,textvariable=Student_fees_mobile_number_var)
        Student_fees_mobile_number_input.place(x=240,y=50)

        Student_fees_mobile_number_input.bind('<Return>',search)

        # Student fees Press Enter label
        Student_fees_press_enter_label = Label(Student_Fees_Window,text="Press Enter",bg="#ccffcc") 
        Student_fees_press_enter_label.place(x=410,y=50)

        # Student Fees First Name label
        Student_fees_first_name_label = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_first_name_label.place(x=40,y=90)

        # Student Fees First Name value
        Student_fees_first_name_value = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_first_name_value.place(x=140,y=90)

        # Student Fees Last Name label
        Student_fees_last_name_label = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_last_name_label.place(x=40,y=130)

        # Student Fees Last Name value
        Student_fees_last_name_value = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_last_name_value.place(x=140,y=130)

        # Student Fees Course label
        Student_fees_course_label = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_course_label.place(x=40,y=170)

        # Student Fees Course value
        Student_fees_course_value = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_course_value.place(x=140,y=170)

        # Student Fees Semester label
        Student_fees_semester_label = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_semester_label.place(x=40,y=210)

        # Student Fees Semester value
        Student_fees_semester_value = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_semester_value.place(x=140,y=210)

        # Student Fees Semester Fees label
        Student_fees_semester_fees_label = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_semester_fees_label.place(x=40,y=250)

        # Student Fees Semester Fees value
        Student_fees_semester_fees_value = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_semester_fees_value.place(x=160,y=250)

        # Student Fees Pending Fees label
        Student_fees_pending_fees_label = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_pending_fees_label.place(x=40,y=290)

        # Student Fees Pending Fees value
        Student_fees_pending_fees_value = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_pending_fees_value.place(x=160,y=290)

        # Student Fees Paid Fees label
        Student_fees_paid_fees_label = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_paid_fees_label.place(x=40,y=330)

        # Student Fees Paid Fees value
        Student_fees_paid_fees_value = Label(Student_Fees_Window,text="",font=4,bg="#ccffcc")
        Student_fees_paid_fees_value.place(x=140,y=330)

        # Student fees update fees
        Student_fees_update_fees = Label(Student_Fees_Window,text="",bg="#ccffcc")
        Student_fees_update_fees.place(x=510,y=100)


        # Student fees update fees mobile number label
        Student_fees_update_fees_mobile_number_label = Label(Student_Fees_Window,text="",bg="#ccffcc")
        Student_fees_update_fees_mobile_number_label.place(x=410,y=140)

        # Student Fees update fees mobile number input
        Student_fees_update_mobile_number_input = Entry(Student_Fees_Window, width=25,textvariable=Student_fees_update_mobile_number_var)

        # Student fees update Paid Fees label
        Student_fees_update_paid_fees_label = Label(Student_Fees_Window,text="",bg="#ccffcc")
        Student_fees_update_paid_fees_label.place(x=440,y=180)

        # Student fees update Paid Fees input
        Student_fees_update_paid_fees_input = Entry(Student_Fees_Window,width=25,textvariable= Student_fees_update_paid_fees_var)

        # Student_fees_update last payment received date label
        Student_fees_update_last_payment_received_date_label = Label(Student_Fees_Window,text="",bg="#ccffcc")
        Student_fees_update_last_payment_received_date_label.place(x=340,y=220)

        # Student_fees_update last payment received date input
        Student_fees_update_last_payment_received_date_input = Entry(Student_Fees_Window,width=25,textvariable=Student_fees_update_last_payment_received_date_var)

        # Student fees update pending Fees label
        Student_fees_update_pending_fees_label = Label(Student_Fees_Window,text="",bg="#ccffcc")
        Student_fees_update_pending_fees_label.place(x=420,y=260)

        # Student fees update pending Fees input
        Student_fees_update_pending_fees_input = Entry(Student_Fees_Window,width=25,textvariable=Student_fees_update_pending_fees_var)

        Student_fees_update_pending_fees_input.config(state="disabled")

        # Student fees update Button
        Student_fees_update_button =Button(Student_Fees_Window,text="update fees",command=update_fees)

        # Student fees update alert
        Student_fees_alert_label = Label(Student_Fees_Window,text="student record is not exist",bg="#ccffcc")
    
        Student_fees_Paid_Amount_alert = Label(Student_Fees_Window,text="",bg="#ccffcc")
        Student_fees_Paid_Amount_alert.place(x=480,y=340)

        Student_fees_update_pending_fees_alert = Label(Student_Fees_Window,text="Please click on the update fees button\n to check the pending fees",bg="#ccffcc")

        # back Button
        back_Button = Button(Student_Fees_Window,text="Back",command=back_function)
        back_Button.place(x=380,y=440)
    
    def Student_details():

        def find_student_details():

            Student_details_mobile_number = Student_details_mobile_number_var.get()

            sql = f"select * from New_Admission where MobileNumber={Student_details_mobile_number}"
            cursor.execute(sql)

            record = cursor.fetchone()

            if(record!=None):
                Student_details_first_name_label.config(
                    text="First Name"
                )
                Student_details_first_name_value.config(
                    text=record[0]
                )
                Student_details_last_name_label.config(
                    text="Last Name"
                )
                Student_details_last_name_value.config(
                    text=record[1]
                )
                Student_details_father_name_label.config(
                    text="Father Name"
                )
                Student_details_father_name_value.config(
                    text=record[2]
                )
                Student_details_mobile_number_label.config(
                    text="Mobile Number"
                )
                Student_details_mobile_number_value.config(
                    text=record[3]
                )
                Student_details_gender_label.config(
                    text="Gender"
                )
                Student_details_gender_value.config(
                    text=record[4]
                )
                Student_details_email_id_label.config(
                    text="Email Id"
                )
                Student_details_email_id_value.config(
                    text=record[5]
                )
                Student_details_address_label.config(
                    text="Address"
                )
                Student_details_address_value.config(
                    text=record[6]
                )
                Student_details_student_admission_date_label.config(
                    text="Student Admission Date"
                )
                Student_details_student_admission_date_value.config(
                    text=record[7]
                )
                Student_details_date_of_birth_label.config(
                    text="Date of Birth"
                )
                Student_details_date_of_birth_value.config(
                    text=record[8]
                )
                Student_details_last_payment_received_date_label.config(
                    text="Last Payment Received Date"
                )
                Student_details_last_payment_received_date_value.config(
                    text=record[9]
                )
                Student_details_Course_label.config(
                    text="Course"
                )
                Student_details_Course_value.config(
                    text=record[10]
                )
                Student_details_course_duration_label.config(
                    text="Course Duration"
                )
                Student_details_course_duration_value.config(
                    text=record[11]
                )
                Student_details_semester_label.config(
                    text="Semester"
                )
                Student_details_semester_value.config(
                    text=record[12]
                )
                Student_details_course_fees_label.config(
                    text="Course Fees"
                )
                Student_details_course_fees_value.config(
                    text=record[13]
                )
                Student_details_semester_fees_label.config(
                    text="Semester Fees"
                )
                Student_details_semester_fees_value.config(
                    text=record[14]
                )
                Student_details_pending_fees_label.config(
                    text="Pending Fees"
                )
                
                Student_details_pending_fees_value.config(
                    text=record[15]
                )
                Student_details_paid_fees_label.config(
                    text="Paid Fees"
                )
                Student_details_paid_fees_value.config(
                    text=record[16]
                )
                Student_details_alert_label.place_forget()
            else:
                Student_details_first_name_label.config(
                    text=""
                )
                Student_details_first_name_value.config(
                    text=""
                )
                Student_details_last_name_label.config(
                    text=""
                )
                Student_details_last_name_value.config(
                    text=""
                )
                Student_details_father_name_label.config(
                    text=""
                )
                Student_details_father_name_value.config(
                    text=""
                )
                Student_details_mobile_number_label.config(
                    text=""
                )
                Student_details_mobile_number_value.config(
                    text=""
                )
                Student_details_gender_label.config(
                    text=""
                )
                Student_details_gender_value.config(
                    text=""
                )
                Student_details_email_id_label.config(
                    text=""
                )
                Student_details_email_id_value.config(
                    text=""
                )
                Student_details_address_label.config(
                    text=""
                )
                Student_details_address_value.config(
                    text=""
                )
                Student_details_student_admission_date_label.config(
                    text=""
                )
                Student_details_student_admission_date_value.config(
                    text=""
                )
                Student_details_date_of_birth_label.config(
                    text=""
                )
                Student_details_date_of_birth_value.config(
                    text=""
                )
                Student_details_last_payment_received_date_label.config(
                    text=""
                )
                Student_details_last_payment_received_date_value.config(
                    text=""
                )
                Student_details_Course_label.config(
                    text=""
                )
                Student_details_Course_value.config(
                    text=""
                )
                Student_details_course_duration_label.config(
                    text=""
                )
                Student_details_course_duration_value.config(
                    text=""
                )
                Student_details_semester_label.config(
                    text=""
                )
                Student_details_semester_value.config(
                    text=""
                )
                Student_details_course_fees_label.config(
                    text=""
                )
                Student_details_course_fees_value.config(
                    text=""
                )
                Student_details_semester_fees_label.config(
                    text=""
                )
                Student_details_semester_fees_value.config(
                    text=""
                )
                Student_details_pending_fees_label.config(
                    text=""
                )
                Student_details_pending_fees_value.config(
                    text=""
                )
                Student_details_paid_fees_label.config(
                    text=""
                )
                Student_details_paid_fees_value.config(
                    text=""
                )
                Student_details_alert_label.place(x=180,y=90)

        def on_closing():
            Student_details_mobile_number_var.set(value='')
            Student_details_Window.destroy()

        def back_function():
            Student_details_mobile_number_var.set(value='')
            Student_details_Window.destroy()

        width = 700
        height = 550
        Student_details_Window = Toplevel()
        system_width = Student_details_Window.winfo_screenwidth()
        system_height=Student_details_Window.winfo_screenheight()
        Student_details_Window.config(bg="#ccffcc")

        c_x = int(system_width/2-width/2)
        c_y = int(system_height/2-height/2)


        Student_details_Window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        Student_details_Window.maxsize(width, height)
        Student_details_Window.minsize(width, height)

        Student_details_Window.wm_protocol("WM_DELETE_WINDOW", on_closing)

        # Student details main label
        Student_details_main_label = Label(Student_details_Window,text="Student Details",font=10,bg="#ccffcc")
        Student_details_main_label.pack(pady=7)

        # Student details mobile number label
        Student_details_mobile_number_label = Label(Student_details_Window,text="Mobile Number",bg="#ccffcc")
        Student_details_mobile_number_label.place(x=140,y=50)

        # Student details mobile number input
        Student_details_mobile_number_input = Entry(Student_details_Window, width=25,textvariable=Student_details_mobile_number_var)
        Student_details_mobile_number_input.place(x=240,y=50)

        # Student details find Button
        Student_details_find_Button = Button(Student_details_Window,text="Find",command=find_student_details)
        Student_details_find_Button.place(x=410,y=45)
        
        # Student Details First Name label
        Student_details_first_name_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_first_name_label.place(x=40,y=90)

        # Student Details First Name value
        Student_details_first_name_value = Label(Student_details_Window,text='',font=4,bg="#ccffcc")
        Student_details_first_name_value.place(x=140,y=90)

        # Student Details Last Name label
        Student_details_last_name_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_last_name_label.place(x=40,y=130)

        # Student Details Last Name value
        Student_details_last_name_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_last_name_value.place(x=140,y=130)

        # Student Details Father Name label
        Student_details_father_name_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_father_name_label.place(x=40,y=170)

        # Student Details Father Name value
        Student_details_father_name_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_father_name_value.place(x=140,y=170)

        # Student Details Mobile Number label
        Student_details_mobile_number_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_mobile_number_label.place(x=40,y=210)
        
        # Student Details Mobile Number value
        Student_details_mobile_number_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_mobile_number_value.place(x=160,y=210)
        
        # Student Details Gender label
        Student_details_gender_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_gender_label.place(x=40,y=250)

        # Student Details Gender value
        Student_details_gender_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_gender_value.place(x=110,y=250)
        
        # Student Details Email Id label
        Student_details_email_id_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_email_id_label.place(x=40,y=290)

        # Student Details Email Id value
        Student_details_email_id_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_email_id_value.place(x=110,y=290)

        # Student Details Address label
        Student_details_address_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_address_label.place(x=40,y=330)
        
        # Student Details Address value
        Student_details_address_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_address_value.place(x=110,y=330)
        
        # Student Details Student Admission Date label
        Student_details_student_admission_date_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_student_admission_date_label.place(x=40,y=370)
        
        # Student Details Student Admission Date value
        Student_details_student_admission_date_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_student_admission_date_value.place(x=220,y=370)

        # Student Details Date of Birth label
        Student_details_date_of_birth_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_date_of_birth_label.place(x=40,y=410)

        # Student Details Date of Birth value
        Student_details_date_of_birth_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_date_of_birth_value.place(x=140,y=410)

        # Student Details Last Payment Received Date label
        Student_details_last_payment_received_date_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_last_payment_received_date_label.place(x=40,y=450)

        # Student Details Last Payment Received Date value
        Student_details_last_payment_received_date_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_last_payment_received_date_value.place(x=260,y=450)

        # Student Details Course label
        Student_details_Course_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_Course_label.place(x=40,y=490)
        
        # Student Details Course value
        Student_details_Course_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_Course_value.place(x=100,y=490)

        # Student Details Course Duration label
        Student_details_course_duration_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_course_duration_label.place(x=400,y=90)

        # Student Details Course Duration value
        Student_details_course_duration_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_course_duration_value.place(x=530,y=90)

        # Student Details Semester label
        Student_details_semester_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_semester_label.place(x=400,y=130)

        # Student Details Semester value
        Student_details_semester_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_semester_value.place(x=480,y=130)

        # Student Details Course Fees label
        Student_details_course_fees_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_course_fees_label.place(x=400,y=170)

        # Student Details Course Fees value
        Student_details_course_fees_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_course_fees_value.place(x=500,y=170)

        # Student Details Semester Fees label
        Student_details_semester_fees_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_semester_fees_label.place(x=400,y=210)

        # Student Details Semester Fees value
        Student_details_semester_fees_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_semester_fees_value.place(x=520,y=210)

        # Student Details Pending Fees label
        Student_details_pending_fees_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_pending_fees_label.place(x=400,y=250)

        # Student Details Pending Fees value
        Student_details_pending_fees_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_pending_fees_value.place(x=520,y=250)

        # Student Details Paid Fees label
        Student_details_paid_fees_label = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_paid_fees_label.place(x=400,y=290)

        # Student Details Paid Fees value
        Student_details_paid_fees_value = Label(Student_details_Window,text="",font=4,bg="#ccffcc")
        Student_details_paid_fees_value.place(x=490,y=290)

        Student_details_alert_label = Label(Student_details_Window,text="student record is not exist",font=4,bg="#ccffcc")

        Student_details_back_button =  Button(Student_details_Window,text="Back",command=back_function)
        Student_details_back_button.place(x=310,y=500)
    
    def Remove_student():

        def back_function():
            Remove_student_mobile_number_var.set(value ="")
            Remove_student_Window.destroy()

        def on_closing():
            Remove_student_mobile_number_var.set(value ="")
            Remove_student_Window.destroy()
        
        def Remove():

            Remove_student_mobile_number= Remove_student_mobile_number_var.get()
            sql = f"select * from New_Admission where MobileNumber={Remove_student_mobile_number}"
            cursor.execute(sql)

            record = cursor.fetchone()

            if(record!=None):
                sql2 = f"delete from New_Admission where MobileNumber={Remove_student_mobile_number}"
                cursor.execute(sql2)
                conn.commit()
                messagebox.showinfo("", "Deleted Student Record",parent=Remove_student_Window)
                student_record_is_not_exist.config(
                    text=""
                )
                Remove_student_mobile_number_var.set(value='')
            else:
                student_record_is_not_exist.config(
                    text="student record is not exist"
                )
                Remove_student_mobile_number_var.set(value='')   
                
        width = 560
        height = 250
        Remove_student_Window = Toplevel()
        system_width = Remove_student_Window.winfo_screenwidth()
        system_height=Remove_student_Window.winfo_screenheight()

        c_x = int(system_width/2-width/2)
        c_y = int(system_height/2-height/2)


        Remove_student_Window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        Remove_student_Window.maxsize(width, height)
        Remove_student_Window.minsize(width, height)
        Remove_student_Window.config(bg="#ccffcc")

        Remove_student_Window.wm_protocol("WM_DELETE_WINDOW", on_closing)

        # Remove student main label
        Remove_student_main_label = Label(Remove_student_Window,text="Remove Student",font=10,bg="#ccffcc")
        Remove_student_main_label.pack(pady=7)

        # Remove student Mobile Number label
        Remove_student_mobile_number_label = Label(Remove_student_Window,text="Mobile Number",font=4,bg="#ccffcc")
        Remove_student_mobile_number_label.place(x=80,y=90)

        # Remove student Mobile Number input
        Remove_student_mobile_number_input = Entry(Remove_student_Window, width=25,textvariable=Remove_student_mobile_number_var)
        Remove_student_mobile_number_input.place(x=210,y=90)

        # Remove student Button
        Remove_student_Button = Button(Remove_student_Window,text="Remove Student",command=Remove)
        Remove_student_Button.place(x=380,y=90) 

        # back Button
        back_Button = Button(Remove_student_Window,text="Back",command=back_function)
        back_Button.place(x=250,y=170)

        # student record is not exist
        student_record_is_not_exist = Label(Remove_student_Window,text="",font=4,bg="#ccffcc")
        student_record_is_not_exist.place(x=200,y=120)

    def upgrade_semester():

        def upgrade_semester_search(event):
            upgrade_semester_mobile_number = upgrade_semester_mobile_number_var.get()
            
            sql = f"select  First_Name, Last_Name, Course, Semester, Pending_Fees, Paid_Fees from New_Admission where MobileNumber={upgrade_semester_mobile_number}"

            cursor.execute(sql)

            record = cursor.fetchone()

            if(record!=None):

                upgrade_semester_first_name_label.grid(row=0,column=0,pady=7)

                upgrade_semester_first_name_input.grid(row=0,column=0,pady=9)

                upgrade_semester_first_name_var.set(record[0])

                upgrade_semester_last_name_label.grid(row=1,column=0,pady=7)
                
                upgrade_semester_last_name_input.grid(row=1,column=0,pady=9)

                upgrade_semester_last_name_var.set(record[1])

                upgrade_semester_Course_label.grid(row=2,column=0,pady=7)

                upgrade_semester_Course_input.grid(row=2,column=0,pady=9)

                upgrade_semester_Course_var.set(record[2])
                
                upgrade_semester_label.grid(row=3,column=0,pady=7)
                
                upgrade_semester_option_menu.grid(row=3,column=0,pady=9)

                upgrade_semester_pending_fees_label.grid(row=4,column=0,pady=7)

                upgrade_semester_pending_fees_input.grid(row=4,column=0,pady=9)
                upgrade_semester_pending_fees_var.set(record[4])

                upgrade_semester_paid_fees_label.grid(row=5,column=0,pady=7)

                upgrade_semester_paid_fees_input.grid(row=5,column=0,pady=9)

                upgrade_semester_paid_fees_var.set(record[5])

                upgrade_semester_button.place(x=240,y=340)

                upgrade_semester_record_is_not_exist.place_forget()

                if("B-Tech"==record[2]):
                    semester_option = ["1st","2nd","3rd","4th","5th","6th","7th","8th"]
                    upgrade_semester_option_menu['menu'].delete(0, 'end')
                    upgrade_semester_var.set(record[3])
                    for option in semester_option:
                        upgrade_semester_option_menu['menu'].add_command(label=option, command=tk._setit(upgrade_semester_var, option))

                elif("M-Tech"==record[2]):
                    semester_option = ["1st","2nd","3rd","4th"]
                    upgrade_semester_option_menu['menu'].delete(0, 'end')
                    upgrade_semester_var.set(record[3])
                    for option in semester_option:
                        upgrade_semester_option_menu['menu'].add_command(label=option, command=tk._setit(upgrade_semester_var, option))

                elif("BCA"==record[2]):
                    semester_option = ["1st","2nd","3rd","4th","5th","6th"]
                    upgrade_semester_option_menu['menu'].delete(0, 'end')
                    upgrade_semester_var.set(record[3])
                    for option in semester_option:
                        upgrade_semester_option_menu['menu'].add_command(label=option, command=tk._setit(upgrade_semester_var, option))
                
                elif("MCA"==record[2]):
                    semester_option = ["1st","2nd","3rd","4th"]
                    upgrade_semester_option_menu['menu'].delete(0, 'end')
                    upgrade_semester_var.set(record[3])
                    for option in semester_option:
                        upgrade_semester_option_menu['menu'].add_command(label=option, command=tk._setit(upgrade_semester_var, option))
                
                elif("BSc"==record[2]):
                    semester_option = ["1st","2nd","3rd","4th","5th","6th"]
                    upgrade_semester_option_menu['menu'].delete(0, 'end')
                    upgrade_semester_var.set(record[3])
                    for option in semester_option:
                        upgrade_semester_option_menu['menu'].add_command(label=option, command=tk._setit(upgrade_semester_var, option))
                
                elif("MSc"==record[2]):
                    semester_option = ["1st","2nd","3rd","4th"]
                    upgrade_semester_option_menu['menu'].delete(0, 'end')
                    upgrade_semester_var.set(record[3])
                    for option in semester_option:
                        upgrade_semester_option_menu['menu'].add_command(label=option, command=tk._setit(upgrade_semester_var, option))
                
                upgrade_semester_fees_alert.place_forget()    
            else:
                upgrade_semester_first_name_label.grid_forget()
                upgrade_semester_first_name_input.grid_forget()

                upgrade_semester_last_name_label.grid_forget()
                upgrade_semester_last_name_input.grid_forget()

                upgrade_semester_Course_label.grid_forget()
                upgrade_semester_Course_input.grid_forget()

                upgrade_semester_label.grid_forget()
                upgrade_semester_option_menu.grid_forget()
                upgrade_semester_button.place_forget()

                upgrade_semester_pending_fees_label.grid_forget()
                upgrade_semester_pending_fees_input.grid_forget()

                upgrade_semester_paid_fees_label.grid_forget()
                upgrade_semester_paid_fees_input.grid_forget()

                upgrade_semester_record_is_not_exist.place(x=180,y=80)

        def upgrade_semester_function():
            upgrade_semester_mobile_number = upgrade_semester_mobile_number_var.get()
            upgrade_semester = upgrade_semester_var.get()

            sql = f"select Pending_Fees, Course from New_Admission where MobileNumber={upgrade_semester_mobile_number}"
            cursor.execute(sql)

            record = cursor.fetchone()

            if(record[0]==0):
                
                if(record[1]=="B-Tech"):

                    semester_fees = 18000
                    sql1 = f"update New_Admission set Pending_Fees=Pending_Fees+{semester_fees}, Semester='{upgrade_semester}' where MobileNumber={upgrade_semester_mobile_number}" 
                    cursor.execute(sql1)
                    conn.commit()
                    
                    messagebox.showinfo("", "Your semester status will be upgraded.",parent=upgrade_semester_window)

                    sql2 = f"select Pending_Fees from New_Admission where MobileNumber={upgrade_semester_mobile_number}"
                    cursor.execute(sql2)

                    record2=cursor.fetchone()
                    upgrade_semester_pending_fees_var.set(record2[0])

                elif(record[1]=="M-Tech"):

                    semester_fees = 22000
                    sql1 = f"update New_Admission set Pending_Fees=Pending_Fees+{semester_fees}, Semester='{upgrade_semester}' where MobileNumber={upgrade_semester_mobile_number}" 
                    cursor.execute(sql1)
                    conn.commit()
                    
                    messagebox.showinfo("", "Your semester status will be upgraded.",parent=upgrade_semester_window)


                    sql2 = f"select Pending_Fees from New_Admission where MobileNumber={upgrade_semester_mobile_number}"
                    cursor.execute(sql2)

                    record2=cursor.fetchone()
                    upgrade_semester_pending_fees_var.set(record2[0])


                elif(record[1]=="BCA"):

                    semester_fees = 14000
                    sql1 = f"update New_Admission set Pending_Fees=Pending_Fees+{semester_fees}, Semester='{upgrade_semester}' where MobileNumber={upgrade_semester_mobile_number}" 
                    cursor.execute(sql1)
                    conn.commit()
                    
                    messagebox.showinfo("", "Your semester status will be upgraded.",parent=upgrade_semester_window)


                    sql2 = f"select Pending_Fees from New_Admission where MobileNumber={upgrade_semester_mobile_number}"
                    cursor.execute(sql2)

                    record2=cursor.fetchone()
                    upgrade_semester_pending_fees_var.set(record2[0])


                elif(record[1]=="MCA"):

                    semester_fees = 16000
                    sql1 = f"update New_Admission set Pending_Fees=Pending_Fees+{semester_fees}, Semester='{upgrade_semester}' where MobileNumber={upgrade_semester_mobile_number}" 
                    cursor.execute(sql1)
                    conn.commit()
                    
                    messagebox.showinfo("", "Your semester status will be upgraded.",parent=upgrade_semester_window)


                    sql2 = f"select Pending_Fees from New_Admission where MobileNumber={upgrade_semester_mobile_number}"
                    cursor.execute(sql2)

                    record2=cursor.fetchone()
                    upgrade_semester_pending_fees_var.set(record2[0])


                elif(record[1]=="BSc"):

                    semester_fees = 15000
                    sql1 = f"update New_Admission set Pending_Fees=Pending_Fees+{semester_fees}, Semester='{upgrade_semester}' where MobileNumber={upgrade_semester_mobile_number}" 
                    cursor.execute(sql1)
                    conn.commit()

                    messagebox.showinfo("", "Your semester status will be upgraded.",parent=upgrade_semester_window)


                    sql2 = f"select Pending_Fees from New_Admission where MobileNumber={upgrade_semester_mobile_number}"
                    cursor.execute(sql2)

                    record2=cursor.fetchone()
                    upgrade_semester_pending_fees_var.set(record2[0])


                elif(record[1]=="MSc"):

                    semester_fees = 17000
                    sql1 = f"update New_Admission set Pending_Fees=Pending_Fees+{semester_fees}, Semester='{upgrade_semester}' where MobileNumber={upgrade_semester_mobile_number}" 
                    cursor.execute(sql1)
                    conn.commit()

                    messagebox.showinfo("", "Your semester status will be upgraded.",parent=upgrade_semester_window)


                    sql2 = f"select Pending_Fees from New_Admission where MobileNumber={upgrade_semester_mobile_number}"
                    cursor.execute(sql2)

                    record2=cursor.fetchone()
                    upgrade_semester_pending_fees_var.set(record2[0])
                
                upgrade_semester_fees_alert.place_forget()
            else:
                messagebox.showinfo("", "Your previous semester fees is pending!",parent=upgrade_semester_window)
                upgrade_semester_fees_alert.place(x=140,y=400)
        
        def back_function():
            upgrade_semester_mobile_number_var.set(value='')
            upgrade_semester_window.destroy()

        def on_closing():
            upgrade_semester_mobile_number_var.set(value='')
            upgrade_semester_window.destroy()

        width = 550
        height = 520
        upgrade_semester_window = Toplevel()
        system_width = upgrade_semester_window.winfo_screenwidth()
        system_height=upgrade_semester_window.winfo_screenheight()
        upgrade_semester_window.config(bg="#ccffcc")

        c_x = int(system_width/2-width/2)
        c_y = int(system_height/2-height/2)

        upgrade_semester_window.geometry(f"{width}x{height}+{c_x}+{c_y}")
        upgrade_semester_window.maxsize(width, height)
        upgrade_semester_window.minsize(width, height)

        upgrade_semester_window.wm_protocol("WM_DELETE_WINDOW", on_closing)

        upgrade_semester_label_frame = Frame(upgrade_semester_window,bg="#ccffcc")
        upgrade_semester_label_frame.place(x=100,y=90)

        upgrade_semester_value_frame = Frame(upgrade_semester_window,bg="#ccffcc")
        upgrade_semester_value_frame.place(x=240,y=90)

        upgrade_semester_main_label = Label(upgrade_semester_window,text="Upgrade Semester",font=10,bg="#ccffcc")
        upgrade_semester_main_label.pack(pady=7)

        # upgrade semester Mobile Number label
        upgrade_semester_mobile_number_label = Label(upgrade_semester_window,text="Mobile Number",font=4,bg="#ccffcc")
        upgrade_semester_mobile_number_label.place(x=90,y=45)

        # upgrade semester mobile number input
        upgrade_semester_mobile_number_input = Entry(upgrade_semester_window, width=25,textvariable= upgrade_semester_mobile_number_var)
        upgrade_semester_mobile_number_input.place(x=210,y=50)

        # Student fees Press Enter label
        upgrade_semester_press_enter_label = Label(upgrade_semester_window,text="Press Enter" ,bg="#ccffcc")
        upgrade_semester_press_enter_label.place(x=370,y=50)

        upgrade_semester_mobile_number_input.bind('<Return>',upgrade_semester_search)

        #upgrade semester First Name label
        upgrade_semester_first_name_label = Label(upgrade_semester_label_frame,text="First Name",font=4,bg="#ccffcc")

        #upgrade semester First Name value
        upgrade_semester_first_name_input = Entry(upgrade_semester_value_frame,width=25,textvariable=upgrade_semester_first_name_var)

        # upgrade semester Last Name label
        upgrade_semester_last_name_label = Label(upgrade_semester_label_frame,text="Last Name",font=4,bg="#ccffcc")

        # upgrade semester Last Name input
        upgrade_semester_last_name_input = Entry(upgrade_semester_value_frame,width=25,textvariable=upgrade_semester_last_name_var)

        #upgrade semester Course label
        upgrade_semester_Course_label = Label(upgrade_semester_label_frame,text="Course",font=4,bg="#ccffcc")

        #upgrade semester Course input
        upgrade_semester_Course_input = Entry(upgrade_semester_value_frame,width=25,textvariable=upgrade_semester_Course_var)

        # upgrade Semester label
        upgrade_semester_label = Label(upgrade_semester_label_frame,text="Semester",font=4,bg="#ccffcc")

        options = ['']

        #upgrade semester value
        upgrade_semester_option_menu = OptionMenu(upgrade_semester_value_frame, upgrade_semester_var, *options)

        #upgrade semester pending fees label
        upgrade_semester_pending_fees_label = Label(upgrade_semester_label_frame,text="Pending Fees",font=4,bg="#ccffcc")

        #upgrade semester pending fees value 
        upgrade_semester_pending_fees_input = Entry(upgrade_semester_value_frame,width=25,textvariable=upgrade_semester_pending_fees_var)

        #upgrade semester paid fees label
        upgrade_semester_paid_fees_label = Label(upgrade_semester_label_frame,text="Paid Fees",font=4,bg="#ccffcc")

        #upgrade semester paid fees value 
        upgrade_semester_paid_fees_input = Entry(upgrade_semester_value_frame,width=25,textvariable=upgrade_semester_paid_fees_var)

        upgrade_semester_fees_alert= Label(upgrade_semester_window, text="Go back to the main menu and click student fees \n for submission of fees",bg="#ccffcc")


        upgrade_semester_button = Button(upgrade_semester_window,text="upgrade",command=upgrade_semester_function) 
        
        upgrade_semester_back_button = Button(upgrade_semester_window,text="back",command=back_function)
        upgrade_semester_back_button.place(x=240,y=470)

        upgrade_semester_record_is_not_exist = Label(upgrade_semester_window,text="Student record is not exist",bg="#ccffcc")
    
    # window main label
    window_label = Label(window, text="College Management System",font={"bold",12},bg="#ccffcc")
    window_label.pack(pady=12)

    window_button =  Button(window,text="Proceed to Main Menu",command=main_window)
    window_button.pack(pady=50)
window.mainloop()