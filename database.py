from blood_calculator import HDL_analysis
print("This is the database.py file")
print("Python thinks this is called {}".format(__name__))

# import blood_calculator
# import blood_calculator as bc
# from blood_calculator import HDL_analysis as hdl_anal
# from blood_calculator import * --> to import everything in blood_calculator
# ^bad coding practice because it's not readable
# ^import blood_calculator as bc is preferred

HDL = 55
HDL_analysis_op = HDL_analysis(HDL)
print(f'HDL Analysis output: {HDL_analysis_op}')

# pycache - makes bytecode, runs bytecode
# intermediate copy of .py file stored
# you can delete these files, but it'll recreate it
# to get rid of your pycache
