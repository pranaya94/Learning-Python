import pandas as pd 

#data munging
rawdata = pd.read_csv('C:/Users/prtomar/Documents/Github Repos/LearningPython/test_data.csv',index_col = False)
print(rawdata)

rawdata.to_html('edu.html')

new_data = rawdata.reindex(columns=['Age']) #select columns
new_data = new_data.set_index(["Age"]) #make only column we have index so no columns now ! lol
print(new_data)

