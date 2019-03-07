# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:31:36 2019

@author: nilsh
"""

import pandas as pd
import numpy as np
from fetch_books import fetch_ratings
import pdb
import matplotlib.pyplot as plt
import seaborn as sns

#Reading in data with fetch_ratings method
data=fetch_ratings()

#Average rating and nr of ratings per book title
average_rating=pd.DataFrame(data.groupby("ISBN")["Book-Rating"].mean())
average_rating["nr ratings"]=data.groupby("ISBN")["Book-Rating"].count()

#Plot average rating and average rating against nr of ratings
average_rating["nr ratings"].hist(bins=100)
sns.jointplot(x="Book-Rating",y="nr ratings",data=average_rating)

#Nr of ratings
print(average_rating.sort_values("nr ratings",ascending=False).head(15))

def return_similar_book(ISBN):
    books=data.pivot_table(index="User-ID",columns="ISBN",values="Book-Rating")
    
    book_ratings=books[ISBN]    
    similar_to_book=books.corrwith(book_ratings)
    similar_to_book.dropna(inplace=True)
    similar_to_book=similar_to_book.sort_values(ascending=False)
    
    print("Similar to {} are the following:".format(data.loc[data["ISBN"]==ISBN]["Book-Title"].unique()[0]))
    for book in similar_to_book.index[:5]:
        print(data.loc[data["ISBN"]==book]["Book-Title"].unique()[0])


# Return Book Titles similar to the book with the ISBN "971880107"        
return_similar_book(971880107)



















