import appointment as ap
# from appointmentSkel import DAYS_OF_WEEK, LAST_HOUR_OF_DAY, FIRST_HOUR_OF_DAY
from constants import DAYS_OF_WEEK, LAST_HOUR_OF_DAY, FIRST_HOUR_OF_DAY


def schedule_appointment(appt_calendar):
    print("\nSchedule an appointment: ")
    day_of_week = input("What Day: ")
    start_hour = int(input("Enter start hour (24hr clock 9-16): "))

    if day_of_week.capitalize() not in DAYS_OF_WEEK: 
        print("Invalid day of the week.")
        return ''
    
    if start_hour < FIRST_HOUR_OF_DAY or start_hour > LAST_HOUR_OF_DAY:
        print("Invalid start hour. The salon is opem from 9 to 4!")
        return ''
    
    appointment = find_appointment_by_time(appt_calendar, day_of_week, start_hour)
    if appointment and appointment.get_client_name():
        print("Appointment slot already booked!")
    
    else:
        if appointment is not None:
            appointment.cancel()

        client_name = input("Client Name: ").capitalize()
        client_phone = input("Client Phone: ")
        print("1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
        appt_type = int(input("Type of Appointment: "))

        new_appointment = ap.Appointment(day_of_week, start_hour)
        new_appointment.schedule(client_name, client_phone, appt_type)
        print(f"OK, {client_name}'s appointment is scheduled!")

        appt_calendar[appt_calendar.index(appointment)] = new_appointment

def cancel_appointment(appt_calendar: list[ap.Appointment], day_of_week, start_hour, end_hour):
    appointment_to_cancel = find_appointment_by_time(appt_calendar, day_of_week, start_hour)

    if appointment_to_cancel is not None and appointment_to_cancel.get_client_name() is not None:
        print(f"Cancelling appointment for {appointment_to_cancel.get_client_name()}, on {day_of_week} at {start_hour}:00 - {end_hour}:00")
        appointment_to_cancel.cancel()

    elif appointment_to_cancel is not None:
        print(f"No appointments scheduled on {day_of_week} at {start_hour}:00")
    
    else:
        print("Invalid day or time")

def find_appointment_by_time(appt_calendar: list[ap.Appointment], day_of_week, start_hour):
    # find_appointment_by_time - given a list of appointments and a specific day and time,
    # this function finds and returns the corresponding appointment. If no appointment
    # is found, returns None
    for appointment in appt_calendar:
        if appointment.get_day_of_week().capitalize() == day_of_week.capitalize() and appointment.get_start_time_hour() == start_hour:
            return appointment
        
    return None
