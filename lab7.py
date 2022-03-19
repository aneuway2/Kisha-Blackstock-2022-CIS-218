"""Calculate BMI and return Category
"""
import check
def calculate_bmi (weight, height):
    """Calculate the BMI from the height and the weight."""
    weight = float(weight)
    height = float(height)
    bmi = weight*703/(height*height)
    return round(bmi,1)

def test_calculate_bmi ():
    """Test calculation of BMI formula"""
    assert check.check (calculate_bmi (97, 61), 18.328)
    assert check.check (calculate_bmi (159, 67), 24.903)
    assert check.check (calculate_bmi (125, 56), 28.024)
    assert check.check (calculate_bmi (200, 69), 29.535)
    assert check.check (calculate_bmi (195, 65), 32.449)
    assert check.check (calculate_bmi (250, 73), 32.983)
    print ("all checks OK")

def bmi_to_cat (bmi):
    """Determine category after BMI calculation"""
    if bmi < 18.5:
        return "Underweight"
    if bmi >= 18.5 and bmi <= 25.0:
        return "Normal Weight"
    if bmi > 25.0 and bmi <= 30.0:
        return "Overweight"
    if bmi > 30.0:
        return "Obese"

def test_bmi_to_cat():
    """Test BMI Calculation"""
    assert bmi_to_cat(10) == "Underweight"
    assert bmi_to_cat(22) == "Normal Weight"
    assert bmi_to_cat(29) == "Overweight"
    assert bmi_to_cat(32) == "Obese"

def main ():
    """Input from user and return information on BMI"""
    test_calculate_bmi()
    test_bmi_to_cat()
    weight= input ("Please type in weight in pounds ")
    height= input ("Please type in height in inches ")
    bmi = calculate_bmi(weight, height)
    cat = bmi_to_cat(bmi)
    print ("Your BMI is", bmi, "Which is considered",cat)

if __name__ == "__main__":
    main()
