# Mob_Simulator-Q2.py
# By: Samer Al-khateeb

# A program to simulate a Mob using Monte Carlo
# methods and the Theory of Collective Action.

# Q2: Given the following parameters (Number of Invited People,
# Threshold Value of the Mob Success, and the Number of Simulations (Mobs)),
# how many powerful actors are needed to have a successful mob?


from random import randrange
import math
import csv
import os

# funciton to write each mob stat into a row in a CSV file
def writeIndividualMobStatToCSV(biglist):
    # column names
    columnNames = ["Threshold", "Mob_Result", "Needed_Powerful_Actors", "Act_Counter", "Withdraw_Counter", "Power_Exchange_Counter", "Act_Against_Counter", "Participation_Rate"]
    
    # data rows of csv file
    rows = biglist

    # name of csv file
    filename = "Q2-IndividualMobStats.csv"

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
                    "Average Needed Powerful Actors"]
    
    # data rows of csv file
    row = biglist

    # name of csv file
    filename = "Q2-OverallSimulationStats.csv"

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
    Mob_Practitioners = int(input("Enter the Total Number of Invited People: "))
    Success_Threshold = float(input("Enter the Threshold Value for a Mob to Succeed: ")) 
    Num_Of_Simulation = int(input("Enter the Number of Simulations (or Number of Mobs) you want to run: "))
    return Mob_Practitioners, Success_Threshold, Num_Of_Simulation


def SimulateOneMob(Mob_Practitioners, Success_Threshold):
    # initialize the counters 
    Act_Counter = 0
    Withdraw_Counter = 0
    S_Withdraw_Counter = 0
    Power_Exchange_Counter = 0
    Act_Against_Counter = 0

    Participation_Rate = 0

    Needed_Powerful_Actors = 0

    #for each participant lets examing what will (s)he do?
    for participant in range(Mob_Practitioners):
        
        # randomly assigning the participant an interest and control
        P_Interest = randrange(0,2)
        P_Control = randrange(0,2)
        
        # have interest and have control, practitioner will ACT
        if ((P_Interest == 1) and (P_Control == 1)):
            Act_Counter = Act_Counter + 1
            
        # have interest but no control, practitioner will ACT or WITHDRAW
        elif ((P_Interest == 1) and (P_Control == 0)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 1):
                Act_Counter = Act_Counter + 1
            else:
                # this is a special withdraw case because if they get control they will act 
                S_Withdraw_Counter = S_Withdraw_Counter + 1
                
                
        # No interest but have control, practitioner will WITHDRAW or POWER EXCHANGE 
        elif ((P_Interest == 0) and (P_Control == 1)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 0):
                Withdraw_Counter = Withdraw_Counter + 1
            else:
                # these individuals are willing to power exchange with the special withdraw case above
                Power_Exchange_Counter = Power_Exchange_Counter + 1
            
        # No interest and No control, practitioner will WITHDRAW or ACT AGAINST
        elif ((P_Interest == 0) and (P_Control == 0)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 0):
                Withdraw_Counter = Withdraw_Counter + 1
            else:
                Act_Against_Counter = Act_Against_Counter + 1

    #### for each mob do the following ###
    ###--------------------------------###
    #if the number of participants who have interest but no control is more than
    #the number of participants who are willing to power exchange
    if (S_Withdraw_Counter >= Power_Exchange_Counter):
        #increment the number of act by the people who are willing to power exchange
        Act_Counter = Act_Counter + Power_Exchange_Counter
        #update the number of withdraw by adding the people who are left after the power exchange
        Withdraw_Counter = Withdraw_Counter + (S_Withdraw_Counter - Power_Exchange_Counter)
        #after this no one is left for power exchange, because they all exchanged and now are acting
        Power_Exchange_Counter = 0
    else:
        #increment the number of act by the people who have interest but no control
        Act_Counter = Act_Counter + S_Withdraw_Counter
        #since all the people who have interest and no control did the power exchange
        #(and now are acting) no one is left to be added
        Withdraw_Counter = Withdraw_Counter + 0
        #subtract the number who did the power exchange already (and now are acting) from
        #the original number of power exchange
        Power_Exchange_Counter = Power_Exchange_Counter - S_Withdraw_Counter

    #the participation rate in a mob counting for the number of acted actors, powerful actors, and acted against actors divided by all the invited people.
    #a negative participation rate means more people were opposing the mob than agreening with it

    #Participation_Rate = (Act_Counter - Act_Against_Counter) / Mob_Practitioners
    Participation_Rate = (Act_Counter) / Mob_Practitioners

    #if the participation rate is greater than the threshold, its a successful Mob
    if (Participation_Rate >= (Success_Threshold / 100)):
        Mob_Result = "Success"
        Needed_Powerful_Actors = 0
    #else its a fail Mob and we need to calculate how much was needed to be successful
    else:
        Mob_Result = "Fail"
        #Needed_Powerful_Actors = (((Success_Threshold * Mob_Practitioners ) / 100)) - Act_Counter + Act_Against_Counter
        Needed_Powerful_Actors = (((Success_Threshold * Mob_Practitioners ) / 100)) - Act_Counter
        
    return Mob_Result, Needed_Powerful_Actors, Act_Counter, Withdraw_Counter, Power_Exchange_Counter, Act_Against_Counter, Participation_Rate

