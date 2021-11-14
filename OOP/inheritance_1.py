#inheritance knowledge

class date():
    def date_print(self):
        print("15-06-1996")

class time (date):
    def time_print(self):
        print("07:00:00")


a = time()
a.time_print()
a.date_print()
