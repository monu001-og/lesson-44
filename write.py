#write in file using with()function
with open('Codingal.txt','w')as file:
    file.write("Hi I am Penguin and I am 1 yr old")
file.close()

#split file into words
with open('Codingal.txt','r') as file:
    data=file.readlines()
    print("words is this files are .....")
    for lines in data:
        word=lines.split()
        print(word)
        file.close()
