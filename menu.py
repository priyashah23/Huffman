from Huffman import *
import time
import os
import sys

def cls():
    """
    Clears screen depending on operating system
    :return: None
    """
    os.system('cls' if os.name=='nt' else 'clear')

HH = Huffman()
def menu() -> None:
    """
    A menu system giving user the options
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
    """
    Menu so the user can choose whether to return to menu or exit
    :param user: contains an integer that indicates users choice
    :return:
    """
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
    """
    User menu for both encoding and printout out the codes
    :param options: Keep track of whether user wanted to compress or not
    :return:
    """
    filename = input("Enter a filename: ")
    try: #If user fails to import file then it will let user know
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
    """
    Menu for when the user has selected to decode
    :return: None
    """
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
    """
    Prints codes to the console
    :param codes: Dictionary of codes that have been created via the huffman tree
    :return: None
    """
    for code in codes:
        table = f"| {code} | {codes[code]} |"
        print(table)