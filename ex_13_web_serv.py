# Parsing XML
import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +79179307997
    </phone>
    <email hide="yes" />
</person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

''' Calling fromstring converts the string representation of the XML into a “tree” of XML elements. When the XML is in a tree,
we have a series of methods we can call to extract portions of data from the XML string. The find function searches through the XML tree 
and retrieves the element that matches the specified tag '''
'''Using an XML parser such as ElementTree has the advantage that while the XML in this example is quite simple, it turns out there are many rules 
regarding valid XML, and using ElementTree allows us to extract data from XML without worrying about the rules of XML syntax.'''

# Looping through nodes
