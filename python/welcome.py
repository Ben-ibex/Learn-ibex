import numpy as np

# Example array with NaN and Inf values
data = np.array([1, 2, np.nan, 4, np.inf, 6, -np.inf])

print("Original Data:")
print(data)

# Check for NaN and Inf values
print("\nIs NaN:")
print(np.isnan(data))

print("\nIs Inf:")
print(np.isinf(data))

# Replace NaN with 0 and Inf with a finite value (e.g., 999)
cleaned_data = np.nan_to_num(data, nan=0, posinf=999, neginf=-999)
print("\nCleaned Data:")
print(cleaned_data)

# Compute statistics ignoring NaN values
data_with_nan = np.array([1, 2, np.nan, 4, 5])
mean_without_nan = np.nanmean(data_with_nan)  # Mean excluding NaN
sum_without_nan = np.nansum(data_with_nan)    # Sum excluding NaN

print("\nStatistics Ignoring NaN:")
print(f"Mean: {mean_without_nan}")
print(f"Sum: {sum_without_nan}")
