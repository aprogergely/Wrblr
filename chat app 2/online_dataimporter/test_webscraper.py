import pytest
from webscraper import APICaller
from webscraper import ListFromXMLData
from webscraper import ExcelWriterTestable
import openpyxl
import os

def testAPICaller():
    arfolyam = APICaller()
    try:
      flowers=arfolyam.make_api_call("https://www.w3schools.com/xml/plant_catalog.xml")
      assert True
    except:
      assert False



def APICallerTest():
   flowers ='''
    <CATALOG>
      <PLANT>
        <COMMON>Bloodroot</COMMON>
        <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
        <ZONE>4</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$2.44</PRICE>
        <AVAILABILITY>031599</AVAILABILITY>
      </PLANT>
      <PLANT>
        <COMMON>Columbine</COMMON>
        <BOTANICAL>Aquilegia canadensis</BOTANICAL>
        <ZONE>3</ZONE>
        <LIGHT>Mostly Shady</LIGHT>
        <PRICE>$9.37</PRICE>
        <AVAILABILITY>030699</AVAILABILITY>
      </PLANT>
    </CATALOG>
    '''
   return flowers



def testListFromXMLData():
    arfolyam = APICaller()
    flowers=arfolyam.make_api_call("https://www.w3schools.com/xml/plant_catalog.xml")

    xmldata = ListFromXMLData()
    list=xmldata.CreateList(flowers, "BOTANICAL")
    expected_output = "Aquilegia canadensis"

    actual_output = list[2]

    assert actual_output == expected_output




def testListFromXMLData2():
    flowers=APICallerTest()
    xmldata = ListFromXMLData()
    list=xmldata.CreateList(flowers, "BOTANICAL")
    expected_output = "Aquilegia canadensis"

    actual_output = list[2]

    assert actual_output == expected_output




@pytest.mark.parametrize('path' , ['C:/Users/Acer/Documents/GitHub/Wrblr/chat app 2/online_dataimporter'])
@pytest.mark.parametrize('backup_file' , ['Excel_backup.xlsx'])
@pytest.mark.parametrize('file' , ['Excel.xlsx'])
def testExcelWriter(path, file, backup_file):
    wb = openpyxl.load_workbook(str(path) +'/' + str(file))
    wb.save(str(path) +'/' + str(backup_file))
    wb.close()

    excel=ExcelWriterTestable()
    list=("BOTANICAL", "hello", "pingvin", "43edg52")
    excel.write_data(list, path, backup_file)

    wb = openpyxl.load_workbook(str(path) +'/' + str(backup_file))
    sheet = wb.active

    actual_output=sheet.cell(row=2, column=2).value
    expected_output = "hello"

    os.remove(str(path) +'/' + str(backup_file))
    assert actual_output == expected_output