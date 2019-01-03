#!/usr/bin/env python3

import datetime
import time as t
import sys

class Guard(object):
    def __init__(self, start, message):
        self.start = start
        self.message = message.split(" ")[1]
        self.times_asleep = []
        self.total_time_asleep = None

    def falls_asleep(self, time):
        self.fell_asleep = self._datetime(time)

    def wakes_up(self, time):
        self.wake_up = self._datetime(time)
        self.time_asleep = self.wake_up - self.fell_asleep
        self.times_asleep.append((self.time_asleep, self.wake_up, self.fell_asleep))

    def _datetime(self, time):
        return datetime.datetime.strptime(time.strip("[]"), "%Y-%m-%d %H:%M")

    def sort_asleep(self):
        self.times_asleep.sort(key=lambda x: x[0], reverse=True)
        i = None
        for x in self.times_asleep:
            if i == None:
                i = x[0]
                continue
            i = i + x[0]
        self.total_time_asleep = i

def most_common(array):
    return max(set(array), key=array.count)

with open("./input.txt", "r") as f:
    lines = [x.strip("\r\n") for x in f.readlines()]
    lines.sort(key=lambda x: datetime.datetime.strptime(x.split("]")[0].strip("["), "%Y-%m-%d %H:%M"))
    for line in lines:
        print(line)

    g = None
    guards = []
    for line in lines:
        time = ' '.join(line.split(" ")[:2])
        message = ' '.join(line.split(" ")[2:])
        if "Guard" in message:
            already = [x for x in guards if x.message == message.split(" ")[1]]
            if already:
                if g and g.times_asleep:
                    g.sort_asleep()
                    guards.append(g)
                g = already[0]
            else:
                if g and g.times_asleep:
                    g.sort_asleep()
                    guards.append(g)
                g = Guard(time, message)
        elif "falls asleep" in message:
            g.falls_asleep(time)
        elif "wakes up" in message:
            g.wakes_up(time)
        elif g == None:
            raise Exception("Guard is None")

    guards.sort(key=lambda x: x.total_time_asleep)
    # Minutes is a datetime object
    minutes = []
    for i in guards[-1].times_asleep:
        delta = i[1] - i[2]
        for k in range(delta.seconds):
            minutes.append((i[1] + datetime.timedelta(k)))
    print(most_common([x.minute for x in minutes]))
    for minute in minutes:
        print(minute)
