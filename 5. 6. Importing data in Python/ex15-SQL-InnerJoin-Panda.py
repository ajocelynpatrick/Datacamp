# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:34:14 2018

@author: Oberle
"""


# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title,Name from Album INNER JOIN Artist where Album.ArtistID=Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())
