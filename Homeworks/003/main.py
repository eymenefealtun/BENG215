from statistics import stdev
import matplotlib.pyplot as plt

import numpy as np

# handling the file and lines
file = open("TFbinding-HW3-F23.txt", "r")
lines = file.readlines()
lines.pop(0)

gene_name = []
nanos = []
oct_4 = []
sox_2 = []
stat_3 = []
c_myc = []
klf_4 = []
expression_level = []

mean_expression = 0
standard_deviation_expression = 0
total_binding_scores = {}
mean_total_binding = 0
standard_deviation_total_binding = 0

# values are filled from the txt file
for i in range(len(lines)):
    vls = lines[i].split()
    gene_name.append(str(vls[0]))
    nanos.append(float(vls[1]))
    oct_4.append(float(vls[2]))
    sox_2.append(float(vls[3]))
    stat_3.append(float(vls[4]))
    c_myc.append(float(vls[5]))
    klf_4.append(float(vls[6]))
    expression_level.append(float(vls[7]))


def calculate_mean(given_list):
    sum = 0
    for ele in given_list:
        sum += ele
    return round(sum / len(given_list), 2)


def calculate_total_binding():
    def get_sum(j):
        return round(nanos[j] + oct_4[j] + sox_2[j] + stat_3[j] + c_myc[j] + klf_4[j], 2)

    temp_dict_total_binding = {}
    for i in range(len(gene_name)):
        temp_dict_total_binding[gene_name[i]] = get_sum(i)
    return temp_dict_total_binding


mean_expression = calculate_mean(expression_level)
standard_deviation_expression = round(stdev(expression_level), 2)

total_binding_scores = calculate_total_binding()

mean_total_binding = calculate_mean(list(total_binding_scores.values()))
standard_deviation_total_binding = round(stdev(list(total_binding_scores.values())), 2)

# step 4
bins = np.linspace(0, 1, 20)
fig, ax = plt.subplots(1, 2, figsize=(12,6))
# handle first plot
ax[0].set_ylabel('Frequency')
ax[0].set_xlabel('Expression Level')
ax[0].set_title("Expression Levels")
ax[0].hist(expression_level, bins = 12, alpha=0.5, color='r')
ax[0].axvline(mean_expression, color='green', linestyle='dashed', linewidth=3, label=f'Mean: {mean_expression:.2f}')
ax[0].axvline(mean_expression + standard_deviation_expression, color='red', linestyle='dashed', linewidth=3, label=f'Std: {standard_deviation_expression:.2f}')
ax[0].legend()


# handle second plot
ax[1].set_ylabel('Frequency')
ax[1].set_xlabel('Total Binding Score')
ax[1].set_title("Total Binding Scores")
ax[1].hist(list(total_binding_scores.values()), bins = 12, alpha=0.5, color='g')
ax[1].axvline(mean_total_binding, color='green', linestyle='dashed', linewidth=3, label=f'Mean: {mean_total_binding:.2f}')
ax[1].axvline(mean_total_binding + standard_deviation_total_binding, color='red', linestyle='dashed', linewidth=3, label=f'Std: {standard_deviation_total_binding:.2f}')
ax[1].legend()



data = 20
x = np.arange(data)
y = np.arange(data)

m, b  = np.polyfit(list(total_binding_scores.values()), expression_level, 1)


ax[0].plot(x, y, 'yo', x, m*x+b, '--k')
ax[1].plot(x, y, 'yo', x, m*x+b, '--k')



# Linear regression equation: Expression_Level = a + b * Total_binding_score

# Predicted Expression Levels
total_binding_scores_integer_list = []
for i in total_binding_scores.values():
    total_binding_scores_integer_list.append(int(i))


predicted_expression = m + b * total_binding_scores_integer_list

# Calculate errors
errors = expression_level - predicted_expression

# Add errors to DataFrame
prediction_error = errors

# Print DataFrame
print(f"{total_binding_scores},{expression_level} ,{prediction_error}")


plt.show()

