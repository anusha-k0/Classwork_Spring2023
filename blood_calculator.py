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
   
interface()