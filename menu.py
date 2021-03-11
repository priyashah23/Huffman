from Huffman import *
import time
import os
import sys


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

HH = Huffman()
def menu() -> None:
    """
    A menu system:
    :return:
    """
    options = input(f"Enter an option to begin:\n\n{1}. create codes\n{2}. encode a file\n{3}. decode a file\n\n{0}. to exit\n")
    try:
        options = int(options)
    except:
        pass
        #logging.info("Not an integer")
    if (options == 1) or (options == 2) or (options == 4):
        cls()
        userEncoding(options)
    elif options == 3:
        cls()
        userDecoding()
    else:
        sys.exit(0)

def returnMenu(user) -> None:
    try:
        user = int(user)
    except:
        pass
    if user == 1:
        menu()
    elif user == 0:
        sys.exit(0)
    else:
        print("invalid input")
        menu()

def userEncoding(options: int) -> None:
    filename = input("Enter a filename: ")
    try:
        with open("books/" + filename + ".txt", "r", encoding="utf-8") as text:
            values = freqDictionary(text)
    except:
        print("Unable to read file")
    heap = dict(sorted(values.items(), reverse=True, key=lambda item: item[1]))

    leafNodes = HH.createLeafNodes(heap)
    root = HH.huffmanTree(leafNodes)
    HH.makeCodes(root)

    if options == 1:
        print("Creating codes...")
        printCodes(HH.codes)
        print("Finished Creating Codes")
    else:
        start = time.time()
        HH.createCompressText(filename, root)
        end = time.time()
        print(f"Time taken for compression is: {end-start}")
    returnMenu(input(f"Enter {0} to exit, or {1} to return to main menu \n"))

def userDecoding() -> None:
    filename = input("Enter a filename: ")
    try:
        text = open("output/" + filename + ".bin", "r", encoding="utf-8")
    except:
        print("Unable to read file")
    start=time.time()
    HH.createDecompressText(filename)
    end=time.time()
    print(f"Time to decompress is: {end - start} ")
    returnMenu(input(f"Enter {0} to exit, or {1} to return to main menu"))

def printCodes(codes: dict) -> None:
    for code in codes:
        table = f"| {code} | {codes[code]} |"
        print(table)