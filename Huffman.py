from bitstring import BitArray
import pickle

class Node:
    """
    This class contains a Node which is used to contain frequencies, chars and links to other Node objects
    """
    # initalising a Node
    def __init__(self, freq, char=None, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.char = char
    # toString method of a node
    """
    def __str__(self):
        return f'Node left is {self.left}, Node Right is {self.right}, char is {self.char}, freq is {self.freq}'
    """
class Huffman:
    """
    Huffman Class contains the bulk - has decompression, creation of tree and compression
    """
    def __init__(self):
        #Initialises Code
        self.codes = {}

    def getCodes(self):
        return self.codes

    def createLeafNodes(self, d) -> list:
        """
        Creates a list of leafnodes for the priority queue
        :param d: dictionary of character frequencies in text
        :return: a list of nodes with an assigned character and
        """
        LeafNodes = []
        for i in range(len(d)):
            smallValue = d.popitem()
            LeafNodes.append(Node(char=smallValue, freq=smallValue[1]))
        return LeafNodes

    def huffmanTree(self, Lnodes):
        """
        Creates the huffman tree using a min-priority queue
        :param Lnodes: Leaf Nodes which contain frequency and char
        :return: The root which contains the entire Huffman tree
        """
        n = len(Lnodes)
        # Creating a tree using a min-priority queue
        while (n != 1):
            Left = self.findMin(Lnodes)
            Right = self.findMin(Lnodes)
            Z = Node(left=Left, right=Right, freq = Left.freq + Right.freq)
            Lnodes.append(Z)
            n -= 1
        root = Lnodes[0]
        return root

    def findMin(self, Lnodes) -> Node:
        """
        Find the minimum value
        :param Lnodes: An array of leaf nodes
        :return: The minimum number
        """
        MIN = Lnodes[0]

        for node in Lnodes:
            if (node.freq < MIN.freq) and node != MIN:
                MIN = node
        for node in Lnodes:
            if node == MIN:
                Lnodes.remove(node)

        return MIN

    def makeCodes(self, root, empty_string = ""):
        """
        Creates the codes for the Huffman Tree
        :param root:
        :param empty_string:
        :return:
        """
        current_node = root
        if current_node.left == None and current_node.right == None:
            self.codes[current_node.char[0]] = empty_string
        else:
            self.makeCodes(root.left, empty_string + '0')
            self.makeCodes(root.right, empty_string + '1')

    def createCompressText(self, filename, root) -> None:
        """
        This function opens a text and uses the codes created to encode the tree
        it then write the bytes to a bin file
        :return: VOID
        """

        code = self.getCodes()
        temp = []

        with open("books/" + filename + ".txt", "r", encoding="utf-8") as text:
            converted_file = text.read()
            for char in converted_file:
                temp.append(self.codes[char])
            string = "".join(temp)

        binary_string = BitArray(bin=string)
        with open("output/" + filename + ".bin", "wb") as newFile:
            pickle.dump(root, newFile)
            binary_string.tofile(newFile)
        newFile.close()

    def createDecompressText(self, filename: str) -> None:
        """
        Opens a file with the extension .bin and attempts to encode
        according to header file
        :param root: Refers to the root of a generated huffman tree
        :return: VOID
        """
        temp = []
        new_string = ""

        with open("output/" + filename + ".bin", "rb") as compressedText:
            root = pickle.load(compressedText)
            bits = BitArray(compressedText.read())

        current = root
        compressedText.close()
        bits = bits.bin

        for bit in bits:
            if bit == '0':
                current = current.left
            else:
                current = current.right

            if current.left == None and current.right == None: #You have hit a leaf node
                temp.append(current.char[0])
                current = root
        new_string = "".join(temp)


        with open("output/text/" + filename + ".txt", "w", encoding="utf-8") as decompressedText:
            decompressedText.write(new_string)
        decompressedText.close()



# Build frequency dictionary.
def freqDictionary(text) -> dict:
    """
    Frequency dictionary, counts the characters in a .txt file of no. of occurances
    :return: A dictionary containing the frequencies and characters
    """
    frequencyDict = {} #blank dictionary to contain frequency
    total_char = 0
    for line in text: # iterating for each character
        for char in line:
            total_char+=1
            if char in frequencyDict:
                frequencyDict[char] += 1
            else:
                frequencyDict.update({char: 1})
    text.close()
    return frequencyDict