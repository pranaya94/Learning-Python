import pandas as pd 

xyz_web = { 'Day' : [1,2,3,4,5,6],
			'Visitors' : [1000,700,6000,1000,400,350],
			'Bounce Rate' : [20,20,23,15,10,34]
			}

df = pd.DataFrame(xyz_web) #all lists must have same no of elements to convert to dataframe
print(df)
print(df['Bounce Rate'][2])