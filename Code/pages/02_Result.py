import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd


def EnergyOutput():
    if "SolarPVResult" not in st.session_state:
        st.session_state.TotalConsumption = 0
        st.session_state.SolarPVResult = 0
        st.session_state.storagebattery = 0
        st.session_state.TotalArea = 0
        st.session_state.introducespv = 0

    # res capacity on site
    # assumption is that the area effective is 80 percent
    # second assumption is that the capacity of 1 solar pv is 500 Watt (0.5KW)
    Rescapacity = 0
    if st.session_state.introducespv == 0:
        Rescapacity = st.session_state.TotalArea*0.8*0.5
    elif st.session_state.TotalArea == 0:
        Rescapacity = st.session_state.introducespv

    # annual energy generation
    AnnualGeneration = st.session_state.SolarPVResult*Rescapacity

    # total storage capacity on site
    StorageCapacity = st.session_state.storagebattery*Rescapacity

    # Total Consumption of the community
    TotalConsumption = st.session_state.TotalConsumption

    # Energy Savings
    if StorageCapacity == 0:
        EnergySavings = 0.7 * AnnualGeneration
    else:
        EnergySavings = AnnualGeneration

    # Energy remain or deficit
    Energyremain = EnergySavings - TotalConsumption

#     # return [Rescapacity, StorageCapacity, AnnualGeneration, TotalConsumption, EnergySavings]
    return StorageCapacity, Rescapacity, AnnualGeneration, TotalConsumption, Energyremain, EnergySavings


def EconomyOutput(Power, Battery, energySaving):
    # Initial investment, ROI, PREPEX, CAPEX, OPEX
    # Assumption that each KWP of solar PV is 1200 euros
    # invest value
    capex = (Power*1200)+(500*Battery)
    # OPEX value
    opex = 0.03*capex
    # SAVINGS (€) = Energy Savings (kWh) * Energy Price (€/kWh) - OPEX
    savings = (energySaving * 0.25) - opex
    # the Introduce PAYBACK = total investment/(savings per year)
    if savings == 0 or capex == 0:
        payback = 0
    else:
        payback = capex/savings

    return capex, opex, savings, payback


def ClassificationOutput(Energyres):
    if Energyres > 0:
        resEnergy = str(Energyres)
        st.success(
            "The energy communities is self-sufficient")
    elif Energyres < 0:
        resEnergy = str(Energyres)
        st.warning(
            "The community is still in shortage of energy")


st.title("The Result of Energy Communities")
EnergyResult = EnergyOutput()
st.subheader("Energy Output")
#     Energy output result barchart
energydata = pd.DataFrame(
    np.array([[EnergyResult[2], 0, 0, 0], [
             0, EnergyResult[3], 0, 0], [0, 0, EnergyResult[5], 0], [0, 0, 0, EnergyResult[4]]]),
    columns=["E. Generated(kWh)", "E. Consumption(kWh)", "E. Savings(kWh)", "E. Remain/Needed(kWh)"],  index=["Generated", "Consumption", "Savings", "(+)Remain / (-)Needed"])
st.bar_chart(energydata)

col1, col2 = st.columns(2)

with col1:
    #     RES storage capacity on site
    rescap = str(EnergyResult[1])
    st.metric(label="RES Capacity", value=rescap+" kWp")
with col2:
    #     total storage capacity on site
    stocap = str(EnergyResult[0])
    st.metric(label="Storage Capacity", value=stocap+" kWh")


# Economic Result
st.subheader("Economic Output")
EconomyResult = EconomyOutput(
    EnergyResult[1], EnergyResult[0], EnergyResult[5])

#     Economic Result
economicdata = pd.DataFrame(
    np.array([[EconomyResult[0], 0], [0, EconomyResult[1]]]),
    columns=["Capex", "Opex"],  index=["Capex (€)", "Opex (€)"])
st.bar_chart(economicdata)

# piechart
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
if EconomyResult[0] == 0:
    sizes = [50, 50]
else:
    sizes = [97, 3]
labels = 'CAPEX', 'OPEX'
explode = (0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle.
ax1.axis('equal')
st.pyplot(fig1)


col3, col4 = st.columns(2)

with col3:
    # Savings
    save = str(EconomyResult[2])
    st.metric(label="Savings", value=save+" €")
with col4:
    # Payback
    Pback = str(EconomyResult[3])
    st.metric(label="Payback Rate/Year", value=Pback+" %")


# Clasification Result
with st.container():
    st.subheader("Classification Output")
    st.write("Energy Balance Classification")
    ClassificationOutput(EnergyResult[4])
