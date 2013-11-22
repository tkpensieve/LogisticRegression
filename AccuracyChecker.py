import sys
import os

#default values
predictedLabelFileName = "predictedLabels.dat"
trueLabelFileName = "trainingLabel.dat"

parameters = sys.argv
#override with command-line parameters
if len(parameters) > 1:
    predictedLabelFileName = parameters[1]
    trueLabelFileName = parameters[2]

baseDirectory = os.path.dirname(os.path.realpath(__file__))
predictedLabelFile = open(os.path.join(baseDirectory,"Data/" + predictedLabelFileName), 'r')
trueLabelFile = open(os.path.join(baseDirectory,"Data/" + trueLabelFileName), 'r')

i = 0;
match = 0;
for line in predictedLabelFile:
    if line == trueLabelFile.readline():
        match += 1
    i += 1

print "Accuracy - "
print float(match)/i