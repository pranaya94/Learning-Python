import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import style	
style.use("fivethirtyeight")

xyz_web = { 'Day' : [1,2,3,4,5,6],
			'Visitors' : [1000,700,6000,1000,400,350],
			'Bounce Rate' : [20,20,23,15,10,34]
			}

df = pd.DataFrame(xyz_web) #all lists must have same no of elements to convert to dataframe
print(df)
#Slicing
print(df.head(2)) #first 2 rows
print(df.tail(2)) #last 2 rows


#Merging

df1 = pd.DataFrame({"HPI" : [80,90,70,60],
					"Int_Rate" : [2,1,2,3],
					"IND_GDP" : [50,45,45,67]},
					 index = [2001,2002,2003,2004])

df2 = pd.DataFrame({"HPI" : [80,90,70,60],
					"Int_Rate" : [2.5,1.4,2.3,3.3],
					"IND_GDP" : [55,46,89,54]},
					index = [2005,2006,2007,2008])

merge_df = pd.merge(df1,df2, on = "HPI")
print(merge_df)

#joining
#this is full outer join


df1 = pd.DataFrame({"HPI" : [80,90,70,60],
					"Int_Rate" : [2,1,2,3],
					"wootwoot" : [50,45,45,67]},
					 index = [2001,2002,2003,2004])

df2 = pd.DataFrame({"HPI_L" : [80,90,70,60],
					"Ishmoote" : [2.5,1.4,2.3,3.3],
					"IND_GDP" : [55,46,89,54]},
					index = [2001,2002,2004,2004])

join_df = df1.join(df2, how = 'right')
print(join_df)

#change index
df1.set_index("HPI", inplace=True)
print(df1)

df1.plot()
plt.show()

#change column names
df1 = df.rename(columns={"HPI":"Users"})
print(df1)

#Concatenation

df1 = pd.DataFrame({"HPI" : [80,90,70,60],
					"Int_Rate" : [2,1,2,3],
					"IND_GDP" : [50,45,45,67]},
					 index = [2001,2002,2003,2004])

df2 = pd.DataFrame({"HPI" : [80,90,70,60],
					"Int_Rate" : [2.5,1.4,2.3,3.3],
					"IND_GDP" : [55,46,89,54]},
					index = [2005,2006,2007,2008])

concat_df = pd.concat([df1,df2])
print(concat_df)