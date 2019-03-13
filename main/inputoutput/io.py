from zipfile import ZipFile
def inc(num):
    return num+2

def unzip_file(fromPath,toPath):
    file=ZipFile(fromPath,'r')
    file.extractall(toPath)
    file.close()
    return 1