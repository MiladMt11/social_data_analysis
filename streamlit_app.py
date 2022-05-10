import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Marine Protected Areas", page_icon="🌊", layout="centered", initial_sidebar_state="auto", menu_items=None)


st.image("images.jpg", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")
"""
# Welcome to Marine Protected Areas Project!
This website is here to introduce you to Marine protected areas and guide you through the Flickr dataset about the MPAs...

"""
st.markdown("# Do Flickr people like Marine Protected Areas more than other Areas? And how can we help in their preservation?")
        
#st.markdown("## Introduction")
'''
Marine protected areas (MPAs) are advocated as a key tool to manage the restoration and sustainable use of the oceans[1]. For the scope of this project we used the [datasets](https://data.mendeley.com/datasets/dmk97w5vrr/1?fbclid=IwAR1uZzFUyJAfMBtbBFNPJ-Dn28Qi3l3blThaEPDsgH9DUHO96DZCeUfse-E) from the article [OneEarth: Marine Protected Areas provide more cultural ecosystem services than other adjacent coastal areas](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3720309), and they include information about Flickr posts, that were made in Marine Protected Areas (MPAs) around the globe, but also posts that were made in control areas (areas with similar characteristics as MPAs, but are not MPAs). So for each Marine Protected Area, a control area near it exists with similar characteristics. 
'''
st.markdown("## What Marine Protected Areas (MPAs) actually are ?")
'''
Our dataset consists of more than 13000 locations for marine protected areas (13262 different WDPA_PID).
As we can see in the plot below, the Flickr users, are posting mostly pictures from Europe and Central Asia:
'''

'''
In terms of countries, most Marine Protected Areas are Breat Britain's territories, then Swedish, and then USA's: '''

'''
This is a bit surprising, but a reason is that many Great Britain's territories, are small islands in remote areas, across all the globe. A secondary reason is that Britain, Sweden and USA, seem like they have been engeged more with their Marine Areas, and Protect them better than other countries. '''
'''
ABNJ PLOT COMMENTS '''
# ABNJ PLOT

'''
COUNTRIES AREA PLOT COMMENTS '''
'''
MPA, CONTROL COUNT Comments
'''


st.markdown("## Data Analysis")
'''
Text for data analysis
'''



st.markdown("### Temporal Data")
'''
Text for Temporal data
'''
# Temporal plots using Bokeh


HtmlFile = open("bokeh.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 600)



st.markdown("### Spatial Data")
'''
Text for spatial data
'''
st.image("MPAs.jpg", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
Text for UK spatial data
'''
st.image("UKMPAs.jpg", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''

'''




#st.header("test html import")

HtmlFile = open("static.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 600)


#st.header("test html import")

HtmlFile = open("interactive.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 600)

st.markdown("### Machine Learning")
'''
Text for machine learning
'''
st.markdown("### Conclusion")
'''
Text for conclusion
'''

st.markdown("### References")
'''
[1]: Marine Protected Areas provide more cultural ecosystem services than other adjacent coastal areas
Emily Erskine,1 Rosie Baillie,1 and David Lusseau1

'''
