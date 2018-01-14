from matplotlib import pyplot as plt 
from matplotlib import style
style.use("ggplot")

plt.plot([1,2,3],[4,5,1]) #[x],[y]
plt.show()

#add title and lables
x = [5,8,19]
y = [12,16,6]

plt.plot(x,y)
plt.title('info')
plt.ylabel('y axis')
plt.xlabel('x axis')
plt.show()

#add style to your graph

x2 = [1,2,3,4]
y2 = [1,5,5,3]
plt.plot(x,y,'g',label = 'line one',linewidth=5)
plt.plot(x2,y2,'c',label = 'line two',linewidth=5) # c is cyan
plt.title("Epic info")
plt.ylabel("Y axis")
plt.xlabel("X axis")
plt.legend()
plt.grid(True,color='k') #k is black
plt.show()

#bar plot
plt.bar(x,y,label = "example 1")
plt.show()

#histogram
plt.hist([10,12,14,16,18],[0,5,10,15,20,25],histtype='bar',rwidth=0.8)
plt.show()

#scatter plot
plt.scatter(x,y,label='skitsacat',color='k')
plt.show()

#area plot
plt.stackplot(x,y,colors=['m','c'])
plt.show()

plt.subplot(211)
plt.plot(x,y)
plt.subplot(212)
plt.plot(x2,y2)
plt.show()


