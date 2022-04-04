import sys 
with open(sys.argv[1], 'rt') as f:
    data = f.read()  #storing f.read() in a variable called data so it is more accessable
print (data)

#checking that I have saved the dataset correcly and checking if i can read it in from the command line
