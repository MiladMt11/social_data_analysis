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

''' 
The analysis of number of photos taken in each month of the year shows a decreasing trend throughout the year. Most of the photos were taken in the first 6,7 months of the year. This might be caused due to the fact that in the first months of the year there is more daylight during the day, hence photographers could have more time and also better lighting for taking the pictures.

A nearly steady trend is also observable in the number of photos taken along different days of the month.

Going through the weekday plot, it is clear that the number of photos taken during weekdays remained constant with very small fluctuations. On the other hand, there is a noticeable increase during the weekend. This increase, actually reasons the fact that people have more time on weekends to go to MPA or controlled areas and take pictures and post them on Flickr.

Analysing the number of photos taken in the different hours of the day, a gradual increase is apparent from 5 am in the morning and this growth continues till 12 at noon when it reaches the pick and then starts to decrease throughout the rest of the day. The given explanation for this rise and fall might be that the photographers took the photos mostly during the day because of the proper amount of light and also perhaps there are some restrictions to access those areas at night.

Also, it is obvious that 'control' areas have more number of photos than 'MPA' areas. This might happen due to the limitations to access 'MPA' locations.


Finally, there is an abnormally high number of photos in January, on the first day of the month and at 1am. Let's find why, by looking more in details at the time of photos.
'''

st.image("figs/histogram between 1 and 2 am.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
As you can see above, there is an abnormally high number of photos taken at exactly 1am on the 1st of January and the same can be observed on the other days, but not for other hours (see following plot). This might be because the default value set on Flickr for the time at which a photo was taken is 1am.
'''

st.image("figs/histogram between 1 and 2 january.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
Let's go further and check number of photos in different days of last month of 2018 and first month of 2019
'''

st.image("figs/histogram between dec and jan.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
Such a big and abrupt difference in the number of photos between December and January might be due to the hypothesis that the default month at which a photo was taken is set to January on Flickr.
'''

st.markdown("### Where Flickr users frequently going?")
'''
The plot below, present us the MP areas where people are visiting the most. By the color of the area, we are able to understand how many posts have been made from there.

As we can see in the map below, the biggest (in terms of area) MPAs, are small island in the middle of the Oceans, and some ABNJs. Thus, from their colors, we observe that they do not have many postings made from those areas. Specifically, the areas with a big amount of posts, are so small, that we cannot distinguish them in the global map, and we need to zoom in, in order to find them.
'''
st.image("figs/Choropleth map.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
Below, we created an interactive map, where we can see the top 100 (in terms of postings) areas in the Great Britain.
'''

'''
In the plot below, we can explore the map with the top 100 MPAs in Great Britain. As we can see the most popular place is in the middle of England, but in general the places are distributed evenly across the United Kingdom.

*The interactive plot takes some time to load, if you want to use it, press the `Show` button below, and wait a few seconds:
'''
if st.button('Show'):
     #st.write('Why hello there')
    HtmlFile = open("htmls/GBRplotly.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height = 600)


'''
In the heatmap below, there is a very high concentration of photos in England, perhaps because England is the biggest user of Flickr among the English-speaking countries and because it has a lot of MPA as we saw before. In addition to England, the main areas are Europe, North America, Australia and South East Asia. As mentionned previously, these areas might contain most of the English-speaking users of Flick and contain a high number of MPA. Other locations such as Latin America and Africa might be touristic locations for these English-speaking users. This heatmap might therefore indicate where people travel to along the coasts.
'''

#st.header("test html import")

HtmlFile = open("htmls/static.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 600)


#st.header("test html import")

'''
Now, let's take a look at the heatmap with time combines temporal and spatial information:
'''

HtmlFile = open("htmls/interactive.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 600)

'''
It shows that through the year, the spread of photos in the world gradually decreases: in January, there are photos all over the world and in December, they are concentrated in the English-speaking world (Europe, North America, Australia and South East Asia). Indeed, the users might stay in their home country as the days get shorter and colder at the end of the year and might start traveling abroad when the weather gets warmer. The same January boom of photos that we have noticed during the temporal analysis can be seen in the movie.
'''


st.markdown("### Is there a difference between MPA and control in how people interact with photos on Flickr? ")

'''
In this section, we try to use machine learning models in order to predict the treatment of each photo (whether the photo is taken in 'MPA' or 'control' area).
'''

'''
At first we wanted to try to predict whether an area is MPA or control, based on some other characteristics of a Flickr posting. By doing some preprocess to the dataset df3, we decided to try predict the treatment column based on the Social related data we have, and these are the number of views, faves, comments, country, continent and the number of words in tags and description(since we need numbers for the machine learning model). We selected these specific columns, by iterating through the code, and we decided that these are the columns that do not bias the method. In a previous iteration we also used the time columns(year, month, day, weekday, hour), but the results were suspiciously good, and we realised that the dataset is biased in time variables. Especially the year is biased towards the MPA treatment, because as we saw in temporal data, in 2017, we miss many data about control areas, so the algorithm could easily classify data from 2017 as MPA.
'''

st.image("figs/feature importance 1.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
In order to see more precisely, which features are the most important for the prediction, we created the plot above, containing the overall importance of each feature. By that figure, we confirm that the description is the most important factor with 25%. Then, the country is also quite important with 20%. The rest social features are between 10% and 15%, while the continent is the least important feature with less than 10% of importance.
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
