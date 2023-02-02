from numpy import double
import csv
import matplotlib.pyplot as plt

def spectral(spectralClassArr,redDwarfCount, brownDwarfCount, whiteDwarfCount, mainSequenceCount, superGiantsCount, hyperGiantsCount ):
      redDwarf = []
      brownDwarf = []
      whiteDwarf = []
      mainSequence = []
      superGiants = []
      hyperGiants = []


      for x in spectralClassArr:
        if (x[4] == 0):
          redDwarf.append(x)
        elif (x[4] == 1):
          brownDwarf.append(x)
        elif (x[4] == 2):
          whiteDwarf.append(x)
        elif (x[4] == 3):
          mainSequence.append(x)
        elif (x[4] == 4):
          superGiants.append(x)
        elif (x[4] == 5):
          hyperGiants.append(x)

      
      if(not(not redDwarf)):
        redDwarfTempMinArr = min(redDwarf, key=lambda x: x[0])
        redDwarfTempMin = redDwarfTempMinArr[0]

        redDwarfTempMaxArr = max(redDwarf, key=lambda x: x[0])
        redDwarfTempMax = redDwarfTempMaxArr[0]

        redDwarfMagnitudeMinArr= min(redDwarf, key=lambda x: x[3])
        redDwarfMagnitudeMin = redDwarfMagnitudeMinArr[3]

        redDwarfMagnitudeMaxArr = max(redDwarf, key=lambda x: x[3])
        redDwarfMagnitudeMax = redDwarfMagnitudeMaxArr[3]


      if(not(not brownDwarf)):
        brownDwarfTempMinArr = min(brownDwarf, key=lambda x: x[0])
        brownDwarfTempMin = brownDwarfTempMinArr[0]

        brownDwarfTempMaxArr = max(brownDwarf, key=lambda x: x[0])
        brownDwarfTempMax = brownDwarfTempMaxArr[0]

        brownDwarfMagnitudeMinArr= min(brownDwarf, key=lambda x: x[3])
        brownDwarfMagnitudeMin = brownDwarfMagnitudeMinArr[3]

        brownDwarfMagnitudeMaxArr = max(brownDwarf, key=lambda x: x[3])
        brownDwarfMagnitudeMax = brownDwarfMagnitudeMaxArr[3]


      if(not(not whiteDwarf)):
        whiteDwarfTempMinArr = min(whiteDwarf, key=lambda x: x[0])
        whiteDwarfTempMin = whiteDwarfTempMinArr[0]

        whiteDwarfTempMaxArr = max(whiteDwarf, key=lambda x: x[0])
        whiteDwarfTempMax = whiteDwarfTempMaxArr[0]

        whiteDwarfMagnitudeMinArr= min(whiteDwarf, key=lambda x: x[3])
        whiteDwarfMagnitudeMin = whiteDwarfMagnitudeMinArr[3]

        whiteDwarfMagnitudeMaxArr = max(whiteDwarf, key=lambda x: x[3])
        whiteDwarfMagnitudeMax = whiteDwarfMagnitudeMaxArr[3]

      if(not(not mainSequence)):
        mainSequenceTempMinArr = min(mainSequence, key=lambda x: x[0])
        mainSequenceTempMin = mainSequenceTempMinArr[0]

        mainSequenceTempMaxArr = max(mainSequence, key=lambda x: x[0])
        mainSequenceTempMax = mainSequenceTempMaxArr[0]

        mainSequenceMagnitudeMinArr= min(mainSequence, key=lambda x: x[3])
        mainSequenceMagnitudeMin = mainSequenceMagnitudeMinArr[3]

        mainSequenceMagnitudeMaxArr = max(mainSequence, key=lambda x: x[3])
        mainSequenceMagnitudeMax = mainSequenceMagnitudeMaxArr[3]

      if(not(not superGiants)):
        superGiantsTempMinArr = min(superGiants, key=lambda x: x[0])
        superGiantsTempMin = superGiantsTempMinArr[0]

        superGiantsTempMaxArr = max(superGiants, key=lambda x: x[0])
        superGiantsTempMax = superGiantsTempMaxArr[0]

        superGiantsMagnitudeMinArr= min(superGiants, key=lambda x: x[3])
        superGiantsMagnitudeMin = superGiantsMagnitudeMinArr[3]

        superGiantsMagnitudeMaxArr = max(superGiants, key=lambda x: x[3])
        superGiantsMagnitudeMax = superGiantsMagnitudeMaxArr[3]

      if(not(not hyperGiants)):
        hyperGiantsTempMinArr = min(hyperGiants, key=lambda x: x[0])
        hyperGiantsTempMin = hyperGiantsTempMinArr[0]

        hyperGiantsTempMaxArr = max(hyperGiants, key=lambda x: x[0])
        hyperGiantsTempMax = hyperGiantsTempMaxArr[0]

        hyperGiantsMagnitudeMinArr= min(hyperGiants, key=lambda x: x[3])
        hyperGiantsMagnitudeMin = hyperGiantsMagnitudeMinArr[3]

        hyperGiantsMagnitudeMaxArr = max(hyperGiants, key=lambda x: x[3])
        hyperGiantsMagnitudeMax = hyperGiantsMagnitudeMaxArr[3]

      for x in  spectralClassArr:

          if(not(not redDwarf)):
            if(redDwarfMagnitudeMin <= x[3] <= redDwarfMagnitudeMax  and redDwarfTempMin <= x[0] <= redDwarfTempMax): 
              print("Red Dwarf star found! with the attributes:");
              print(x)
              print()
              redDwarfCount = redDwarfCount + 1
          if(not(not brownDwarf)):
            if(brownDwarfMagnitudeMin <= x[3] <= brownDwarfMagnitudeMax  and brownDwarfTempMin <= x[0] <= brownDwarfTempMax): 
                print("Brown Dwarf star found! with the attributes:");
                print(x)
                print()
                brownDwarfCount = brownDwarfCount + 1
          if(not(not whiteDwarf)):#something is wrong
            if(whiteDwarfMagnitudeMin <= x[3] <= whiteDwarfMagnitudeMax  and whiteDwarfTempMin <= x[0] <= whiteDwarfTempMax): 
                print("White Dwarf star found! with the attributes:");
                print(x)
                print()
                whiteDwarfCount =whiteDwarfCount + 1
          if(not(not mainSequence)): #something is wrong
            if(mainSequenceMagnitudeMin <= x[3] <= mainSequenceMagnitudeMax  and mainSequenceTempMin <= x[0] <= mainSequenceTempMax): 
                print("Main Sequence star found! with the attributes:");
                print(x)
                print()
                mainSequenceCount = mainSequenceCount + 1
          if(not(not superGiants)):
            if(superGiantsMagnitudeMin <= x[3] <= superGiantsMagnitudeMax  and superGiantsTempMin <= x[0] <= superGiantsTempMax):
                print("Super Giants star found! with the attributes:");
                print(x)
                print()
                superGiantsCount = superGiantsCount + 1
          if(not(not hyperGiants)):
            if(hyperGiantsMagnitudeMin <= x[3] <= hyperGiantsMagnitudeMax  and hyperGiantsTempMin <= x[0] <= hyperGiantsTempMax):
                print("Hyper Giants star found! with the attributes:");
                print(x)
                print()
                hyperGiantsCount = hyperGiantsCount + 1
      
      return(redDwarfCount,brownDwarfCount,whiteDwarfCount,mainSequenceCount,superGiantsCount,hyperGiantsCount)

