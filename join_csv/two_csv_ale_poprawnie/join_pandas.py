#%% INNER
import pandas as pd
employee_df = pd.read_csv("employee.csv")
branch_df = pd.read_csv("branch.csv")

merged = pd.merge(employee_df, branch_df, on=["emp_id"])
merged

#%% LEFT
import pandas as pd
employee_df = pd.read_csv("employee.csv")
branch_df = pd.read_csv("branch.csv")

left_merged = pd.merge(employee_df, branch_df,
                        how="left", on=["emp_id"])
left_merged

# %% RIGHT
import pandas as pd
employee_df = pd.read_csv("employee.csv")
branch_df = pd.read_csv("branch.csv")

right_merged = pd.merge(employee_df, branch_df,
                        how="right", on=["emp_id"])
right_merged

# %%
