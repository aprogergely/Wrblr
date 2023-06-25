import pytest
from webscraper import APICaller
from webscraper import ListFromXMLData
from webscraper import ExcelWriter

def testAPICaller():
    arfolyam = APICaller()
    try:
      flowers=arfolyam.make_api_call("https://www.w3schools.com/xml/plant_catalog.xml")
      assert True
    except:
      assert False

def testListFromXMLData():
    arfolyam = APICaller()
    flowers=arfolyam.make_api_call("https://www.w3schools.com/xml/plant_catalog.xml")

    xmldata = ListFromXMLData()
    list=xmldata.CreateList(flowers, "BOTANICAL")
    expected_output = "Aquilegia canadensis"

    actual_output = list[2]

    assert actual_output == expected_output

def testListFromXMLData2():
    flowers='''
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
    xmldata = ListFromXMLData()
    list=xmldata.CreateList(flowers, "BOTANICAL")
    expected_output = "Aquilegia canadensis"

    actual_output = list[2]

    assert actual_output == expected_output

#def testExcelWriter():
#    excel=ExcelWriter()
#    list=("3", "hello", "pingvin", "43edg52")
#    excel.write_data(list)

    #expected_output = True
    #assert actual_output == expected_output