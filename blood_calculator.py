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
 
interface()