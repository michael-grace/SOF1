def save_list2file(sentences, filename):
    f = open(filename, 'a')
    for elem in sentences:
        f.write(elem+"\n")
    f.close()

save_list2file(["hello", "next sentence", "final sentence"], "P09.2A.txt")


