import csv 
import pandas as pd 
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


fil = pd.read_csv ("movie_data_for_assignment.csv",delimiter=",")



movie_title 			= fil ["movie_title"]#Sounds useless
# Colour = 1 or black and white = 0
colour = []
for element in (fil["color"]): 
	if element=="Color":
		colour.append(1)
	else:
		colour.append(0)

# For genres 
genre 					= fil ["genres"]
list_genre=[]
for element in genre: 
	list_genre.append(element.split('|'))

flatten = [item for sublist in lists for item in sublist]
#Gives you a list of different types of genres 
genreTypes				= set(flatten)

lang 					= fil["language"]
differentLang			= set(lang)

country					= fil["country"]	
ratings  				= fil["content_rating"]	
budget					= fil["budget"]
year 					= fil["title_year"]	
aspect_ratio			= fil["aspect_ratio"]
duration				= fil ["duration"]
gross					= fil ["gross"]	
facenumber 				= fil["facenumber_in_poster"]	
keywords 				= fil["plot_keywords"]


# Number of likes the actor has 
actor1_likes 			= fil ["actor_1_facebook_likes"]

actor2_likes 			= fil ["actor_2_facebook_likes"]


actor3_likes 			= fil ["actor_3_facebook_likes"]


director_likes  		= fil ["director_facebook_likes"]

num_critic_for_review	= fil ["num_critic_for_reviews"]
voted_users 			= fil ["num_voted_users"]	
movie_likes				= fil ["movie_facebook_likes"]
totalLikes				= fil ["cast_total_facebook_likes"]	

#imdb_link 				= fil["movie_imdb_link"]

num_reviews  			= fil["num_user_for_reviews"]	
	
result					= fil["imdb_score"]




		
_train(fil)