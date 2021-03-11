import bitarray
from Huffman import *
import time


#Get user to import text file


def main():
    # Get user to input a file
    try:
        text = open("books/" + "world_leaders.txt", "r", encoding="utf-8")
    except:
        print("Unable to read file")

    values = freqDictionary(text)

    # Makes heap
    heap = dict(sorted(values.items(), reverse=True, key=lambda item: item[1]))
    #Creates huffman tree and codes
    HH = Huffman()
    leafNodes = HH.createLeafNodes(heap)
    root = HH.huffmanTree(leafNodes)
    HH.makeCodes(root)
    # Calls to compress text
    HH.createCompressText(text)
    #Calls to decompress text
    HH.createDecompressText(root)
    #print(root)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)