import configparser
import openpyxl
import xlrd

class ReadFromText():

    def readFromProp(self):
        PathFile = "D:/FinalFrameWork/CredenceWeb_DataSource/BrowserEnter.txt"
        self.config = configparser.RawConfigParser()
        self.config.read(PathFile)
        self.value = self.config.get('BROWSER', 'Browser')
        return self.value





