# Name: Ryan Gelston and John Torres
# Assignment: Lab 6
# Description: Contains functions that are used within the command line 
#  programs required for this assignment.

###########################################################
# File I/O Functions
###########################################################

def read_data_file(filePath):
   """ Reads known reviews from the specified file and returns them
         in the required data structure

      RETURNS: [(usrId, [rat0, rat1, ..., ratN]), ...]
         A list of tuples with the user's id number as an int in the first
         place and a non-sparse vector containing the user's item ratings
   """

   with open(filePath, 'r') as f:
      rawData = f.read()

   ratingsLines = rawData.split('\n')
   ratingsLists = [line.split(',') for line in ratingsLines if line != ""]

   return [(int(usrRat[0]), [float(r) for r in usrRat[1:]])
           for userRat in ratingsLists]


def read_predictions_file(filePath):
   """ Reads a file of predictions ratings, as output by a test run.

      RETURNS: [(userId, itemId, 
                 Actual_Rating, Predicted_Rating, Delta_Rating), ...]
   """

   with open(filePath, 'r') as f:
      rawPred = f.read()

   predictions = rawPred.split('\n')
   predictions = [pred.split(',') for pred in predictions if pred != ""]

   return [(int(pred[0]), int(pred[1]), 
            float(pred[2]), float(pred[3]), float(pred[4]))
           for pred in predictions]

###########################################################
# Random Number Generating functions
###########################################################

def rand_user_item_idx(ratings, dontUse=[]):
   """ Returns a pair of random indecies for a rating in ratings that is
       not in dontUse
   """
   #TODO: Impliment
   pass


###########################################################
# Printing functions
###########################################################

def print_prediction(pred):
   """ Prints a singular prediction to stdout """

def print_predictions(preds):
   """ Prints predictions to stdout, as in page 5 of the assignment prompt 
      preds -- A list of prediction elements
   """

   for pred in preds:
      print_prediction(pred)






