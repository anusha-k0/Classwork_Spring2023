import pytest

test_HDL = [(65, "Normal"),(45, "Borderline Low"),(20, "Low")]

@pytest.mark.parametrize("HDL_input, expected", test_HDL) #Decorates a function and gives it additional functionality
#^Decorator

def test_HDL_analysis(HDL_input, expected):
    from blood_calculator import HDL_analysis
    # Arrange
    #Act
    answer = HDL_analysis(HDL_input)
    #Assert
    assert answer == expected
    
    
test_LDL = [(100, "Normal"),(140, "Borderline High"),(175, "High"), (200, "Very High")]
@pytest.mark.parametrize("LDL_input, expected", test_LDL) #Decorates a function and gives it additional functionality
#^Decorator

def test_LDL_analysis(LDL_input, expected):
    from blood_calculator import LDL_analysis
    # Arrange
    #Act
    answer = LDL_analysis(LDL_input)
    #Assert
    assert answer == expected
    
#pytest can't input code, which is why we make 
# the inputs a separate function