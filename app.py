# %%
import streamlit as st 
# %%
st.title("One Page Briefing for `Aramco`")
overview = st.container()
stockMarket = st.container()
potentialProjects = st.container()
chatbot = st.container()
news = st.container()
# %%
with overview: 
    st.header("Aramco's Overview")
    st.write("Aramco is a major player in the global energy market and is committed to providing reliable, affordable, and sustainable energy to the world. The company is also investing in new technologies to develop cleaner and more sustainable energy sources. Aramco is a leading force in the global economy and is playing a key role in the energy transition.  ")
    with st.expander("Key Facts"): 
        st.write("""
    - Founded in 1933
    - Headquarters in Dhahran, Saudi Arabia
    - Employees: over 70,000
    - Proven oil reserves: 338.43 billion barrels
    - Natural gas reserves: 290 trillion cubic feet
    - Revenue (2022): $446.3 billion""")
        
with stockMarket: 
    st.header("Finatial Details")
    tab1, tab2 = st.tabs(["market capitalization", "Aramco's Shareholders"])
    with tab1:
        st.write("Aramco has a market capitalization of ` 2.49 trillion SAR`. This gives it a market share of about 40% of the Tadawu")
    with tab2: 
        st.metric(label="The government of Saudi Arabia", value="94%")
        st.metric(label="Public Shareholders   ", value="6%")
        
with potentialProjects: 
    st.header("What's the potential projects ?")
    with st.expander("Expansion of the Marjan and Berri oilfields"): 
        st.write("""
   These two offshore oilfields are the largest in Saudi Arabia. Aramco plans to expand production capacity at these fields by 550,000 barrels per day by 2025.""")
    with st.expander("Development of the Hail and Ghawar oilfields"): 
        st.write("""
                 These two onshore oilfields are also major producers for Aramco. The company plans to invest in enhanced oil recovery (EOR) projects at these fields to maintain production levels.
    """)
    with st.expander("Investment in renewable energy"): 
        st.write("""
Aramco is investing in renewable energy projects, such as solar and wind power. The company plans to have 50 gigawatts of renewable energy capacity by 2030""")
with news: 
    st.header("Aramco's Latest News ")
  
with chatbot:
    st.header("What do you want to know more about `ARAMCO`")
    st.text('This chatbot will build using Genai and LLMs services')
    prompt = st.text_input('Ask for more info')
