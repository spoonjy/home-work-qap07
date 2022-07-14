import xml.etree.ElementTree as ET


def author_book(name_author):
    tree = ET.parse('E:/Видео/py_projects/first/HomeWork/Lesson26/library (1).xml')
    root = tree.getroot()
    for child in root:
        for author in child:
            if not f'{name_author}' in author.text:
                text = "None"
            else:
                text = author.text
                print(f'{child.tag}{child.attrib} => Author: {text}')


def prices_book(price_book):
    tree = ET.parse('E:/Видео/py_projects/first/HomeWork/Lesson26/library (1).xml')
    root = tree.getroot()
    for book in root:
        for price in book:
            if not f'{price_book}' in price.text:
                text = None
            else:
                text = price.text
                print(f'{book.tag}{book.attrib} => Price: {text}')


def title_book(title_name: str):
    tree = ET.parse('E:/Видео/py_projects/first/HomeWork/Lesson26/library (1).xml')
    root = tree.getroot()
    for book in root:
        for title in book:
            if not f'{title_name}' in title.text:
                text = None
            else:
                text = title.text
                print(f'{book.tag}{book.attrib} => Title: {text}')


def description_book(description_name: str):
    tree = ET.parse('E:/Видео/py_projects/first/HomeWork/Lesson26/library (1).xml')
    root = tree.getroot()
    for book in root:
        for description in book:
            if not f'{description_name}' in description.text:
                text = None
            else:
                text = description.text
                print(f'{book.tag}{book.attrib} => Description: {text}')


if __name__ == "__main__":
    author_book('Matthew')
    prices_book(4)
    title_book('XML De')
    description_book('A former architect')
