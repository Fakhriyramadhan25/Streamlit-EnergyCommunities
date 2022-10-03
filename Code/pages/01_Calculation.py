from asyncio.windows_events import NULL
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
import requests as rq
import pandas as pd
import json

st.title(f"Energy Communities Calculation")
st.subheader("1. Select and Input The Coordinate and Country")
components.html(
    """<html>
  <head>
    <link
      href="https://api.mapbox.com/mapbox-gl-js/v2.9.2/mapbox-gl.css"
      rel="stylesheet"
    />
    <script src="https://api.mapbox.com/mapbox-gl-js/v2.9.2/mapbox-gl.js"></script>

    <script src="https://api.mapbox.com/mapbox-gl-js/v2.9.2/mapbox-gl.js"></script>
    <!-- Load the `mapbox-gl-geocoder` plugin. -->
    <script src="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-geocoder/v5.0.0/mapbox-gl-geocoder.min.js"></script>
    <link rel="stylesheet" href="https://api.mapbox.com/mapbox-gl-js/plugins/mapbox-gl-geocoder/v5.0.0/mapbox-gl-geocoder.css" type="text/css">

    <style>
      body {
        margin: 0;
        padding: 0;
      }
      #map {
        position: absolute;
        top: 0;
        bottom: 0;
        width: 100%;
      }
    </style>
    <style type="text/css">
      #info {
        display: table;
        position: relative;
        margin: 530px auto;
        word-wrap: anywhere;
        white-space: pre-wrap;
        padding: 10px;
        border: none;
        border-radius: 3px;
        font-size: 12px;
        text-align: center;
        color: #222;
        background: #fff;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>

    <pre id="info"></pre>

    <script src="https://code.jquery.com/jquery-3.5.0.js"></script>
    <script>
      // TO MAKE THE MAP APPEAR YOU MUST
      // ADD YOUR ACCESS TOKEN FROM
      // https://account.mapbox.com
       mapboxgl.accessToken = "pk.eyJ1IjoiZmFraHJpeXJhbWFkaGFuMjUiLCJhIjoiY2w3ZXdzY2ZjMDRqczNucXdmbmRoYms0diJ9.haoutFJByyix_kn0sMdALQ";
      const map = new mapboxgl.Map({
        container: "map", // container id
        style: "mapbox://styles/mapbox/streets-v11",
        center: [-3.701585297941483,40.41669144318541], // starting position
        zoom: 5, // starting zoom
      });

      map.on("click", (e) => {
        const coords = e.lngLat.wrap();
        const point = e.point;
        document.getElementById("info").innerHTML =
          // `e.lngLat` is the longitude, latitude geographical position of the event.
          "Longitude: "+ coords.lng+ "<br/>"+
          "Latitude: " + coords.lat;
      });

 map.addControl(
      new MapboxGeocoder({
      accessToken: mapboxgl.accessToken,
      mapboxgl: mapboxgl
      })
      );

    </script>
  </body>
</html>

""",

    height=600,
)


def renewable(latitude, longitude):
    token = '11b1c806638a66499d96a8649183a7d56bf0cdf8'
    api_base = 'https://www.renewables.ninja/api/'

    s = rq.session()
    # Send token header with each request
    s.headers = {'Authorization': 'Token ' + token}
    # PV Calculation
    url = api_base + 'data/pv'
    args = {
        'lat': latitude,
        'lon': longitude,
        'date_from': '2020-01-01',
        'date_to': '2020-12-31',
        'dataset': 'merra2',
        'capacity': 1.0,
        'system_loss': 0.16,
        'tracking': 0,
        'tilt': 25,
        'azim': 0,
        'format': 'json'
    }
    r = s.get(url, params=args)
    # Parse JSON to get a pandas.DataFrame of data and dict of metadata
    parsed_response = json.loads(r.text)
    data = pd.read_json(json.dumps(
        parsed_response['data']), orient='index')
    metadata = parsed_response['metadata']
    SumEnergy = data.sum()
    totalenergy = SumEnergy['electricity']
    return totalenergy


if "disabled" not in st.session_state:
    st.session_state["disabled"] = False

