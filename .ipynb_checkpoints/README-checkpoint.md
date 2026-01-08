# Taxi-Data-Analysis

## Introduction

This project is about analyzing and predicting NYC Taxi fares, based on infromation that you would have _before_ hailing a taxi. For instance, it will be based on the distance, pickup borough, dropoff borough, hour of the day, and the day of the week. 

I used multiple machine learning algorithims to predict the fare price, and the K Nearest Neighbors (KNN) model performed the best at 17 neighbors. I determined this was the best model by utilizing a for loop to test different numbers of neighbors to see which performed the best. 

## Problem Statement
- This dataset contains NYC taxi information such as distance travelled, fare, tip, pickup borough, dropoff borough, and more.  

- The purpose of this analysis is to build a model that can predict the fare of a cab, before you have to hail one. This will include the distance, pickup borough, dropoff borough, hour of the day, and day of the week. 

## Data Dictionary
Include a data dictionary to explain the meaning of each variable or field in the dataset. You can also link to an external data dictionary.

| Column Name | Description |
|-------------|-------------|
| **pickup**       | Pickup datetime (timestamp)                    |
| **dropoff**      | Dropoff datetime (timestamp)                   |
| **passengers**   | Number of passengers                           |
| **distance**     | Trip distance in miles                         |
| **fare**         | Fare amount (USD)                              |
| **tip**          | Tip amount (USD)                               |
| **tolls**        | Tolls paid (USD)                               |
| **total**        | Total amount charged (USD)                     |
| **color**        | Taxi type: `"yellow"` or `"green"`             |
| **payment**      | Payment type (e.g., `"credit card"`, `"cash"`) |
| **pickup_zone**  | Pickup neighborhood zone                       |
| **dropoff_zone** | Dropoff neighborhood zone                      |
| **time_duration** | duration of the trip (in timedelta format) |
| **duration_in_minutes** | duration of the trip in minutes |
| **trip_hour** | hour of day (24-clock) |
| **trip_day** | day of the trip (day name) |
| **trip_day_num** | day of the trip (day number, Sun-0, Sat-6) |

## Executive Summary

### Data Cleaning Steps
There was not too much to clean for this dataset, as there were very few missing values, so those rows were able to be dropped (aounted to 1.4% of the total number of rows)

### Key Visualizations

#### Visualization 1: [Tip with and without Outliers]
[Description and interpretation of the first visualization.]

![tip](images/tip_diff.png)

#### Visualization 2: [Total with and without Outliers]
[Description and interpretation of the second visualization.]

![total](images/total_diff.png)

#### Visualization 3: [Distance with and without Outliers]
[Description and interpretation of the second visualization.]

![distance](images/distance_diff.png)

### Exploratory Data Analysis

Here are some visualizations of different questions I investigated in this analysis. 

#### What day of the week has the highest average fare?

![day_avg_fare](images/avg_fare_day.png)

#### What is the average trip duration by day?

![average duration by day](images/avg_dur_day_diff.png)

#### Where are most customers picked up / dropped off?

![pickup and dropoff common areas](images/pickup_dropoff.png)

#### Which color taxi gets the highest fares?

![cab color fares](images/cab_color_fare.png)

####  What are the busiest times (hours)

![busiest times](images/busy_times.png)


## Conclusions/Recommendations
Using different regression modeling techniques, I found the best performing model to accurately predict `fare` within ~$3 on average. 

I used the models Linear Regression, Random Forest, and K Nearest Neighbors. 

Here are the best results of each. 

| Model | R2 Score | RMSE Score |
| ----- | -------- | ---------- |
| Linear Regression | 0.89 | 3.45 |
| Random Forest | 0.89 | 3.51 | 
| KNN (neighbors = 17) | 0.91 | 3.3 |

The best performing model was KNN, which scored highest for both R2 and RMSE. 

This means that the KNN model can explain 91% of the varience in fare, and can accurately predict the fare price within $3.3 on average. 

#### Linear Regression vs Random Forest R2 Scores

![lr vs rf](./images/lr_rf_r2.png)

#### KNNt R2 Scores

![knn r2](./images/knn_r2.png)

## Additional Information
Include any additional information, references, or resources that might be relevant for understanding the analysis.

---

Feel free to replace the placeholders with your actual content. Additionally, if you have images for your visualizations, make sure to replace the placeholder paths with the correct file paths or URLs.

Once you've filled in the content, save the file with a `.md` extension (e.g., `README.md`). You can use this Markdown file on platforms like GitHub to provide a well-structured README for your analysis.
