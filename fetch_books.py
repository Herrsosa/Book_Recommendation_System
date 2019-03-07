# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:05:38 2019

@author: nilsh
"""
import pandas as pd
    
def fetch_ratings():
    users=pd.read_excel("Book Reviews/BX-Book-Ratings.xls")
    books=pd.read_excel("Book Reviews/BX-Books.xls")
    complete_df=pd.merge(users,books[["ISBN","Book-Title"]],on=["ISBN"])
    
    return complete_df

