if 'test' not in st.session_state:
    st.session_state.test = True


def storage():
    if "storage" not in st.session_state:
        st.session_state.storage = ""


def truefalse():
    st.session_state.test = False


if 'good' not in st.session_state:
    st.session_state.good = True


def good():
    st.session_state.good = False


if 'like' not in st.session_state:
    st.session_state.like = True


def like():
    st.session_state.like = False


if 'HArea' not in st.session_state:
    st.session_state.HArea = True


def HArea():
    st.session_state.HArea = False


if 'BArea' not in st.session_state:
    st.session_state.BArea = True


def BArea():
    st.session_state.BArea = False


if 'IArea' not in st.session_state:
    st.session_state.IArea = True


def IArea():
    st.session_state.IArea = False


def arearooftops(a, b, c, d, e, f):
    g = 0
    if d is not NULL:
        a = d
        b = e
        c = f
        g = a+b+c
    return g


def EnergyConsumption(const1, const2, small, big):
    total = 0
    if small is not NULL:
        small = const1*small
        big = const2*big
        total = small+big
    return total


def outputenergy():
    # calculating the renewable energy
    if 'Lat' not in st.session_state:
        st.session_state.Lat = 0
        st.session_state.Longit = 0
    SolarPVResult = renewable(st.session_state.Lat, st.session_state.Longit)
    st.session_state.SolarPVResult = SolarPVResult
    # Solarpv by introduced energy
    # SolarPV
    if 'intsolarpv' not in st.session_state:
        st.session_state.intsolarpv = 0
        st.session_state.introducespv = 0
    st.session_state.introducespv = st.session_state.intsolarpv
    # Calculating the battery storage
    # Battery Storage
    if 'sassets' not in st.session_state:
        st.session_state.sassets = 0
        st.session_state.storagebattery = 0
    st.session_state.storagebattery = Storage
# Calculating area of the buildings
    # Area of the house
    st.session_state.AreaH1 = 0
    st.session_state.AreaH2 = 0
    st.session_state.AreaH3 = 0
    if 'HA1' not in st.session_state:
        st.session_state.HA1 = 0
        st.session_state.HA2 = 0
        st.session_state.HA3 = 0
    HouseAreaRoof = arearooftops(st.session_state.AreaH1, st.session_state.AreaH2, st.session_state.AreaH3,
                                 st.session_state.HA1, st.session_state.HA2, st.session_state.HA3)
    # Area of the building
    st.session_state.AreaB1 = 0
    st.session_state.AreaB2 = 0
    st.session_state.AreaB3 = 0
    if 'BA1' not in st.session_state:
        st.session_state.BA1 = 0
        st.session_state.BA2 = 0
        st.session_state.BA3 = 0
    BuildingAreaRoof = arearooftops(st.session_state.AreaB1, st.session_state.AreaB2, st.session_state.AreaB3,
                                    st.session_state.BA1, st.session_state.BA2, st.session_state.BA3)
    # Area of the industry
    st.session_state.AreaI1 = 0
    st.session_state.AreaI2 = 0
    st.session_state.AreaI3 = 0
    if 'IA1' not in st.session_state:
        st.session_state.IA1 = 0
        st.session_state.IA2 = 0
        st.session_state.IA3 = 0
    IndustryAreaRoof = arearooftops(st.session_state.AreaI1, st.session_state.AreaB2, st.session_state.AreaI3,
                                    st.session_state.BA1, st.session_state.IA2, st.session_state.IA3)
    TotalArea = IndustryAreaRoof+BuildingAreaRoof+HouseAreaRoof
    st.session_state.TotalArea = TotalArea
    # house Consumption
    if 'shouse' not in st.session_state:
        st.session_state.shouse = 0
        st.session_state.bhouse = 0
    HouseConsumption = EnergyConsumption(
        4000, 8000, st.session_state.shouse, st.session_state.bhouse)
    # building Consumption
    if 'mcomm' not in st.session_state:
        st.session_state.mcomm = 0
        st.session_state.bcomm = 0
    BuildingConsumption = EnergyConsumption(
        15000, 40000, st.session_state.mcomm, st.session_state.bcomm)
    # industry Consumption
    if 'sind' not in st.session_state:
        st.session_state.sind = 0
        st.session_state.bind = 0
    IndustryConsumption = EnergyConsumption(
        80000, 120000, st.session_state.sind, st.session_state.bind)
    TotalConsumption = IndustryConsumption+BuildingConsumption+HouseConsumption
    st.session_state.TotalConsumption = TotalConsumption
    st.success("data has been submitted see the result!")


