f = open("data/precipitations-world.txt", 'r')
precip_data = {}
for line in f:
    if line[0] == '#':
        continue
    else:
        line_data = line.split(',')
        precip_data[int(line_data[0])]=float(line_data[1])
f.close()

def min_Precipitation(data):
    return min(data.values())


def max_Precipitation(data):
    return max(data.values())


def average_Precipitation(data):
    return sum(data.values())//len(data.values())


print('Min: {}'.format(min_Precipitation(precip_data)))
print('Max: {}'.format(max_Precipitation(precip_data)))
print('Avg: {}'.format(average_Precipitation(precip_data)))