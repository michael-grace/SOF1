def extract_data(file):
    """Extracts data from file into dictionary

    Args
        file: String - the file path

    Returns
        precip_data: Dictionary - all the extracted data

    Throws
        FileNotFoundError
    """
    try:
        f = open(file, 'r')
    
    except (FileNotFoundError):
        raise Exception("File Path Not Found")

    else:
        precip_data = {}
        for line in f:
            if line[0] == '#':
                continue
            else:
                line_data = line.split(',')
                precip_data[int(line_data[0])]=float(line_data[1])
        f.close()
        return precip_data
    

europe_data = extract_data("data/precipitations-Europe.txt")
america_data = extract_data("data/precipitations-NAmerica.txt")
world_data = extract_data("data/precipitations-world.txt")

combined_data = {}

f = open("precipitations_records.txt", 'a')
for key in europe_data.keys():
    output = "{0}, {1}, {2}, {3}\n".format(key, europe_data[key], america_data[key], world_data[key])
    f.write(output)

f.close()
