import numpy as np

print("=========================================================")
print("== Problem 1 ============================================")
print("=========================================================")

''' Problem 1 '''
# Generate 2D data array
data = np.random.normal(loc=-1, scale=1.5, size=(1000, 800))

# Set approximately 10% of the data points to NaN
nan_indices = np.random.choice(
    data.size, 
    size=int(0.1 * data.size), 
    replace=False
)
for i in nan_indices:
    data[i // 800][i % 800] = np.nan

print("Original data shape:", data.shape)
print("Number of NaNs:", np.isnan(data).sum())

print("=========================================================")
print("== Problem 2 ============================================")
print("=========================================================")

''' Problem 2 '''
avg = np.nanmean(data)
for i in nan_indices:
    data[i // 800][i % 800] = avg
print("Mean after inputing NaNs: ", np.mean(data))
print("Std after inputing NaNs: ", np.std(data))

avg = np.mean(data)
std = np.std(data)
data_norm = np.zeros(shape=(1000, 800))
for i in range(1000):
    for j in range(800):
        data_norm[i][j] = (data[i][j] - avg) / std
avg_norm = np.mean(data_norm)
std_norm = np.std(data_norm)
print("Mean after Norm: ", avg_norm)
print("Std after Norm: ", std_norm)

print("=========================================================")
print("== Problem 3 ============================================")
print("=========================================================")

''' Problem 3 '''
filtered_data = data_norm[data_norm > avg_norm]
print("Number of elements greater than mean: ", len(filtered_data))
print("First 10 selected elements: ", filtered_data[:10])

print("=========================================================")
print("== Problem 4 ============================================")
print("=========================================================")

''' Problem 4 '''
filtered_data *= 2
filtered_data[filtered_data < 1] = 0
filtered_data = filtered_data[:320000]
filtered_data = filtered_data.reshape(200, 1600)
print("First 10 selected elements: ", filtered_data[0][:10])
print("New shape of filtered_data: ", filtered_data.shape)
