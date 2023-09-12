import pandas as pd

ALL_PROJECTS_FILE = "C:/Users/adeli/Downloads/ME FYP and MEi Projects.xlsx"
FILTERED_PROJECTS_FILE = "C:/Users/adeli/Downloads/ME FYP and MEi Projects - filtered.xlsx"

df = pd.read_excel(ALL_PROJECTS_FILE)

# save only where FYP is not null
df = df[df["FYP"].notnull()]

with pd.ExcelWriter(FILTERED_PROJECTS_FILE) as writer:
    df.to_excel(writer, index=False)