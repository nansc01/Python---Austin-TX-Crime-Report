import pandas as pd

#Task A
df = pd.read_csv("APD_Incident_Extract_2010.csv")

df.columns = ["id", "crime", "date", "time", "ltype", "address", "lng", "lat", "loc"]
df = df[["crime", "time"]]

#Task B
a = df.groupby("crime")["time"].count().nlargest(5)
print("Here are top 5 crimes:")
print (a)


#Task C

while True:
    
    crime = input("Enter Crime: ")
    
    if crime == "EXIT":
        break;
    
    xaxis = range(24)
    data = []
    labels = []
    
    hNum = 0
    hTime = 0
    lNum = 99999999
    lTime = 0
    
    for time in xaxis:
        stime = time * 100
        etime = stime + 100
        f = df[((df.crime == crime) | (crime == "ALL")) & (df.time >= stime) & (df.time < etime)]
        count = len(f)
        
        if count > hNum:
            hNum = count
            hTime = stime
            
        if count < lNum:
            lNum = count
            lTime = stime
            
        data.append(count)
        labels.append(str(stime) + "-" + str(etime))
        
    print("Crime Report for: " + crime)
    print("Lowest between" + str(lTime) + " and " + str(lTime + 100))
    print("Highest between" + str(hTime) + " and " + str(hTime + 100))
    
    import matplotlib.pyplot as plt
    plt.plot(xaxis, data)
    plt.xticks(xaxis, labels, rotation='vertical')
    plt.show()

print("ok bye! Thank you")