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
    print("Program ended!")

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
interface()