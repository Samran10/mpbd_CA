# Pipeline Design
Pipeline conists of 4 elements - Data Acquisition, Data Processing, Data Analysis & Data Migration.

![42](https://user-images.githubusercontent.com/78740991/214965350-0410cf50-dba0-46f4-a203-5133c94b1919.png)

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

Discovered that in the “Poll” column “Votes & Gross” were both in the same row and wanted it to be adjusted into separate columns, therefore I applied the following to remove the “Poll” column and merge it into the Votes and Gross column. As seen below it has merged into 1000 rows and 11 columns.

![17](https://user-images.githubusercontent.com/78740991/214919822-4a0b87c6-060c-4100-a484-8a9c09136eeb.png)

I found out that Appropriate, Score & Gross were null so I then called out a method to replace all the nulls (np.NaN) in the Appropriate, Score & Gross column with a single 0.

![18](https://user-images.githubusercontent.com/78740991/214919961-83f8a1d0-ccde-4977-8773-1905512673a7.png)
![19](https://user-images.githubusercontent.com/78740991/214920039-a70e8794-21a8-4a49-81d0-ee2876977994.png)

The collected data of Score, Votes & Gross was transformed into its correct data types (float & int) as it was firstly categorised as an object. As a result, from all this processing of data I found out that all the film data types and columns had been corrected ready for the next phase.

![20](https://user-images.githubusercontent.com/78740991/214920157-27c00b7d-f422-43d5-866c-8c96acc79ed8.png)

# Data Analysis
Data analysis is a method for studying data by employing visual methods. With the use of statistical summaries and graphical representations, it is used to identify trends, patterns, or to verify any sort of graphical depictions. In my pipeline, the analysis included creating data with respect to the film information that was procured. I used matplotlib and seaborn to analyse all the film data.

This graph displays “ Total Amount Of Films Along With The Years Which They Released”. I declared the objects of the axes as xy (basically all the elements of the plot on the x and y axis) and searched for all the film “Term” (films year release date). 

![21](https://user-images.githubusercontent.com/78740991/214920989-1ed528a7-0be4-4906-9dd8-ed32cf7b55e8.png)

Method for getting the Top 5 directors with the longest film, Top 10 directors with the highest film score, Top 10 directors with the highest film rating, Top 5 directors with the highest film votes, Top 15 directors with the highest film gross.

![22](https://user-images.githubusercontent.com/78740991/214921205-f6b4a347-f67d-4e80-984d-4dc2544d7845.png)
![23](https://user-images.githubusercontent.com/78740991/214921272-8704fb91-e983-42d5-a703-b1f335be19b4.png)
![24](https://user-images.githubusercontent.com/78740991/214921301-1521d590-013e-4f45-ba7e-c324fe82e14a.png)
![25](https://user-images.githubusercontent.com/78740991/214921330-815bdaf9-d128-4c7a-be68-4295fb59450e.png)

Plotting the Top 5 directors with the longest film, Top 10 directors with the highest film score, Top 10 directors with the highest film rating, Top 5 directors with the highest film votes, & Top 15 directors with the highest film gross on a graph.

![26](https://user-images.githubusercontent.com/78740991/214921416-d4e69806-d6bb-45cc-9991-f923b824383e.png)
![27](https://user-images.githubusercontent.com/78740991/214921471-15f978a3-c8ac-4ad2-ac1f-4d681a28214c.png)
![28](https://user-images.githubusercontent.com/78740991/214921488-688ae072-14fd-4327-b19f-ddea824e67bb.png)
![29](https://user-images.githubusercontent.com/78740991/214921512-5a160e84-3906-4c42-8c91-1f40e16c53d9.png)
![30](https://user-images.githubusercontent.com/78740991/214921535-a442168a-fb89-41be-919b-d23929bf2b3d.png)

Method for finding the average grading, score, votes & gross based on the category total.

![31](https://user-images.githubusercontent.com/78740991/214921620-f333d41e-8690-4821-bafb-227ee117c02b.png)
![32](https://user-images.githubusercontent.com/78740991/214921673-bc8c0335-357d-4009-ba36-8af96c385c1a.png)

Plotting the result on a graph.

![33](https://user-images.githubusercontent.com/78740991/214921729-6ad3284c-8e28-4215-9527-ea8001326ee2.png)
![34](https://user-images.githubusercontent.com/78740991/214921795-9b967881-1b98-487b-a761-e283dd34dbc4.png)

Method for gaining and displaying the Top 3 categories with the highest votes on a graph.

![35](https://user-images.githubusercontent.com/78740991/214921855-b2e1a90c-f07f-4332-8d78-ef60f16b69f3.png)
![36](https://user-images.githubusercontent.com/78740991/214921906-157adbca-50d8-4af4-8b62-8aecb85cc447.png)

Used the seaborn library with matplotlib for displaying the correlation between grading, score, votes and gross. This was utilised to provide better visualizations.

![37](https://user-images.githubusercontent.com/78740991/214921998-f444ca0a-ac63-4a08-9d97-f880c7d31bd5.png)

# Data Migration
Finally, the last element of the pipeline is Data Migration. In this phase, I loaded my main IMDb data-frame into the MySQL database, this is where I firstly created a new database “filmschema” and initially loaded the main data-frame in the form of a table “filmsrec”.

![40](https://user-images.githubusercontent.com/78740991/214964114-274cdc59-1d9b-4ca2-b360-91c53698181f.png)

I used the following 1. SQLAlchemy for facilitating the communication between the Python language and database, 2. MySQL Connector for providing connectivity to MySQL database server, and 3. PyMySQL for connecting to the MySQL database server using Python.

![39](https://user-images.githubusercontent.com/78740991/214964196-2ff4bf76-8e38-4b8a-948e-75b124940914.png)
![41](https://user-images.githubusercontent.com/78740991/214964244-778df5d8-3bae-4177-ae26-a7e1c91a310f.png)
