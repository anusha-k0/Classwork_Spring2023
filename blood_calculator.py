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
 
interface()