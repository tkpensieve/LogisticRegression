import sys
import os
import math

parameters = sys.argv
if len(parameters) < 7:
    #default values
    trainingFeatureFileName = "trainingFeature.dat"
    trainingLabelFileName = "trainingLabel.dat"
    modelFileName = "model.dat"
    dimensions = 785
    lambdaValue = 0.000001
    nIter = 1
    print "Usage: python TrainLogReg.py [trainingFeatureFileName] [trainingLabelFileName] [modelFileName] [D] [lambda] [Niter]"
else:
    #override with command-line parameters
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
    wx = sum([wi*xi for wi,xi in zip(w,features[i])])
    h = 1.0 / (1 + math.exp(-wx))
    dwMultiplier = -1 * (labels[i] - h) * h * (1 - h) 
    dw = [xi*dwMultiplier for xi in features[i]]
    wMultiplier = float(lambdaValue / t)
    w = [w[i] - dw[i]*wMultiplier for i in range(dimensions)]

#write the calculated weights to the model file and close it
for element in w:
    modelFile.write(str(element) + "\n")                
modelFile.close()