import sys
import os
import math

#default values
modelFileName = "model.dat"
testingFeatureFileName = "testFeature.dat"
predictedLabelFileName = "predictedLabels.dat"

parameters = sys.argv
#override with command-line parameters
if len(parameters) > 1:
    modelFileName = parameters[1]
    testingFeatureFileName = parameters[2]
    predictedLabelFileName = parameters[3]

#Open the specified files
baseDirectory = os.path.dirname(os.path.realpath(__file__))
testingFeatureFile = open(os.path.join(baseDirectory,"Data/" + testingFeatureFileName), 'r')
modelFile = open(os.path.join(baseDirectory,"Data/" + modelFileName), 'r')
predictedLabelFile = open(os.path.join(baseDirectory,"Data/" + predictedLabelFileName), 'w')

features = []
#Initialize the test feature vectors from file
for line in testingFeatureFile:
    features.append([int(s) for s in line.split(' ')])
testingFeatureFile.close()

w = []
#Initialize the weight vector from model file
for line in modelFile:    
    w.append(float(line))
modelFile.close()

for i in range(len(features)):
    wx = sum([a*b for a,b in zip(w,features[i])])
    sig = (1.0 / (1 + math.exp(-wx)))
    if sig > 0.5:
        predictedLabelFile.write("1\n")
    else:
        predictedLabelFile.write("0\n")        