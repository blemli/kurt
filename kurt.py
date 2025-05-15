#!/usr/bin/env python3

from cashctrl import Client
from icecream import ic
import xml.etree.ElementTree as ET


number_types = ["phoneWork", "phonePrivate", "mobileWork", "mobilePrivate"]

# Create the root element for the XML
root = ET.Element("ProblemliIPPhoneDirectory")

cc = Client()
people = cc.person.list(sort="id", dir="ASC")["data"]
directory = []

for person in people:
    numbers = []
    for number_type in number_types:
        if person[number_type] is not None:
            numbers.append(person[number_type])
    if len(numbers) > 0:
        entry = ET.Element("DirectoryEntry")
        name_element = ET.SubElement(entry, "Name")
        name_element.text = person["name"]

        for number in numbers:
            telephone_element = ET.SubElement(entry, "Telephone")
            telephone_element.text = number.replace(" ", "")

        directory.append(entry)

# Append the DirectoryEntry elements to the root element
root.extend(directory)

# Create an ElementTree object
tree = ET.ElementTree(root)

# Write the XML to a file or print it
tree.write("phonebook.xml", xml_declaration=True, encoding="utf-8")
