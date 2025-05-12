import pandas as pd

# Load CSV
df = pd.read_csv('math_operations.csv')

# Invert pixel columns: 255 - pixel_value
pixel_cols = [col for col in df.columns if col.startswith('pixel')]
df[pixel_cols] = 255 - df[pixel_cols]

# Optional: Save the inverted version
df.to_csv('math_operations_inverted.csv', index=False)

print("Inversion complete. File saved as 'math_operations_inverted.csv'")
