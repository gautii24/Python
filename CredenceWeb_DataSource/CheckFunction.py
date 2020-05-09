import os

path = "D:/FinalFrameWork/CredenceWeb_DataSource/MasterData.xlsx"
start = "CredenceWeb_DataSource/MasterData.xlsx"

relativepath = os.path.relpath(path, start)

print(relativepath)





