import pandas as pd
import numpy as np 
from nltk import pos_tag, word_tokenize
import nltk.corpus 
from nltk.corpus import stopwords
from nltk.tag import brill 
from nltk.stem.snowball import SnowballStemmer
import re 
import os
import codecs
import mpld3  
import csv 
import sys
import itertools
del sys.modules['sklearn.__check_build']; 
from sklearn import feature_extraction
from pywsd.lesk import simple_lesk 

#First, each sentence is partitioned into a list of tokens.
#Part-of-speech disambiguation (or tagging).
#Stemming words.
#Find the most appropriate sense for every word in a sentence (Word Sense Disambiguation).
#Finally, compute the similarity of the sentences based on the similarity of the pairs of words.


fil = pd.read_csv("questions_data_for_assignment.csv",delimiter=',')

stops = set(stopwords.words('english'))
######################################################################################################################################
#-----------Getting the two questions and correspondingly storing their ids and questions seperately as well as merging the lists----- 
######################################################################################################################################

ListqId1 = fil ['qid1']
ListqId2 = fil ['qid2']

Listq1 = fil ['question1']
Listq2 = fil ['question2']


#Merging the list 
questionsList	= 	np.r_[Listq1, Listq2] 
qIdList 		=	np.r_[ListqId1, ListqId2]
######################################################################################################################################



        		
#print nltk.word_tokenize(Listq1[0])
 

class QuestionData(): 
	
	#def __init__(self,ids,qid1,qid2,question1,question2): 
	def __init__(self,question1,question2):
		#self.id 		= ids
		#self.qid1 		= qid1
		#self.qid2 		= qid2
		self.question1 	= question1
		self.question2 	= question2
		self.words1 	= []
		self.words1stem	= []
		self.words2 	= []
		self.words2stem = []
		self.answer1	= []
		self.answer2	= []
	#Tokenizing,stemming and tagging the string
	def tagging(self):
		
		if len(self.question1) <=0 or len(self.question2)<=0: 
			return NULL
		else: 
			stemmer1 = SnowballStemmer("english")	
			stemmer2= SnowballStemmer("english")		
			#for self.w in :
	        self.words1 = pos_tag(word_tokenize(self.question1))
	        for i in range(0,len(self.words1)):
	        	#To create a list of lists instead of a read only tuple 
	        	self.words1stem.append([])
	        	self.words1stem[i].append(stemmer1.stem((self.words1[i])[0]))
	        	self.words1stem[i].append((self.words1[i])[1])

	        for word in self.words1stem: 
	        	print word

	        	print (simple_lesk(self.question1, word[0]))
	        #print self.answer1
	        		#if self.w.lower() not in stops:
	        				#print stemmer1.stem(self.w)
	            			#self.words1.append(stemmer.stem(self.w))
	            			#self.words1.append(nltk.pos_tag(self.w))
	            			#temp=stemmer1.stem(self.w)
	            			
	            			#print WORD1[0]
	            			#self.answer1.append(simple_lesk(self.question1,WORD1[0],WORD1[1]))
	            			#answer = simple_lesk
			#self.words1pos=nltk.pos_tag(self.words1)
			#print self.answer1	 
			#words1=stem(words1)
	        for self.w2 in self.question2.split(): 
	        		if self.w2.lower() not in stops: 
	        			#self.words2.append(stemmer2.stem(self.w2))
	        			#self.words2.append(self.w2)
	        			WORD2=nltk.pos_tag(stemmer2.stem(self.w2))


data = QuestionData(Listq1[0],Listq2[0])  
data.tagging()
