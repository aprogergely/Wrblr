from webscraper import *

# returns the xml content in the "flowers" variable
arfolyam = APICaller()
flowers=arfolyam.make_api_call("http://api.napiarfolyam.hu/?bank=kh&valutanem=valuta")

headers = ['bank', 'datum', 'penznem', 'vetel', 'eladas']

xmldata = ListFromXMLData()

for i in headers:
    list=xmldata.CreateList(flowers, i)

    writer = ExcelWriter()
    writer.write_data(list)