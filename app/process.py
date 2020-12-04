import xlrd
import pdb

class XLCrusher(object):

    def __init__(self, fileName):
        self.fileName = fileName

    def process(self):
        output = []
        products = {}
        departments = {}
        book = xlrd.open_workbook(self.fileName)
        sh1 = book.sheet_by_index(0)
#        pdb.set_trace()
        for rx in range(1, sh1.nrows):
            if sh1.row(rx)[2].value == "Invoice":
                product_str = sh1.row(rx)[5].value
                if not product_str in products:
                    products[product_str] = [0, 0]
                products[product_str][0] += sh1.row(rx)[6].value
                products[product_str][1] += sh1.row(rx)[8].value

        return products


# xlc = XLCrusher('Monthly_Hawthorne_Valley.xls')
# products = xlc.process()
