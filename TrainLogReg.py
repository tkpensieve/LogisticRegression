import sys
import os
import math

parameters = sys.argv
if len(parameters) > 1:
    trainingFeatureFileName = parameters[1]
    trainingLabelFileName = parameters[2]
    modelFileName = parameters[3]
    dimensions = int(parameters[4])
    lambdaValue = float(parameters[5])
    nIter = int(parameters[6])

baseDirectory = os.path.dirname(os.path.realpath(__file__))
trainingFeatureFile = open(os.path.join(baseDirectory,"Data/" + trainingFeatureFileName), 'r')
trainingLabelFile = open(os.path.join(baseDirectory,"Data/" + trainingLabelFileName), 'r')
modelFile = open(os.path.join(baseDirectory,"Data/" + modelFileName), 'w')

features = []
labels = []
for line in trainingFeatureFile:
    features.append([int(s) for s in line.split(' ')])
    labels.append(int(trainingLabelFile.readline()))
        
t = 0
w = [0] * dimensions
for i in range(len(features)):
    t += 1
    wx = sum([a*b for a,b in zip(w,features[i])])
    h = 1.0 / (1 + math.exp(-wx))
    dwMultiplier = -(labels[i] - h) * h * (1 - h) 
    dw = [e*dwMultiplier for e in features[i]]
    wMultiplier = float(lambdaValue / t)
    w = [w[i] - dw[i]*wMultiplier for i in range(dimensions)]

for element in w:
    modelFile.write(str(element) + "\n")                