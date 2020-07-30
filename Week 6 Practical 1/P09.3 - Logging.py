def save_to_log(entry, logfile):
    f = open(logfile, 'a')
    f.write(entry+'\n')
    f.close()

save_to_log("Entry 1", "P09.3A.txt")
save_to_log("Entry 2", "P09.3A.txt")