def accuracyChecker(spectralClassArr, redDwarfCount, brownDwarfCount, whiteDwarfCount, mainSequenceCount, superGiantsCount, hyperGiantsCount):

  tempredDwarfCount = 0
  tempbrownDwarfCount = 0
  tempwhiteDwarfCount = 0
  tempmainSequenceCount = 0
  tempsuperGiantsCount = 0
  temphyperGiantsCount = 0

  for x in spectralClassArr: 
    if(x[4] == 0):
      tempredDwarfCount = tempredDwarfCount+1
    elif(x[4] == 1):
      tempbrownDwarfCount = tempbrownDwarfCount+1
    elif(x[4] == 2):
      tempwhiteDwarfCount = tempwhiteDwarfCount+1
    elif(x[4] == 3):
      tempmainSequenceCount = tempmainSequenceCount+1
    elif(x[4] == 4):
      tempsuperGiantsCount = tempsuperGiantsCount+1
    elif(x[4] == 5):
      temphyperGiantsCount = temphyperGiantsCount+1

  if(redDwarfCount == tempredDwarfCount and brownDwarfCount == tempbrownDwarfCount and whiteDwarfCount == tempwhiteDwarfCount and mainSequenceCount == tempmainSequenceCount and superGiantsCount == tempsuperGiantsCount and hyperGiantsCount == temphyperGiantsCount):
     print("Calculations Are Accurate For Spectral Class: " + spectralClassArr[0][6])
  else:
     print("Calculations Are Not Accurate For Spectral Class: " + spectralClassArr[0][6])

