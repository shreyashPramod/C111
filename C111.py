import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()

#plotting the graph
fig=ff.create_distplot([data],["Math Score"],show_hist=False)
#fig.show()

#calculating the mean and standard deviation
mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("mean of population:-",mean)
print("standard deviation of population:-",std_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

#pass the number of time you want the mean of the data point as the parameter in range function in for loop
mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)
mean1=statistics.mean(mean_list)
print("mean of sampaling distribution:-",mean1)

fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean1],y=[0,0.20],mode="lines",name="MEAN"))
fig.show()
