import xml.etree.ElementTree as et


def GenerateXML(filename):
    # Start with root element
    root = et.Element("Catalog")

    m1 = et.Element("mobile")
    root.append(m1)

    b1 = et.SubElement(m1, "brand")
    b1.text = "Redmi"
    b2 = et.SubElement(m1, "price")
    b2.text = "6999"

    m2 = et.Element("mobile")
    root.append(m2)

    c1 = et.SubElement(m2, "brand")
    c1.text = "Samsung"
    c2 = et.SubElement(m2, "price")
    c2.text = "9999"

    m3 = et.Element("mobile")
    root.append(m3)

    d1 = et.SubElement(m3, "brand")
    d1.text = "RealMe"
    d2 = et.SubElement(m3, "price")
    d2.text = "11999"

    tree = et.ElementTree(root)

    with open(filename, "wb") as files:
        tree.write(files)


# Driver Code
if __name__ == '__main__':
    GenerateXML("CatalogXML.xml")
