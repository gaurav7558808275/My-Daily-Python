#inheritance knowledge

class date():
    def date_print(self):
        print("15-06-1996")

class time (date):
    def time_print(self):
            time = "07:00:00"
            print("time is %s " %time)
a = time()
a.time_print()
a.date_print()


# using the inheritance technique.
