import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Marine Protected Areas", page_icon="🌊", layout="centered", initial_sidebar_state="auto", menu_items=None)


st.image("images.jpg", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

st.markdown("# How do people interact with the Marine Protected Areas?")
        
#st.markdown("## Introduction")
'''
Marine protected areas (MPAs) are advocated as a key tool to manage the restoration and sustainable use of the oceans [1]. They are also assumed to confer cultural ecosystems services (CES), which are defined as “intangible benefits provided by ecosystems, such as spiritual enrichment, cognitive development, reflection, recreation, and aesthetic experiences”. To test this hypothesis, researchers in [OneEarth: Marine Protected Areas provide more cultural ecosystem services than other adjacent coastal areas](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3720309) sampled millions of Flickr photos taken at MPA sites and adjacent control sites. The results showed that more photos were posted, by more users, from within MPAs than within adjacent control sites. In addition, MPA photos focused more on wildlife and landscapes and were described more positively and were more liked. In our project, we used the [datasets](https://data.mendeley.com/datasets/dmk97w5vrr/1?fbclid=IwAR1uZzFUyJAfMBtbBFNPJ-Dn28Qi3l3blThaEPDsgH9DUHO96DZCeUfse-E) from this article to answer a broader question: How do people interact with coastal areas?

'''
st.markdown("## What is the dataset that we are dealing with?")
'''
By using the datasets from the article mentioned above, we have:
* 1M+ photo descriptions (including time and location) with 14 variables (124 MB)
* Additional datasets related to protected areas

Our dataset consists of more than 13000 locations for marine protected areas (13262 different WDPA_PID).
As we can see in the plot below, the Flickr users, are mostly posting pictures from Europe and Central Asia:
'''

st.image("figs/count by continent.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''

'''
st.image("figs/area vs continent.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")
'''
In terms of countries, most Marine Protected Areas are Breat Britain's territories, then Swedish, and then USA's: '''
st.image("figs/count by country.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")
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


HtmlFile = open("htmls/bokeh.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 600)



st.markdown("### Spatial Data")
'''
Text for spatial data
'''
st.image("figs/Choropleth map.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
Text for UK spatial data

*The interactive plot takes some time to load, if you want to use it, press the `Show` button below, and wait some seconds:
'''
if st.button('Show'):
     #st.write('Why hello there')
    HtmlFile = open("htmls/GBRplotly.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height = 600)

'''

'''




#st.header("test html import")

HtmlFile = open("htmls/static.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 600)


#st.header("test html import")

HtmlFile = open("htmls/interactive.html", 'r', encoding='utf-8')
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
