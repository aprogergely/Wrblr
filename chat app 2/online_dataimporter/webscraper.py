import requests
import xml.etree.ElementTree as ET
import openpyxl

class ExcelWriter():
    def write_data(self, list):
        path = "C:/Users/Acer/Documents/GitHub/Wrblr/chat app 2/online_dataimporter"
        file = "Excel.xlsx"
        wb = openpyxl.load_workbook(str(path) +'/' + str(file))
        sheet = wb.active
        for line in list:
            empty_cell = sheet.max_row + 1
            sheet.cell(row=empty_cell, column=1).value = line
            wb.save(path+"/"+file)
            #print(str(line)+"saved to" +str(empty_cell))

class APICaller():
    def make_api_call(self, link):
        #params ={"valuta": "eur"}
        #headers = {'Accept': 'application/xml'}
        response = requests.get(link)#, params=params, headers=headers)
        if response.status_code == 200:
            xml_content = response.content
            return(xml_content)

class IOHandler():
    def read_input(self):
        result = input()
        return result
    
    def write_output(self, output):
        print(output)

class ListFromXMLData():
    def CreateList(self, xml):
        root = ET.fromstring(xml)
        rate = root.findall("PLANT")
        result=[]
        for x in rate:
            result.append(x.find("BOTANICAL").text)
        return(result)
