import sys
import os
import math

parameters = sys.argv
if len(parameters) < 5:
    #default values
    modelFileName = "model.dat"
    testingFeatureFileName = "testFeature.dat" #"trainingFeature.dat"
    predictedLabelFileName = "predictedLabel.dat"
    dimensions = 785 
    print "Usage: python TestLogReg.py [modelFileName] [testFeatureFileName] [predLabelFileName] [D]"
else:
    #override with command-line parameters
    modelFileName = parameters[1]
    testingFeatureFileName = parameters[2]
    predictedLabelFileName = parameters[3]
    dimensions = parameters[4]

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

#Predict the labels using the model and write the output to file
for i in range(len(features)):
    wx = sum([wi*xi for wi,xi in zip(w,features[i])])
    sig = 1.0 / (1 + math.exp(-wx))
    if sig > 0.5:
        predictedLabelFile.write("1\n")
    else:
        predictedLabelFile.write("0\n")
predictedLabelFile.close()        