from webscraper import *

# returns the xml content in the "flowers" variable
arfolyam = APICaller()
flowers=arfolyam.make_api_call("https://www.w3schools.com/xml/plant_catalog.xml")

headers = ['COMMON', 'BOTANICAL', 'ZONE', 'LIGHT', 'PRICE', 'AVAILABILITY']

xmldata = ListFromXMLData()

for i in headers:
    list=xmldata.CreateList(flowers, i)

    writer = ExcelWriter()
    writer.write_data(list)