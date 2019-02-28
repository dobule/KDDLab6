# Name: Ryan Gelston
# Assignment: Lab 6
# Description: This file contains functions for calculating metrics used in 
#  collaborative filtering.
#
# Descriptions of these measured can be found in Lecture 10 notes



def set_of_users(ratings):
   """ Takes the ratings object and returns a set of users """
   # TODO: Impliment
   pass


def set_of_items(ratings):
   """ Takes a ratings object and returns the set of all items """
   # TODO: Impliment
   pass


###########################################################
# Statistical methods for predicting a user rating
###########################################################

def mean_utility(item, user, ratings, numUserWithItem=None):
   """ Finds the mean utility given an item and a user.
      
       item -- item to calculate mean of
       user -- user to calculate mean of
       ratings -- Object that contains all ratings
       numUserWithItem -- number of users who have rated passed item

       If numUserWithItem is set to none, find the mean in this fuction.
   """
   # TODO: Impliment
   # Returns: Float
   pass


def weighted_sum(item, user, ratings, sim_f, k):
   """ Finds the weighted sum given an item and user

       item -- item to find weighted sum of
       user -- user to find weighted sum of
       ratings -- Object that contains all ratings
       sim_f -- Similarity function, which finds the similarity between 
         users
       k -- normalization factor
   """
   # TODO: Impliment
   # Returns: Float
   pass


def adjusted_weighted_sum(item, user, ratings, sim_f, k, avgUsrRating=None):
   """ Finds the adjusted weighted sum given an item and user

      item -- item to find adjusted weighted sum of
      user -- user to find adjusted weighted sum of
      ratings -- Object that contains all ratings
      sim_f -- Similarity function
      k -- normalization factor
      avgUsrRating -- Average rating given by the passed user

      If avgUsrRating is None, calculate it within the function
   """
   #TODO: Impliment
   # Returns: Float
   pass


###########################################################
# Similarity Metrics
###########################################################

def pearson_correlation(user1, user2):
   """ Finds the pearson correlation between the ratings of two users 

      user1 -- Ratings from some user
      user2 -- Ratings from another user
   """
   # TODO: Impliment
   # Returns: Float
   pass


def cosine_similarity(user1, user2):
   """ Finds the cosine similarity between two users
   
      user1 -- Ratings from some user
      user2 -- Ratings from another user
   """
   #TODO: Impliment
   # Returns: Float
   pass


def default_voting(user1, user2):
   """ Finds the default voting similarity between two users
      
      user1 -- Ratings from some user
      user2 -- Ratings from another user
   """
   #TODO: Impliment
   # Returns: Float
   pass


def transformed_voting(user1, user2):
   """ Finds the transformed default voting similarity 

      user1 -- Ratings from some user
      user2 -- Ratings from another user
   """
   #TODO: Impliment
   # Returns: Float
   pass


def case_amplification(user_ratings):
   """ Returns amplified user ratings"""
   #TODO: Impliment
   # Returns: Float
   pass
