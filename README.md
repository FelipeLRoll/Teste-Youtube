[![author](https://img.shields.io/badge/author-feliperoll-purple.svg)](https://www.linkedin.com/in/felipe-roll/)

### :brazil: [Portuguese version](https://github.com/FelipeLRoll/Teste-Youtube/blob/main/readmePortuguese.md)

# YouTube Performance Analysis Project

## Motivation

Understanding what makes a video perform well on YouTube is essential for content creators who want to grow their audiences, improve engagement, and monetize their content. By analyzing historical video data, it is possible to identify patterns and factors that influence views, average viewing time, and click-through rates.

## Objectives

The main objective of this project is to analyze data on the performance of videos on a YouTube channel, using exploratory analysis and data visualization techniques to generate insights that guide strategic decisions.

- Investigate the factors that influence video performance

- Identify patterns

- Discover which topics generate the most engagement

## Project Stages

- Data loading and initial analysis: Inspection of the dataset exported from YouTube Studio

- Data cleaning and processing: Column conversion, handling of null values, standardization

- Attribute engineering: Creation of new variables

- Exploratory data analysis (EDA): Statistical evaluation and identification of trends and outliers

- Visualization with graphs: Creation of bar plots, scatter plots, and word clouds to facilitate data interpretation

- Generation of insights: Based on the analyses, identify actions that can improve the channel's performance

# Data Dictionary - YouTube Analytics

## General Description

This dataset contains performance analysis data for videos from a YouTube channel focused on Counter-Strike 2 (CS2) content, including tutorials on grenades and smokes for different maps.

## Data Structure

### General Information

- **Source**: YouTube Analytics
- **Period**: 2013-2025
- **Number of records**: 11 videos
- **Format**: CSV

---

## Variables

| Variable | Type | Description | Example | Notes |
|----------|------|-----------|---------|-------------|
| **Content** | String | Unique YouTube video ID | `PU50erzKEjk` | Unique identifier generated by YouTube |
| **Video title** | String | Video title | `CS2 - Smokes Anubis` | Public title of the video |
| **Video publish time** | String | Publication date | `Feb 25, 2025` | Format: MMM DD, YYYY |
| **Duration** | Integer | Video duration in seconds | `257` | Total video duration |
| **Average view duration** | String | Average viewing time | `0:00:42` | Format: H:MM:SS |
| **Unique viewers** | Integer | Number of unique viewers | - | Data not available in the dataset |
| **Stayed to watch (%)** | Float | Retention percentage | - | Data not available in the dataset |
| **Average views per viewer** | Float | Average views per person | - | Data not available in the dataset |
| **New viewers** | Integer | New viewers | - | Data not available in the dataset |
| **Returning viewers** | Integer | Returning viewers | - | Data not available in the dataset |
| **Views** | Integer | Total views | `52` | Total number of views |
| **Watch time (hours)** | Float | Total watch time | `0.6107` | Sum of all watch time |
| **Subscribers** | Integer | Subscribers gained | `2` | New subscribers through the video |
| **Impressions** | Integer | Video impressions | `1572` | How many times the video was shown |
| **Impressions click-through rate (%)** | Float | Click-through rate on impressions | `1.15` | Percentage of clicks on impressions |

---

# Results

### **Descriptive Analysis**

What happened?

- Videos from my YouTube channel were analyzed between October 16, 2013, and March 21, 2025
- The videos had a median of 3 views
- The median duration of the videos is 3 minutes and 55 seconds
- Videos with words such as “CS2” and “Smokes” performed better in most metrics
- Longer videos tend to have a higher average viewing time
- The more people watch a video, the shorter the average viewing time
- Videos with more views tend to have more impressions
- The number of views and the number of subscribers gained over time follow the same trend
- Videos were more successful after 2023
- Titles with “Grenades” instead of “Smokes” generate fewer views
- The two videos of the “Anubis” map had the highest number of views in CS2 compared to the CS:GO video (“Smokes Anubis”)

---

### **Diagnostic Analysis**

Why did this happen?

- Videos with keywords such as “CS2” and “Smokes” got more views, probably because the game ‘CS2’ was recently released and many players are looking for videos on how to do “Smokes” in the game
- The same reason meant that videos released after 2023 had higher engagement
- Videos with more views tend to have a more realistic CTR, as they appear to a larger number of people and are therefore more likely to be clicked on.
- The more people watch a video, the shorter the average viewing time. This is because, especially with this type of video, users tend to watch only a specific part of the video (a specific “Smoke”) rather than the entire content.
- The curve of the number of views and the number of subscribers gained over time follow a very similar curve because the more people watch a video, the greater the chance of gaining subscribers 
- The “Anubis” map had the highest number of views because it is a relatively new map, generating greater interest. This was especially true for CS2 videos, which received a much higher number of views than the CS:GO version.

---

### **Predictive Analysis**

What will happen?

- If the channel continues to post videos with the words “CS2” and “Smokes,” it will likely continue to grow.
- The same goes for videos made between 2023-2025, as the game is still relevant and many people are looking for this type of video. However, there will come a point where this will no longer be as relevant because people have watched this type of video and have already learned what they need to know.
- Continuing to make videos of new and relevant maps may generate greater interest in the videos.

---

### **Prescriptive Analysis**

What should we do?

- Post videos with keywords that generate the highest number of views
- Post videos with newly released maps in order to generate greater interest in the video, as many players want to learn about the map as quickly as possible
- Post while CS2 is still relevant

# Developed by: 

  * [Felipe Roll - Linkedin](https://www.linkedin.com/in/felipe-roll)
  * [Felipe Roll - Github](https://github.com/FelipeLRoll)
  * [Felipe Roll - Gmail](felipelroll@gmail.com)


