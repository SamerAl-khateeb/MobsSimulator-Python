# A program to simulate a CFM using Monte Carlo
# methods and the Theory of Collective Action.
#Q: Given the number of participants, how many powerful
#   actors are needed to make a successful CFM?

from random import randrange
import math

def getInputs():
    CFM_Practitioners = int(input("Enter the Total Number of Invited CFM Practitioners: "))
    Success_Threshold = float(input("Enter the Threshold Value for a CFM to Success: ")) 
    Num_Of_Simulation = int(input("Enter the Number of Simulations (or Number of CFMs): "))

    return CFM_Practitioners, Success_Threshold, Num_Of_Simulation


def SimulateOneCFM(CFM_Practitioners, Success_Threshold):
    Act_Counter = 0
    Withdraw_Counter = 0
    Power_Exchange_Counter = 0
    Act_Against_Counter = 0

    Participation_Rate = 0
    
    Needed_Powerful_Actors = 0

    #for each participant lets examing what (s)he will do
    for participant in range(CFM_Practitioners):
        
        P_Interest = randrange(0,2)
        P_Control = randrange(0,2)
        
        #have interest and have control, practitioner will ACT
        if ((P_Interest == 1) and (P_Control == 1)):
            Act_Counter = Act_Counter + 1
            
        #have interest but no control, practitioner will ACT or WITHDRAW
        elif ((P_Interest == 1) and (P_Control == 0)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 1):
                Act_Counter = Act_Counter + 1
            else:
                Withdraw_Counter = Withdraw_Counter + 1
                
        #No interest but have control, practitioner will ACT or POWER EXCHANGE 
        elif ((P_Interest == 0) and (P_Control == 1)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 0):
                Withdraw_Counter = Withdraw_Counter + 1
            else:
                Power_Exchange_Counter = Power_Exchange_Counter + 1
            
        #No interest and No control, practitioner will WITHDRAW or ACT AGAINST
        elif ((P_Interest == 0) and (P_Control == 0)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 0):
                Withdraw_Counter = Withdraw_Counter + 1
            else:
                Act_Against_Counter = Act_Against_Counter + 1

    #once we examine each participant, lets see if the CFM succeed or Fail        
    Participation_Rate = (Act_Counter / CFM_Practitioners)

    #if the participation rate is greater than the threshold, its a successful CFM
    if (Participation_Rate >= (Success_Threshold / 100)):
        return "Success", 0, Act_Counter, Withdraw_Counter, Power_Exchange_Counter, Act_Against_Counter, Participation_Rate

    #else its a fail CFM and we need to calculate how much was needed to be successful
    else:
        Needed_Powerful_Actors = (((Success_Threshold * CFM_Practitioners ) / 100)) - Act_Counter
        return "Fail", Needed_Powerful_Actors, Act_Counter, Withdraw_Counter, Power_Exchange_Counter, Act_Against_Counter, Participation_Rate


def SimulateManyCFM(Practitioners, Threshold, Num_Simulation):
    num_Of_Success_CFM = 0
    num_Of_Fail_CFM = 0

    needed = 0

    print("{0:<15} {1:^22} {2:^15} {3:^15} {4:^15} {5:^15} {6:^15}".format("Result", "Needed Powerful Actors", "Acted", "Withdraw", "Power Exchange", "Acat Against", "Participation Rate"))
    print("-------------------------------------------------------------------------------------------------------------------------")

    #lets simulate many CFMs
    for cfm in range(Num_Simulation):
        #by calling simulate one multiple times
        result = SimulateOneCFM(Practitioners, Threshold)
        #based on result we can check how many succeded, failed, and what was the needed Powerful Actors
        if (result[0] == "Success"):
            num_Of_Success_CFM = num_Of_Success_CFM + 1
            needed = needed + 0
        else:
            num_Of_Fail_CFM = num_Of_Fail_CFM + 1
            needed = needed + float(result[1])
        print("{0:<15} {1:^22} {2:^15} {3:^15} {4:^15} {5:^15} {6:^15}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))

    Average_Needed_Powerful_Actors = math.ceil(needed/num_Of_Fail_CFM)

    return num_Of_Success_CFM, num_Of_Fail_CFM, Average_Needed_Powerful_Actors

def printStats(Num_Of_CFM_Success, Num_Of_CFM_Fail, Num_Simulation, Average_Needed_Powerful_Actors):
    print("This program simulated ", Num_Simulation, "Cyber Flash Mobs")
    print("The CFMs Success rate is ", round(((Num_Of_CFM_Success / Num_Simulation) * 100),2), "%")
    print("The CFMs Fail rate is ", round(((Num_Of_CFM_Fail / Num_Simulation) * 100), 2), "%")
    print("On Average you need at least", Average_Needed_Powerful_Actors, " more Powerful Actors to Succeed")
    


def main():
    P, T_o, N_Sim = getInputs()
    Num_Of_CFM_Success, Num_Of_CFM_Fail, Needed = SimulateManyCFM(P, T_o, N_Sim)
    printStats(Num_Of_CFM_Success, Num_Of_CFM_Fail, N_Sim, Needed)
    
main()

    
