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
            wb.save(file)

class APICaller():
    def make_api_call(self, link):
        #params ={"valuta": "eur"}
        #headers = {'Accept': 'application/xml'}
        response = requests.get(link)#, params=params, headers=headers)
        if response.status_code == 200:
            xml_content = response.content
            #return(xml_content)
            root = ET.fromstring(xml_content)
            rate = root.findall("PLANT")
            result=[]
            for x in rate:
                result.append(x.find("BOTANICAL").text)
            return(result)

class IOHandler():
    def read_input(self):
        result = input()
        return result
    
    def write_output(self, output):
        print(output)

class ListFromXMLData():
    def CreateList(self, xml):
        selected_data = ()
        for data_row in xml:
            selected_data.append(data_row)

        return selected_data

        



#valuta=("gbp", "aud", "dkk", "jpy", "cad", "nok", "chf", "sek", "usd", "czk", "pln", "eur", "hrk", "ron", "try")



arfolyam = APICaller()
print(arfolyam.make_api_call("https://www.w3schools.com/xml/plant_catalog.xml"))

#excel=ExcelWriter()
#list=("3", "hello", "pingvin", "43edg52")
#excel.write_data(list)
