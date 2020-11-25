# A program to simulate a CFM using Monte Carlo
# methods and the Theory of Collective Action.

from random import randrange

def getInputs():
    CFM_Practitioners = int(input("Enter the Total Number of Invited CFM Practitioners "))
    Success_Threshold = float(input("Enter the Threshold Value for a CFM to Success ")) / 100
    Num_Of_Simulation = int(input("Enter the Number of Simulations or Number of CFMs "))
    Num_Of_Powerful_Actors = int(input("Enter the Number of Powerful Actors "))

    return CFM_Practitioners, Success_Threshold, Num_Of_Simulation, Num_Of_Powerful_Actors


def SimulateOneCFM(CFM_Practitioners, Success_Threshold, Num_Powerful_Actors):
    Act_Counter = Num_Powerful_Actors
    Withdraw_Counter = 0
    Power_Exchange_Counter = 0
    Act_Against_Counter = 0
    Participation_Rate = 0
    
    
    for participant in range(CFM_Practitioners):
        
        P_Interest = randrange(0,2)
        P_Control = randrange(0,2)
        
        #have interest and have control, practitioner will act
        if ((P_Interest == 1) and (P_Control == 1)):
            Act_Counter = Act_Counter + 1
            
        #have interest but no control, practitioner will act or withdraw
        if ((P_Interest == 1) and (P_Control == 0)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 0):
                Act_Counter = Act_Counter + 1
            else:
                Withdraw_Counter = Withdraw_Counter + 1
                
        #No interest but have control, practitioner will act or withdraw 
        if ((P_Interest == 0) and (P_Control == 1)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 1):
                Withdraw_Counter = Withdraw_Counter + 1
            else:
                Power_Exchange_Counter = Power_Exchange_Counter + 1
            
        #No interest and No control, practitioner will withdraw or Act Against
        if ((P_Interest == 0) and (P_Control == 0)):
            Participant_Decision = randrange(0,2)
            if (Participant_Decision == 1):
                Withdraw_Counter = Withdraw_Counter + 1
            else:
                Act_Against_Counter = Act_Against_Counter + 1
            
    Participation_Rate = Act_Counter / CFM_Practitioners

    if (Participation_Rate > Success_Threshold):
        return "Success"
    else:
        return "Fail"
        


def SimulateManyCFM(Practitioners, Threshold, Num_Simulation, Num_Powerful_Actors):
    num_Of_Success_CFM = 0
    num_Of_Fail_CFM = 0
    
    for cfm in range(Num_Simulation):
        result = SimulateOneCFM(Practitioners, Threshold, Num_Powerful_Actors)
        if (result == "Success"):
            num_Of_Success_CFM = num_Of_Success_CFM + 1
        else:
            num_Of_Fail_CFM = num_Of_Fail_CFM + 1

    return num_Of_Success_CFM, num_Of_Fail_CFM
        


def printStats(Num_Of_CFM_Success, Num_Of_CFM_Fail, Num_Simulation):
    print("This program simulated ", Num_Simulation, "Cyber Flash Mobs")
    print("The CFMs Success rate is ", round(((Num_Of_CFM_Success / Num_Simulation) * 100),3), "%")
    print("The CFMs Fail rate is ", round(((Num_Of_CFM_Fail / Num_Simulation) * 100), 3), "%")



def main():
    P, T_o, N_Sim, N_Pow_Act = getInputs()
    Num_Of_CFM_Success, Num_Of_CFM_Fail = SimulateManyCFM(P, T_o, N_Sim, N_Pow_Act)
    printStats(Num_Of_CFM_Success, Num_Of_CFM_Fail, N_Sim)
    
main()
