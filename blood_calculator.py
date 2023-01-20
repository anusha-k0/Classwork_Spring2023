def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Options: ")
        print("9 - Quit")
        choice = input("Select an option: ")
        if choice == "9":
            keep_running = False
    print("Program ended!")
    
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