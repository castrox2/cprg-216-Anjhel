import appointment as ap
from apptMgmt import find_appointment_by_time
from constants import DAYS_OF_WEEK, LAST_HOUR_OF_DAY, FIRST_HOUR_OF_DAY
# import for path functions
from os import path
from os import system

def load_scheduled_appointments(appt_calendar: list[ap.Appointment]):
    while True:
        filePath = input("Enter appointment filename: ")

        if path.exists(filePath):
            with open(filePath, 'r') as file:
                for line in file:
                    data = line.strip().split(',')

                    if len(data) != 5:
                        print(f"invalid data format: {data}")

                    client_name, client_phone, appt_type, day_of_week, start_hour  = data

                    try:
                        start_hour = int(start_hour)
                        appt_type = int(appt_type)
                    
                    except ValueError:
                        print(f"Invalid start_hour or appt_type value: {start_hour}, {appt_type}")
                        
                    appointment = find_appointment_by_time(appt_calendar, day_of_week, start_hour)
                    
                    if appointment is not None:
                        appointment.schedule(client_name, client_phone, appt_type)
                        print(f"Loaded appointment for {client_name} on {day_of_week} at {start_hour}:00")

                break
        else:
            print(f"File not found: {filePath}")

    if not appt_calendar:
        print("No appointments loaded!")

def save_scheduled_appointments(appt_calendar: list[ap.Appointment]):
    filePath = input("Enter the path to save scheduled appointments: ")

    with open(filePath, 'w') as file:
        for appointment in appt_calendar:
            if appointment.get_client_name() is not None:
                file.write(f"{appointment.get_day_of_week()}, {appointment.get_start_time_hour()},"
                           f"{appointment.get_client_name()}, {appointment.get_client_phone()},"
                           f"{appointment.get_appt_type}\n")
    
    print(f"Appointments saved to {filePath}")

