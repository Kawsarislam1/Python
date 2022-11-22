tot =0.0
mon =0.0
ave= 0.0
years = 0
totMonths = 0

years = int (input ("Enter the number of years: "))

for year in range(years):
    print ("For year", year + 1, ":")
    for mon in range (12):
        mon = float(input("Enter the rainfall amount for the month "+str(mon +1)+": "))
        totMonths += 1
        tot += mon
             
ave = tot/ totMonths
print ("For", totMonths,"months")
print ('Total rainfall ',format (tot,'.2f'),'inches')
print ('Average monthly rainfall: ', format (ave,'.2f'),'inches')
