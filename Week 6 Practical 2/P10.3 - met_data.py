try:
    f = open("data/aberporth_meteorological_data.txt", 'r')
except (FileNotFoundError):
    raise Exception("File Path not Found")
else:

    met_data = []

    for line in f:
        if line[0].isalpha():
            continue
        else:
            data = line.split(',')
            met_data.append([data[0], data[4], data[5], data[6][:-1]])
    f.close()

    total_af = {}
    total_rain = {}
    total_sun = {}

    for month in met_data:
        if month[0] in total_af.keys():
            total_af[month[0]] += float(month[1])
            total_rain[month[0]] += float(month[2])
            total_sun[month[0]] += float(month[3])
        else:
            total_af[month[0]] = float(month[1])
            total_rain[month[0]] = float(month[2])
            total_sun[month[0]] = float(month[3])

    f = open("total_data.csv", "a")

    for year in total_af.keys():
        f.write("{0}, {1}, {2}, {3}\n".format(int(year), round(total_af[year], 1), round(total_rain[year], 1), round(total_sun[year], 1)))
    f.close()