def postimage(a, b, c):
    imgResult = Image.open(a)
    st.image(imgResult, caption=b, width=c)


with st.container():
    Storage = 0
    Longit = st.number_input("Longitude from -180 to 180 degree",
                             min_value=-180.00, max_value=180.00, key="Longit")
    Lat = st.number_input("Latitude from -90 to 90 degree", min_value=-90.00,
                          max_value=90.00, key="Lat")
    st.subheader(
        "2. Select the country to determine you electricity price rate")
    countrypayrate = st.selectbox(
        'Select the country that you live in?',
        ('Spain', 'Germany', 'Belgium', 'France', 'Bulgaria', 'Austria', 'Netherland', 'Italy', 'Sweden', 'Denmark', 'Norway'))
    st.subheader("3. Describe the stage of your project")
    postimage("stageproject.png", "Stage Project", 700)
    colum1, colum2, colum3, colum4 = st.columns(4)
    with colum1:
        st.write('''
        I have an idea and I am conceptualizing the CES,
        identifying the location, the buildings, the stakeholders,
        I am going to perform an
        initial simulation of my system
        ''')
    with colum2:
        st.write('''
        The CES is already designed and I am one step forward.
        I am contacting stakeholders and running technical
        simulations and and economical feasibility studies
        to confirm the viability of my project
        ''')
    with colum3:
        st.write('''
        I am building the CES, I have contacted the investors,
        and I will start installing the electrical assets,
        smart meters, etc.
        ''')
    with colum4:
        st.write('''
        My CES is already functioning and I am monitoring
        the right functioning of the CES
        ''')
    stageproject = st.selectbox(
        'What is the stage of the project?',
        ('initiating', 'Plannning', 'Implementation', 'Operation'))
    st.subheader("4. Describe The Types of Your Energy Community")
    col_a, col_b, col_c = st.columns(3)
    with st.container():
        with col_a:
            postimage("residential.png", "Residential", 100)
        with col_b:
            postimage("hotel.png", "Municipality", 100)
        with col_c:
            postimage("industry.png", "Industrial", 100)

    ecommunity = st.radio(
        "What kind of energy community better fits the project?",
        ('Residential', 'Municipality', 'Industrial'))
    st.subheader(
        "5. Describe Your Storage Assets")
    coll1, coll2, coll3 = st.columns(3)
    with st.container():
        with coll1:
            st.empty()
        with coll2:
            postimage("battery.png", " ", 150)
        with coll3:
            st.empty()
    Sassets = st.selectbox(
        'Do you want to have a storage?',
        ('No Storage', 'Consider Storage'))
    if Sassets == 'Consider Storage':
        # Storage = st.number_input(
        #     "input the capacity of the Storage(KWP)", min_value=0, disabled=st.session_state.disabled, key="sassets")
        Storage = 0.6
    elif Sassets == 'No Storage':
        Storage = 0
    st.subheader("6.a. Describe the Renewable Energy Generation Assets")
    coll4, coll5, coll6 = st.columns(3)
    with st.container():
        with coll4:
            st.empty()
        with coll5:
            postimage("solarpv.png", " ", 150)
        with coll6:
            st.empty()
    Gassets = st.selectbox(
        'Do you want to input the capicity or do you want us to recommend for you the capacity?',
        ('Introduced capacity', 'Recommended capacity'))
    if Gassets == 'Introduced capacity':
        solarPV = st.number_input(
            "Insert the capacity of your Solar PV (kWP)", disabled=st.session_state.disabled, key="intsolarpv")
    elif Gassets == 'Recommended capacity':
        # default size belum ketemu
        st.subheader(
            "6.b. Describe Your Available Rooftop Types and Area")
        coll10, coll11, coll12 = st.columns(3)
        with st.container():
            with coll10:
                postimage("houseroof.jpg", " ", 150)
                Hroofs = st.number_input(
                    "House Rooftops (qty)", disabled=st.session_state.disabled, step=1)
                st.button("House rooftop Area", on_click=HArea)
                HA1 = st.number_input(
                    "House Area1 (m2)", min_value=0, step=1, disabled=st.session_state.HArea, key="HA1")
                HA2 = st.number_input(
                    "House Area2 (m2)", min_value=0, step=1, disabled=st.session_state.HArea, key="HA2")
                HA3 = st.number_input(
                    "House Area3 (m2)", min_value=0, step=1, disabled=st.session_state.HArea, key="HA3")
            with coll11:
                postimage("commercialroof.png", " ", 150)
                Broofs = st.number_input(
                    "Buildings Rooftops (qty)", disabled=st.session_state.disabled, step=1)
                st.button("Building rooftop Area", on_click=BArea)
                BA1 = st.number_input(
                    "Building Area1 (m2)", min_value=0, step=1, disabled=st.session_state.BArea, key="BA1")
                BA2 = st.number_input(
                    "Building Area2 (m2)", min_value=0, step=1, disabled=st.session_state.BArea, key="BA2")
                BA3 = st.number_input(
                    "Building Area3 (m2)", min_value=0, step=1, disabled=st.session_state.BArea, key="BA3")
            with coll12:
                postimage("industryroof.png", " ", 150)
                BIroofs = st.number_input(
                    "Big Industrial Rooftops (qty)", disabled=st.session_state.disabled, step=1)
                st.button("Industrial rooftop Area", on_click=IArea)
                IA1 = st.number_input(
                    "Industry Area1 (m2)", min_value=0, step=1, disabled=st.session_state.IArea, key="IA1")
                IA2 = st.number_input(
                    "Industry Area2 (m2)", min_value=0, step=1, disabled=st.session_state.IArea, key="IA2")
                IA3 = st.number_input(
                    "Industry Area3 (m2)", min_value=0, step=1, disabled=st.session_state.IArea, key="IA3")
    with st.container():
        st.subheader(
            "7. Describe your Energy Consumption, Chose Your Types and Input The Quantity")
        coll7, coll8, coll9 = st.columns(3)
        with st.container():
            with coll7:
                st.empty()
            with coll8:
                postimage("energyconsumption.jpg", " ", 150)
            with coll9:
                st.empty()
    col1, col2, col3 = st.columns(3)
    with st.container():
        with col1:
            Residential = st.number_input(
                "Houses | Apartments | Small Stores", min_value=0, step=1, key="resident", max_value=3)
            st.button('Residential', on_click=truefalse)
            shouse = st.number_input(
                "Small Residential (Annual Consumption 2.000-5.000 kWh)", min_value=0, disabled=st.session_state.test, key="shouse")
            bhouse = st.number_input(
                "Big Residential (Annual Consumption 6.000-10.000 kWh)", min_value=0, disabled=st.session_state.test, key="bhouse")
        with col2:
            Commercial = st.number_input(
                "Medium Stores | Hotels | Building", min_value=0, step=1, key="commerce", max_value=3)
            st.button('Commercial', on_click=good)
            mcomm = st.number_input(
                "Medium Commercial (Annual Consumption 10.000-30.000 kWh)", min_value=0,  disabled=st.session_state.good, key="mcomm")
            bcomm = st.number_input(
                "Big Commercial (Annual Consumption 30.000-80.000 kWh)", min_value=0, disabled=st.session_state.good, key="bcomm")
        with col3:
            Industries = st.number_input(
                "Industrial Buildings | Tertiary Building", min_value=0, step=1, key="industry", max_value=3)
            st.button('Industry', on_click=like)
            sind = st.number_input(
                "Small Industries (Annual Consumption 80.000-150.000 kWh)", min_value=0, disabled=st.session_state.like, key="sind")
            bind = st.number_input(
                "Big Industries (Annual Consumption >150.000 kWh)", min_value=0, disabled=st.session_state.like, key="bind")

    st.button("Submit", on_click=outputenergy)
