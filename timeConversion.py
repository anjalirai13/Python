def timeConversion(t):
    converted_time = ''
    if t[:2] == '12':
        if t[-2:] == 'AM':
            converted_time = "00"+t[2:-2]
        elif t[-2:] == 'PM':
            converted_time = t[:-2]
    elif t[-2:] == 'PM':
        converted_time = str(int(t[:2])+12)+t[2:-2]
    else:
        converted_time = t[:-2]
    return converted_time

t = '07:05:45AM'
t = '12:05:45AM'
t = '12:05:45PM'
print(timeConversion(t))