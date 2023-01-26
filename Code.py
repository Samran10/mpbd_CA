#Importing all the libraries I need for this choosen pipeline
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re
import seaborn as sns
from sqlalchemy import create_engine
import mysql.connector as sql
import pymysql

#Requests used to download the imdb webpage
#BeautifulSoup utilised to pull out all the information from the webpage
#BeautifulSoup used for parsing, which involves tokenization of html files
imdb_url = 'https://www.imdb.com/search/title/?groups=top_1000&start=1&ref_=adv_nxt'
result = requests.get(imdb_url)
fdata = result.text
beso_data = BeautifulSoup(fdata, 'html.parser')
headers = {'Accept-Language': 'en-US, en;q=0.5'}

#Asking for the result of the request, response displaying as 200 which means request is successful
result

#Starting of webscraping and extracting
imdb_division= beso_data.find_all('div', class_= 'lister-item mode-advanced')
#Getting the names of the films
names =[]
for holder in imdb_division:
    name = holder.h3.a.text
    names.append(name)
#Getting the rankings of the films  
placement = []
for holder in imdb_division:
    place = holder.h3.find('span', class_= 'lister-item-index unbold text-primary').text
    placement.append(place)
#Getting the release years of the films    
terms = []
for holder in imdb_division:
    term = holder.h3.find('span', class_= 'lister-item-year').text
    terms.append(term)
#Getting the categories of the films    
category = []
for holder in imdb_division:
    cat = holder.find('span', class_= 'genre').text.replace('\n','').strip()
    category.append(cat)
#Getting the directors of the films    
director = []
for holder in imdb_division:
    dire = holder.find('p', {'class': ""}).a.text
    director.append(dire)
#Getting the age recommendations of the films    
appropriate = []
for holder in imdb_division:
    appr = holder.find('span', class_= 'certificate').text if holder.p.find('span', class_= 'certificate') else np.NaN
    appropriate.append(appr)
#Getting the lengths of the films    
times = []
for holder in imdb_division:
    time = holder.find('span', class_= 'runtime').text if holder.p.find('span', class_= 'runtime') else np.NaN
    times.append(time)
#Getting the gradings of the films     
gradings = []
for holder in imdb_division:
    grading = float(holder.strong.text)
    gradings.append(grading)
#Getting the scores of the films        
scores = []
for holder in imdb_division:
    score = holder.find('span', class_= 'metascore').text if holder.find('span', class_= 'metascore') else np.NaN
    scores.append(score.strip())
#Getting the polls of the films     
polls = []
for holder in imdb_division:
    poll = holder.find('p', attrs = {'class': 'sort-num_votes-visible'}).text
    polls.append(poll.replace('\n',''))
#There was a total of 1000 of films, each webpage went up in 50s    
webpages = np.arange(1,1000,50)

#Extracting the information from th imdb webpage
placement = []
names =[]
terms = []
category = []
director = []
appropriate = []
times = []
gradings = []
scores = []
polls = []

for webpage in webpages:
    webpage = requests.get('https://www.imdb.com/search/title/?groups=top_1000&start='+str(webpage)+'&ref_=adv_nxt',headers=headers)
    soup = BeautifulSoup(webpage.text,'html.parser')
    imdb_division = soup.find_all('div', class_= 'lister-item mode-advanced')
    
    for holder in imdb_division:
        
        name = holder.h3.a.text
        names.append(name)
        
        dire = holder.find('p', {'class': ""}).a.text
        director.append(dire)
        
        place = holder.h3.find('span', class_= 'lister-item-index unbold text-primary').text
        placement.append(place)
                
        cat = holder.find('span', class_= 'genre').text.replace('\n','').strip()
        category.append(cat)
    
        term = holder.h3.find('span', class_= 'lister-item-year').text
        terms.append(term)
        
        appr = holder.find('span', class_= 'certificate').text if holder.p.find('span', class_= 'certificate') else np.NaN
        appropriate.append(appr)
    
        time = holder.find('span', class_= 'runtime').text if holder.p.find('span', class_= 'runtime') else np.NaN
        times.append(time)
    
        score = holder.find('span', class_= 'metascore').text if holder.find('span', class_= 'metascore') else np.NaN
        scores.append(score)
        
        grading = float(holder.strong.text)
        gradings.append(grading)
    
        poll = holder.find('p', attrs = {'class': 'sort-num_votes-visible'}).text
        polls.append(poll.replace("\n",""))
        
