# StanfordNLP-Chinese

The Stanford NLP group have released Chinese language parsers, tokenizers, part-of-speech taggers and more for the last few years. These software releases are all done in Java, and while there are python wrappers available, it is often hard to find information on how to set the software to work properly.
I use nltk and langdetect and define simple functions to import easily instead of focusing on setting up the program every time.

First: Java is necessary to run all these programs.

## Install Java Development Kit

https://www.ntu.edu.sg/home/ehchua/programming/howto/JDK_HowTo.html 

To see if previously installed

javac -version

Download Java SE

http://www.oracle.com/technetwork/java/javase/downloads/index.html

## Set up root directory

In my project, I set up my working directory to be

~/Stanford NLP/

Unzip all the following files in this folder.

## Install Stanford NLP Chinese Segmenter

The system requires Java 1.8+ to be installed.

https://nlp.stanford.edu/software/segmenter.shtml

Download Stanford Word Segmenter version 3.8.0

https://nlp.stanford.edu/software/stanford-segmenter-2017-06-09.zip

Unzip at ~/Stanford NLP/
There is a missing file in last versions 2017-06-09 and 2016-10-31, it is supposed to be in the Java PATH after installing anyways, but it is easier to point at it in python manually.
So also download the previous version or 2015-12-09, which has it included, or find it in the Java PATH file.

Then copy 'slf4j-api.jar' and ‘slf4j-simple.jar’ to the newest version root folder, and point to it manually when running.

## Install Stanford NLP Chinese Part-Of-Speech (POS) Tagger

The system requires Java 1.8+ to be installed.

https://nlp.stanford.edu/software/tagger.shtml

Download full Stanford Tagger version 3.8.0

https://nlp.stanford.edu/software/stanford-postagger-full-2017-06-09.zip

Unzip at ~/Stanford NLP/

## Install Stanford NLP Chinese Parser

The system requires Java 1.8+ to be installed.

https://nlp.stanford.edu/software/lex-parser.shtml 

Download Stanford Parser version 3.8.0

https://nlp.stanford.edu/software/stanford-parser-full-2017-06-09.zip 

Unzip at ~/Stanford NLP/

## Python setup environment

After this, place StanfordNLP.py in any folder you like and do:

import os.path
import sys
PersonalLibraries_path = os.path.join(os.path.expanduser('~'), 'PersonalLibraries')
sys.path.append(os.path.abspath(PersonalLibraries_path))
import StanfordNLP

Now we can freely call the methods in this library and segment Chinese text from python.
