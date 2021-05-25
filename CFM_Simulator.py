# A program to simulate a CFM using Monte Carlo
# methods and the Theory of Collective Action.
#Q: Given the following parameters (Number of Invited
#   CFM Practitioners, the Threshold Value of Success CFM,
#   the Number of Simulations, the Number of Powerful Actors)
#   what is the chance a CFM will be successful?

from random import randrange

def getInputs():
    CFM_Practitioners = int(input("Enter the Total Number of Invited CFM Practitioners: "))
    Success_Threshold = float(input("Enter the Threshold Value for a CFM to Success: ")) / 100
    Num_Of_Simulation = int(input("Enter the Number of Simulations (or Number of CFMs): "))
    Num_Of_Powerful_Actors = int(input("Enter the Number of Powerful Actors: "))

    return CFM_Practitioners, Success_Threshold, Num_Of_Simulation, Num_Of_Powerful_Actors

def SimulateOneCFM(CFM_Practitioners, Success_Threshold, Num_Powerful_Actors):
    Act_Counter = 0
    Withdraw_Counter = 0
    Power_Exchange_Counter = 0
    Act_Against_Counter = 0
    Participation_Rate = 0
    
    for participant in range(CFM_Practitioners - Num_Powerful_Actors):
        
        P_Interest = randrange(0,2)
        P_Control = randrange(0,2)
        
        #have interest and have control, practitioner will act
        if ((P_Interest == 1) and (P_Control == 1)):
            Act_Counter = Act_Counter + 1
            
        #have interest but no control, practitioner will act or withdraw
        elif ((P_Interest == 1) and (P_Control == 0)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 1):
                Act_Counter = Act_Counter + 1
            else:
                Withdraw_Counter = Withdraw_Counter + 1
                
        #No interest but have control, practitioner will act or withdraw 
        elif ((P_Interest == 0) and (P_Control == 1)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 0):
                Withdraw_Counter = Withdraw_Counter + 1
            else:
                Power_Exchange_Counter = Power_Exchange_Counter + 1
            
        #No interest and No control, practitioner will withdraw or Act Against
        elif ((P_Interest == 0) and (P_Control == 0)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 0):
                Withdraw_Counter = Withdraw_Counter + 1
            else:
                Act_Against_Counter = Act_Against_Counter + 1
            
    Participation_Rate = ((Act_Counter + Num_Powerful_Actors) / CFM_Practitioners)

    if (Participation_Rate >= Success_Threshold):
        return "Success", Num_Powerful_Actors, Act_Counter, Withdraw_Counter, Power_Exchange_Counter, Act_Against_Counter, Participation_Rate
    else:
        return "Fail", Num_Powerful_Actors, Act_Counter, Withdraw_Counter, Power_Exchange_Counter, Act_Against_Counter, Participation_Rate


def SimulateManyCFM(Practitioners, Threshold, Num_Simulation, Num_Powerful_Actors):
    num_Of_Success_CFM = 0
    num_Of_Fail_CFM = 0
    Total_Participation_Rate = 0

    print("{0:<15} {1:^22} {2:^15} {3:^15} {4:^15} {5:^15} {6:^15}".format("Result", "Number of Powerful Actors", "Acted", "Withdraw", "Power Exchange", "Acat Against", "Participation Rate"))
    print("----------------------------------------------------------------------------------------------------------------------------")
    
    for cfm in range(Num_Simulation):
        result = SimulateOneCFM(Practitioners, Threshold, Num_Powerful_Actors)
        
        if (result[0] == "Success"):
            num_Of_Success_CFM = num_Of_Success_CFM + 1
        elif (result[0] == "Fail"):
            num_Of_Fail_CFM = num_Of_Fail_CFM + 1
        print("{0:<15} {1:^22} {2:^15} {3:^15} {4:^15} {5:^15} {6:^15}".format(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))

        Total_Participation_Rate = Total_Participation_Rate + result[6]

    Avg_Participation_Rate = Total_Participation_Rate/Num_Simulation

    return num_Of_Success_CFM, num_Of_Fail_CFM, Avg_Participation_Rate
        
def printStats(Num_Of_CFM_Success, Num_Of_CFM_Fail, Num_Simulation, Avg_Participation_Rate):
    print("This program simulated ", Num_Simulation, "Cyber Flash Mobs")
    print("The CFMs Success rate is ", round(((Num_Of_CFM_Success / Num_Simulation) * 100),2), "%")
    print("The CFMs Fail rate is ", round(((Num_Of_CFM_Fail / Num_Simulation) * 100), 2), "%")
    print("The Average Participation Rate is ", round(((Avg_Participation_Rate) * 100), 2), "%")


def main():
    P, T_o, N_Sim, N_Pow_Act = getInputs()
    Num_Of_CFM_Success, Num_Of_CFM_Fail, Avg_Participation_Rate = SimulateManyCFM(P, T_o, N_Sim, N_Pow_Act)
    printStats(Num_Of_CFM_Success, Num_Of_CFM_Fail, N_Sim, Avg_Participation_Rate)
    
main()
