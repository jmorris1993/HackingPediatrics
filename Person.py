# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 14:07:24 2014

@author: jmorris
"""

"""This file contains information about the person that we are interested in.
Format: Person(age,vaccine,insurance,ethnicity,isHighRisk)
It takes in age of the person(in months), the vaccine that is being checked(vaccine class), 
insurance type(True/False), ethnicity(True/False), whether the person is high risk or not(True/False).


But don't focus on this class because it is not important for you.
"""
class Person:
    def __init__(self,age,vaccine,insurance,ethnicity,isHighRisk):
        self.age = age
        self.vaccine = vaccine
        self.insurance = insurance        
        self.isHighRisk = isHighRisk
        self.ethnicity = ethnicity
        
    def getAge(self):
        return self.age
    
    def getVaccine(self):
        return self.vaccine

    def getInsurance(self):
        return self.insurance
    
    def getEthnicity(self):
        return self.getEthnicity
    
    def getIsHighRisk(self):
        return self.isHighRisk
    
    def getAll(self):
        return self.age, self.vaccine, self.insurance, self.isVFC, self.isHighRisk
    
    def getIsVFC(self):
        if self.insurance == False and self.ethnicity == False:
            return False
        else:
            return True
            