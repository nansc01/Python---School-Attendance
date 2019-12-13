import pandas as pd
import matplotlib.pyplot as plt

#Step 1: Read csv
df = pd.read_csv("attendance.csv")

#Step 2: Drop SchoolYear Column
df = df.drop(columns = ["SchoolYear"])

#Step 3: Remove released ratio >= 5%
df["total"] = df.Present + df.Absent + df.Released
df = df[(df.Released / df.total) <= 0.05]

#Step 4: Finding min and max enrollment
print("Step 4\n=====\nMin Enrollment: " + str(df.total.min()) + "\nMax Enrollment: " + str(df.total.max()) + "\n")

size = (df.total.max() - df.total.min()) / 5
segBoundaries = []
segBoundariesString = []

for i in range(5):
    if i == 0:
        segBoundaries.append([df.total.min(), round((df.total.min() + size),1)])
    else:
        segBoundaries.append([round(segBoundaries[i-1][1],1), round(segBoundaries[i-1][1] + size,1)])
#print(segBoundaries)
        
for i in range(5):
    segBoundariesString.append(str(segBoundaries[i][0]) + "-" + str(segBoundaries[i][1]))
    
#print(segBoundariesString)
avg = []
for i in range(5):
    a = df[:].copy()
    a = a[(a.total >= segBoundaries[i][0]) & (a.total <= segBoundaries[i][1])]
    a["attendance"] = a.Present / a.total
    attendance = a["attendance"].mean()
    avg.append(attendance)
#print(avg)
for i in range(5):
    print("Enrollment range " + segBoundariesString[i] + ", rate is " + str(avg[i]))
plt.plot(avg)
plt.show()

###############################################################################
#Step 5 - grouping by school and choosing only schools with more than 50 entries
a = df.groupby("School").count()
a = a[a.total >= 50]
print("Step 5\n========\nThere are " + str(len(a)) + " schools in the system.")

#choosing only schools that are in the 'over 50' group
b = df[df.School.isin(a.index)]

c = b[:].copy()
c["attendance"] = c.Present/c.total
d = c.groupby("School").attendance.mean()
print("\nStep 6\n========\n")
print("Best and worst Average attendance by Schools")
print("School " + d.idxmin() + " with rate of " + str(d.min()))
print("School " + d.idxmax() + " with rate of " + str(d.max()))

###############################################################################
print("\nStep 7\n==========\n")
e = df[df.School == d.idxmax()].sort_values(by = ["Date"])
print(e)
e["attendance"] = e.Present/e.total

#plotting the attendance
plt.plot(e["attendance"])
plt.show()
###############################################################################
print("\nStep 8\n==========\nLowest Attendance was in " + str(e[e.attendance == e.attendance.min()].Date.item()))


















