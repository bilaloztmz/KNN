from sklearn import datasets
ds = datasets.load_iris()

data = ds.data[:, :4]
target = ds.target

x = ds.data[:, :4]
y = ds.target
from sklearn.model_selection import train_test_split
dataTrainset, dataTestset, targetTrainset, targetTestset = train_test_split(x, y, test_size = 0.30)

def findNearest(testset,k):
    lengths = [([((dataTrainset[a,0] - testset[0])**2 + (dataTrainset[a,1] - testset[1])**2 + (dataTrainset[a,2] - testset[2])**2 + (dataTrainset[a,3] - testset[3])**2)**0.5 , targetTrainset[a]]  )
               for a in range (0,len(dataTrainset))]
    lengths.sort()
    count0 = 0
    count1 = 0
    count2 = 0
    for i in lengths[:k]: # Using k in here 
        if i[1] == 0:
            count0 = count0 + 1
        elif i[1] == 1:
            count1 = count1 + 1
        elif i[1] == 2 :
            count2 = count2 + 1
  
    if (count0 >= count1) and (count0 >= count2):
        nearest = 0
    elif ( count1 >= count0) and (count1 >= count2):
        nearest= 1
    else:
        nearest = 2
    return nearest
def CalculateRate(testset):
    true=0
    false=0
    for i in range(len(testset)):
        if targetTestset[i] == testset[i]:
            true = true+1
        else:
            false = false+1
    return (100*true) / (true+false) 


testdatasetk1 = []
testdatasetk3 = []
testdatasetk5 = []
for i in dataTestset:
    testdatasetk1.append(findNearest(i,1))
for i in dataTestset:
    testdatasetk3.append(findNearest(i,3))
for i in dataTestset:
    testdatasetk5.append(findNearest(i,5))
    
print('Accuracy rate for k=1:', CalculateRate(testdatasetk1))
print('Accuracy rate for k=3:', CalculateRate(testdatasetk3))
print('Accuracy rate for k=5:', CalculateRate(testdatasetk5))    

print('Enter K: ')
x = input()
testdatasetkAny = []
for i in dataTestset:
    testdatasetkAny.append(findNearest(i,int(x)))
print('Accuracy rate for k=', CalculateRate(testdatasetkAny))    
testdatasetkAny.clear() 
    
    