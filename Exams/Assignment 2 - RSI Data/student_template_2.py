"""
CULMINATING ASSIGNMENT 2: RSI

Create a program which will provide answers to the tasks posed in the assignment description.

For this assignment, you will start from scratch with this blank template.
It is your reponsibility to include all necessary program components in this file.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.

The relevant data file is named "all_participant_data_rsi.csv" and is located in data > drop-jump.

All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the data from the RSI CSV file 
data_path = os.path.join(
    os.path.dirname(__file__), # Get the directory of the current file
    "..", "..", "data", "drop-jump",
    "all_participant_data_rsi.csv"  # Relative path to the CSV file
)

df = pd.read_csv(data_path)

# Extract the paired RSI measuremets 
force_plate = df["force_plate_rsi"]
accelerometer = df["accelerometer_rsi"]

# TASK 1: Paired t-test
# H0: The mean difference between methods is zero.
# H1: The mean difference between methods is not zero.
alpha = 0.05

# Perform the paired t-test
t_stat, p_value = stats.ttest_rel(force_plate, accelerometer)

print("Task 1: Paired T-Test")
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

# Interpret the results
if p_value < alpha:
    print("Reject the null hypothesis. There is a significant difference between the two methods.")
else:    
    print("Fail to reject the null hypothesis. No statistically significant mean difference was detected.")

# Filter the dataset to include only Participant F
participant_f = df[df["trial"].str.startswith("F_trial_")]

print(f"Number of trials for Participant F: {len(participant_f)}")

# TASK 2: Normal Distribution and Chi-Square Goodness-of-Fit Test

# Fit a normal distribution to the accelerometer RSI data
mean, std = stats.norm.fit(accelerometer)

# Create 5 bins with equal expected probabilities
num_bins = 5

bin_edges = stats.norm.ppf(np.linspace(0, 1, num_bins + 1),loc=mean, scale=std)

# Count the observed RSI values in each bin
observed, _ = np.histogram(accelerometer, bins=bin_edges)

# Calculate the expected counts
expected = np.full(num_bins, len(accelerometer) / num_bins)

# Conduct Chi-Square Goodness-of-Fit Test
# Subtract 2 degrees of freedom for estimated mean and std
chi2_stat, p_chi2 = stats.chisquare(f_obs=observed, f_exp=expected, ddof=2)

print("\nTask 2: Chi-Square Goodness-of-Fit Test")
print(f"Mean RSI: {mean:.4f}")
print(f"Standard Deviation: {std:.4f}")
print(f"Chi-Square Statistic: {chi2_stat:.4f}")
print(f"P-value: {p_chi2:.4f}")

if p_chi2 < alpha:
    print("Reject the null hypothesis.")
    print("The normal distribution is not a good fit.")
else:
    print("Fail to reject the null hypothesis.")
    print("The normal distribution is a plausible fit.")

# Plot histogram with fitted normal distribution
plt.figure(figsize=(8, 5))

plt.hist(accelerometer, bins=10, density=True, alpha=0.6, edgecolor="black", label="Accelerometer RSI")

x = np.linspace(accelerometer.min(), accelerometer.max(), 200)
y = stats.norm.pdf(x, loc=mean, scale=std)

plt.plot(x, y, color="red", label="Normal Distribution")

plt.xlabel("Reactive Strength Index (RSI)")
plt.ylabel("Probability Density")
plt.title("Accelerometer RSI Normal Distribution Fit")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

expected = np.full(num_bins, len(accelerometer) / num_bins)

# Verify expected frequencies for Chi-square test
print(f"Number of observations: {len(accelerometer)}")
print(f"Expected frequencies: {expected}")

if np.all(expected >= 5):
    print("Expected frequency requirement is satisfied.")
else:
    print("Expected frequency requirement is not satisfied.")
# TASK 3: Participant F Confidence Intervals

# Filter the dataset to include only Participant F
participant_f = df[df["trial"].str.startswith("F_trial_")]

# Print the filtered dataframe
print("\nTask 3: Participant F RSI Data")
print(participant_f)

# Extract Participant F's RSI measurements
f_force_plate = participant_f["force_plate_rsi"]
f_accelerometer = participant_f["accelerometer_rsi"]

# Calculate 95% confidence intervals
confidence_level = 0.95

# Force plate calculations
fp_mean = np.mean(f_force_plate)
fp_sem = stats.sem(f_force_plate)

fp_ci = stats.t.interval( confidence_level, df=len(f_force_plate) - 1, loc=fp_mean, scale=fp_sem)

# Accelerometer calculations
acc_mean = np.mean(f_accelerometer)
acc_sem = stats.sem(f_accelerometer)

acc_ci = stats.t.interval(confidence_level, df=len(f_accelerometer) - 1, loc=acc_mean, scale=acc_sem)

# Print results
print("\nParticipant F: 95% Confidence Intervals")

print(f"Force Plate Mean RSI: {fp_mean:.4f}")
print(f"Force Plate 95% CI: ({fp_ci[0]:.4f}, {fp_ci[1]:.4f})")

print(f"Accelerometer Mean RSI: {acc_mean:.4f}")
print(f"Accelerometer 95% CI: ({acc_ci[0]:.4f}, {acc_ci[1]:.4f})")
