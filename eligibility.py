# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 13:52:22 2014

@author: jmorris
"""

"""This is where the main code is. Go to the bottom of the file to make your inputs.
"""
from Vaccine import *
from Person import *

"""Makes the list of Vaccines with their specifications. See Vaccine file for details of specification."""
ListOfVaccines = []
ListOfVaccines.append(Vaccine("DT","All",2,72,2,72,2,72))
ListOfVaccines.append(Vaccine("DTap","All",2,72,2,72,2,72))
ListOfVaccines.append(Vaccine("DTaP-HepB-IPV (Pediarix)","All",2,72,2,72,2,72))
ListOfVaccines.append(Vaccine("DTaP-IPV-Hib (Pentacel)","All",2,48,2,48,2,48))
ListOfVaccines.append(Vaccine("DTap-IPV (Kinrix)","All",48,72,48,72,48,72))
ListOfVaccines.append(Vaccine("Hep A","Both",12,36,12,216,12,216))
ListOfVaccines.append(Vaccine("Hep B","All",0,216,0,216,0,216))
ListOfVaccines.append(Vaccine("Hib","All",2,59,2,59,2,216))
ListOfVaccines.append(Vaccine("HPV","VFC",0,0,108,216,0,0))
ListOfVaccines.append(Vaccine("Influenza","Both",6,216,6,216,6,216))
ListOfVaccines.append(Vaccine("MCV4","Both",121,216,121,216,2,216))
ListOfVaccines.append(Vaccine("MMR","All",12,216,12,216,12,216))
ListOfVaccines.append(Vaccine("MMRV","Both",12,144,12,144,12,144))
ListOfVaccines.append(Vaccine("PCV13","All",2,59,2,59,2,216))
ListOfVaccines.append(Vaccine("PPSV23","All",0,0,0,0,2,216))
ListOfVaccines.append(Vaccine("Polio","All",2,216,2,216,2,216))
ListOfVaccines.append(Vaccine("Rotavirus","All",1.5,8,1.5,8,1.5,8))
ListOfVaccines.append(Vaccine("Td","All",84,216,84,216,84,216))
ListOfVaccines.append(Vaccine("Tdap","Both",121,144,84,216,121,216))
ListOfVaccines.append(Vaccine("Varicella","Both",12,72,12,216,12,216))


"""Creates a list of people with different Vaccines.
So I am creating a list of 20 different people with everything being the same
except for the vaccine that the person is being tested for.
This needs to be done to test the person's eligibility for all Vaccines.
"""
def getListOfAllTestPeople(age,insurance,isVFC,isHighRisk):
    ListOfPerson = []
    for i in range(len(ListOfVaccines)):
        ListOfPerson.append(Person(age, getAllNamesVac()[i], insurance, isVFC, isHighRisk))
    return ListOfPerson

"""Returns the list of the names of all vaccines."""
def getAllNamesVac():
    nameList = []
    for vac in ListOfVaccines:
        nameList.append(vac.getName())
        
    return nameList

"""Searches the list of Vaccines to see if the specified vaccine (input is String format) is in the list.
If yes, it will return the Vaccine object. """
def matchVaccine(name):
    for vac in ListOfVaccines:
        if vac.getName()==name:
            return vac

"""Checks to see if the person is eligible for a particular vaccine."""
def eligibility(person):
    vac = matchVaccine(person.getVaccine())

    if person.getIsVFC() == False and person.getIsHighRisk() == False:    
        if vac.getMinAgeAll() <= person.getAge() and vac.getMaxAgeAll() >= person.getAge():
            return True         
        else:
            return False
                
    elif person.getIsVFC() == True and person.getIsHighRisk() == False:
        if vac.getMinAgeVFC() <= person.getAge() and vac.getMaxAgeVFC() >= person.getAge():
            return True
        else:
            return False
    
    elif person.getIsVFC() == False and person.getIsHighRisk() == True:
        if vac.getMinAgeHighRisk() <= person.getAge() and vac.getMaxAgeHighRisk() >= person.getAge():
            return True
        else:
            return False
            
    elif person.getIsVFC() == True and person.getIsHighRisk() == True:
        if min(vac.getMinAgeHighRisk(),vac.getMinAgeVFC()) <= person.getAge() and max(vac.getMaxAgeHighRisk(),vac.getMaxAgeHighRisk()) >= person.getAge():
            return True
        else:
            return False


"""eligibleAll is the most important function, where the input from the user goes.
Checks to see the eligibility for every vaccine on our list for the person, and outputs
a list of dictionary elements that has information on each vaccine.
Format: [{'Name: ': 'DT', 'Eligibility: ': True, 'VFC: ': False}, repeated for every vaccine]

'Name: ': 'DT' pair tells you the name of the vaccine.
'Eligibility: ': True pair tells you whether the person is eligible for the vaccine or not. True means yes, False means no. 
'VFC: ': False pair tells you whether the person is VFC or not. True means yes, False means no.

"""
def eligibleAll(age,insurance,isVFC,isHighRisk):     
    eligAll = []      
    VFC = []
    Strings = []   
    vacNames = getAllNamesVac()
    finalList = []
    
    for person in getListOfAllTestPeople(age,insurance,isVFC,isHighRisk):
        eligAll.append(eligibility(person))
        VFC.append(person.getIsVFC())

    Strings.append("Name: ")
    Strings.append("Eligibility: ")
    Strings.append("VFC: ")
    
    for i in range(len(getAllNamesVac())):
        Info=[]
        Info.append(vacNames[i])
        Info.append(eligAll[i])
        Info.append(VFC[i])
        
        firstDict = dict(zip(Strings,Info))

        finalList.append(firstDict)
    
    return finalList


"""eligibleAll is where you make your inputs.
There must be four inputs in this format: eligibleAll(age, insurance,isVFC,isHighRisk)

age = the person's age in months (Any number)
insurance = Whether the person has good insurance (True/False)
isVFC = Whether the person is VFC (True/False)
isHighRisk = Whether the person is a high risk person or not (True/False)

The next line below is an example input that prints out the results on the consol.
"""
print eligibleAll(34,False,False,False)   

"""
The output I got from: print eligibleAll(34,False,False,False)

[{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'DT'}, 
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'DTap'}, 
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'DTaP-HepB-IPV (Pediarix)'},
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'DTaP-IPV-Hib (Pentacel)'},
{'VFC: ': False, 'Eligibility: ': False, 'Name: ': 'DTap-IPV (Kinrix)'},
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'Hep A'}, 
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'Hep B'},
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'Hib'}, 
{'VFC: ': False, 'Eligibility: ': False, 'Name: ': 'HPV'},
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'Influenza'},
{'VFC: ': False, 'Eligibility: ': False, 'Name: ': 'MCV4'}, 
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'MMR'}, 
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'MMRV'}, 
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'PCV13'},
{'VFC: ': False, 'Eligibility: ': False, 'Name: ': 'PPSV23'},
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'Polio'},
{'VFC: ': False, 'Eligibility: ': False, 'Name: ': 'Rotavirus'},
{'VFC: ': False, 'Eligibility: ': False, 'Name: ': 'Td'}, 
{'VFC: ': False, 'Eligibility: ': False, 'Name: ': 'Tdap'},
{'VFC: ': False, 'Eligibility: ': True, 'Name: ': 'Varicella'}]   
"""
        




















