## Interpolation fills missing values by estimating them
# based on surrounding known values (linear interpolation by default)
import pandas as pd

df = pd.DataFrame({
    "Day": [1, 2, 3, 4, 5, 6],
    "Sales": [100, None, None, 160, None, 220]
})
print("Before Interpolation:")
print(df)

print("After Interpolation:")
df["Sales"] = df["Sales"].interpolate()
print(df)
