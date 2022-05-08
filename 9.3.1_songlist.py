import re

def my_mp3_playlist(file_path):
    #file_path = file_path.replace('\n', '')
    LIST = []
    fileread = open(file_path,"r")
    read = fileread.read()
    file_splitted = read.split("\n")
    for item in file_splitted:
        LIST.append(item.split(";"))
    print(LIST)    
    #readandreplace = read.replace("\n" , "")
    #for line in fileread:
    #    line.replace('\n', '')
    #print(readandreplace)    
    #List = [line.split(',') for line in open(file_path)]
    List =[]
    #List = [line.split(';') for line in readandreplace]
    #print(List)   
    #newlist =  []
    #for x in List:
        #newlist.append(x.replace("\n", ""))
   #List = (List.replace('\n', ''))
    #for i in List:
        #List.str.replace('\n', '')
    #print(List)
    
    
    
   # print(list(map(lambda x:x.strip(),List)))
    #print(newlist)
    #List.replace("\n","")
    #print(List)
    #newlist = []
    #for element in List:
    #    newlist.append(element.strip())
    #print(newlist)
    #fileread = open(file_path,"r")
    #filedata = fileread.read()
    #print(filedata)
    
    #filedata_remove_line = filedata.replace("\n","").split(";")
    #print(filedata_remove_line)
    #filedata_splitted = filedata_remove_line.split(";")
    #print(filedata_splitted)



def main():
    # Call the function func
    my_mp3_playlist("/Users/uriel/python/songlist.txt")
if __name__ == "__main__":
    main()