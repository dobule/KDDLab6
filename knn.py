# Name: Ryan Gelston
# Assignment: Lab 6
# Description: Impliments the knn classification algorithm

def knn(k, target, data, d_func):
   """ Takes a data point and returns the k nearest neighbors
      k -- The number of neighbors to return
      target -- The datapoint to compare other points to
      data -- A list of datapoints to compare the target to
      d_func -- A distance function that takes two data points

      NOTE: Each data point is a tuple (class, featureVector).
   """

   distList = []

   for d in data:
      dist = d_func(target[1], d[1])
      distList.append((dist, d))

   distList.sort()

   return [d[1] for d in distList[:k]]
