data = [ 
    ['Yes', 'No', 'Yes'], 
    ['No', 'Yes', 'Yes'], 
    ['Yes', 'Yes', 'Yes'], 
    ['No', 'No', 'No'], 
    ['Yes', 'No', 'Yes'], 
    ['No', 'No', 'Yes'], 
    ['Yes', 'No', 'Yes'], 
    ['Yes', 'No', 'No'], 
    ['No', 'Yes', 'Yes'], 
    ['No', 'Yes', 'No'], 
] 
 
from collections import defaultdict 
 
# Count classes 
yes = sum(1 for row in data if row[2] == 'Yes') 
no = len(data) - yes 
total = yes + no 
 
# Feature counts 
counts = { 
    'Covid': {'Yes': defaultdict(int), 'No': defaultdict(int)}, 
    'Flu': {'Yes': defaultdict(int), 'No': defaultdict(int)} 
} 
 
for row in data: 
    covid, flu, fever = row 
    counts['Covid'][fever][covid] += 1 
    counts['Flu'][fever][flu] += 1 
 
def predict(covid, flu): 
    # Prior probabilities 
    p_yes = yes / total 
    p_no = no / total 
 
    # Likelihoods without smoothing 
    try: 
        covid_yes = counts['Covid']['Yes'][covid] / yes 
        flu_yes = counts['Flu']['Yes'][flu] / yes 
        p_yes *= covid_yes * flu_yes 
    except ZeroDivisionError: 
        p_yes = 0 
 
    try: 
        covid_no = counts['Covid']['No'][covid] / no 
        flu_no = counts['Flu']['No'][flu] / no 
        p_no *= covid_no * flu_no 
    except ZeroDivisionError: 
        p_no = 0 
 
    print(f"\nInput: Covid={covid}, Flu={flu}") 
    print(f"P(Fever=Yes): {p_yes:.5f}") 
    print(f"P(Fever=No):  {p_no:.5f}") 
 
    return 'Yes' if p_yes > p_no else 'No' 
 
# Tests 
print("Predicted Fever:", predict('Yes', 'Yes'))  
