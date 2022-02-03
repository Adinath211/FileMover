def swapFile():
    import shutil  
    source = input("enter the file name:- ")
    destination = input("enter the destination:- ")
    dest=shutil.move(source,destination)
    
swapFile()