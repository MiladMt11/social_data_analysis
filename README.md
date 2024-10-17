# Temporal & Spatial Analysis of Flickr Pictures

This repository contains the files needed to host the website in Streamlit, about the final project of the course Social data analysis and visualization (02806)

Project [website](https://share.streamlit.io/haridimos9/social_data_analysis/main).

One minute project pitch [video](https://www.youtube.com/watch?v=I9XVDlP_pxg).

A detailed notebook with the code and details of the project: [Descriptive notebook](https://drive.google.com/file/d/1Vs8-y3-WxRNnGx0MvJgGxd7zko2TiCtq/view?usp=drive_link)

## Objective:
This project aims to investigate and analyze a dataset of pictures of [Marine Protected Areas](https://en.wikipedia.org/wiki/Marine_protected_area) published on [Flickr](https://www.flickr.com/) with their user-generated descriptions and geo-refrences. In this we have conducted:

1. Data preprocessing, cleaning and conversion.
2. A thorough exploratory data analysis and descriptive analysis.
3. Temporal and Spatial analysis and indentifying trends through time using:
   * geo location interactive maps [(GeoPandas)](https://geopandas.org/en/stable/getting_started/introduction.html)
   * heatmaps
   * interactive visualizations [(Bokeh)](https://bokeh.org/).
4. Predictive analysis and ML modeling to classify photos using RandomForest technique.
5. Predictive analysis and ML modeling to predict the number of likes.

## Packages & Frameworks
* scikit-learn
* GeoPandas
* Bokeh
* pandas
* numpy
* Plotly


## Data
The compelte dataset is available [here](https://data.mendeley.com/datasets/dmk97w5vrr/1). Note that we just used a subset of data. The details are mentioned in [the notebook](https://drive.google.com/file/d/1Vs8-y3-WxRNnGx0MvJgGxd7zko2TiCtq/view?usp=drive_link).

## Installation
remember to install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Contact
We're open to any feedback, suggestions, or questions regarding the projects or the repository. Don't hesitate to contact via email at milad.mtkh@gmail.com.

# References:
[1] Erskine, Emily & Baillie, Rosie & Lusseau, David. (2020). Marine Protected Areas Provide More Cultural Ecosystem Services than Other Adjacent Coastal Areas. SSRN Electronic Journal. 10.2139/ssrn.3720309. 

[2] https://www.protectedplanet.net

[3] https://www.flickr.com/
