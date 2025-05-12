import pandas as pd
from tabulate import tabulate
import os
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", None)

#load the file excel
file_path = "Database_2025.xlsx"
df1 = pd.read_excel(file_path, sheet_name="PIVOT", engine="openpyxl", header=0)
df2 = pd.read_excel(file_path, sheet_name="Character_Role", engine="openpyxl", header=0)
merged_df = pd.merge(df1, df2, on=["Name", "Element"] , how="inner")


#search
def search_character(character_name):
    result = merged_df[merged_df['Name'].str.contains(character_name, case=False, na=False)]
    if not result.empty:
        for _, row in result.iterrows():
            print(f"Full Name: {row['Name']}")
            print(f"Weapon: {row['Weapon']}")
            print(f"Quality (star): {row['Quality (star)']}")
            print(f"Element: {row['Element']}")
            print(f"HP: {row['HP']}")
            print(f"ATK: {row['ATK']}")
            print(f"DEF: {row['DEF']}")

            roles = []
            if row['DPS'] == 'Yes':
                    roles.append('DPS')
            if row['On-field'] == 'Yes':
                    roles.append('On-field')
            if row['Off-field'] == 'Yes':
                    roles.append('Off-field')       
            if row['Support'] == 'Yes':
                    roles.append('Support') 
            if row['Survivability'] == 'Yes':
                    roles.append('Survivability')

            if roles:
                  print(f"Roles: {', '.join(roles)}")
            else:
                  print("Roles: None")
    else:
        print()
        print(f"Not found")


print()


# SEARCH LOOPING        
def ask_and_search():
      while True: 
        character_name = input("Enter the character name to search: ")
        search_character(character_name)
        answer = input ("Search another character? ").lower()
        if answer == 'no':
                print("Enjoy the game!")
                break
        else: 
                if answer !='yes':
                        print("ANSWER WITH YES OR NO!")
                        break 

ask_and_search()
