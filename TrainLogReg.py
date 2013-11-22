import sys
import os
import math

#default values
trainingFeatureFileName = "trainingFeature.dat"
trainingLabelFileName = "trainingLabel.dat"
modelFileName = "model.dat"
dimensions = 785
lambdaValue = 0.0001
nIter = 1

parameters = sys.argv
#override with command-line parameters
if len(parameters) > 1:
    trainingFeatureFileName = parameters[1]
    trainingLabelFileName = parameters[2]
    modelFileName = parameters[3]
    dimensions = int(parameters[4])
    lambdaValue = float(parameters[5])
    nIter = int(parameters[6])

#Open the specified files
baseDirectory = os.path.dirname(os.path.realpath(__file__))
trainingFeatureFile = open(os.path.join(baseDirectory,"Data/" + trainingFeatureFileName), 'r')
trainingLabelFile = open(os.path.join(baseDirectory,"Data/" + trainingLabelFileName), 'r')
modelFile = open(os.path.join(baseDirectory,"Data/" + modelFileName), 'w')

features = []
labels = []
#Initialize the feature vectors and labels from files
for line in trainingFeatureFile:
    features.append([int(s) for s in line.split(' ')])
    labels.append(int(trainingLabelFile.readline()))

#Close the file once data is read    
trainingFeatureFile.close()
trainingLabelFile.close()
    
#Logistic regression
t = 0
w = [0] * dimensions
for i in range(len(features)):
    t += 1
    wx = sum([a*b for a,b in zip(w,features[i])])
    h = 1.0 / (1 + math.exp(-wx))
    dwMultiplier = -2 * (labels[i] - h) * h * (1 - h) 
    dw = [e*dwMultiplier for e in features[i]]
    wMultiplier = float(lambdaValue / t)
    w = [w[i] - dw[i]*wMultiplier for i in range(dimensions)]

#write the calculated weights to the model file
for element in w:
    modelFile.write(str(element) + "\n")                
