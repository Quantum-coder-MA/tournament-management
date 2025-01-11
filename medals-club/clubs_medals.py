import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt 

mt = pd.read_excel("tournament_management.xlsx")
table1 = pd.read_excel("tournament_management.xlsx", sheet_name="medals-club")
def clubs_medals():
    plt.figure(figsize=(18, 10))
    x_positions = range(len(table1["club"]))  

    plt.bar([x - 0.25 for x in x_positions], table1["bronze"], width=0.25, label="bronze", color = "#cd7f32")
    plt.bar(x_positions, table1["silver"], width=0.25, label="silver", color = "silver")
    plt.bar([x + 0.25 for x in x_positions], table1["gold"], width=0.25, label="gold", color = "gold")

    plt.xticks(x_positions, table1["club"], rotation=45, fontsize=12)  

    plt.xlabel("Clubs", fontsize=14)
    plt.ylabel("number of medals", fontsize=14)
    plt.yticks(range(0, int(table1[["bronze", "silver", "gold"]].max().max()) + 1, 1)) 
    plt.title("clubs status", fontsize=16)
    plt.legend(fontsize=12)

    st.pyplot(plt)
