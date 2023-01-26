# BACKGROUND
As you know that the film industry had emerged at the start of the 19th century between a sequence of technical growths. It evolved swiftly and due to its expenses, it continued to stay well put. At the moment we all know that the film industry is somewhere known to be the biggest due to its popularity and market value.

In this project, I will look to utilise genuine trending data from the IMDb website which technically stores information of films using an online database. During the course of this project, my objective will be to implement a Data Acquisition & Pre-processing Pipeline for the film data. Through this I will look to process data of the “Top 1000” films based on their popularity from IMDb.

# Pipeline Design
Pipeline conists of 4 elements - Data Acquisition, Data Processing, Data Analysis & Data Migration.

# Data Acquisition
The first element of the pipeline is Data Acquisition. All the data was obtained from the IMDb website, the data involved Top 1000 films based on popularity. As you are aware Data Acquisition requires many procedures to extract data, therefore I firstly used the following tools Requests to pull out the data from my desired chosen repository (Top 1000 films based on popularity). Secondly, I used the Beautiful Soup library to parse and extract the information from IMDb's repository. Later on, when I tested out the request I got a response of 200 which meant that my request was successful.

![2](https://user-images.githubusercontent.com/78740991/214917950-b72b3813-7d30-48ef-b130-935f61ac7131.png)

