import pytest
from webscraper import APICaller
from webscraper import ListFromXMLData
from webscraper import ExcelWriter

#def testAPICaller():
#    arfolyam = APICaller()
#    flowers=arfolyam.make_api_call("https://www.w3schools.com/xml/plant_catalog.xml")

    #assert actual_output == expected_output

def testListFromXMLData():
    arfolyam = APICaller()
    flowers=arfolyam.make_api_call("https://www.w3schools.com/xml/plant_catalog.xml")

    xmldata = ListFromXMLData()
    list=xmldata.CreateList(flowers)
    expected_output = "Aquilegia canadensis"

    actual_output = list[1]

    assert actual_output == expected_output


#def testExcelWriter():
#    excel=ExcelWriter()
#    list=("3", "hello", "pingvin", "43edg52")
#    excel.write_data(list)

    #expected_output = True
    #assert actual_output == expected_output