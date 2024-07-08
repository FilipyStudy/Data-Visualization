# Data Visualization and prediction with Python and SQL

This project is focused on show and learn ML concepts to predic a virtual precipitation of rain.
The database is available on Kaggle.
The dataset used in this project have some informations about rain in some USA cities.
When i decided to start this project i was focused and just show a plot of the data, but in the progress i learned a lot about ML algorithm's. So i decided to use some of them in this project.

# Used technologies:

- Python:
    Used to clean, organize and upload the data to a database.
- Docker:
    Used to containerize the files and allow the easy share and deploy of the project.
- MySQL:
    DBMS used to manage the database and the process of the DMBS.
- Pandas:
    Used to manipulate the data inside the script.
- Matplotlib:
    Used to plot the data.
- SciKit-Learn:
    Used to train the ML algorithm with the data.

# Plot image:
![plot image](https://i.imgur.com/a3vBMuu.png)

# Machine Learning algorithm:

I used the Linear Regression algorithm to analyze the data. This algorithm get two variables one as a target value and two variables for the training data. The algorithm tests the data and discover a relation between the input values and the target value. Then, he create a function 

Y = f(x)

Then, he calculate and predict a result.

The target of this project is to predic a precipitation mm with a input data, the humidity of the air in the moment of the analyses and the temperature of the moment.

# Why this project is inside a docker file?

With a docker file, everyone can run this on any platform. So, by this, my project is a cross-platform project. And you can run without concern about the installation requirements of the project.

# But, why you shoud use MySQL as DMBS?

This DBMS (Database Management System) can store and easily manipulate the data. So, if you want to access the data after run the Linear Regression algorithm with another algorithm, the data are stored inside a database. And this DMBS is easy to use and have a very compatible DBAPI with Python.