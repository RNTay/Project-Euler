#!/usr/bin/env python3

import datetime

this_day = datetime.date(1901, 1, 1)
count_sundays = 0
while this_day != datetime.date(2001, 1, 1):
    if this_day.day == 1:
        if this_day.isoweekday() == 7:
            count_sundays += 1
    this_day += datetime.timedelta(days=1)
print(count_sundays)
