# Data Sources

### IMDb

IMDb provides a non-commerial dataset on movies here: https://developer.imdb.com/non-commercial-datasets/. However, they are split into relational tables and also lack some data we particularly want, for example, budget and distributor. This data is available publicly on their website, but to obtain the data files with this additonal data we need a subscription to their service.


### Rotten Tomatoes

We found two datasets on Kaggle relating to rotten tomatoes data.

1. https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset?select=rotten_tomatoes_movies.csv

2. https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews?select=rotten_tomatoes_movies.csv 

The first dataset looks promising because it does not have many NaN values unlike the second.

### APIs

There are APIs to gather additional data such as the Open Movie Database API, https://www.omdbapi.com/, but to collect this data would require a lot of manual effort and we are also limited to 1000 API calls a day on the free version. However, this route would give us a lot more data such as ratings from all of Metacritic, IMDb, and Rotten Tomatoes ratings all in one.