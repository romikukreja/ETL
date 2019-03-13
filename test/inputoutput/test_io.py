from main.inputoutput.io import inc,unzip_file
import os

def test_answer():
    assert inc(3) == 5

def test_unzip_file():
    fromPath=r"test\data\Desktop.zip"
    toPath=r"test\data\target"
    curDir=os.getcwd()
    fromPath=os.path.join(str(curDir),str(fromPath))
    toPath=os.path.join(str(curDir),str(toPath))
    assert unzip_file(fromPath,toPath) == 1