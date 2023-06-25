def list_Output(list):
    count = 0
    print("----------------------------------------------------------------")
    for i in list:
        print(i,end = " ")
        count += 1
        if count%4 == 0:
            print("\n")
