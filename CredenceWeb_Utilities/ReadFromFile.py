import configparser
import xlrd


class ReadFromFiles():

    def readFromProp(self, propertyKey):
        PathFile = "../CredenceWeb_DataSource/BrowserEnter.txt"
        self.config = configparser.RawConfigParser()
        self.config.read(PathFile)
        self.value = self.config.get('BROWSER', propertyKey)
        return self.value

    @staticmethod
    def readFromExcel(self, SheetName, rowNum, ColumnNum):
        ExcelPath="../CredenceWeb_DataSource/MasterData.xlsx"
        self.worbook = xlrd.open_workbook(ExcelPath)
        value = self.worbook.sheet_by_name(SheetName).cell(rowNum, ColumnNum).value
        return value

    def countActiveRows(SheetName):
        ExcelPath = "../CredenceWeb_DataSource/MasterData.xlsx"
        worbook = xlrd.open_workbook(ExcelPath)
        maxRowCount = worbook.sheet_by_name(SheetName).nrows
        print(maxRowCount)

    

