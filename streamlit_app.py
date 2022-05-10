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

The dataset consists of more than 13000 locations for marine protected areas (13262 different WDPA_PID).
As we can see in the plot below, the Flickr users, are mostly posting pictures from Europe and Central Asia:
'''
st.image("figs/count by continent.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
In terms of countries, most Marine Protected Areas are Great Britain's territories, then Swedish, and then USA's: '''
st.image("figs/count by country.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")
'''
This is a bit surprising, but a reason is that many Great Britain's territories, are small islands in remote areas, across all the globe, due to their colonial history. A secondary reason is that Britain, Sweden and USA, seem like they have been engaged more with their Marine Areas, and protect them better than other countries. '''


st.image("figs/mean area by country.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")
'''
As it can be seen in the plot above, we tried to show top 30 countries with the biggest marine protected areas. Most of the places with the highest area are islands which are overseas territories of other countries like UK, France etc.
The box plot reveals that most of the locations are very small and are less than 100 $km^2$. Going further to the details of the plots above and taking into account that only a couple of countries with high number of MPA locations are shown in the 'Mean Area by Country (top 30)' and also considering low amount of mean area of those countries, it can be concluded areas in countries with high number of MPA locations, are rather small places.'''


st.image("figs/area vs continent.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")
'''
From what we have seen in the previous plots, Areas Beyond National Jurisdiction (ABNJ) had the least number of protected areas among all the continents, while on the other hand, on the plots above ABNJ has the biggest locations with MPA areas with the mean of 60000 $km^2$. With further investigation in the dataset it is revealed there is only 2 vast areas located in ABNJ. Sub-Saharan Africa and East Asia & Pacific with the mean area of 10000 and almost 5000, are the other 2 continents with big marine protected areas respectively.
'''


st.markdown("### When do people visit coastal areas?")
'''
Let's do a temporal analysis of the data and see how often people go to coastal areas and take pictures and post them on Flickr. In this section, we analyze the number of photos taken in 2017, 2018, and 2019, in each month of the year, days of the month, weekday, and hour of the day. The below plot is interactive, which means that you can explore the dataset by yourself.'''
# Temporal plots using Bokeh


HtmlFile = open("htmls/bokeh.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 600)



st.markdown("### Where Flickr users frequently going?")
'''
The plot below, present us the MP areas where people are visiting the most. By the color of the area, we are able to understand how many posts have been made from there.

As we can see in the map below, the biggest (in terms of area) MPAs, are small island in the middle of the Oceans, and some ABNJs. Thus, from their colors, we observe that they do not have many postings made from those areas. Specifically, the areas with a big amount of posts, are so small, that we cannot distinguish them in the global map, and we need to zoom in, in order to find them. Below, we created an interactive map, where we can see the top 100 (in terms of postings) areas in the Great Britain.
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
