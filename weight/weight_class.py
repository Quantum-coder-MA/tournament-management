import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt 
tc = pd.read_excel("tournament_management.xlsx")
table1 = pd.read_excel("tournament_management.xlsx", sheet_name="weight_class")

def weight_class():


    categories = table1["weight"].tolist()
    x_positions = range(len(categories))

  
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))  

    axes[0].bar(x_positions, table1["participant"], color='blue')
    axes[0].set_title('Bar Graph 1')
    axes[0].set_xlabel('Weight')
    axes[0].set_ylabel('Participants')
    axes[0].set_xticks(x_positions)
    axes[0].set_xticklabels(categories, rotation=45) 


    width = 0.4  
    axes[1].bar([x - width/2 for x in x_positions], table1["Homme"], width=width, color='blue', label='Homme')
    axes[1].bar([x + width/2 for x in x_positions], table1["Femme"], width=width, color='pink', label='Femme', alpha=0.7)
    axes[1].set_title('Bar Graph 2')
    axes[1].set_xlabel('Weight')
    axes[1].set_ylabel('Values')
    axes[1].set_xticks(x_positions)
    axes[1].set_xticklabels(categories, rotation=45)  
    axes[1].legend()

    plt.tight_layout()
    st.pyplot(fig)

