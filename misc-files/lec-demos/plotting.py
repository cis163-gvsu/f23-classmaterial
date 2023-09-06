import matplotlib.pyplot as plt

# Line graph
xs = list(range(1,10))
ys = [val**2 for val in xs] #list comprehension

#plt.plot(xs, ys)
#plt.show()

ys = [8,8,5,1,5,2,7,6,12]
plt.bar(xs,ys)
plt.title('bit frequencies')
plt.xlabel('x-label')
plt.ylabel('some y-label')
plt.show() # pop up plot
#plt.savefig('barchart.pdf') #save to file
