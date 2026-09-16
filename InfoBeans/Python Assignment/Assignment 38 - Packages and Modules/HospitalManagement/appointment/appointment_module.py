'''
Appointment Management Package

Create a package named "appointment".

Create module:
appointment_module.py


Implement:


a) book_appointment()

Take appointment details:

- Appointment ID
- Patient ID
- Doctor ID
- Appointment Date
- Appointment Time


Store appointment information.


b) show_appointments()

Display all booked appointments.

 '''

# A = []
# def book_appointment():
#     AppointmentID = int(input("Enter Appointment ID : "))
#     PatientID = int(input("Enter Patient ID : "))
#     DoctortID = int(input("Enter Doctor ID : "))
#     AppointmenDate = input("Enter Appointment Date : ")
#     AppointmentTime = input("Enter Appointment Time : ")

#     A.append([AppointmentID,PatientID,DoctortID,AppointmenDate,AppointmentTime])

#     print("\nAppointment added successfully")

# def show_appointments():
#     for i in A:
#         print(i)

appointments = []

def book_appointment():
    appointment = {}

    appointment["Appointment ID"] = int(input("Enter Appointment ID  : "))
    appointment["Patient ID"] = int(input("Enter Doctor Patient ID : "))
    appointment["Doctor ID"] = int(input("Enter Doctor Doctor ID : "))
    appointment["Appointment Date"] = input("Enter Appointment Date : ")
    appointment["Appointment Time"] = input("Enter Appointment Time : ")
   

    appointments.append(appointment)

    print("\nAppointment booked successfully!")


def show_appointments():
    if len(appointments)==0:
        print("\nNo Appointments Added Now")

    else:
        print("\n                    Appointment Details : ")

        for a in appointments:
            print("Appointment ID :", a["Appointment ID"])
            print("Patient ID :", a["Patient ID"])
            print("Doctor ID :", a["Doctor ID"])
            print("Appointment Date :", a["Appointment Date"])
            print("Appointment Time :", a["Appointment Time"])
            print()