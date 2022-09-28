import csv
import PyPDF2
import tabula
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join
from pathlib import Path

# TODO: 1. Read pdf file or convert to CSV
#  2. Search in file for VO number and add to list
#  3. Search in file for serial number, 17B, 18B or 19B
#  4. Subtract the SKU number from the number and add to list#

class AutomateReadPdf:
    def __init__(self):
        self.serialnum = []
        self.lst17B = []
        self.lst18B = []
        self.lst19B = []
        self.lstVO = []

        # Substrings
        self.serial17B = '17B'
        self.serial18B = '18B'
        self.serial19B = '19B'
        self.orderNumber = 'VO'

        # TODO: Add this maybe to __init__ variables
        # , lst17B=None, lst18B=None, lst19B=None, lstVO=None
        # if lst17B is None:
        #     self.lst17B = []
        # if lst18B is None:
        #     self.lst18B = []
        # if lst19B is None:
        #     self.lst19B = []
        # if lstVO is None:
        #     self.lstVO = []

# TODO: Scrath code. Can possibly be removed.

    #
    # self.pdf_folder = Path('/Users/tom/Desktop/testDocs/PDF')
    # self.CSV_folder = Path('/Users/tom/Desktop/testDocs/CSV')
    # for pdf in self.pdf_folder:
    #     while self.index < len(pdf):
    #
    #
    # onlyfiles = [f for f in listdir('/Users/tom/Desktop/testDocs') if isfile(join('/Users/tom/Desktop/testDocs', f))]
    # for file in onlyfiles:
    #     while self.index < len(file):

    # self.object = PyPDF2.PdfFileReader('/Users/tom/Desktop/testDocs/21VO023504.pdf')
    # self.df = tabula.read_pdf('/Users/tom/Desktop/testDocs/21VO023504.pdf', pages='all')
    # self.df_csv = tabula.convert_into('/Users/tom/Desktop/testDocs/21VO023504.pdf', 'test.csv', output_format="csv", pages='all')

    def readPdf(self):
        cols = ['VO number', '17B', '18B', '19B']
        df = pd.DataFrame()

        self.index = 0
        self.file = open('/Users/tom/Desktop/testDocs/PDF/21VO023504.pdf', 'rb')
        self.readPDF = PyPDF2.PdfFileReader(self.file)
        self.totalpages = self.readPDF.numPages
        print(self.totalpages)

        self.fileCSV = open('/Users/tom/PycharmProjects/automate_logistics/test.csv')

        while self.index < self.totalpages:
            # TODO: Iterate over pages in PDF file.
            # TODO: Write from the PDF files in the folder to the CSV file.
            tabula.convert_into('/Users/tom/Desktop/testDocs/PDF/21VO023504.pdf', 'test.csv',
                                output_format="csv", pages=self.index)
            # Read from CSV
            with open('test.csv', newline='') as csvfile:
                csvreader = csv.reader(self.fileCSV)
                for row in csvreader:  # Read every row
                    for x in row:
                        self.serialSplit = x.split(" ")  # Split on str level in list
                        self.testString =  ' '.join(self.serialSplit)  # Make a string
                        if self.serial17B in self.testString:
                            for x in self.serialSplit:
                                if self.serial17B in x:
                                    self.lst17B.append(x)
                        elif self.serial18B in self.testString:
                            for x in self.serialSplit:
                                if self.serial18B in x:
                                    self.lst18B.append(x)
                        elif self.serial19B in self.testString:
                            for x in self.serialSplit:
                                if self.serial19B in x:
                                    self.lst19B.append(x)
                        elif self.orderNumber in self.testString:
                            for x in self.serialSplit:
                                if self.orderNumber in x:
                                    self.lstVO.append(x)
                        else:
                            pass

            self.s17B = []
            self.s18B = []
            self.s19B = []
            self.VO = []
            self.serialNumbers = []

        # def extractSerial(self):
            for x in self.lst17B:
                begin17B = x.index(self.serial17B)
                end17B = x.index(self.serial17B) + 8
                self.s17B.append(x[begin17B:end17B])
                self.serialNumbers.append(x[begin17B:end17B])
            for x in self.lst18B:
                begin18B = x.index(self.serial18B)
                end18B = x.index(self.serial18B) + 8
                self.s18B.append(x[begin18B:end18B])
                self.serialNumbers.append(x[begin18B:end18B])
            for x in self.lst19B:
                begin19B = x.index(self.serial19B)
                end19B = x.index(self.serial19B) + 8
                self.s19B.append(x[begin19B:end19B])
                self.serialNumbers.append(x[begin19B:end19B])
            for x in self.lstVO:
                beginVO = x.index(self.orderNumber) - 2
                endVO = x.index(self.orderNumber) + 8
                self.VO.append(x[beginVO:endVO])
                self.serialNumbers.append(x[beginVO:endVO])

            # def toCsv(self):
            if len(self.s17B) == 0:
                self.s17B.append('-')
            if len(self.s18B) == 0:
                self.s18B.append('-')
            if len(self.s19B) == 0:
                self.s19B.append('-')
            if len(self.VO) == 0:
                self.VO.append('-')

            raw_data = {
                'VO Number': [self.VO],
                '17B': [self.s17B],
                '18B': [self.s18B],
                '19B': [self.s19B]
                        }

            # create second DataFrame to which the data is added
            df2 = pd.DataFrame(raw_data)
            df = df.append(df2)
            df.to_csv('Orderdocument.csv')
            print(f'This is df2{df2}')

            self.index += 1
            continue
