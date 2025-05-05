# Data 
experience = [3, 8, 9, 13, 3, 6, 11, 21, 1, 16] 
salary =     [30, 57, 64, 72, 36, 43, 59, 90, 20, 83] 
 
# Step 1: Calculate means 
n = len(experience) 
mean_x = sum(experience) / n 
mean_y = sum(salary) / n 
 
# Step 2: Calculate slope (m) and intercept (c) 
numerator = sum((experience[i] - mean_x) * (salary[i] - mean_y) for i in 
range(n)) 
denominator = sum((experience[i] - mean_x) ** 2 for i in range(n)) 
m = numerator / denominator 
c = mean_y - m * mean_x 
# Step 3: Predict salary for 10 years of experience 
x_new = 10 
y_pred = m * x_new + c 
# Output 
print("Slope (m):", m) 
print("Intercept (c):", c) 
print("Predicted Salary for 10 years experience:", y_pred)
