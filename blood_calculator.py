#Main
def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Options: ")
        print("Option - 1: HDL")
        print("9 - Quit")
        choice = input("Select an option: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            total_cholestrol_driver()
    print("Program ended!")

#HDL analysis 
def HDL_driver():
    HDL_in = HDL_input()
    HDL_analys = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_analys)

def HDL_input():
    HDL_value = int(input("Enter the HDL result:"))
    return HDL_value
   
def HDL_analysis(HDL_int):
    if HDL_int >=60:
        answer = "Normal"
    elif 40>HDL_int>60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer
    
def HDL_output(HDL_value, HDL_analys):
    print(f'The HDL result of {HDL_value} is considered {HDL_analys}')
    return
    
#LDL Analysis
def LDL_driver():
    LDL_in = int(input("Enter the LDL result: "))
    LDL_analys = LDL_analysis(LDL_in)
    print(f'The LDL result of {LDL_in} is considered {LDL_analys}')
    return
 
def LDL_analysis(LDL_input):
    if LDL_input <130:
        answer = "Normal"
    elif 130<LDL_input<160:
        answer = "Borderline High"
    elif 160<LDL_input<189:
        answer = "High"
    else:
        answer = "Very High"
    return answer
    
#Total Cholestrol Analysis
def total_cholestrol_driver():
    tot_chol = int(input("Enter Total Cholestrol result: "))
    tot_chol_analys = tot_cholestrol_analysis(tot_chol)
    print(f'A total cholestrol result of {tot_chol} is considered {tot_chol_analys}')
    
def tot_cholestrol_analysis(total_cholestrol):
    if total_cholestrol<200:
        answer = "Normal"
    elif 200<=total_cholestrol<239:
        answer = "Borderline High"
    else:
        answer = "High"
    return answer
    
interface()