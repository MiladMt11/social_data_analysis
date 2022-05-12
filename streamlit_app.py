import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Marine Protected Areas", page_icon="🌊", layout="centered", initial_sidebar_state="auto", menu_items=None)


st.image("images.jpg", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

st.markdown("# How do people interact with the Marine Protected Areas?")

st.markdown("#### Supplementary material:")

'''* [Explainer notebook and Datasets on Google Drive](https://drive.google.com/drive/folders/1WqG49lnxhoP4N1XJZt5GtAPtZMcRJHSN?usp=sharing)'''

        
#st.markdown("## Introduction")
'''
Marine protected areas (MPAs) are advocated as a key tool to manage the restoration and sustainable use of the oceans [1]. They are also assumed to confer cultural ecosystems services (CES), which are defined as “intangible benefits provided by ecosystems, such as spiritual enrichment, cognitive development, reflection, recreation, and aesthetic experiences”. To test this hypothesis, researchers in [OneEarth: Marine Protected Areas provide more cultural ecosystem services than other adjacent coastal areas](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3720309) sampled millions of Flickr photos taken at MPA sites and adjacent control sites. The results showed that more photos were posted, by more users, from within MPAs than within adjacent control sites. In addition, MPA photos focused more on wildlife and landscapes and were described more positively and were more liked. In our project, we used the [datasets](https://data.mendeley.com/datasets/dmk97w5vrr/1?fbclid=IwAR1uZzFUyJAfMBtbBFNPJ-Dn28Qi3l3blThaEPDsgH9DUHO96DZCeUfse-E) from this article to answer a broader question: How do people interact with coastal areas?

'''
st.markdown("## What is the dataset that we are dealing with?")
'''
By using the datasets from the article mentioned above, we have:
* 1M+ English photo descriptions (including time and location) with 14 variables (124 MB)
* Additional datasets related to protected areas

The dataset consists of more than 13000 locations for marine protected areas (13262 different WDPA_PID).
In the plot below, we can see that more than half of the marine protected areas are located in Europe & Central Asia, after that East Asia & Pacific is the second continent with biggest share of marine protected areas with roughly 2500 locations. North America with roughly 1500 locations and Latin America & Caribbean with 1000 locations are next in the plot. The rest of the cantinents have less than 1000 MPA locations.
'''
st.image("figs/count by continent.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
This is reflected in the number of Flickr photos per day in each continent. The continents that contain more MPAs also have more photos per day. 
'''
st.image("figs/Histogram no photos each continent.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")
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
The above figure shows that Areas Above National Jurisdiction (ABNJ) have MPAs with the highest mean area, 60000 $km^2$. However, the total area covered by MPAs in ABNJ is the smallest because as we have seen in the previous plots, ABNJ has the least number of MPAs among all the continents. Indeed, it is more difficult to create MPAs in ABNJ because of the complex legal framework in place. That is why only 1.18% of ABNJ, which constitutes more than half of the global ocean, is protected [2]. However, international discussions are underway to simplify the creation of MPAs in ABNJ.
'''

st.image("figs/Mean no views faves comments fortreatment.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")
'''
MPA photos have more views, faves and comments on average. This means that MPAs have a higher impact on people than other areas.
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

st.markdown("### Where do Flickr users frequently go?")
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
In the heatmap below, there is a very high concentration of photos in England, perhaps because England is the biggest user of Flickr among the English-speaking countries and because it has a lot of MPA as we saw before. In addition to England, the main areas are Europe, North America, Australia and South East Asia. As mentionned previously, these areas might contain most of the English-speaking users of Flick and contain a high number of MPA. Other locations such as Latin America and Africa might be touristic locations for these English-speaking users. This heatmap might therefore indicate where people travel to along the coasts. Feel free to zoom on the heatmap to discover the most photographed places in the country of your choice.
'''

#st.header("test html import")

HtmlFile = open("htmls/static.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, height = 600)


#st.header("test html import")

'''
Now, let's take a look at the heatmap with time which combines temporal and spatial information about the monthly number of photos from 2017 to 2019:
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
At first we wanted to try to predict whether an area is MPA or control, based on some other characteristics of a Flickr posting. By doing some preprocess to the dataset, we decided to try predict the treatment based on the social related data we have, and these are the number of views, faves, comments, country, continent and the number of words in tags and description(since we need numbers for the machine learning model).
'''

st.image("figs/feature importance 1.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
In order to see more precisely, which features are the most important for the prediction, we created the plot above, containing the overall importance of each feature. By that figure, we confirm that the description is the most important factor with 25%. Then, the country is also quite important with 20%. The social features are between 10% and 15%, while the continent is the least important feature with less than 10% of importance.
'''

'''
The results from our model (with an accuracy score of ~57%) are good enough to prove that there is indeed a connection between the treatment of the area, and the social features('count_views', 'count_faves', 'count_comments', 'tags', 'description'). So we confirm that the treatment of an area impacts its popularity on Flickr as it was mentioned in [1].
'''

st.markdown("### What influences the popularity of a photo on Flickr? ")

'''
The goal here is to understand what makes a photo popular. The popularity of a photo can be measured by its number of views, faves and comments. We would like to choose number of views to be our target variable for the prediction.
Let's the a look at the variable importance for this prediction:

'''

st.image("figs/feature importance 2.png", caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

'''
The most important predictors of the number of views are the latitude and longitude, which bring more than 50% of the reduction of the criterion, followed by the number of words in the description and the number of tags, the time at which the photo was taken, and finally the country. The treatment and continent are the least important features. We would have expected the treatment to play a bigger role in predicting the number of views, since MPA have more views on average.


Here are the results of the prediction:

*Score: 0.13
*Average absolute difference of the predictions on the test set: 625.92
*Average number of views: 778.95

The score is the coefficient of determination R2 which is between 0 and 1. The score of the model on the test set is close to 0, so the model doesn't perform very well. It is confirmed by the value of the average absolute difference of the predictions on the test set, which is aslmost as high as the average number of views.
'''

st.markdown("### Conclusion")
'''
In this project, we gained insight about how people interact with coastal areas through the Flickr social media. First, we learned about MPA, their distribution around the globe and how it affects their popularity, and their difference in popularity compared to adjacent control areas. In particular, we noticed that the UK has a lot of MPAs in overseas territories and this might be due to its colonial history. On the contrary, ABNJ has the least MPAs, perhaps because it is more difficult to create MPAs in international waters. These areas could be worth protecting because they offer cultural benefits to humans, as suggested by MPAs’ higher popularity on Flickr compared to adjacent coastal areas.

Then, the temporal and spatial analysis revealed human patterns of visiting coastal areas. People are more often visiting coastal areas and taking photos during the spring, the weekend, and the middle of the day. As winter approaches, people tend to stop traveling abroad, as suggested by the high concentration of photos in the English-speaking regions of the world. Additionally, the choropleth map showed that smaller MPAs near cities were more visited than bigger overseas locations, perhaps because visitors might mostly live in cities. 

Lastly, the classification task showed that the treatment (whether it is protected or not) of a coastal area might depend on social factors: how people talk about them, and their popularity, suggesting that protecting a coastal area might have a beneficial impact on people. The regression model, which gave less reliable results, showed that the popularity of a photo depends mostly on its location. 
'''

st.markdown("### References")
'''
[1] Marine Protected Areas provide more cultural ecosystem services than other adjacent coastal areas
Emily Erskine,1 Rosie Baillie,1 and David Lusseau1
[2] Protected pnalet: https://www.protectedplanet.net/en/thematic-areas/marine-protected-areas

'''

'''





*This webpage was created by Lucie Fontaine, Milad Taghikhani and Charidimos Vradis as part of the final project for the course Social Data Analysis at DTU*
'''
