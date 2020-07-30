def to_upper_case(input_file, output_file):
    f1 = open(input_file, 'r')
    f2 = open(output_file, 'w')
    f2.write(f1.read().upper())
    f1.close()
    f2.close()

to_upper_case("P09.5A.txt", "P09.5B.txt")