import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt 
tc = pd.read_excel("tournament_management.xlsx")
table1 = pd.read_excel("tournament_management.xlsx", sheet_name="technique")
def technique():
    plt.figure(figsize=(20, 10))


    x_positions = range(len(table1["technique"]))  

    plt.bar([x + 0.20 for x in x_positions], table1["win"], width=0.2, label="win", color="blue")
    plt.bar(x_positions, table1["lose"], width=0.2, label="lose", color="red")

    plt.xticks(x_positions, table1["technique"], fontsize=16)
    plt.title("win rate by Technique", fontsize=20, color="red")
    plt.legend(fontsize=12)
    plt.xlabel("technique used", fontsize=16, color="blue")
    plt.ylabel("performance", fontsize=16, color="blue")


    st.pyplot(plt)