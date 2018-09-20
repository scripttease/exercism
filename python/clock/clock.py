class Clock(object):
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        hour = (self.hour + self.minute//60) % 24
        minute = self.minute % 60
        # if len(str(hour)) ==1 and len(str(minute)) == 1: 
        #     return "0%s:0%s" % (hour, minute)
        # if len(str(hour)) ==2 and len(str(minute)) == 1: 
        #     return "%s:0%s" % (hour, minute)
        # if len(str(hour)) ==1 and len(str(minute)) == 2:
        #     return "0%s:%s" % (hour, minute)
        # if len(str(hour)) ==2 and len(str(minute)) == 2:
        
        return "%s:%s" % (pad(hour), pad(minute))

    def __repr__(self):
        pass

    def __eq__(self, other):
        print(self)
        print(other)
        return str(self) == str(other)

    def __add__(self, minutes):
        hour = (self.hour + (self.minute + minutes)//60) % 24
        minute = (self.minute + minutes) % 60
        return "%s:%s" % (pad(hour), pad(minute))

    def __sub__(self, minutes):
        hour = (self.hour + (self.minute - minutes)//60) % 24
        minute = (self.minute - minutes) % 60
        return "%s:%s" % (pad(hour), pad(minute))

def pad(number):
    if number <= 9:
        return "0%s" % (number)
    else:
        return str(number)
