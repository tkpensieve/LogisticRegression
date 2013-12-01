import sys
import os

parameters = sys.argv
if len(parameters) < 3:
    #default values
    predictedLabelFileName = "predictedLabel.dat"
    trueLabelFileName = "trainingLabel.dat"
    print "Usage: python Accuracy.py [predLabelFileName] [trueLabelFileName]"
else:
    #override with command-line parameters
    predictedLabelFileName = parameters[1]
    trueLabelFileName = parameters[2]

#Open the specified files
baseDirectory = os.path.dirname(os.path.realpath(__file__))
predictedLabelFile = open(os.path.join(baseDirectory,"Data/" + predictedLabelFileName), 'r')
trueLabelFile = open(os.path.join(baseDirectory,"Data/" + trueLabelFileName), 'r')

#Calculate and display accuracy
i = 0;
match = 0;
for line in predictedLabelFile:
    i += 1
    if line == trueLabelFile.readline():
        match += 1

print "Accuracy = %f" % (float(match)/i)