# %%
import pandas as pd
df = pd.read_csv(r"C:\Users\srika\OneDrive\Documents\York\Sem-1 york\MBAN 6110 - Data Science 1\Assignment 2\experiment_dataset.csv",index_col='Unnamed: 0')
print(df.shape)
df.head()

# %%
df.describe(include = 'all')

# %%
import seaborn as sns


# %%
# # group by location vs time spent & CTR
dflt = df.groupby('Location')['Time Spent'].sum()
dflt.head()


# %%
# # group by location vs time spent & CTR
dflc = df.groupby('Location')['CTR'].sum()
dflc.head()

# %%
# # group by device vs time spent & CTR
dfdt = df.groupby('Device')['Time Spent'].sum()
dfdt.head()

# %%
# # group by device vs time spent & CTR
dfdc = df.groupby('Device')['CTR'].sum()
dfdc.head()

# %%
# group by varient vs time spent & CTR
dfvt = df.groupby('Variant')['Time Spent'].sum()
dfvt.head()

# %%
# group by varient vs time spent & CTR
dfvc = df.groupby('Variant')['CTR'].sum()
dfvc.head()


# %%
import scipy.stats as stats
import pandas as pd

# Separate the data into separate groups
control_data = df[df['Variant'] == 'Control']['Time Spent']
variant_a_data = df[df['Variant'] == 'Variant A']['Time Spent']
variant_b_data = df[df['Variant'] == 'Variant B']['Time Spent']

# Perform a t-test between control and variant A
t_statistic_a, p_value_a = stats.ttest_ind(control_data, variant_a_data)

# Perform a t-test between control and variant B
t_statistic_b, p_value_b = stats.ttest_ind(control_data, variant_b_data)

# Compare the p-values to determine the best variant
if p_value_a < p_value_b:
    best_variant = 'Variant A'
    t_statistic = t_statistic_a
    p_value = p_value_a
else:
    best_variant = 'Variant B'
    t_statistic = t_statistic_b
    p_value = p_value_b

# Print the results
print("Variant A vs Control:")
print("  t-statistic:", t_statistic_a)
print("  p-value:", p_value_a)
print()
print("Variant B vs Control:")
print("  t-statistic:", t_statistic_b)
print("  p-value:", p_value_b)
print()
print("Best Variant:", best_variant)
print("  t-statistic:", t_statistic)
print("  p-value:", p_value)


# %%

# Separate the data into separate groups
control_data = df[df['Variant'] == 'Control']['CTR']
variant_a_data = df[df['Variant'] == 'Variant A']['CTR']
variant_b_data = df[df['Variant'] == 'Variant B']['CTR']

# Perform a t-test between control and variant A
t_statistic_a, p_value_a = stats.ttest_ind(control_data, variant_a_data)

# Perform a t-test between control and variant B
t_statistic_b, p_value_b = stats.ttest_ind(control_data, variant_b_data)

# Compare the p-values to determine the best variant
if p_value_a < p_value_b:
    best_variant = 'Variant A'
    t_statistic = t_statistic_a
    p_value = p_value_a
else:
    best_variant = 'Variant B'
    t_statistic = t_statistic_b
    p_value = p_value_b

# Print the results
print("Variant A vs Control:")
print("  t-statistic:", t_statistic_a)
print("  p-value:", p_value_a)
print()
print("Variant B vs Control:")
print("  t-statistic:", t_statistic_b)
print("  p-value:", p_value_b)
print()
print("Best Variant:", best_variant)
print("  t-statistic:", t_statistic)
print("  p-value:", p_value)





