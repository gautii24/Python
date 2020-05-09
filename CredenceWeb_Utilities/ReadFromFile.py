import configparser
import xlrd


class ReadFromFiles():

    @staticmethod
    def readFromProp(self, propertyKey):
        PathFile = "D:/FinalFrameWork/CredenceWeb_DataSource/MasterData.xlsx"
        self.config = configparser.RawConfigParser()
        self.config.read(PathFile)
        self.value = self.config.get('BROWSER', propertyKey)
        return self.value

    @staticmethod
    def readFromExcel(self, SheetName, rowNum, ColumnNum):
        excelPath = "..//CredenceWeb_DataSource//MasterData.xlsx"
        worbook = xlrd.open_workbook(excelPath)
        value = worbook.sheet_by_name(SheetName).cell_value(rowNum, ColumnNum)
        return value

    @staticmethod
    def countActiveRows(self, SheetName):
        excelPath = "..//CredenceWeb_DataSource//MasterData.xlsx"
        worbook = xlrd.open_workbook(excelPath)
        maxRowCount = worbook.sheet_by_name(SheetName).nrows
        return maxRowCount

    

