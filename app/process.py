import xlrd
import pdb

class XLCrusher(object):

    def __init__(self, fileName):
        self.fileName = fileName

    def process(self):
        output = []
        departments = {'TOTAL': 0}
        current_dept = "uncategorized"
        book = xlrd.open_workbook(self.fileName)
        sh1 = book.sheet_by_index(0)
#        pdb.set_trace()
        for rx in range(1, sh1.nrows):
            if sh1.row(rx)[0].value == "TOTAL":
                break
            if len(sh1.row(rx)[0].value) > 0 and sh1.row(rx+1)[2].value == "Invoice":
                current_department = sh1.row(rx)[0].value
                departments[current_department] = {'TOTAL': 0}
            if sh1.row(rx)[2].value == "Invoice":
                product_str = sh1.row(rx)[5].value
                if not product_str in departments[current_department]:
                    departments[current_department][product_str] = [0, 0]
                departments[current_department][product_str][0] += sh1.row(rx)[6].value
                departments[current_department][product_str][1] += sh1.row(rx)[8].value
                departments[current_department]['TOTAL'] += sh1.row(rx)[8].value
                departments['TOTAL'] += sh1.row(rx)[8].value


        return departments


# xlc = XLCrusher('Monthly_Hawthorne_Valley.xls')
# depts = xlc.process()
