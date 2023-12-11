class Appointment:
    # write your appointment class here!!!

    APPT_TYPE_DESCS = ("Available", "Mens Cut", "Ladies Cut", "Mens Colouring", "Ladies Colouring")
    APPT_TYPE_PRICES = (0, 50, 80, 50, 120)
    
    # constructor for the Appointment class
    def __init__(self, day_of_week, start_time_hour):
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour
        self.__client_name = ""
        self.__client_phone = ""
        self.__appt_type = 0

    def get_client_name(self):
        return self.__client_name

    def set_client_name(self, client_name):
        self.__client_name = client_name

    def get_client_phone(self):
        return self.__client_phone
    
    def set_client_phone(self, client_phone):
        self.__client_phone = client_phone

    def get_appt_type(self):
        return self.__appt_type
    
    def set_appt_type(self, appt_type):
        if 0 <= appt_type < len(self.APPT_TYPE_DESCS):
            self.__appt_type = appt_type
        else:
            print("Invalid Appointment Type")

    def get_day_of_week(self):
        return self.__day_of_week

    def get_start_time_hour(self):
        return self.__start_time_hour
    
    def get_end_time_hour(self):
        return (self.__start_time_hour + 1)

    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(appt_type)

    def cancel(self):
        self.__client_name = None
        self.__client_phone = None
        self.__appt_type = 0 

    def get_appt_type_desc(self):
        return self.APPT_TYPE_DESCS[self.__appt_type]
    
    def format_record(self):
       return f"{self.get_client_name():<15} {self.get_client_phone():<15} {self.get_day_of_week():<15} {self.get_start_time_hour()}:00 - {self.get_end_time_hour()}:00 {self.get_appt_type_desc():>18}"

    def __str__(self):
        return self.format_record()