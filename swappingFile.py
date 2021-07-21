def swapFileData():
    file1Input=input("Enter File 1 Name:")
    file2Input=input("Enter File 2 Name:")
    with open(file1Input,"r")as a:
        data_a=a.read()
    with open(file2Input,"w")as a:
        a.write(data_a)    
    print("This Text Is From:"+ file2Input +":"+ data_a)

swapFileData()        
