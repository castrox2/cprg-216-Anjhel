import appointment as ap

def show_appointments_by_name(appt_calendar: list[ap.Appointment], client_name):
    print(f"\nAppointments for {client_name}:")
    print(f"{'Client Name':<15} {'Phone':<15} {'Day':<15} {'Start':<8} {'End':<15} {'Type':<15}")
    print("-" * 100)
    found_appointments = False

    for appointment in appt_calendar:
        if client_name in appointment.get_client_name():
            print(appointment.format_record())
            found_appointments = True

    if not found_appointments:
        print("No Appointments Found")

def show_appointments_by_day(appt_calendar: list[ap.Appointment], day_of_week):
    # show_appointments_by_day - prints a report of all appointments for a specific day of the week
    print(f"\nAppointmnets for {day_of_week}")
    print(f"{'Client Name':<15} {'Phone':<15} {'Day':<15} {'Start':<8} {'End':<15} {'Type':<15}")
    print("-" * 100)
    found_appointments = False

    for appointment in appt_calendar:
        if appointment.get_day_of_week().lower() == day_of_week.lower() and \
            appointment.get_client_name() is not None:
            print(appointment.format_record())
            found_appointments = True
    
    if not found_appointments:
        print(f"No appointments found for {day_of_week}")
