#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 17:31:44 2020

@author: anhnguyen
"""

#Initilize variable to store the start year 
startYear = 1903
teamYear = {} #create teamYear dictionary with keys of team name and values consists of years of winnings
file = open("WorldSeriesWinners.txt") # open the file
line = file.readline() # read a line from the file

#loop to read the whole file from the beginning to the end
while(line):
               if startYear in [1904, 1994]:
                              startYear += 1
               if line.strip() in teamYear:
                              teamYear[line.strip()].append(startYear) # append the year to the list
               else: 
                              teamYear[line.strip()] = [startYear] 
               startYear += 1 # increment the start_year
               line = file.readline() # read the next line
#close the file
file.close()
# get the list of teams from the dictionary             
teams = list(teamYear.keys())

#display the results
print('\n%30s : %s' %('Team','Win Years'))
for team in sorted(teams):
               print('%30s : %s' %(team,teamYear[team]))

#create teamWins dictionary             
teamWins = {}
          
for team in list(teamYear.keys()):
               teamWins[team] = len(teamYear[team])      
               
teams = list(teamWins.keys()) # get the list of teams
wins = list(teamWins.values()) # get the list of values

#loop to sort the teams and wins
i=0
while(i<len(wins)-1):
               j = i+1
               max = i
               while(j < len(wins)):

                              if wins[j] > wins[max]:
                                             max = j
                              j += 1
               if(max != i):
                              tempWin = wins[i]
                              wins[i] = wins[max]
                              wins[max] = tempWin                             
                              tempTeam = teams[i]
                              teams[i] = teams[max]
                              teams[max] = tempTeam
               i += 1

#display the results     
print('')
print('\n%30s : %s' %('Team','Total Wins'))        
for team in teams:
               print('%30s : %d' %(team,teamWins[team]))

# print the results 
print('')
print('\n%33s : %s' %('Team','Total Wins Bar Graph'))        
for team in teams:
               print('%30s(%s) : %s' %(team, teamWins[team],'*'*teamWins[team]))  
#Happy ending     
