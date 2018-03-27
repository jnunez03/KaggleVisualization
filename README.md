# Project: Visualizing NYC Payroll Data :chart_with_upwards_trend:
Data can be found [here](https://www.kaggle.com/new-york-city/nyc-citywide-payroll-data).

The data isn't anything special, but it offers a lot of cleaning and discerning! I had fun with it and learned a lot along the way. Also, you may know, kaggle has a lot of datasets and the popular ones have many input from other analysts and really great programmers, so I wanted to choose a dataset that could really show I didn't just "copy/paste" code and I think there was only 2 people who analyzed this data, but one of them used R and the other barely did any analysis. So I went and chose NYC Payroll as my project. Everything shown was inspired by me and all my decision making/questioning. I wanted to use my own fresh approach to this data set.

- Note 1: I will try and reproduce this in blog format and/or jupyter notebook, so stay tuned for that! Also, explain code line by line.

- Note 2: Clicking on graphs that may be hard to read will help make them more clear as it opens it in a new tab in most cases or just brings it in a kind of zoom and it becomes more clear.

- Note 3: I use a lot of boxplots. Here is a refresher: [Interpreting Boxplots](https://en.wikipedia.org/wiki/Box_plot).
###### Code can be found in .py file above!!

# Here is what I Found! 
## Breakdown of the most employees by Agency per year. 
I chose to use this style of graph that way you can see any discrepancies
easily seeing them side by side and the bold color helps notice the bars and you could see the difference in the heights per year. One thing to note is the size of "Police Department" is different between the years due to the name not being a unique value in the data set. Another thing is there are a lot of different departments and could be categorized based on context, for example, "Education", etc., and these could be merged into 1 category. For instance, colleges could be merged instead of having "Hostos CC, Laguardia CC, etc." as separate index rows. (I ended up using this approach for boxplots on "all occupations pay vs. years of experience" plots)!
![Data](https://user-images.githubusercontent.com/23710841/37132894-3c34f71e-225e-11e8-81b9-f24a0542c03b.png)

## Here is the mean Base Salary and Gross Salary and how they changed over the years. 
![Data](https://user-images.githubusercontent.com/23710841/37130181-4d9ca956-2250-11e8-8ca6-799e8f92bb74.png)

![Data](https://user-images.githubusercontent.com/23710841/37130182-4daa812a-2250-11e8-955d-922d516f0543.png)
- Axis on these graphs are slightly different due to Base Salary being an integer and Gross Salary being a float data type. This is could easily be fixed, by making Gross Pay variable an integer.
## Who were the lowest paid employees and in what years? (I could have done a breakdown year by year and graph the change)
![Data](https://user-images.githubusercontent.com/23710841/37130179-4d881efa-2250-11e8-8f2d-81c347f94040.png)
## Who were the highest paid employees and in what years?
![Data](https://user-images.githubusercontent.com/23710841/37130178-4d7da150-2250-11e8-9aa9-614f37942986.png)

## Top Salary by Borough over the years! 2014 to 2017.
![Data](https://user-images.githubusercontent.com/23710841/37130169-4d106356-2250-11e8-8414-dce65a7fbc0d.png)
![Data](https://user-images.githubusercontent.com/23710841/37132454-ce0bc03a-225b-11e8-8b4d-8499deb533d2.png)
![Data](https://user-images.githubusercontent.com/23710841/37132456-ce316c72-225b-11e8-85f4-0727f57c3576.png)
![Data](https://user-images.githubusercontent.com/23710841/37132455-ce1931f2-225b-11e8-81a0-700a8eb56c6b.png)

## Some Distributions
![base](https://user-images.githubusercontent.com/23710841/37167217-4cb1fe5e-22cf-11e8-8df3-da3d00dc2fb9.png)

![gross](https://user-images.githubusercontent.com/23710841/37167223-50d24a2a-22cf-11e8-8d75-079632a36385.png)

## These are the distributions yearly.
![Data](https://user-images.githubusercontent.com/23710841/37130175-4d5b605e-2250-11e8-9160-28f1977473f9.png)

## With Kernal Densities.
![Data](https://user-images.githubusercontent.com/23710841/37130174-4d4a986e-2250-11e8-836f-fb260d5c8be2.png)

## Normal Distribution Added (*The normal line for 2017 is 3 graphs up. Again, had a problem processing pixel density.)
![nested_distributions](https://user-images.githubusercontent.com/23710841/37166690-b7645550-22cd-11e8-81d9-f92b7fed14fc.png)

## QQ Plots
[The Q-Q plot, or quantile-quantile plot, is a graphical tool to help us assess if a set of data plausibly came from some theoretical distribution such as a Normal or exponential. ... A Q-Q plot is a scatterplot created by plotting two sets of quantiles against one another.](http://data.library.virginia.edu/understanding-q-q-plots/)
- This tests for normality in the data.
## 2014 QQplot of Gross Pay 
![2014](https://user-images.githubusercontent.com/23710841/37192663-bf769426-2334-11e8-8d30-de24921befea.png)
## 2015 QQplot of Gross Pay
![2015](https://user-images.githubusercontent.com/23710841/37192664-bf8f5a38-2334-11e8-9541-e77f63b7ecd1.png)
## 2016 QQplot of Gross Pay
![2016](https://user-images.githubusercontent.com/23710841/37192665-bfa3fe98-2334-11e8-9379-e518f6c94701.png)
## 2017 QQplot of Gross Pay
![2017](https://user-images.githubusercontent.com/23710841/37192667-bfb51b74-2334-11e8-9688-0d56601776d3.png)

None of these plots look like they would go through the origin if they were straight lines. However, even when following a normal distribution, a qq-plot is almost never near perfect. What is displayed in the curve-ish like form away from the quantile line is an indicator of skewed data and data with heavy tails (kurtosis). These in particular look like they fall under a chi-squared distribution or a student t-distribution. However, in this case it is normal, but possesses a right skew! 
## There is some skewness in our Gross Paid data. 
This leads me to study the other variables: Total OT paid - Total Other Pay! Studying further we can see if this "other pay" is what is causing the skewness. However, doing a QQplot of base salary the same skewness still appears which shows me this is not due to the OT paid and Total other pay. Also, this just confirms the right skewness that is visible in the histograms above.
## Top 8 Average Paid Jobs?
![top8avgpaidjobs](https://user-images.githubusercontent.com/23710841/37267541-5f4bdd58-2597-11e8-90f9-a3fdf0f4056e.png)
## In General, how does experience relate to base pay & gross pay?
#### Caveat, someone could be hired in each year with experience outside of NYC! This experience is not reflective of overall experience, but experience based on being a registered worker in NYC! For example, a random NYC worker who started working in 2006. In 2017, we could expect that persons salary to be somewhere around 50,000 to 80,000! However, there could be someone who comes in with more experience and could get paid $120,000, but will show up in the 2017 section of the plot, because he was never registered as a worker in NYC only until 2017. (I hope this explanation is clear. However there is a "slight trend", where on average, more experience = more pay!)
![boxplot_general](https://user-images.githubusercontent.com/23710841/37267124-b03edec0-2594-11e8-8b5c-6f3d70b77f9c.png)
## However, no strong correlation detected. Let's see how this differs from gross pay!
### This is across all occupations for workers from 2000 to 2017, paid minimum of 20,000 annually
![spearmanr](https://user-images.githubusercontent.com/23710841/37383752-1c02ca3a-2721-11e8-97af-716ed12a7a60.png)
- The score is moderate. This is a statistical measure of monotonic relationship between data. So it has to be either increasing or decreasing when plotted against each other (can't be both in the same plot like a sine curve). 
- A score closer to 1 shows perfect correlation. A score closer to 0 means there is absolutely no correlation.
- .47 tells us there is some slight correlation between Gross Pay and Years of Experience. **Let's graph it!**
### We see an obvious upward trend! 
![yoe_gross_plot](https://user-images.githubusercontent.com/23710841/37426215-268724da-279c-11e8-9c96-fd495c4ba2a9.png)
### This differs greatly from what Base Salary showed. Which shows Gross Salary is the true indicator of Pay Vs. Experience!
![yoe_gross_newboxplot](https://user-images.githubusercontent.com/23710841/37427018-6e30184e-279e-11e8-91d8-1efed532eede.png)
## Let's Analyze this Difference:   Gross Pay - Base Pay
![grossminusbase](https://user-images.githubusercontent.com/23710841/37444484-368f1102-27e8-11e8-8b91-b5d9c83c137d.png)
- Mean: -2636.90 (Which means Base Salary was greater than Gross Salary on average)
- Median: -1076.7
- Standard Deviation: 11029
- Minimum positive value: .11 (~11 cents...taxes must have been brutal!)
-Caveat, I did this without taking care of outliers!
### Our QQ plot below just shows that we have A LOT of extreme values! In statistics term: Fat-Tails! 
![grossminusbaseqqplot](https://user-images.githubusercontent.com/23710841/37444648-1a6c3a6c-27e9-11e8-9345-e2399df64384.png)


### Conclusion! 
- When we looked above at Base Salary, we did not see a strong correlation between Base Salary and Years of Experience! The Boxplot only revealed a slight upward trend. When we took a look at Gross Salary, we saw a stronger trend (stronger correlation) which was denoted by the spearman rank test that had a value of .47 which is a moderate score. Across All Occupations, it is revealed the more experience you have the more money you will end up making, despite what your base salary value is! We know that there are other forms of payment such as bonuses, OT paid, stocks, bonds, etc. 
# NEXT!
## I chose to look at the "jobs with the most employees"(most common jobs) and find the distribution of gross pay! 
![alljobs3 0](https://user-images.githubusercontent.com/23710841/37370693-5f26cc82-26e3-11e8-8569-6bf4ad25a059.png)
- note: clicking on the actual graph will make viewing it more clear!
- Only 1 of the variables is indecipherable. If anyone wants to take a shot at figuring it out, please let me know!
- I chose the axis in a way where outliers can be visible. Obviously, it takes away from the aesthetics and is likely unnecessary, but this is for observational purposes!
- (In reality, those dots way outside are outliers and don't need to be shown. There is a technique to calculate outliers beforehand and remove them from the plot)
- You can also note which jobs have employees that are paid way above the normal pay and there are many jobs where all employees are paid within the IQR (Inter-Quartile Range) and display no outliers at all. 
- You can also note there are employees that are paid below the 25th percentile, which could be due to lack of experience and/or a host of other reasons.

## What Variables are related? Well besides the obvious, OT hours and OT paid are the only other most correlated variable (makes sense)!
### This is across all occupations for workers from 2000 to 2017, paid minimum of 20,000 annually
![heatmap](https://user-images.githubusercontent.com/23710841/37383882-f8820840-2721-11e8-94ff-0ec28a9b3948.png)
## This is another way to view the heatmap. As you can see which variables are correlated by actual plots using seaborn.pairplot function!
![pairplot](https://user-images.githubusercontent.com/23710841/37385031-72c8acfc-2728-11e8-9071-8c427590d962.png)
__________________________________________________________________________________________________________________
# Next: Analyzing Teacher Data!
- My subset: Teachers paid annually registered in 2017, with starting work dates from 2000 to 2017 (~18 years of experience to ~1 year of experience). 
## Distribution
Let's see how the pay is distributed based on years of experience!
![aabase](https://user-images.githubusercontent.com/23710841/37250325-10ca08dc-24c8-11e8-9252-5101c2b8d6d0.png)
![aagros](https://user-images.githubusercontent.com/23710841/37250326-10d56966-24c8-11e8-83f4-66d7fd7a05fd.png)
- One thing to note, in 2015 there was a huge increase in teachers who started working with 3430. However, due to the data not being accumulated enough for 2017 (we only have data of 149 teachers who started in 2017). We can note the discrepancy, because the mean base salary drastically drops, but if there was more data, it would be closer to how 2015 and 2016 look.
- Shame on myself for not plotting this the other way! The downward trend is only showing as experience decreases so does pay!
- There was not a lot of 2017 data, so that is why the value is truly so low. There being outliers as well makes it even lower.
![numnum](https://user-images.githubusercontent.com/23710841/37249930-11f9a806-24bf-11e8-8030-a81edac8e4fa.png)
# How do Variables relate to each other? 
## There seems to be no relationship with total other pay and how much you make!
![basewtotalotherpay2016](https://user-images.githubusercontent.com/23710841/37249991-57d1eb12-24c0-11e8-830d-e285d3d20b2b.png)
![grosswtotalotherpay2016](https://user-images.githubusercontent.com/23710841/37249992-57df5e32-24c0-11e8-95b1-55fbff4e189e.png)
## In 2016, there does seem to be a relation with your base salary and gross salary! So we could ultimately predict how much someone will end up making by the end of the year based on their Base Salary.(Yes, seems obvious, I know, but still fun.)
![basewithgross2016](https://user-images.githubusercontent.com/23710841/37249999-6e79ce5c-24c0-11e8-8099-8c20b0dcf383.png)

## Base Vs. Gross Pay For 2017 (n=149, smaller than 2016 sample size)
![basewithgross2017](https://user-images.githubusercontent.com/23710841/37250002-891910b0-24c0-11e8-9b0f-fc06a9344cf4.png)
## Teachers in their first year of work don't seem to make much!
#### Gross Pay 
![teachersfirstyear](https://user-images.githubusercontent.com/23710841/37250029-1c17640c-24c1-11e8-9b57-fb939bc52477.png)
#### Base Pay   (Large discrepancy with Gross Pay!)
![2017basesalary_histogram](https://user-images.githubusercontent.com/23710841/37266232-453d90c6-258f-11e8-9d1e-a3c52ae30996.png)

## Teachers with ~18 years experience make on average $84,482 (USD)!
![teacherwith17yearexp11](https://user-images.githubusercontent.com/23710841/37250050-b3548354-24c1-11e8-8cf8-073439c06a53.png)
## ~22 Years of Experience? (Average is $90,263)!
![teachers1995_exp](https://user-images.githubusercontent.com/23710841/37250158-1acf9738-24c4-11e8-8332-db9944fa164f.png)
## To top it off, here are Boxplot Pay distributions based on the "YEAR" a teacher started working for registered teachers in 2017.
### This is Base Pay BTW! (Which differs largely from Gross Pay!)
![teacherboxplot](https://user-images.githubusercontent.com/23710841/37265980-8a45ea8a-258d-11e8-8bbd-44208c66813a.png)
### Gross Pay (I did not try to fix it, just so you could see the outliers and the huge differences between Base Pay)
![teachergrosshisto](https://user-images.githubusercontent.com/23710841/37266521-0066bb38-2591-11e8-8f1b-db9f8b190bd5.png)

## What I Learned?
- My intuition lead me to think otherwise of what the data showed.
- I learned so much more in Python, I feel like a connoisseur.
- Visualizing data definitely gives the overall picture of what is hidden in just words and numbers. Sure you could do this in excel, but definitely nowhere near the caliber and felxibility that Python offers.
- Seeing negative salaries was shocking and salaries that were very small. It didn't trip me, I just knew that some people are hired as poll workers, or seasonally and may have salaries under 10,000, so most of my analysis was using a subset of the overall data to leave out all the "seasonal" or temporary workers hired and to get a better detail of true annual salaries.
## What I would love to do? 
- I want to implement some machine learning just to play with it. **COMING SOON!**
- Also, I would have liked to add a visual with the actual state of New York and color code by county the amount of employess/salary. Note that there were counties outside of NY in this dataset, due to the fact that people work remotely.



###### Data from [Kaggle](https://www.kaggle.com/competitions)