imdb = pd.DataFrame({"Place": placement,"Name": names,"Term": terms,"Category": category,"Director": director,"Appropriate": appropriate,"Time": times,"Grading": gradings,"Score": scores,"Poll": polls})

#Starting of the data preprocessing phase
#Using the regular expression which will specify the set of strings, this case 1000 - due to the total amount of 1000 films
re.sub(r"[^\d]","","(1,000.)")

def change_term(term):
    if (pd.notna(term)):
        term = re.sub(r"[^\d]","",str(term))
        return int(term)
    else:
        return term
    
imdb[["Term","Time","Place"]] = imdb[["Term","Time","Place"]].applymap(change_term)

imdb["Poll"][1]

votes = r"Votes:\d+,\d+,?\d+"
gross = r"Gross:\$[0-9]+.[0-9]+M"

imdb["Votes"] = imdb["Poll"].apply(lambda x : re.search(votes,x).group() if re.search(votes,x) != None else np.NaN)
characteristics_lis = {"Votes":votes, "Gross":gross}

for top_value, shape in characteristics_lis.items():
    imdb[top_value] = imdb["Poll"].apply(lambda x : re.search(shape,x).group() if re.search(shape,x) != None else np.NaN)
    
imdb.drop("Poll", axis =1, inplace = True)

#Calling out a method to replace all the nulls in the record with 0
imdb["Appropriate"] = imdb["Appropriate"].replace(np.NaN,0)
imdb["Score"] = imdb["Score"].replace(np.NaN,0)
imdb["Gross"] = imdb["Gross"].replace(np.NaN,0)

def change_votes(votes):
    if (pd.notna(votes)):
        votes = re.sub(r"[^0-9.]","",str(votes))
        return votes
    else:
        return votes
    
imdb[["Votes","Gross"]]= imdb[["Votes","Gross"]].applymap(change_votes)
imdb["Appropriate"] = imdb["Appropriate"].replace(np.NaN,0)
imdb["Score"] = imdb["Score"].replace(np.NaN,0)
imdb["Gross"] = imdb["Gross"].replace(np.NaN,0)

#Changing the data type for the following headings
imdb["Score"] = imdb.Score.astype(float)
imdb["Votes"] = imdb.Votes.astype(int)
imdb["Gross"] = imdb.Gross.astype(float)

#Analyzing the imdb film data using matplotlib
#Displays the Total Amount of Films along with the years which they released
xy = imdb['Term'].value_counts().plot.bar(figsize = [18,8])
xy.set_xlabel('Term');
xy.set_ylabel('Total Amount Of Movies');

#Method for getting the top five directors with the longest film length
director_time = imdb.groupby('Director').agg({'Time':'mean','Place':'count'})
top_five_director_time = director_time.rename(columns= {'Place':'Total Amount Of Films'}).sort_values('Time',ascending=False)[:5]
#Method for getting the top ten directors with the highest score
director_score = imdb.groupby('Director').agg({'Score':'mean','Place':'count'})
top_ten_director_score = director_score.rename(columns= {'Place':'Total Amount Of Films'}).sort_values('Score',ascending=False)[:10]
#Method for getting the top ten directors with the highest grading
director_grading = imdb.groupby('Director').agg({'Grading':'mean','Place':'count'})
top_ten_director_grading = director_grading.rename(columns={'Place':'Total Amount Of Films'}).sort_values('Grading',ascending=False)[:10]
#Method for getting the top five directors with the highest film votes
director_votes = imdb.groupby('Director').agg({'Votes':'mean','Place':'count'})
top_five_director_votes = director_votes.rename(columns= {'Place':'Total Amount Of Films'}).sort_values('Votes',ascending=False)[:5]
#Method for getting the top fifteen directors with the highest film gross
director_gross = imdb.groupby('Director').agg({'Gross':'mean','Place':'count'})
top_fifteen_director_gross = director_gross.rename(columns={'Place':'Total Amount Of Films'}).sort_values('Gross',ascending=False)[:15]

