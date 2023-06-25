def file_Write(list):
    print("----------------------------------------------------------------")
    count = 0
    file_W = open("textfile.txt","a")
    for i in list:
        file_W.write(str(i))
        file_W.write(" ")
        count += 1
        if count%4 == 0:
            file_W.write("\n")
    file_W.close()

