import xml.etree.ElementTree as ET
tree = ET.parse('countries.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

for child in root:
    print(" Tag:{0}, Country:{1}".format(child.tag, child.attrib))

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name,rank)

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated','yes')

for year in root.iter('year'):
    new_year = year.text[2:]
    year.text = str(new_year)
    year.set('updated','yes')

tree.write('output.xml')