CITIES = ["Ottawa", "Victoria", "Edmonton", "Winnipeg", "Toronto", "Halifax", "St. John's"]

ottawa_time = int(input())
time = []

time.append(ottawa_time)

loop_count = 0

modifier = -300

while loop_count < 5:

    new_time = ottawa_time + modifier

    time.append(new_time)

    modifier += 100

    loop_count += 1

nl_time = ottawa_time + 130


if int(str(nl_time)[len(str(nl_time))- 2:len(str(nl_time))]) > 59:

    nl_time += 100

    nl_time -= 60

time.append(nl_time)

for x in range(0, len(time)):

    if time[x] > 2359:

        time[x] -= 2400

for x in range(0, len(time)):

    if time[x] < 0:

        time[x] += 2400

for x in range(0, len(time)):

    print("{time} in {city}".format(time=time[x], city=CITIES[x]))
