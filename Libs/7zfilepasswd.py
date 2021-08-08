import py7zr
import os
def extract():
    passwd=input("password:")
    rarPath=input("rar file path:")
    with py7zr.SevenZipFile(rarPath, mode='r', password=passwd) as z:
        z.extractall()

def compress():
    name=input("nombre del .7z:")
    passwd=input("Set password:")
    path=input("archivo a comprimir(path):")
    with py7zr.SevenZipFile(name, 'w', password=passwd) as archive:
        archive.writeall(path, os.path.basename(path))

whatToDo = input("What do you want to do?(compress/extract): ")

if __name__ == "__main__":
    if whatToDo=="extract":
        extract()
    elif whatToDo=="compress":
        compress()
