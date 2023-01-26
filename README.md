# BACKGROUND
As you know that the film industry had emerged at the start of the 19th century between a sequence of technical growths. It evolved swiftly and due to its expenses, it continued to stay well put. At the moment we all know that the film industry is somewhere known to be the biggest due to its popularity and market value.

In this project, I will look to utilise genuine trending data from the IMDb website which technically stores information of films using an online database. During the course of this project, my objective will be to implement a Data Acquisition & Pre-processing Pipeline for the film data. Through this I will look to process data of the “Top 1000” films based on their popularity from IMDb.

# Pipeline Design
Pipeline conists of 4 elements - Data Acquisition, Data Processing, Data Analysis & Data Migration.

# Data Acquisition
The first element of the pipeline is Data Acquisition. All the data was obtained from the IMDb website, the data involved Top 1000 films based on popularity. As you are aware Data Acquisition requires many procedures to extract data, therefore I firstly used the following tools Requests to pull out the data from my desired chosen repository (Top 1000 films based on popularity). Secondly, I used the Beautiful Soup library to parse and extract the information from IMDb's repository. Later on, when I tested out the request I got a response of 200 which meant that my request was successful.

![2](https://user-images.githubusercontent.com/78740991/214917950-b72b3813-7d30-48ef-b130-935f61ac7131.png)

I started to web scrape by extracting the films based on names, placement, terms, category, director, appropriate, times, gradings, scores & polls as this was my main aim that I was looking for. Used the numpy library to create an instance of an array with reference to the IMDb webpage.

![3](https://user-images.githubusercontent.com/78740991/214918744-465bb31c-eaec-49f8-b0c5-c31cc62b642e.png)

Following a search, the IMDb URL is supplied, using the process as the group and number of items to be scraped as parameters which were all passed into the pandas data-frame to represent the film data in the format of columns and rows. All that was being done was information extraction from every webpage using a loop. The webpage (URL) that returned the soup element receives the resulting URL as a parameter. The soup element's data is then stored and returned in a list of a data-frames. As you can see, I used “else np.NaN” so that all the values which are missing can be replaced for not a number (NaN).

![14](https://user-images.githubusercontent.com/78740991/214919045-71cd7a37-b4d5-4367-b4d0-b704178bbf54.png)
![15](https://user-images.githubusercontent.com/78740991/214919104-07804fd7-29c5-4173-93df-7601db7096ad.png)

# Data Processing
Starting of the Data Processing phase, I used the re library to manage all the regular expressions in the data and get rid of the missing values. I defined the function “change_term” to detect the non-missing values using the pandas.notna for “Term, Time, Place".

![16](https://user-images.githubusercontent.com/78740991/214919409-b010178a-a8db-4c55-a043-2055e02dbe95.png)


