
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


column_names=['user_id','item_id','ratings','timestamp']   #giving the column names


# In[3]:


df = pd.read_csv("u.data",sep="\t",names=column_names)      #read the dataset


# In[4]:


df.head()


# In[5]:


movie_titles = pd.read_csv("Movie_Id_Titles")


# In[6]:


movie_titles.head()


# In[7]:


df1=pd.merge(df,movie_titles,on="item_id")        #merge the data on the bais of the item id


# In[8]:


df1


# In[9]:


df11=df1.groupby('title')['ratings']                      #groupby on the basis of rating and titles..


# In[10]:


rating = pd.DataFrame(df1.groupby('title')['ratings'].mean())        #calculate the mean rating of each movie..


# In[11]:


rating.head()


# In[12]:


rating['no_of_raters']=df1.groupby('title')['ratings'].count()       #count the no. of users who gaves the ratings..


# In[13]:


rating.head()


# In[14]:


rating["no_of_raters"].hist()            #plot the histogram on the basis of no_of_raters


# In[15]:


rating["ratings"].hist(bins=20)                 #plot the histogram on the basis ratings


# In[16]:


sns.jointplot(x="ratings", y="no_of_raters" , data=rating)     #plot the joinplot between ratings and no_of_raters


# In[17]:


rating_matrix=df1.pivot_table(index="user_id", columns="title", values='ratings')    
#we design the pivot table to display which user gives ratings to which movie...


# In[18]:


rating_matrix.head()


# In[19]:


rating.sort_values("no_of_raters",ascending=False)       #sort the values in descending order on the basis of no of raters...


# In[20]:


Independence_Day_rating=rating_matrix['Independence Day (ID4) (1996)']     #taking the ratings of independance day movie as a example...  


# In[21]:


star_wars_rating=rating_matrix['Star Wars (1977)']     


# In[22]:


star_wars_rating.head()


# In[23]:


corelated_independance_day=rating_matrix.corrwith(Independence_Day_rating)  
#corrwith function gives the corelated values of that movie from the dataset..https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corrwith.html


# In[24]:


corelated_independance_day.head()


# In[25]:


recommended_movies_independance=pd.DataFrame(corelated_independance_day,columns=["related_movies"])   
#create the extraa column in the new dataframe


# In[26]:


recommended_movies_independance.head(20)     


# In[27]:


recommended_movies_independance.dropna(inplace=True)           #drop all the "nan" values...
recommended_movies_independance.head(20)


# In[28]:


recommended_movies_independance.sort_values("related_movies",ascending=False)     
#sort the values on the basis of related movies...


# In[29]:


recommended_movies_independance=recommended_movies_independance.join(rating['no_of_raters'])    
#join the two columns with rating dataframe


# In[30]:


recommended_movies_independance


# In[31]:


sorted_recommended_movie= recommended_movies_independance[recommended_movies_independance['no_of_raters']>75].sort_values('related_movies',ascending=False).head()  
#sort the no of raters from recommended movies which are 75 above. and sort the movies on the basis of related movie


# In[32]:


sorted_recommended_movie.head()     #final result

