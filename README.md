# Project: Visualizing NYC Payroll Data :chart_with_upwards_trend:
Data can be found [here](https://www.kaggle.com/new-york-city/nyc-citywide-payroll-data).

The data isn't anything special, but it offers a lot of cleaning and discerning! I had fun with it and learned a lot along the way. Also, you may know, kaggle has a lot of datasets and the popular ones have many input from other analysts and really great programmers, so I wanted to choose a dataset that could really show I didn't just "copy/paste" code and I think there was only 2 people who analyzed this data, but one of them used R and the other barely did any analysis. So I went and chose NYC Payroll as my project. Everything shown was inspired by me and all my decision making/questioning. I wanted to use my own fresh approach to this data set.

## Here is what I Found! (Code can be found in the .py file!) 

## Here is a breakdown of the most employees by Agency per year. 
I chose to use this style of graph that way you can see any discrepancies
easily seeing them side by side and the bold color helps notice the bars and you could see the difference in the heights per year. One thing to note is the size of "Police Department" is different between the years due to the name not being a unique value in the data set. Another thing is there are a lot of different departments and could be categorized based on context, for example, "Education", etc., and these could be merged into 1 category. For instance, colleges could be merged instead of having "Hostos CC, Laguardia CC, etc." as separate index rows. I also couldn't do further analysis on individual "work titles" like distribution of pay between teachers and fire-fighters, because that was the variable that was giving me much trouble and I couldn't figure out how to fix it.
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

## Yearly?
![Data](https://user-images.githubusercontent.com/23710841/37130175-4d5b605e-2250-11e8-9160-28f1977473f9.png)

## With Kernal Densities you ask? (My computer didn't have the cpu power to  create a density for the 2017 graph)
![Data](https://user-images.githubusercontent.com/23710841/37130174-4d4a986e-2250-11e8-836f-fb260d5c8be2.png)

## Normal Distribution Added (*The normal line for 2017 is 3 graphs up. Again, had a problem processing pixel density.)
![nested_distributions](https://user-images.githubusercontent.com/23710841/37166690-b7645550-22cd-11e8-81d9-f92b7fed14fc.png)

## QQ Plots
[The Q-Q plot, or quantile-quantile plot, is a graphical tool to help us assess if a set of data plausibly came from some theoretical distribution such as a Normal or exponential. ... A Q-Q plot is a scatterplot created by plotting two sets of quantiles against one another.](http://data.library.virginia.edu/understanding-q-q-plots/)
- This tests if our data is truly "Normal"
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

## What I Learned?
- My intuition was definitely not the best guide. Much of the data will surprise you!
- Data can be very difficult to work with. One of the variables was cleaned, but did not behave as a normal string type and I could not work with it fully. This dataset was very messy. A lot of things I refrained from doing (being short on time), so I worked with what I believed were results that would want to be seen, instead of being super nitpicky. I leave my nitpickiness for another data set.
- I learned a lot more about python
- Visualizing data definitely gives the overall picture of what is hidden in just words and numbers. Sure you could do this in excel, but definitely not with the caliber that python offers.
- Seeing negative salaries was shocking and salaries that were very small. It didn't trip me, I just knew that some people are hired as poll workers, or seasonally and may have salaries under 10,000, so most of my analysis was using a subset of the overall data to leave out all the "seasonal" or temporary workers hired and to get a better detail of true annual salaries.
## What I would have loved to do?  (Better Stated: What I will try to add at a later date. The analytics in me will push me!)
- I would have liked to done more with distributions and maybe implement some machine learning just to play with it. But I will leave that for another day. Time was of the essence (sorry for the cliche).
- Also, I would have liked to add a visual with the actual state of New York and color code by county the amount of employess/salary. Note that there were counties outside of NY in this dataset, due to the fact that people work remotely.
- I would have loved to figure out a way to fix one of my variables that just did not want to work as a string type so even a line of code like this ```'TEACHER' in df["Title Description"] ``` did not work and Teacher was inside of the data, just not "readable", despite me trying to strip whitespace, non-alpha characters, and casting it to string type. I will look more into this!

__________________________________________________________________________________________________________________
# UPDATE 1.0! (3/10/2018)
I was able to fix my variable. So now I can look deeper into each job title such as teachers, firefighters, etc and do further analysis. I could check for difference in pay vs experience working as well as distributions of pay for specific job titles, etc..
## Analyzing Teacher Data!
Let's see how the pay is distributed based on years of experience!
![teacherbase](https://user-images.githubusercontent.com/23710841/37249735-f15f532e-24ba-11e8-99f8-691e3e7040de.png)
![teachergross](https://user-images.githubusercontent.com/23710841/37249736-f16ba07a-24ba-11e8-95d3-296dd8a90436.png)




###### Data from [Kaggle](https://www.kaggle.com/competitions)
