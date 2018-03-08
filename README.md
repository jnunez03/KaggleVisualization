# Project: Visualizing NYC Payroll Data :chart_with_upwards_trend:
Data can be found [here](https://www.kaggle.com/new-york-city/nyc-citywide-payroll-data).

The data isn't anything special, but it offers a lot of cleaning and discerning! I had fun with it and learned a lot along the way. Also, you may know, kaggle has a lot of datasets and the popular ones have many input from other analysts and really great programmers, so I wanted to choose a dataset that could really show I didn't just "copy/paste" code and I think there was only 2 people who analyzed this data, but one of them used R and the other barely did any analysis. So I went and chose NYC Payroll as my project. Everything shown was inspired by me and all my decision making/questioning. I wanted to use my own fresh approach to this data set.

## Here is what I Found! (Code can be found in the .py file!) 

## Here is a breakdown of the most employees by Agency per year. 
I chose to use this style of graph that way you can see any discrepancies
easily seeing them side by side and the bold color helps notice the bars and you could see the difference in the heights per year. One thing to note is the size of "Police Department" is different between the years due to the name not being a unique value in the data set. Another thing is there are a lot of Different Departments and could be categorized into "Education", etc., and these could be merged into 1 category. For instance, colleges could become 1 variable1 instead of having "Hostos CC, Laguardia CC" as separate variables. Also, the Department of Education Admin seems to be cutting workers, as it only showed in 2014 graph. 
![Data](https://user-images.githubusercontent.com/23710841/37132894-3c34f71e-225e-11e8-81b9-f24a0542c03b.png)

## Here is the mean Base Salary and Gross Salary and how they changed over the years. 
![Data](https://user-images.githubusercontent.com/23710841/37130181-4d9ca956-2250-11e8-8ca6-799e8f92bb74.png)

![Data](https://user-images.githubusercontent.com/23710841/37130182-4daa812a-2250-11e8-955d-922d516f0543.png)

## Who were the lowest paid employees and in what years? (We could have done a breakdown year by year and graph the change)
![Data](https://user-images.githubusercontent.com/23710841/37130179-4d881efa-2250-11e8-8f2d-81c347f94040.png)
## Who were the highest paid employees and in what years?
![Data](https://user-images.githubusercontent.com/23710841/37130178-4d7da150-2250-11e8-9aa9-614f37942986.png)

## Top Salary by Borough over the years! 2014 to 2017.
![Data](https://user-images.githubusercontent.com/23710841/37130169-4d106356-2250-11e8-8414-dce65a7fbc0d.png)
![Data](https://user-images.githubusercontent.com/23710841/37132454-ce0bc03a-225b-11e8-8b4d-8499deb533d2.png)
![Data](https://user-images.githubusercontent.com/23710841/37132456-ce316c72-225b-11e8-85f4-0727f57c3576.png)
![Data](https://user-images.githubusercontent.com/23710841/37132455-ce1931f2-225b-11e8-81a0-700a8eb56c6b.png)

## Some Distributions
![Data](https://user-images.githubusercontent.com/23710841/37130176-4d69bfaa-2250-11e8-8afe-c80c3051bd65.png)

## Yearly?
![Data](https://user-images.githubusercontent.com/23710841/37130175-4d5b605e-2250-11e8-9160-28f1977473f9.png)

## With Kernal Densities you ask? (My computer didn't have the cpu power to  create a density for the 2017 graph)
![Data](https://user-images.githubusercontent.com/23710841/37130174-4d4a986e-2250-11e8-836f-fb260d5c8be2.png)


## What I Learned?
- My intuition was definitely not the best guide. Much of the data will surprise you!
- Data can be very difficult to work with. One of the variables was cleaned, but did not behave as a normal string type and I could not work with it fully. This dataset was very messy. A lot of things I refrained from doing (being short on time), so I worked with what I believed were results that would want to be seen, instead of being super nitpicky. I leave my nitpickiness for another data set.
- I learned a lot more about python
- Visualizing data definitely gives the overall picture of what is hidden in just words and numbers. Sure you could do this in excel, but definitely not with the caliber that python offers.
- Seeing negative salaries was shocking and salaries that were very small. It didn't trip me, I just knew that some people are hired as poll workers, or seasonally and may have salaries under 10,000, so most of my analysis was using a subset of the overall data to leave out all the "seasonal" or temporary workers hired and to get a better detail of true annual salaries.
## What I would have loved to do?
- I would have liked to done more with distributions and maybe implement some machine learning just to play with it. But I will leave that for another day. Time was of the essence (sorry for the cliche).
- Also, I would have liked to add a visual with the actual state of New York and color code by county the amount of employess/salary. Note that there were counties outside of NY in this dataset, due to the fact that people work remotely.
- I would have loved to figure out a way to fix one of my variables that just did not want to work as a string type so even a line of code like this ```'TEACHER' in df["Title Description"] ``` did not work and Teacher was inside of the data, just not "readable", despite me trying to strip whitespace, non-alpha characters, and casting it to string type. I will look more into this!


###### Data from [Kaggle](https://www.kaggle.com/competitions)
