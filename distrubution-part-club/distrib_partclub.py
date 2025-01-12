import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt 
tc = pd.read_excel("tournament_management.xlsx")
table1 = pd.read_excel("tournament_management.xlsx", sheet_name="club-part")
def club_part():
    plt.figure(figsize=(20, 10))

    categories = table1["club"].tolist()
    x_positions = range(len(categories))

  
    
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))  

    axes[0].bar(x_positions, table1["participant"], color='blue')
    axes[0].set_title('Participant par club', fontsize=18 , color = 'red' )
    axes[0].set_xlabel('club', fontsize=18)
    axes[0].set_ylabel('Participants')
    axes[0].set_xticks(x_positions)
    axes[0].set_xticklabels(categories) 


    width = 0.4  
    axes[1].bar([x - width/2 for x in x_positions], table1["Homme"], width=width, color='blue', label='Homme')
    axes[1].bar([x + width/2 for x in x_positions], table1["Femme"], width=width, color='pink', label='Femme', alpha=0.7)
    axes[1].set_title(' graphique sexe', fontsize=18 , color = 'red')
    axes[1].set_xlabel('club' , fontsize=18)
    axes[1].set_ylabel('Values')
    axes[1].set_xticks(x_positions )
    axes[1].set_xticklabels(categories)  
    axes[1].legend()

    plt.tight_layout()
    st.pyplot(fig)

