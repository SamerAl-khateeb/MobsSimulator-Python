# Mob_Simulator-Q3.py
# By: Samer Al-khateeb

# A program to simulate a Mob using Monte Carlo
# methods, ABM, and the Theory of Collective Action.

# Q3: Given the following parameters (Number of Invited People,
# Threshold Value of the Mob Success, the Number of Simulations (Mobs),
# the Number of Powerful Actors),
# How does the time it takes a participant to decide to join a mob affect the participation rate? 
from random import randrange
import csv
import os
import math

class Agent():
    def __init__(self):
        self.interest = randrange(0,2)
        self.control = randrange(0,2)


# function to write each mob stat into a row in a CSV file
def writeIndividualMobStatToCSV(biglist):
    # column names
    columnNames = ["Threshold", "Mob_Result", "Num_Powerful_Actors", "Act_Counter", "Withdraw_Counter", "Power_Exchange_Counter", "Act_Against_Counter", "Participation_Rate"]
    # data rows of csv file
    rows = biglist
    # name of csv file
    filename = "Q3-IndividualMobStats-Eq2.csv"
    # opening the csv file in append mode
    with open(filename, 'a', encoding='utf-8') as csv_output_file:
        # define a variable to check if the file is empty (of size zero)
        fileIsEmpty = os.stat(filename).st_size == 0
        # creating a csv writer object
        csvwriter = csv.writer(csv_output_file)
        # if the file is empty (i.e., has size of 0) write the header or columnNames
        if fileIsEmpty:
            # writing the columnNames
            csvwriter.writerow(columnNames)
        # always write the data rows sent
        csvwriter.writerows(rows)


# function to write the overall simulation stats into a row in a CSV file
def writeOverAllStatToCSV(biglist):
    # column names
    columnNames = ["Threshold Value", "Number Of Mobs Simulated", 
                    "Mobs Success Rate", "Mobs Fail Rate", 
                    "Average Participation Rate"]
    # data rows of csv file
    row = biglist
    # name of csv file
    filename = "Q3-OverallSimulationStats-Eq2.csv"
    # opening the csv file in append mode
    with open(filename, 'a', encoding='utf-8') as csv_output_file:
        # define a variable to check if the file is empty (of size zero)
        fileIsEmpty = os.stat(filename).st_size == 0
        # creating a csv writer object
        csvwriter = csv.writer(csv_output_file)
        # if the file is empty (i.e., has size of 0) write the header or columnNames
        if fileIsEmpty:
            # writing the columnNames
            csvwriter.writerow(columnNames)
        # write the data row sent
        csvwriter.writerow(row)


def getInputs():
    # Ask the user to insert some info
    Mob_Practitioners = int(input("Enter the Total Number of Invited Mob Practitioners: "))
    Success_Threshold = float(input("Enter the Threshold Value for a Mob to Success: ")) / 100
    Num_Of_Simulation = int(input("Enter the Number of Simulations (or Number of Mobs): "))
    Num_Of_Powerful_Actors = int(input("Enter the Number of Powerful Actors: "))
    return Mob_Practitioners, Success_Threshold, Num_Of_Simulation, Num_Of_Powerful_Actors


