# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 13:47:13 2014

@author: jmorris
"""

"""This file contains information about the vaccine that we are interested in.

Format: Vaccine(name, eligibility, minAgeAll,maxAgeAll,minAgeVFC,maxAgeVFC,minAgeHighRisk,maxAgeHighRisk)

Where the inputs are name of the vaccine, for which groups of people the eligibility changes, 
min/max age limits for All category(month), VFC category(month), and High risk categories(month).

But don't focus on this class because it is not important for you.
"""
class Vaccine:
    
    def __init__(self,name, eligibility, minAgeAll,maxAgeAll,minAgeVFC,maxAgeVFC,minAgeHighRisk,maxAgeHighRisk):
        self.name = name
        self.eligibility = eligibility
        self.minAgeAll = minAgeAll
        self.maxAgeAll = maxAgeAll
        self.minAgeVFC = minAgeVFC
        self.maxAgeVFC = maxAgeVFC
        self.minAgeHighRisk = minAgeHighRisk
        self.maxAgeHighRisk = maxAgeHighRisk
        
    def getName(self):
        return self.name
    def getEligibility(self):
        return self.eligibility
        
    def getMinAgeAll(self):
        return self.minAgeAll
    def getMaxAgeAll(self):
        return self.maxAgeAll
    def getMinAgeVFC(self):
        return self.minAgeVFC
    def getMaxAgeVFC(self):
        return self.maxAgeVFC
    
    def getMinAgeHighRisk(self):
        return self.minAgeHighRisk
    def getMaxAgeHighRisk(self):
        return self.maxAgeHighRisk
        
    def getAll(self):
        return self.name,self.eligibility, self.minAgeAll, self.maxAgeAll, self.minAgeVFC, self.maxAgeVFC, self.minAgeHighRisk,self.maxAgeHighRisk


        


