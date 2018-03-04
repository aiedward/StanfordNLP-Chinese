#-*- coding: utf-8 -*-
#!python3

import os.path
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
from nltk.tag import StanfordPOSTagger
from nltk.parse.stanford import StanfordParser
from langdetect import detect
import langdetect
import nltk

#########################################
########## Word Segmenter  ##############
#########################################

# Setup

def Segmenter(segmenter_folder_name='',  
		segmenter_jarname = '',
		segmenter_folder='',  
		segmenter_jarpath='', 
		segmenter_corpora='', 
		segmenter_model='', 
		segmenter_dictpath='', 
		segmenter_slfpath=''):
	###
	default_segmenter_folder_name='stanford-segmenter-2017-06-09'
	if len(segmenter_folder_name)==0:
		segmenter_folder_name = default_segmenter_folder_name
	###
	default_segmenter_jarname = 'stanford-segmenter-3.8.0.jar'
	if len(segmenter_jarname) == 0:
		segmenter_jarname = default_segmenter_jarname
	###
	default_segmenter_folder = os.path.join(os.path.expanduser('~'), 'Stanford NLP', segmenter_folder_name)
	if len(segmenter_folder)==0:
		segmenter_folder = default_segmenter_folder
	###
	default_segmenter_jarpath = os.path.join(segmenter_folder, segmenter_jarname)
	if len(segmenter_jarpath) == 0:
		segmenter_jarpath = default_segmenter_jarpath
	###
	default_segmenter_corpora = os.path.join(segmenter_folder, 'data')
	if len(segmenter_corpora) == 0:
		segmenter_corpora = default_segmenter_corpora
	###
	default_segmenter_model = os.path.join(segmenter_folder, 'data', 'pku.gz')
	if len(segmenter_model) == 0:
		segmenter_model = default_segmenter_model
	###
	default_segmenter_dictpath = os.path.join(segmenter_folder, 'data', 'dict-chris6.ser.gz')
	if len(segmenter_dictpath) == 0:
		segmenter_dictpath = default_segmenter_dictpath
	###
	default_segmenter_slfpath = os.path.join(segmenter_folder, 'slf4j-api.jar')
	if len(segmenter_slfpath) == 0:
		segmenter_slfpath = default_segmenter_slfpath
	###
	nltk.internals.config_java("")
	######
	segmenter = StanfordSegmenter(java_class="edu.stanford.nlp.ie.crf.CRFClassifier", path_to_jar=segmenter_jarpath, path_to_sihan_corpora_dict=segmenter_corpora, path_to_model=segmenter_model, path_to_dict=segmenter_dictpath, path_to_slf4j=segmenter_slfpath)
	# segmenter.default_config('zh')
	######
	return segmenter

# Methods

#Grabs a chinese string and returns as list of words.
def Segment(segmenter, text, tolist=True):
	words=[]
	if text!='':
		try:
		    lang = detect(text)
		except langdetect.lang_detect_exception.LangDetectException:
			lang = "undetermined"
		if (lang == "zh-cn"): #If text is chinese segment, else leave it
			segmented = segmenter.segment(text)
		else:
			segmented = text
		words=segmented.split()
	else:
		segmented = text
	if tolist:
		return words #list
	else:
		return segmented

#########################################
########### POS Tagger ##################
#########################################

# Setup

def POSTagger(postag_folder_name='', 
		postag_folder='', 
		postag_model='', 
		postag_jarpath=''):
	###
	# default_postag_folder_name = 'stanford-postagger-full-2015-12-09'
	default_postag_folder_name = 'stanford-postagger-full-2017-06-09'
	if len(postag_folder_name)==0:
		postag_folder_name = default_postag_folder_name
	###
	default_postag_folder = os.path.join(os.path.expanduser('~'), 'Stanford NLP', postag_folder_name)
	if len(postag_folder)==0:
		postag_folder = default_postag_folder
	###
	default_postag_model = os.path.join(postag_folder,'models', 'chinese-distsim.tagger')
	if len(postag_model)==0:
		postag_model = default_postag_model
	###
	default_postag_jarpath = os.path.join(postag_folder,'stanford-postagger.jar')
	if len(postag_jarpath)==0:
		postag_jarpath = default_postag_jarpath
	###
	tagger = StanfordPOSTagger(postag_model, postag_jarpath)
	###
	return tagger

# Methods

def POSTag(tagger, segmented):
	post = [tuple(i[1].split('#')) for i in tagger.tag(segmented.split())]
	return post

def printPOST(post):
	print "\n".join([i[0] + " " + i[1] for i in post])

#########################################
############## Parser ###################
#########################################

# Setup

def Parser(parser_folder_name='',
		parser_folder='',
		parser_model_name='',
		parser_model_path='',
		parser_jarpath=''):
	###
	default_parser_folder_name = 'stanford-parser-full-2017-06-09'
	if len(parser_folder_name)==0:
		parser_folder_name = default_parser_folder_name
	###
	default_parser_folder = os.path.join(os.path.expanduser('~'), 'Stanford NLP', parser_folder_name)
	if len(parser_folder)==0:
		parser_folder = default_parser_folder
	###
	if len(parser_model_path)==0:
		default_parser_model_name = 'stanford-chinese-corenlp-2017-06-09-models.jar'
		if len(parser_model_name)==0:
			parser_model_name = default_parser_model_name
		parser_model = os.path.join(os.path.expanduser('~'), 'Stanford NLP', 'models', parser_model_name)
	else:
		parser_model = parser_model_path
	###
	default_parser_jarpath = os.path.join(parser_folder,'stanford-parser.jar')
	if len(parser_jarpath)==0:
		parser_jarpath = default_parser_jarpath
	###
	parser=StanfordParser(path_to_jar=parser_jarpath, path_to_models_jar=parser_model)
	return parser

# methods

def parsing_examples(parser):
	parser.raw_parse(sentence, verbose=False)
 # |      Use StanfordParser to parse a sentence. Takes a sentence as a string;
 # |      before parsing, it will be automatically tokenized and tagged by
 # |      the Stanford Parser.
 # |
 # |      :param sentence: Input sentence to parse
 # |      :type sentence: str
 # |      :rtype: iter(Tree)
 
 	parser.raw_parse_sents(sentences, verbose=False)
 # |      Use StanfordParser to parse multiple sentences. Takes multiple sentences as a
 # |      list of strings.
 # |      Each sentence will be automatically tokenized and tagged by the Stanford Parser.
 # |      :param sentences: Input sentences to parse
 # |      :type sentences: list(str)
 # |      :rtype: iter(iter(Tree))
	parser.tagged_parse(sentence, verbose=False)
 # |      Use StanfordParser to parse a sentence. Takes a sentence as a list of
 # |      (word, tag) tuples; the sentence must have already been tokenized and
 # |      tagged.
 # |
 # |      :param sentence: Input sentence to parse
 # |      :type sentence: list(tuple(str, str))
 # |      :rtype: iter(Tree)
 # |
 	parser.tagged_parse_sents(sentences, verbose=False)
 # |      Use StanfordParser to parse multiple sentences. Takes multiple sentences
 # |      where each sentence is a list of (word, tag) tuples.
 # |      The sentences must have already been tokenized and tagged.
 # |
 # |      :param sentences: Input sentences to parse
 # |      :type sentences: list(list(tuple(str, str)))
 # |      :rtype: iter(iter(Tree))



#########################################
#########################################
#########################################

if __name__ == "__main__":
    pass