def SimulateOneMob(Mob_Practitioners, Success_Threshold, Num_Powerful_Actors):
    # initialize the counters 
    Act_Counter = 0
    Withdraw_Counter = 0
    S_Withdraw_Counter = 0
    Power_Exchange_Counter = 0
    Act_Against_Counter = 0
    Participation_Rate = 0
    
    #counting how many we want to determin their decision first
    participants = Mob_Practitioners - Num_Powerful_Actors

    #needed for Euler method
    t = 1
    eulerNumber = math.e
    #update the number of participants according to Euler method
    Ni_1 = math.ceil((participants/((t*eulerNumber)+1)))
    #print(participants)
    print(Ni_1)

    # for each participant other than the powerful actors what will (s)he do?
    while participants != 0:
        for mobber in range(Ni_1):
            #create an agent
            participantAgent = Agent()
            # have interest and have control, practitioner will act
            if ((participantAgent.interest == 1) and (participantAgent.control == 1)):
                Act_Counter = Act_Counter + 1
            # have interest but no control, practitioner will act or withdraw
            elif ((participantAgent.interest == 1) and (participantAgent.control == 0)):
                Participant_Decision = randrange(0,2)
                if (Participant_Decision == 1):
                    Act_Counter = Act_Counter + 1
                else:
                    # this is a special withdraw case because if they get control they will act 
                    S_Withdraw_Counter = S_Withdraw_Counter + 1     
            # No interest but have control, practitioner will withdraw or power exchange
            elif ((participantAgent.interest == 0) and (participantAgent.control == 1)):
                Participant_Decision = randrange(0,2)
                if (Participant_Decision == 0):
                    Withdraw_Counter = Withdraw_Counter + 1
                else:
                    # these individuals are willing to power exchange with the special withdraw case above
                    Power_Exchange_Counter = Power_Exchange_Counter + 1
            # No interest and No control, practitioner will withdraw or Act Against
            elif ((participantAgent.interest == 0) and (participantAgent.control == 0)):
                Participant_Decision = randrange(0,2)
                if (Participant_Decision == 0):
                    Withdraw_Counter = Withdraw_Counter + 1
                else:
                    Act_Against_Counter = Act_Against_Counter + 1
        #update the numbers according to Euler method
        participants = participants - Ni_1
        t = t+1
        Ni_1 = math.ceil((participants/((t*eulerNumber)+1)))
        print(Ni_1)
        

    #print(Act_Counter, Withdraw_Counter, S_Withdraw_Counter, Power_Exchange_Counter, Act_Against_Counter)
    
    #### for each mob do the following ###
    ###--------------------------------###
    # if the number of participants who have interest but no control is more than 
    # the number of participants who are willing to power exchange
    if (S_Withdraw_Counter >= Power_Exchange_Counter):
        #increment the number of act by the people who are willing to power exchange
        Act_Counter = Act_Counter + Power_Exchange_Counter
        #update the number of withdraw by adding the people who did the power exchange
        Withdraw_Counter = Withdraw_Counter + Power_Exchange_Counter
        # subtract the number of people who did the exchange from the special withdraw 
        S_Withdraw_Counter = S_Withdraw_Counter - Power_Exchange_Counter
        #after this no one is left for power exchange, because they all exchanged and now are acting
        Power_Exchange_Counter = 0
    else:
        #increment the number of act by the people who have interest but no control
        Act_Counter = Act_Counter + S_Withdraw_Counter
        #since all the people who have interest and no control did the power exchange
        #(and now are acting) the same number of people from the power exchange will not act 
        Withdraw_Counter = Withdraw_Counter + S_Withdraw_Counter
        #subtract the number who did the power exchange already (and now are acting) from
        #the original number of power exchange
        Power_Exchange_Counter = Power_Exchange_Counter - S_Withdraw_Counter

    # the participation rate in a mob counting for the number of acted actors, powerful actors, 
    # and acted against actors divided by all the invited people.
    # a negative participation rate means more people were opposing the mob than agreening with it
    
    #competing switch is ON (Eq1)
    #Participation_Rate = (Act_Counter + Num_Powerful_Actors - Act_Against_Counter) / Mob_Practitioners
    
    #competing switch is OFF (Eq2)
    Participation_Rate = (Act_Counter + Num_Powerful_Actors) / Mob_Practitioners

    # based on the participaiton rate and threshold value we can determine whether a mob succeeded or not
    if (Participation_Rate >= Success_Threshold):
        Mob_Result = "Success"
    else:
        Mob_Result = "Fail"
    return Mob_Result, Num_Powerful_Actors, Act_Counter, Withdraw_Counter, Power_Exchange_Counter, Act_Against_Counter, Participation_Rate


def SimulateManyMobs(Practitioners, Threshold, Num_Simulation, Num_Powerful_Actors):
    num_Of_Success_Mob = 0
    num_Of_Fail_Mob = 0
    Total_Participation_Rate = 0
    print("{0:<15} {1:^22} {2:^15} {3:^15} {4:^22} {5:^15} {6:^15}".format("Result", "Number of Powerful Actors", "Acted", "Withdraw", "Did NOT Power Exchange", "Act Against", "Participation Rate"))
    print("------------------------------------------------------------------------------------------------------------------------------------")
    # list to keep the result of each simulated mob
    individualMobRestulList = []
    for Mob in range(Num_Simulation):
        result = SimulateOneMob(Practitioners, Threshold, Num_Powerful_Actors)
        CSVRow = [Threshold*100, result[0], result[1], result[2], result[3], result[4], result[5], result[6]*100]
        individualMobRestulList.append(CSVRow)
        if (result[0] == "Success"):
            num_Of_Success_Mob = num_Of_Success_Mob + 1
        elif (result[0] == "Fail"):
            num_Of_Fail_Mob = num_Of_Fail_Mob + 1
        print("{0:<15} {1:^22} {2:^22} {3:^7} {4:^30} {5:^7} {6:^24}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
        Total_Participation_Rate = Total_Participation_Rate + result[6]
    Avg_Participation_Rate = Total_Participation_Rate/Num_Simulation
    # write the output to a CSV file
    writeIndividualMobStatToCSV(individualMobRestulList)
    return num_Of_Success_Mob, num_Of_Fail_Mob, Avg_Participation_Rate
     

def printStats(T_o, Num_Of_Mob_Success, Num_Of_Mob_Fail, Num_Simulation, Avg_Participation_Rate):
    mobSuccessRate = round(((Num_Of_Mob_Success / Num_Simulation) * 100),2)
    mobFailRate = round(((Num_Of_Mob_Fail / Num_Simulation) * 100), 2)
    averageParticipationRate = round(((Avg_Participation_Rate) * 100), 2)
    print()
    print("This program simulated ", Num_Simulation, "Mobs")
    print("The Mobs Success rate is ", mobSuccessRate, "%")
    print("The Mobs Fail rate is ", mobFailRate, "%")
    print("The Average Participation Rate Of All The Mobs Simulated is ", averageParticipationRate, "%")
    writeOverAllStatToCSV([T_o * 100, Num_Simulation, mobSuccessRate, mobFailRate, averageParticipationRate])


def main():
    #P, T_o, N_Sim, N_Pow_Act = getInputs()
    thresholdList = [0.5]
    for i in thresholdList:
        P = 10000
        N_Pow_Act = 0
        N_Sim = 100
        T_o = i
        Num_Of_Mob_Success, Num_Of_Mob_Fail, Avg_Participation_Rate = SimulateManyMobs(P, T_o, N_Sim, N_Pow_Act)
        printStats(T_o, Num_Of_Mob_Success, Num_Of_Mob_Fail, N_Sim, Avg_Participation_Rate)
main()
