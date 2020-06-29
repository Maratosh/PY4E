# eXtensible Markup Language - XML
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
''' Often the XML has multiple nodes and we need to write a loop to process all of the nodes. In the following program, we loop through all of the user nodes:'''
import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff> '''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
'''The findall method retrieves a Python list of subtrees that represent the user structures in the XML tree. Then we can write a for loop that looks at 
each of the user nodes, and prints the name and id text elements as well as the x attribute from the user node.'''
'''It is important to include all parent level elements in the findall statement except for the top level element (e.g., users/user). Otherwise, Python will not find 
any desired nodes.'''


#JavaScript Object Notation - JSON
