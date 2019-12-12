# Python---School-Attendance
Our goal is to analyze and investigate a school attendance dataset for any insightful information.  
 
You can download the data set using this link: https://tinyurl.com/attandancecsv 

 Step 1:​ Use pandas library to read the data set into a data frame. [5] 
 
 Step 2:​ We will not be using the ​SchoolYear ​ column -- drop the column from your data frame. [15] 
 
The data set contains information for each school, for a range of days, number of students attended, absent and released. Released are those who were absent with permission from school. Total number of enrolled students on that day is basically the sum of attended, absent and released students.  

 Step 3: ​In the case of an unusual event or weather conditions, students as a whole or at large may be excused from school -- remove any row where the ratio of number of released students to total number of enrolled students greater than or equal to 5%. [30] 
 
 Step 4: ​Display the minimum and maximum “total number of enrolled students” in the dataset. Programmatically divide the range (min to max) into 5 segments and compute the attendance rate for each segment. We are basically computing average attendance rate among rows whose number of total enrolled students is within the segment. Plot your findings on screen to see if there is any correlation between number of students and attendance rate. [40] 
 
 Step 5: ​Some schools do not have enough data -- for example, there are schools that reported attendance only for couple of days. Any school that has reported attendance less than 50 times should be removed from the data set. Display how many schools are in the system after this operation. [40] 
 
 Step 6: ​Display the best and worst average attendance by school. For each school, compute the average attendance rate and report the school with minimum and maximum average attendance rate. [40] 
 
 Step 7: ​For the school with max average attendance rate (found in ​Step 6 ​ ), plot the attendance rate over time. Make sure to sort by Date to make sure that the data points are in order of occurrence. [30] 
 
 Step 8:​ Notice that one of the points is really low on the graph. Display the date corresponding to that lowest point. In my case it is Sep 8 -- which may be the first day of school. Possibly the attendance rate is lowest for the first days of school. [20] 