with open("/stars.csv", 'r') as file:
  csvreader = csv.reader(file)
  oValues = []
  bValues = []
  aValues = []
  fValues = []
  gValues = []
  kValues = []
  mValues = []

  redDwarfCount = 0
  brownDwarfCount = 0
  whiteDwarfCount = 0
  mainSequenceCount = 0
  superGiantsCount = 0
  hyperGiantsCount = 0
 
  for row in csvreader:
    if (row[0] != "Temperature (K)"):
      row[0] = int(row[0])
      row[1] = double(row[1])
      row[2] = double(row[2])
      row[3] = double(row[3])
      row[4] = int(row[4])

      if row[6] == "O":
        oValues.append(row)
      elif row[6] == "B":
        bValues.append(row)
      elif row[6] == "A":
        aValues.append(row)
      elif row[6] == "F":
        fValues.append(row)
      elif row[6] == "G":
        gValues.append(row)
      elif row[6] == "K":
        kValues.append(row)
      elif row[6] == "M":
        mValues.append(row)

  oValueTuple = spectral(oValues, redDwarfCount, brownDwarfCount, whiteDwarfCount, mainSequenceCount, superGiantsCount, hyperGiantsCount)
  bValueTuple = spectral(bValues, redDwarfCount, brownDwarfCount, whiteDwarfCount, mainSequenceCount, superGiantsCount, hyperGiantsCount)
  aValueTuple = spectral(aValues, redDwarfCount, brownDwarfCount, whiteDwarfCount, mainSequenceCount, superGiantsCount, hyperGiantsCount)
  fValueTuple = spectral(fValues, redDwarfCount, brownDwarfCount, whiteDwarfCount, mainSequenceCount, superGiantsCount, hyperGiantsCount)
  gValueTuple = spectral(gValues, redDwarfCount, brownDwarfCount, whiteDwarfCount, mainSequenceCount, superGiantsCount, hyperGiantsCount)
  kValueTuple = spectral(kValues, redDwarfCount, brownDwarfCount, whiteDwarfCount, mainSequenceCount, superGiantsCount, hyperGiantsCount)
  mValueTuple = spectral(mValues, redDwarfCount, brownDwarfCount, whiteDwarfCount, mainSequenceCount, superGiantsCount, hyperGiantsCount)

  accuracyChecker(oValues, oValueTuple[0], oValueTuple[1], oValueTuple[2], oValueTuple[3], oValueTuple[4], oValueTuple[5])
  accuracyChecker(bValues, bValueTuple[0], bValueTuple[1], bValueTuple[2], bValueTuple[3], bValueTuple[4], bValueTuple[5])
  accuracyChecker(aValues, aValueTuple[0], aValueTuple[1], aValueTuple[2], aValueTuple[3], aValueTuple[4], aValueTuple[5])
  accuracyChecker(fValues, fValueTuple[0], fValueTuple[1], fValueTuple[2], fValueTuple[3], fValueTuple[4], fValueTuple[5])
  accuracyChecker(gValues, gValueTuple[0], gValueTuple[1], gValueTuple[2], gValueTuple[3], gValueTuple[4], gValueTuple[5])
  accuracyChecker(kValues, kValueTuple[0], kValueTuple[1], kValueTuple[2], kValueTuple[3], kValueTuple[4], kValueTuple[5])
  accuracyChecker(mValues, mValueTuple[0], mValueTuple[1], mValueTuple[2], mValueTuple[3], mValueTuple[4], mValueTuple[5])







      
