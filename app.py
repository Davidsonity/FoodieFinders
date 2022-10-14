import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import folium
from folium import plugins
from streamlit_folium import folium_static

# Load cleaned data
df = pd.read_csv('clean_data.csv')

# Load Similarity Matrix
sim_matrix = np.load('sim_matrix.npz')
sim_matrix = sim_matrix['a']

names = list(df['Name'].unique())
default_ix = names.index('Maywood Pancake house')


def recommend(name, state, city):
    if name in df['Name'].values:
        # Get index
        index = df[(df['Name'] == name) & (df['state'] == state) & (df['city'] == city)].index[0]
        # Get recommendation scores
        scores = dict(enumerate(sim_matrix[index]))
        # Sort scores
        sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))

        selected_index = [idx for idx, scores in sorted_scores.items()]
        selected_score = [scores for idx, scores in sorted_scores.items()]

        rec_res = df.iloc[selected_index]
        rec_res['similarity'] = selected_score

        recommendation = rec_res.reset_index(drop=True)
        return recommendation[:11]


def table(df):
    fig = go.Figure(data=[go.Table(
        columnorder=[1, 2, 3, 4, 5, 6],
        columnwidth=[20, 20, 20, 30, 20, 20],
        header=dict(values=list(['Name', 'Street Address', 'Location', 'Type', 'Reviews', 'Contact Number']),
                    line_color='black', font=dict(color='black', family="Gravitas One", size=20), height=40,
                    fill_color='#FFD9BA',
                    align='center'),
        cells=dict(
            values=[df['Name'], df['Street Address'], df['Location'], df['Type'], df['Reviews'], df['Contact Number']],
            font=dict(color='black', family="Lato", size=16),
            fill_color='#FFFDD0',
            align='left'))
    ])

    fig.update_layout(height=700,
                      title={'text': "Top 10 Restaurants Recommendations",
                             'font': {'size': 22, 'family': 'Gravitas One'}},
                      title_x=0.5
                      )
    return st.plotly_chart(fig, use_container_width=True)


####################################################################
# streamlit
##################################################################

st.header('Restaurant Recommendation System ')

st.image(
            "https://media.timeout.com/images/105284814/750/422/image.jpg"
        )
st.markdown('<<< Use Side Bar')
st.sidebar.header("Search")
name_ = st.sidebar.selectbox(
    "Name of Restaurant", names, index=default_ix
)

states = df[df['Name'] == name_]['state'].unique()
state_ = st.sidebar.selectbox(
    "State location", states
)

cities = df[(df['Name'] == name_) & (df['state'] == state_)]['city'].unique()
city_ = st.sidebar.selectbox(
    "City location", cities
)

st.sidebar.image('https://1000logos.net/wp-content/uploads/2019/06/TripAdvisor-Logo.png',)

if st.button('Show Recommendations'):
    df_recommend = recommend(name_, state_, city_)
    final_df = df_recommend[1:]

    # Restaurant latitude and longitude values
    latitude = df_recommend['lat'][0]
    longitude = df_recommend['lon'][0]

    # create map and display it
    rest_map = folium.Map(location=[latitude, longitude], zoom_start=6)

    # display the map of restaurant
    rest_map.add_child(
        folium.features.CircleMarker(
            [latitude, longitude],
            radius=5,  # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='Red',
            fill_opacity=0.8
        )
    )
    label = '||NAME||' + '\n' + df_recommend['Name'][0] + '\n' + '|------------------------------------|' + '\n' \
            + '||TYPE||' + '\n' + df_recommend['Type'][0]
    folium.Marker([latitude, longitude], popup=label, icon=folium.Icon(color='red')).add_to(rest_map)

    # instantiate a mark cluster object for the incidents in the dataframe
    restaurants = plugins.MarkerCluster().add_to(rest_map)

    # loop through the dataframe and add each data point to the mark cluster
    for lat, lng, label, type_ in zip(final_df['lat'], final_df['lon'], final_df['Name'], final_df['Type']):
        folium.Marker(
            location=[lat, lng],
            icon=None,
            popup='||NAME||' + '\n' + label + '\n' + '|------------------------------------|' + '\n' + '||TYPE||' + type_,
        ).add_to(restaurants)

    # display map
    st.subheader('Map of Restaurants')
    st.markdown("Red Icon: Restaurant's location ")
    st.markdown("Blue Icon: Recommended Restaurants")
    folium_static(rest_map)

    # display table
    table(final_df)

