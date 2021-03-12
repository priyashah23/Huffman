# README

## Introduction
Huffman Compression Algorithm, while simpler than other compressions out there in the market can be quite effective when compressing text files -  ranging from 20 to 90% effective at saving space from the original file (Cormen et. al). This implementation of Huffman compression and decompression in Python has been
able to acheive effective saving percentages ranging from 30 to 88% depending on the file type. This is a console based program that has several menus
allowing the user to select what they would like to do.\

This Includes:
* Creating codes 
* Compressing a text file
* decompressing a text file

## Prerequisities
* Python 3.8 or higher 
* If it has not been installed you can install python [Here](https://www.python.org/)

## Installation
* Python Modules required:
  * Bitstring must be installed `pip install bistring`
  
## Getting Started
Inside the zip file contains several directories. If you locate to /venv/Huffman/books will contain .txt files 
books in English, French and Portuguese respectively. These were obtained by the Gutenberg Project. (Link [Here](https://www.gutenberg.org/)) 
Also in that folder will have three datasets obtained from [Here](http://pizzachili.dcc.uchile.cl/repcorpus.html). Each dataset came from Psuedo-Real, Artificial and Real respectively\
Another location in the file /venv/Huffman/output will contain .bin files for compression and in the /venv/Huffman/output/texts is where .txt files will be outputted during decompression.\
To get started, launch the main python file and a menu will be presented giving you, the user, the options to either view the huffman encoding of a file of your choosing, to compress a file or decompress a file.
If a file is not found, an error will be thrown. If user has selected to compress or decompress - they will also see the time taken. If user has selected the codes they are able to see the codes that were created.

**Note:** that files **must** be in the directories provided and with the same file type

## Author's Note: 

* Apart from testing purposes it is not possible to construct a tree with and compress with a different file. 
This was only done for a very specific test and will not be included in the user interface design. 
  
## Details
Author: Priya Shah\
License: MIT License