def SimulateManyMob(Practitioners, Threshold, Num_Simulation):
    num_Of_Success_Mob = 0
    num_Of_Fail_Mob = 0

    needed = 0
    
    print()
    print("{0:<15} {1:^22} {2:^15} {3:^15} {4:^22} {5:^15} {6:^15}".format("Mob Result", "Needed Powerful Actors", "Acted", "Withdraw", "Did NOT Power Exchange", "Act Against", "Participation Rate"))
    print("--------------------------------------------------------------------------------------------------------------------------------")
    
    # list to keep the result of each simulated mob
    individualMobRestulList = []
    
    #lets simulate many Mobs
    for Mob in range(Num_Simulation):
        #by calling simulate one multiple times
        result = SimulateOneMob(Practitioners, Threshold)
        CSVRow = [Threshold, result[0], result[1], result[2], result[3], result[4], result[5], result[6]*100]
        individualMobRestulList.append(CSVRow)
        #based on result we can check how many succeded, failed, and what was the needed Powerful Actors
        if (result[0] == "Success"):
            num_Of_Success_Mob = num_Of_Success_Mob + 1
            needed = needed + 0
        else:
            num_Of_Fail_Mob = num_Of_Fail_Mob + 1
            needed = needed + float(result[1])
        print("{0:<15} {1:^22} {2:^15} {3:^15} {4:^22} {5:^15} {6:^15}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))

    # calculate the average needed powerful actors
    Average_Needed_Powerful_Actors = (math.ceil(needed/num_Of_Fail_Mob)) if num_Of_Fail_Mob != 0 else 0
    
    # write the output to a CSV file
    writeIndividualMobStatToCSV(individualMobRestulList)
    
    return num_Of_Success_Mob, num_Of_Fail_Mob, Average_Needed_Powerful_Actors

def printStats(T_o, Num_Of_Mob_Success, Num_Of_Mob_Fail, Num_Simulation, Average_Needed_Powerful_Actors): 
    mobSuccessRate = round(((Num_Of_Mob_Success / Num_Simulation) * 100),2)
    mobFailRate = round(((Num_Of_Mob_Fail / Num_Simulation) * 100), 2)
    print()
    print("This program simulated ", Num_Simulation, "Mobs")
    print("The Mobs Success rate is ", mobSuccessRate, "%")
    print("The Mobs Fail rate is ", mobFailRate, "%")
    print("On Average you need at least", Average_Needed_Powerful_Actors, " more Powerful Actors to Succeed")
    writeOverAllStatToCSV([T_o, Num_Simulation, mobSuccessRate, mobFailRate, Average_Needed_Powerful_Actors])


def main():
    P, T_o, N_Sim = getInputs()
    Num_Of_Mob_Success, Num_Of_Mob_Fail, Needed = SimulateManyMob(P, T_o, N_Sim)
    printStats(T_o, Num_Of_Mob_Success, Num_Of_Mob_Fail, N_Sim, Needed)
    
main()

    
