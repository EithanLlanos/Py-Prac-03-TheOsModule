import os

# path=input("Enter the path: \n")
# dir=input("Enter the directory: \n")

path="./tree"
dir="python"

def osfun (p,d):
    os.chdir(p)
    p=os.getcwd()
    if d in os.listdir():
        print(os.getcwd()+"\\"+d)
    for i in os.listdir():
        osfun(p+"/"+i,d)

osfun(path,dir)
