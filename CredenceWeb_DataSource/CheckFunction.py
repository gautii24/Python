from CredenceWeb_Utilities.ReadFromText import ReadFromText

def check(self):
    read = ReadFromText()

    print(read.getDataFromExcel(self))