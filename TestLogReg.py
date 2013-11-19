import sys
import os
import math

parameters = sys.argv
if len(parameters) > 1:
    modelFileName = parameters[1]
    testingFeatureFileName = parameters[2]
    predictedLabelFileName = parameters[3]

baseDirectory = os.path.dirname(os.path.realpath(__file__))
testingFeatureFile = open(os.path.join(baseDirectory,"Data/" + testingFeatureFileName), 'r')
modelFile = open(os.path.join(baseDirectory,"Data/" + modelFileName), 'r')
predictedLabelFile = open(os.path.join(baseDirectory,"Data/" + predictedLabelFileName), 'w')

features = []
w = []
for line in testingFeatureFile:
    features.append([int(s) for s in line.split(' ')])
for line in modelFile:    
    w.append(float(line))

h=[]
for i in range(len(features)):
    wx = sum([a*b for a,b in zip(w,features[i])])
    h.append(1.0 / (1 + math.exp(-wx)))
print h            