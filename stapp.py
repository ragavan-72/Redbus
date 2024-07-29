from sqlalchemy import column
import streamlit as st
import mysql.connector
import pandas as pd
from datetime import time


con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",
    database="REDBUS_PROJECT"
    )
cursor = con.cursor()

st.markdown("""
    <style>
        h1 {
            color: red;
            text-align: left;
            text-shadow: 2px 2px 4px Blue;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Redbus Data")
show_button = st.button("show bus")
if show_button:
    cursor.execute("select * from Allbus3")
    data = cursor.fetchall()
    df=pd.DataFrame(data,columns=cursor.column_names)
    st.dataframe(df)


with st.sidebar:
    state_transport = st.selectbox('Select the State Transport Corporation:',
    ['Andra', 'Telangana', 'Kerala', 'Kadamba', 'Rajasthan', 'Hariana', 'Uttar Pradesh', 'Assam', 'Sikim', 'West Bengal',])

    if state_transport == 'Andra':
        route = ['Vijayawada to Hyderabad', 'Hyderabad to Vijayawada', 'Kakinada to Visakhapatnam', 
                 'Visakhapatnam to Kakinada', 'Chittoor (Andhra Pradesh) to Bangalore', 'Kadapa to Bangalore',
                 'Anantapur (andhra pradesh) to Bangalore', 'Tirupati to Bangalore', 'Visakhapatnam to Vijayawada',
                 'Ongole to Hyderabad', 'Bangalore to Tirupati', 'Macherla (andhra pradesh) to Hyderabad', 
                 'Rajahmundry to Visakhapatnam', 'Nandyal to Hyderabad', 'Bangalore to Kadapa', 'Hyderabad to Ongole',
                 'Guntur (Andhra Pradesh) to Hyderabad', 'Vijayawada to Visakhapatnam', 'Rajahmundry to Vijayawada',
                 'Hyderabad to Kurnool', 'Bangalore to Chittoor (Andhra Pradesh)', 'Kurnool to Hyderabad', 
                 'Visakhapatnam to Rajahmundry', 'Rayachoti to Bangalore', 'Vinukonda to Hyderabad',
                 'Bangalore to Anantapur (andhra pradesh)', 'Amalapuram to Visakhapatnam', 
                 'Vijayawada to Tirupati', 'Madanapalli to Bangalore', 'Narasaraopet to Hyderabad',
                 'Eluru to Hyderabad', 'Visakhapatnam to Amalapuram', 'Kadiri to Bangalore', 
                 'Chennai to Tirupati', 'Rajahmundry to Hyderabad', 'Kurnool to Vijayawada', 
                 'Vijayawada to Kurnool', 'Kakinada to Vijayawada', 'Bangalore to Madanapalli',
                 'Nellore to Bangalore', 'Hyderabad to Narasaraopet', 'Hyderabad to Guntur (Andhra Pradesh)',
                 'Bangalore to Kadiri', 'Vijayawada to Rajahmundry', 'Bangalore to Rayachoti',
                 'Kurnool to Bangalore', 'Tirupati to Chennai', 'Hyderabad to Anantapur (andhra pradesh)',
                 'Anantapur (andhra pradesh) to Hyderabad']
        
    elif state_transport == 'Telangana':
        route = ['Khammam to Hyderabad', 'Hyderabad to Vijayawada', 'Hyderabad to Khammam', 'Hyderabad to Srisailam',
                'Karimnagar to Hyderabad', 'Hyderabad to Nirmal', 'Hyderabad to Mancherial', 'Hyderabad to Adilabad',
                'Hyderabad to Karimnagar', 'Kothagudem to Hyderabad', 'Guntur (Andhra Pradesh) to Hyderabad',
                'Godavarikhani to Hyderabad', 'Kodad to Hyderabad', 'Hyderabad to Bhadrachalam',
                'Hyderabad to Kothagudem', 'Jagityal to Hyderabad', 'Hyderabad to Kurnool', 'Hyderabad to Sathupally',
                'Hyderabad to Armoor', 'Hyderabad to Godavarikhani', 'Hyderabad to Anantapur (andhra pradesh)', 'Hyderabad to Warangal',
                'Hyderabad to Ongole','Hyderabad to Guntur (Andhra Pradesh)', 'Kadapa to Hyderabad', 'Hyderabad to Tirupati']

    elif state_transport == 'Kerala':
        route = ['Bangalore to Kozhikode', 'Kozhikode to Ernakulam', 'Kozhikode to Bangalore', 'Ernakulam to Kozhikode',
                  'Kozhikode to Mysore','Kozhikode to Thiruvananthapuram', 'Bangalore to Kalpetta (kerala)',
                  'Mysore to Kozhikode', 'Kalpetta (kerala) to Bangalore', 'Kozhikode to Thrissur',
                  'Thiruvananthapuram to Kozhikode', 'Bangalore to Kannur', 'Kozhikode to Kottayam', 
                  'Kannur to Bangalore', 'Kottayam to Kozhikode', 'Thrissur to Kozhikode', 'Kozhikode to Kalpetta (kerala)', 
                  'Coimbatore to Ooty', 'Kalpetta (kerala) to Kozhikode']
        
    elif state_transport == 'Kadamba':
        route = ['Pune to Goa', 'Goa to Pune', 'Mumbai to Goa', 'Goa to Mumbai', 'Pandharpur to Goa',
                 'Bangalore to Goa', 'Goa to Pandharpur', 'Belagavi to Goa', 'Goa to Bangalore',
                 'Solapur to Goa', 'Goa to Kolhapur(Maharashtra)', 'Goa to Solapur', 'Goa to Sangola (Solapur)',
                 'Sangola (Solapur) to Goa', 'Calangute (goa) to Goa Airport', 'Goa to Sangli', 'Calangute (goa) to Mopa Airport',
                 'Mopa Airport to Calangute (goa)', 'Ponda to Belagavi', 'Goa to Miraj', 'Goa Airport to Calangute (goa)',
                 'Marcel to Belagavi', 'Shivamogga to Goa', 'Goa to Mopa Airport', 'Goa to Satara', 'Belagavi to Marcel',
                 'Mopa Airport to Goa', 'Shirdi to Goa', 'Goa to Shivamogga', 'Goa to Shirdi', 'Goa to Goa Airport', 
                 'Margao to Mopa Airport', 'Goa Airport to Goa', 'Mopa Airport to Margao', 'Belagavi to Saquelim',
                 'Panaji to Mopa Airport', 'Saquelim to Belagavi', 'Calangute (goa) to Goa', 'Calangute (goa) to Panaji',
                 'Goa Airport to Panaji']
        
    elif state_transport == 'Rajasthan':
        route = ['Jodhpur to Ajmer', 'Beawar (Rajasthan) to Jaipur (Rajasthan)', 'Udaipur to Jodhpur',
                 'Jaipur (Rajasthan) to Jodhpur','Sikar to Jaipur (Rajasthan)','Kishangarh to Jaipur (Rajasthan)',
                 'Aligarh (uttar pradesh) to Jaipur (Rajasthan)', 'Jodhpur to Beawar (Rajasthan)',
                 'Kota(Rajasthan) to Jaipur (Rajasthan)', 'Jaipur (Rajasthan) to Aligarh (uttar pradesh)', 
                 'Jaipur (Rajasthan) to Kota(Rajasthan)', 'Pali (Rajasthan) to Udaipur', 'Udaipur to Pali (Rajasthan)',
                 'Sikar to Bikaner', 'Jaipur (Rajasthan) to Bharatpur', 'Kishangarh to Jodhpur', 
                 'Jaipur (Rajasthan) to Bhilwara', 'Kota(Rajasthan) to Udaipur', 'Jaipur (Rajasthan) to Pilani',
                 'Jaipur (Rajasthan) to Mathura', 'Bikaner to Sikar']
        
    elif state_transport == 'Hariana':
        route = ['Delhi to Shimla', 'Shimla to Delhi', 'Manali to Chandigarh', 'Chandigarh to Manali',
                 'Delhi to Manali', 'Hamirpur (Himachal Pradesh) to Chandigarh', 'Delhi to Hamirpur (Himachal Pradesh)',
                 'Delhi to Chandigarh', 'Manali to Delhi', 'Hamirpur (Himachal Pradesh) to Delhi',
                 'Chandigarh to Hamirpur (Himachal Pradesh)', 'Shimla to Manali', 'Delhi to Dharamshala (Himachal Pradesh)',
                 'Shimla to Chandigarh', 'Chandigarh to Dharamshala (Himachal Pradesh)', 'Delhi to Baddi (Himachal Pradesh)',
                 'Dharamshala (Himachal Pradesh) to Chandigarh', 'Chamba (Himachal Pradesh) to Chandigarh',
                 'Delhi to Dalhousie', 'Delhi to Chamba (Himachal Pradesh)', 'Dalhousie to Delhi', 
                 'Solan to Delhi', 'Delhi to Palampur', 'Dharamshala (Himachal Pradesh) to Delhi', 'Delhi to Solan',
                 'Chandigarh to Reckong Peo (Himachal Pradesh)', 'Manali to Shimla', 'Palampur to Delhi', 
                 'Chandigarh to Kullu', 'Kangra to Chandigarh', 'Kullu to Chandigarh', 'Delhi to Kangra',
                 'Chamba (Himachal Pradesh) to Delhi', 'Palampur to Chandigarh', 'Chandigarh to Shimla',
                 'Chandigarh to Kangra', 'Delhi to Nalagarh', 'Baddi (Himachal Pradesh) to Delhi', 'Kangra to Delhi',
                 'Ghumarwin to Delhi', 'Delhi to Sarkaghat']
    
    elif state_transport == 'Uttar Pradesh':
        route = ['Bareilly to Delhi', 'Aligarh (uttar pradesh) to Delhi', 'Delhi to Bareilly',
                 'Delhi to Aligarh (uttar pradesh)', 'Farrukhabad (Uttar Pradesh) to Delhi', 
                 'Badaun to Delhi', 'Lucknow to Allahabad', 'Lucknow to Varanasi', 'Delhi to Badaun',
                 'Agra to Bareilly', 'Allahabad to Lucknow', 'Sitapur (Uttar Pradesh) to Delhi', 
                 'Delhi to Farrukhabad (Uttar Pradesh)', 'Moradabad to Delhi', 'Delhi to Haridwar', 
                 'Delhi to Sitapur (Uttar Pradesh)', 'Bareilly to Agra', 'Agra to Lucknow', 'Kanpur (Uttar Pradesh) to Jhansi', 
                 'Lucknow to Agra', 'Varanasi to Lucknow', 'Bareilly to Haridwar', 'Delhi to Agra', 
                 'Delhi to Shahjahanpur (Uttar Pradesh)', 'Agra to Delhi', 'Lucknow to Ballia', 'Bareilly to Dehradun', 
                 'Allahabad to Azamgarh', 'Kanpur (Uttar Pradesh) to Bareilly', 'Lucknow to Ayodhya', 
                 'Aligarh (uttar pradesh) to Lucknow', 'Aligarh (uttar pradesh) to Agra', 'Lucknow to Haridwar', 
                 'Lucknow to Kanpur (Uttar Pradesh)', 'Lucknow to Aligarh (uttar pradesh)', 'Delhi to Etah (Uttar Pradesh)',
                 'Delhi to Kotdwar (Uttarakhand)', 'Allahabad to Varanasi', 'Delhi to Moradabad', 'Varanasi to Allahabad', 
                 'Lucknow to Jaunpur', 'Aligarh (uttar pradesh) to Haridwar', 'Shahjahanpur (Uttar Pradesh) to Delhi', 
                 'Lucknow to Azamgarh', 'Jaunpur to Lucknow', 'Kanpur (Uttar Pradesh) to Lucknow', 'Agra to Haridwar',
                 'Lucknow to Gorakhpur (uttar pradesh)', 'Delhi to Haldwani']
        
    elif state_transport == 'Assam':
        route = ['Tezpur to Guwahati', 'Guwahati to Tezpur', 'Nagaon (Assam) to Guwahati', 'Guwahati to Nagaon (Assam)',
                 'Goalpara to Guwahati', 'Jorhat to North Lakhimpur', 'Dhubri to Guwahati', 'Guwahati to Dhubri',
                 'North Lakhimpur to Sibsagar', 'North Lakhimpur to Jorhat', 'Dhekiajuli to Guwahati', 'Jorhat to Dibrugarh',
                 'Jorhat to Dhemaji', 'Sibsagar to North Lakhimpur', 'Dhemaji to Jorhat', 'Tezpur to Dibrugarh',
                 'Haflong to Guwahati', 'North Lakhimpur to Dibrugarh', 'Jorhat to Tinsukia', 'Dibrugarh to Tezpur',
                 'Guwahati to Biswanath Charali', 'Guwahati to Haflong', 'Dibrugarh to North Lakhimpur', 'Nagaon (Assam) to Haflong',
                 'Tezpur to Moran', 'Dibrugarh to Jorhat', 'Guwahati to Silchar', 'Bihpuria to Dibrugarh', 'Haflong to Nagaon (Assam)',
                 'North Lakhimpur to Tezpur', 'Biswanath Charali to Guwahati', 'Biswanath Charali to Dibrugarh', 'Tinsukia to Jorhat',
                 'Moran to Tezpur', 'Jorhat to Gogamukh', 'Dibrugarh to Biswanath Charali', 'Gohpur to Guwahati', 'Tinsukia to Tezpur',
                 'North Lakhimpur to Golaghat', 'Golaghat to North Lakhimpur', 'Silchar to Guwahati', 'Bokakhat to Dibrugarh',
                 'North Lakhimpur to Moran', 'Tezpur to North Lakhimpur', 'Tezpur to Tinsukia', 'Dibrugarh to Bihpuria',
                 'Dibrugarh to Bokakhat']

    elif state_transport == 'Sikim':
        route = ['Gangtok to Siliguri', 'Siliguri to Gangtok', 'Siliguri to Rangpo','Rangpo to Siliguri',
                 'Siliguri to Pelling (Sikkim)', 'Pelling (Sikkim) to Siliguri', 'Ravangla (Sikkim) to Siliguri',
                 'Siliguri to Jorethang (Sikkim)', 'Singtham (Sikkim) to Siliguri', 'Siliguri to Singtham (Sikkim)',
                 'Siliguri to Namchi (Sikkim)', 'Siliguri to Ravangla (Sikkim)', 'Jorethang (Sikkim) to Siliguri',
                 'Namchi (Sikkim) to Siliguri', 'Siliguri to Melli (Sikkim)']
        
    elif state_transport == 'West Bengal':
        route = ['Kolkata to Digha', 'Digha to Kolkata', 'Mandarmani to Kolkata', 'Kolkata to Mandarmani', 'Kolkata to Bakkhali']

    bus_route = st.selectbox('Select the route:',route)

    bus_type = st.selectbox('Select the bus type:',['Sleeper','Seater'])

    air_con = st.selectbox('Select A/C or Non A/C:',['A/C', 'Non A/C'])

    ratings = st.selectbox('Select the rating range:', ['4 to 5', '3 to 4', '2 to 3', '1 to 2', '0 to 1', 'Unrated'])

    price_options = ['upto 200','upto 400','upto 600','upto 800','upto 1000', '1000+']
    price = st.selectbox('Select the bus fare:',price_options)


    if bus_type == 'Sleeper' and air_con == 'A/C':
        bustype_query = """bustype LIKE '%Sleeper%'
                    AND (bustype LIKE '%AC%' OR
                        bustype LIKE 'A.C%')
                    AND (bustype NOT LIKE '%Non%' OR
                        bustype NOT LIKE 'Non%' OR
                        bustype NOT LIKE 'NON%')"""
    elif bus_type == 'Seater' and air_con == 'A/C':
        bustype_query = """bustype LIKE '%Seater%'
                    AND (bustype LIKE '%AC%' OR
                        bustype LIKE 'A.C%')
                    And (bustype NOT LIKE '%Non%' OR
                        bustype NOT LIKE 'Non%' OR
                        bustype NOT LIKE 'NON%')"""
    elif bus_type == 'Sleeper' and air_con == 'Non A/C':
        bustype_query = """bustype LIKE '%Sleeper%'
                    AND (bustype LIKE '%Non%' OR
                        bustype LIKE 'Non%' OR
                        bustype LIKE 'NON%')"""  
    elif bus_type == 'Seater' and air_con == 'Non A/C':
        bustype_query = """bustype LIKE '%Seater%'
                    AND (bustype LIKE '%Non%' OR
                        bustype LIKE 'Non%' OR
                        bustype LIKE 'NON%')"""
    price_query = ""    
    if price == 'upto 200':
        price_query = "price <= 200"
    elif price == 'upto 400':
        price_query = "price <= 400"
    elif price == 'upto 600':
        price_query = "price <= 600"
    elif price == 'upto 800':
        price_query = "price <= 800"
    elif price == 'upto 1000':
        price_query = "price <= 1000"
    elif price == '1000+':
        price_query = "price >= 1000"
        
    rating_query = ""
    if ratings == '4 to 5':
        rating_query = "star_rating > 4 AND star_rating <= 5"
    elif ratings == '3 to 4':
        rating_query = "star_rating > 3 AND star_rating <= 4"
    elif ratings == '2 to 3':
        rating_query = "star_rating > 2 AND star_rating <= 3"
    elif ratings == '1 to 2':
        rating_query = "star_rating > 1 AND star_rating <= 2"
    elif ratings == '0 to 1':
        rating_query = "star_rating > 0 AND star_rating <= 1"
    elif ratings == 'unrated':
        rating_query = "star_rating = 0"
            
query = f"""select * from Allbus3 where
            route_name = '{bus_route}' and
            {bustype_query} and
            {rating_query} and
            {price_query}"""   
# st.write(bus_route,bustype_query,rating_query,price_query)
# print(query)

# button = st.button('Submit')
# if button:
#     cursor.execute(query)
#     data = cursor.fetchall()
#     df=pd.DataFrame(data,columns=cursor.column_names)
#     st.dataframe(df)

st.markdown("""
    <style>
        h2 {
            color: red;
            text-align: center;
            text-shadow: 2px 2px 4px black;
        }
    </style>
""", unsafe_allow_html=True)

st.title("buses for you")

cursor.execute(query)
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(data, columns=columns)
st.write(df)
                        
                          
