# Name: Ryan Gelston
# Assignment: Lab 6
# Description: Includes functions for accuracy measures.
# 
# Descriptions of the below function can be found in lecture 11 notes

###########################################################
# Predictive Accuracy Measures
#  Measures the accuracy of the value of predicted ratings
###########################################################

def mean_absolute_error(predictions, data):
   """ Calculates the mean absolute error of a set of predictions
   
      predictions -- a list of predicted ratings
      data -- Data object with known ratings
   """
   #TODO: Impliment
   pass


def mean_squared_error(predictions, data):
   """ Calculates the mean squared error of a set of predictions
   
      predictions -- a list of predicted ratings
      data -- Data object with known ratings
   """
   #TODO: Impliment
   pass


def root_mean_squared_error(predictions, data):
   """ Calculates the mean squared error of a set of predictions
   
      predictions -- a list of predicted ratings
      data -- Data object with known ratings
   """
   #TODO: Impliment
   pass


def normalized_mean_absolute_error(predictions, data):
   """ Calculates the mean squared error of a set of predictions
   
      predictions -- a list of predicted ratings
      data -- Data object with known ratings
   """
   #TODO: Impliment
   pass


def mean_absolute_error(predictions, data):
   """ Calculates the mean squared error of a set of predictions
   
      predictions -- a list of predicted ratings
      data -- Data object with known ratings
   """
   #TODO: Impliment
   pass



###########################################################
# Classification Accuracy Measures
###########################################################

def confusion_matrix(predictions, data):
   """ Returns a confusion matrix

      predictions -- a list of predicted ratings
      data -- data object with known ratings

      Returns a tuple of the format (RR, RN, FP, NN)
   """
   #TODO: Impliment
   pass

def precision(predictions, data, conf_mat=None):
   """ Returns the precision of the predictions 

      predictions -- a list of predicted ratings
      data -- data object with known ratings
      conf_mat -- If a confusion matrix is passed, one will
         not be be calculated in this function
   """
   #TODO: Impliment
   pass


def recall(predictions, data, conf_mat=None):
   """ Returns the recall of the predictions 

      predictions -- a list of predicted ratings
      data -- data object with known ratings
      conf_mat -- If a confusion matrix is passed, one will
         not be be calculated in this function
   """
   #TODO: Impliment
   pass


def f_measure(predictions, data, prec=None, rec=None, conf_mat=None):
   """ Returns the f-measure of the passed predictions

      predictions -- a list of predicited ratings
      data -- data object with known ratings
      prec -- If a known precision is passed, one will not be calculated in 
         this function
      rec -- If a known recall is passed, one will not be calculated in this
         function
      conf_mat -- If a known confusion matrix is passed, one will not be 
         calculated in this function
   """
   #TODO: Impliment
   pass


###########################################################
# Rank Accuracy Measures
#  Measures the accuracy of a list of predicted ratings for
#  a user given the order of the ratings when sorted by the 
#  value of the rating.
###########################################################


def spearman_correlation(predictions, data):
   """ Calculates the spearman correlation of the given predictions """
   #TODO: Impliment
   pass


def kendalls_tau(predictions, data):
   """ Calculates the Kendall's Tau of the given predictions """
   #TODO: Impliment
   pass


def half_life_utiliy(predictions, data):
   """ Calculates the half-life utility of the given predictions """
   #TODO: Impliment
   pass

