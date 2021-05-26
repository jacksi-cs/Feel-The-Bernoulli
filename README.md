# [2021 Smart City Hackathon](https://psamant30.github.io/TACC-Smart-City-Hackathon/) - 1st Place (Feel-The-Bernoulli)
### Group Members: Jacob Helwig, Jack Si, Yangxinyu Xie
The Smart City Hackathon is an annual hackathon hosted by the University of Texas at Austin in collaboration with Pecan Street and the City of Austin. As a one day event, it focuses on bringing machine learning enthusiasts to build ideas for smart cities that focuses on improving sustainability of smart energy and water usage. This year's challenge was to use a combination of weather and water consumption data to predict electricity usage within households.

## What does this project do?

Using various classification models (average, KNN, SVM) we are able to take real-time weather and water consumption data to predict electricity usage within households. With a relatively low mean absolute error (~0.298), our models are able to confidently estimate household electric use.

## Who did you design this project for?

While brainstorming, our team decided to examine past studies that shared commonalities with the given challenge. Surprisingly, we found countless experiments and papers recounting similar endeavors of using weather and water data to predict electrical consumption. As it turns out, many cities are still grappling with issues of power shortages and subsequently planned outages due to poor predictive models. Climatological disasters, such as Winter Storm Uri and the 2020 California drought, are prime examples of such problems. Also, power providers and operators need accurate predictions to serve as the foundation for safe and reliable operation on the power grid.

## What features would you add to this project in the future?

As our self-exploration into the provided data saw a correlation between electrical consumption and seasonality, we would like to create an adaptive model for each month. With the data at hand, we would also like to do more exploration into the energy patterns and behaviors exhibited by solar panel consumers (specifically the electricity usage difference between consumers and nonconsumers).
