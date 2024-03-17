"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Stress Detection by AAP")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
            Stress has a significant impact on brain health and can contribute to the development and progression of various brain diseases.
<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
Key points which is given below :-<br><br>
✅Effects on Brain Structure: Prolonged stress can lead to structural changes in the brain, including a reduction in the volume of certain brain regions, such as the hippocampus, which is involved in memory and emotion regulation.<br>✅Neurotransmitter Imbalance: Stress disrupts the balance of neurotransmitters, such as serotonin and dopamine, which play essential roles in mood regulation and cognitive function. This imbalance can contribute to mood disorders like depression and anxiety.<br>✅Inflammation and Oxidative Stress: Chronic stress triggers inflammatory responses and increases oxidative stress in the brain, leading to damage to neurons and impaired cognitive function. These processes are implicated in neurodegenerative diseases like Alzheimer's and Parkinson's.<br>✅Altered Neural Circuits: Stress can alter neural circuits involved in emotion processing and stress regulation, leading to dysregulation of the stress response system. This can exacerbate anxiety disorders and post-traumatic stress disorder (PTSD).<br>✅Impact on Neuroplasticity: Stress impairs neuroplasticity, the brain's ability to adapt and reorganize in response to experiences. This can hinder learning, memory formation, and recovery from brain injuries or strokes.
<p style="font-size:20px;background-color:gray;text-align:left;padding:12px;border-radius:13px">
🛑🛑In summary, managing stress is crucial for maintaining brain health and reducing the risk of developing brain diseases. Strategies such as relaxation techniques, regular exercise, adequate sleep, social support, and seeking professional help when needed can help mitigate the detrimental effects of stress on the brain.🛑🛑
        </p>
    """, unsafe_allow_html=True)