# Time Series Forecasting Example
This shows data projection for the amount of Python and R Repos that will be created over the next 5 years on Github.

## BuildDataset.ipynb
##### Uses github api for retrieving the number of Python and R Repos of every month during 2010~2018. 
##### Need to have token.txt file with your access token in it. 
##### For the access token, refer to: https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
##### Finally, builds dataset and save it to results.csv file.

## BuildModel.ipynb
##### With the results.csv file, uses auto_arima to build time series model.
##### Save each model for python and R to *.pkl file.
##### Predit the amount of Python and R Repos that will be created over the next 5 years. 
##### Finally, figure.png shows the graph.

## flask_app.py
##### Simple flask app that returns the prediction graph.
##### The app is running at: http://louisahn.pythonanywhere.com/

