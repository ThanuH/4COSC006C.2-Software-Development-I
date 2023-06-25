def vertical_Histogram(pro,tra,ret,exc,c_List,o_Total):
    """Printing the Vertical Histogram
       Input -  progress_Count,trailer_Count,retriever_Count,excluded_Count
       Output - Vertical Histogram
    """
    print("----------------------------------------------------------------")
    print("Vertical Histogram")
    columns = (("Progress",["*" for i in range(pro)]),("Trailing",["*" for i in range(tra)]),("Retriever",["*" for i in range(ret)]),("Exclude",["*" for i in range(exc)]))
    max_Value = max(c_List)
    #print(max_Value)
    
    for col in columns:
        print(col[0],end = "\t")
    print("")
    for i in range(max_Value):
        for k in range(len(columns)):
            try:
                print("  ",columns[k][1][i], end ="   \t\t")
            except IndexError:
                print("  ", end = "   \t\t")
        print(" ")
    print(o_Total," outcomes in total.")
