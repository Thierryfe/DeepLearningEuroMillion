import csv
file = open("resultat.csv", "w")
writer = csv.writer(file)


for i in range(2004,2020):
    fname = 'euromillions-'+str(i)+'.csv'

    with open(fname,'r') as f :
        reader = csv.reader(f)
        tmp = 0
        for row in reader :
            if (row[0]=='Date') :
                tmp = 1
            if (tmp == 2):
                print(row[1], row[2], row[3], row[4], row[5], row[6], row[7])

                writer.writerow( [row[1], row[2], row[3], row[4], row[5], row[6], row[7]] )

            if (tmp == 1):
                tmp = 2



