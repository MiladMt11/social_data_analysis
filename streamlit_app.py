from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import pandas as pd

from bokeh.plotting import figure
from bokeh.io import show, output_notebook, reset_output
from bokeh.models import  ColumnDataSource, Legend

from flask import Flask, request, redirect, render_template, url_for, session
from urllib.parse import quote
import requests

import json
import datetime

add_selectbox = st.sidebar.selectbox(
    "Select Page",
    ("Overview", "Spotify Stats", "Facebook Stats", "Daily Overview")
    )

st.markdown('<a href="http://127.0.0.1:8501/" target="_self">The link to the page</a>', unsafe_allow_html=True)

#st.markdown('<a href="..." target="_self">...</a>', unsafe_allow_html=True)

################
# Set up Flask Server
#server = Flask(__name__)
#server.secret_key = 'effro'


# Client ID and Client Secret
# Coming from https://developer.spotify.com/dashboard/

# This particular is called from spotify_app:
# https://developer.spotify.com/dashboard/applications/57b733e352a843eab708ae2a3e3c30bc

CLIENT_ID = '440b548f19b941adb817c581faee1ae7'
CLIENT_SECRET = 'd359b65d02e64ada97c8a7911f7eaa42'

# We need Spotify URLs (for a user to be able authorization through the server)

# To authenticate 
# Needs Client ID
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"

# Generating token for a user
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"

# Base URL
# Needs token to be able to be called (from above)
SPOTIFY_API_BASE_URL = "https://api.spotify.com"

# Why do we need to call a specic API version?
API_VERSION = "v1"

# Concatenating the base url with the api version
# Basically ending up with "https://api.spotify.com/v1"
# Normal HTTP response is 401: "No token provided"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Server Parameters:
# When the server is running, you should be able to click
#CLIENT_SIDE_URL = "http://localhost:8080"
CLIENT_SIDE_URL = "http://localhost:8501"
PORT = 8080
REDIRECT_URI = "{}/callback/q".format(CLIENT_SIDE_URL)

SCOPE = "user-top-read user-follow-modify user-library-read playlist-read-private " \
        "user-read-recently-played "\
        "playlist-read-collaborative user-follow-read user-library-modify"
STATE = ""

# I don't know what this is for
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

access_token = None
refresh_token = None
token_type = None
expires_in = None
#access_token_expires = datetime.datetime.now()
access_token_did_expire = True
authorization_header = None


get_auth_query_parameters= {
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'scope': SCOPE,
        # "state": STATE,
        # "show_dialog": SHOW_DIALOG_str,
        'client_id': CLIENT_ID    
    }



def get_access_token_data(auth_token):
    """
    Second step: Getting the access_token
    """
    return {
        'grant_type': 'authorization_code',
        'code': str(auth_token),
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }



"""
Create authorization url and redirect the user to it
"""
# For each parameter, concatenate it to a single url
url_args = "&".join([
    "{}={}".format(key, quote(val)) for key, val in get_auth_query_parameters.items()
    ])
'URL arguments', url_args
# https://accounts.spotify.com/authorize + url_arge
auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
'AUTH URL:\n', auth_url
redirect("https://google.com")
#if st.button('Continue with Spotify'):
#st.markdown('<a href=auth_url>The link to the page</a>', unsafe_allow_html=True)
link = '[GitHub](auth_url)'
st.markdown(link, unsafe_allow_html=True)
def perform_auth(self):
    # Requests refresh and access tokens
    auth_token = request.args['code']  # access the data from the GET (url)
    access_token_data = get_access_token_data(auth_token)
    'Access token data', access_token_data
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=access_token_data)
    if post_request.status_code not in range(200, 299):
        perform_auth()
    # Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]
    now = datetime.datetime.now()
    expires = now + datetime.timedelta(seconds=self.expires_in)
    self.access_token_expires = expires
    self.access_token_did_expire = expires < now
    return self.callback()
#redirect


import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
#components.iframe("http://127.0.0.1:8080/")
#components.iframe("https://google.com")
"""
# Welcome to Streamlit!
Hello People! It's me Marrio. I am going to save the princess now
See you later

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""











if add_selectbox == "Overview":
    st.markdown("# Welcome to the Productivity tracking App")
    st.markdown("Here you will find out about your productivity")
    
    #st.bokeh_chart(p, use_container_width=True)
elif add_selectbox == "Spotify Stats":
    

    with st.echo(code_location='below'):
        total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
        num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
    
        Point = namedtuple('Point', 'x y')
        data = []
    
        points_per_turn = total_points / num_turns
    
        for curr_point_num in range(total_points):
            curr_turn, i = divmod(curr_point_num, points_per_turn)
            angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
            radius = curr_point_num / total_points
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            data.append(Point(x, y))
    
        st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
            .mark_circle(color='#0068c9', opacity=0.5)
            .encode(x='x:Q', y='y:Q'))
else:
    st.markdown("Print something else")
    
