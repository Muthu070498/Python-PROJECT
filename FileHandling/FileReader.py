def read():
   file= open("E:\MuthuKumar\Gt\Python\javaPython.txt",'r')
   print(file.read())



def write():
    file = open("E:\MuthuKumar\Gt\Python\javaPython.txt", 'w')
    file.write('Muthu')



import  os

# os.remove('E:\MuthuKumar\Gt\Python\javaPython.txt')

# pickling and unpickling

import  pickle

def pickling():
    file=open('Bat.dat','wb')
    lst=[10,20.30,40,50]
    pickle.dump(lst,file)
    file.close()
pickling()
def unpickling():
    try:
        file = open('binary.dat', 'rb')
        data = pickle.load(file)
        print(data)
    except:
        file.close()
unpickling()


