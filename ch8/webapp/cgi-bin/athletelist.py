#!/usr/bin/python3

class AthleteList(list):
    def __init__(self,a_name,a_dob = None, a_times = []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]

    def add_time(self,time):
        self.append(time)

    def add_times(self,list_of_times):
        self.extend(list_of_times)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)