#Displaying five directors with the longest film length on graph
xy = top_five_director_time['Time'].plot.bar();
xy.set_ylabel('Time')
xy.set_title('Top Five Directors Time', y = 1)
xy.set_xticklabels(top_five_director_time.index, rotation = 70);

#Displaying ten directors with the highest score on graph
xy = top_ten_director_score['Score'].plot.bar();
xy.set_ylabel('Score')
xy.set_title('Top Ten Directors Score', y = 1)
xy.set_xticklabels(top_ten_director_score.index, rotation = 70);

#Displaying ten directors with the highest grading on graph
xy = top_ten_director_grading['Grading'].plot.bar();
xy.set_ylabel('Grading')
xy.set_title('Top Ten Directors Grading', y = 1)
xy.set_xticklabels(top_ten_director_grading.index, rotation = 70);

#Displaying five directors with the highest film votes on graph
xy = top_five_director_votes['Votes'].plot.bar();
xy.set_ylabel('Votes')
xy.set_title('Top Five Directors Votes', y = 1)
xy.set_xticklabels(top_five_director_votes.index, rotation = 70);

#Displaying fifteen directors with the highest film gross on graph
xy = top_fifteen_director_gross['Gross'].plot.bar();
xy.set_ylabel('Gross')
xy.set_title('Top Fifteen Directors Votes', y = 1)
xy.set_xticklabels(top_fifteen_director_gross.index, rotation = 70);

#Getting the average grading, score, votes, and gross based on the category total
imdb['category_total'] = imdb.Category.str.split(',').str.len()
category_total = imdb.groupby('category_total')['Grading','Score','Votes','Gross'].mean()
category_total

#Displaying the results of average grading, score, votes, and gross based on the category total
xy1, xy2, xy3, xy4 = category_total.plot.bar(subplots = True);
fig = xy1.get_figure()
fig.set_size_inches (10,10)
xy1.set_ylabel("Grading")
xy1.legend("")
xy1.set_title("")
xy2.set_ylabel("Score")
xy2.legend("")
xy2.set_title("")
xy3.set_ylabel("Votes")
xy3.legend("")
xy3.set_title("")
xy4.set_ylabel("Gross")
xy4.legend("")
xy4.set_title("")
xy4.set_xticklabels(category_total.index,rotation = 0.05);

#Method of displaying which 3 categories has the most votes
category_3 = imdb[imdb.category_total == 3]
category_3 = category_3.groupby('Category')['Grading','Score','Votes','Gross'].mean()
#Displaying all the 3 categories with the highest votes
xy = category_3.Votes.sort_values(ascending=False).head(3).plot.barh();
xy.set_xlabel('Votes');

#Used seaborn for better visualization
# Displaying correlation of grading, score, votes, and gross of the films
gsvg = sns.pairplot(imdb, height=2, vars=['Grading','Score','Votes','Gross']);
gsvg= gsvg.map_offdiag(plt.scatter,s=50,alpha=0.85)
plt.subplots_adjust(top=0.85);
gsvg.fig.suptitle(' Grading, Score, Votes, Gross Correlation Graphs',fontsize=15, color='r',alpha=0.7);

imdb.to_csv("filmsrec.csv", index = False)

UserName='root'
Password='Zara2010'
DatabaseName='filmschema'
 
# Creating the database connection
db_connection_str = "mysql+pymysql://"+UserName+ ":" +Password +"@localhost/"+ DatabaseName
db_connection = create_engine(db_connection_str)
 
# Table present in the database
DataFromDB = pd.read_sql('SELECT * FROM filmsrec', con=db_connection)
 
DataFromDB.head()
