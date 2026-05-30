# YOUTUBE-DESHBOARD
# MRNIRITEACH YOUTUBE CHHENEL PROJECT

# STEP BY STEP 

# Phase 1: Project Planning


# Video Data Store गर्ने
# Total Views निकाल्ने
# Total Likes निकाल्ने
# Total Comments निकाल्ने
# Most Viewed Video पत्ता लगाउने
# Most Liked Video पत्ता लगाउने
# Average Views निकाल्ने
# Graph बनाउने
# Dashboard Report देखाउने

# Phase 3: Pandas

# CSV File Read

# Data Print

import pandas as pd

df = pd.read_csv("youtube_data.csv")

print(df)

import pandas as pd

df = pd.read_csv("youtube_data.csv")

# Data Print

print(df.head())

# Dataset Information
print(df.info())

# Statistical Summary
print(df.describe())

# Column Names
print(df.columns)

# एउटा Column
print(df["Views"])

# Multiple Columns
print(df[["Title", "Views"]])

# full code
import pandas as pd

df = pd.read_csv("youtube_data.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df["Views"])
print(df[["Title", "Views"]])

# Phase 4: Data Analysis

# total view
import pandas as pd

df = pd.read_csv("youtube_data.csv")

total_views = df["Views"].sum()

print(total_views)


# Total Likes


total_likes = df["Likes"].sum()

print(total_likes)

# total comment

total_comments = df["Comments"].sum()

print(total_comments)


# Average Views

average_views = df["Views"].mean()

print(average_views)

# Highest Viewed Video

highest_viewed_index = df["Views"].idxmax()

print(highest_viewed_index)


# Video Name


highest_video = df.loc[highest_viewed_index, "Title"]

print(highest_video)

# Highest Liked Video

highest_like_index = df["Likes"].idxmax()

highest_like_video = df.loc[highest_like_index, "Title"]

print(highest_like_video)


# Lowest Viewed Video

lowest_index = df["Views"].idxmin()

lowest_video = df.loc[lowest_index, "Title"]

print(lowest_video)

# Total Videos Count

total_videos = len(df)

print(total_videos)

# full code
import pandas as pd

df = pd.read_csv("youtube_data.csv")

total_videos = len(df)

total_views = df["Views"].sum()

total_likes = df["Likes"].sum()

average_views = df["Views"].mean()

highest_viewed_index = df["Views"].idxmax()

highest_viewed_video = df.loc[highest_viewed_index, "Title"]

print("===== YOUTUBE DASHBOARD =====")

print("Total Videos:", total_videos)

print("Total Views:", total_views)

print("Total Likes:", total_likes)

print("Average Views:", average_views)

print("Most Viewed Video:", highest_viewed_video)


# | Function    | काम                          |
# | ----------- | ---------------------------- |
# | `.sum()`    | Total निकाल्ने               |
# | `.mean()`   | Average निकाल्ने             |
# | `.idxmax()` | सबैभन्दा ठूलो Value भएको Row |
# | `.idxmin()` | सबैभन्दा सानो Value भएको Row |
# | `len()`     | Total Rows Count             |
# | `.loc[]`    | Particular Data निकाल्ने     |


# Phase 5: NumPy Integration


import pandas as pd
import numpy as np

df = pd.read_csv("youtube_data.csv")

# Views Column लाई NumPy Array मा Convert

views = np.array(df["Views"])

print(views)

# Mean (Average)

mean_views = np.mean(views)

print(mean_views)

# Median

median_views = np.median(views)

print(median_views)

# Maximum Value

max_views = np.max(views)

print(max_views)


# Minimum Value


min_views = np.min(views)

print(min_views)

# Standard Deviation

std_views = np.std(views)

print(std_views)


# Likes


likes = np.array(df["Likes"])

# Average Likes:

print(np.mean(likes))

# Maximum Likes:

print(np.max(likes))

# Minimum Likes:

print(np.min(likes))

# Median Likes:

print(np.median(likes))

# Full NumPy Report


import pandas as pd
import numpy as np

df = pd.read_csv("youtube_data.csv")

views = np.array(df["Views"])

print("===== NUMPY ANALYSIS =====")

print("Mean Views:", np.mean(views))

print("Median Views:", np.median(views))

print("Maximum Views:", np.max(views))

print("Minimum Views:", np.min(views))

print("Standard Deviation:", np.std(views))

# Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset Load

df = pd.read_csv("youtube_data.csv")

# Data

titles = df["Title"]

views = df["Views"]

# Views Bar Chart

plt.bar(titles, views)

plt.show()

# Full Code

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("youtube_data.csv")

titles = df["Title"]
views = df["Views"]

plt.bar(titles, views)

plt.show()

# Chart लाई राम्रो बनाऊ

plt.figure(figsize=(10,5))

plt.bar(titles, views)

plt.title("YouTube Video Views")

plt.xlabel("Video Title")

plt.ylabel("Views")

plt.show()

# Likes Bar Chart

titles = df["Title"]

likes = df["Likes"]

plt.figure(figsize=(10,5))

plt.bar(titles, likes)

plt.title("Video Likes")

plt.xlabel("Video Title")

plt.ylabel("Likes")

plt.show()

# Monthly Views Trend

# Data निकाल

months = df["Upload_Month"]

views = df["Views"]

# Line Chart


plt.figure(figsize=(10,5))

plt.plot(months, views)

plt.title("Monthly Views Trend")

plt.xlabel("Month")

plt.ylabel("Views")

plt.show()

# Likes Pie Chart

likes = df["Likes"]

titles = df["Title"]

# Pie Chart

plt.figure(figsize=(8,8))

plt.pie(likes, labels=titles)

plt.title("Likes Distribution")

plt.show()

# Graph Save

plt.figure(figsize=(10,5))

plt.bar(titles, views)

plt.title("Views")

plt.savefig("views.png")

plt.show()

# mini version

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("youtube_data.csv")

titles = df["Title"]
views = df["Views"]

plt.figure(figsize=(10,5))

plt.bar(titles, views)

plt.title("YouTube Video Views Analysis")

plt.xlabel("Videos")

plt.ylabel("Views")

plt.show()

# Dashboard Report Generation

# Total Views
# Total Subscribers
# Top Videos
# Revenue

# Most Liked Video

highest_like_index = df["Likes"].idxmax()

most_liked_video = df.loc[highest_like_index, "Title"]

most_likes = df.loc[highest_like_index, "Likes"]

# Dashboard Print

print("Total Videos:", total_videos)

print("Total Views:", total_views)

print("Total Likes:", total_likes)

print("Total Comments:", total_comments)

print("Average Views:", average_views)

# Top 3 Videos

top3 = df.sort_values(by="Views", ascending=False)
top3 = top3.head(3)
print(top3[["Title", "Views"]])

# Full Dashboard Layout
print("=" * 50)

print("YOUTUBE ANALYTICS DASHBOARD")

print("=" * 50)

# Phase 8


# Basic Menu System
# ===== YOUTUBE DASHBOARD =====

# 1. Show Dashboard
# 2. Add New Video
# 3. Search Video
# 4. Top 3 Videos
# 5. Save Report
# 6. Exit

# Loop


import pandas as pd
import numpy as np

df = pd.read_csv("youtube_data.csv")

while True:
    print("\n===== YOUTUBE DASHBOARD =====")
    print("1. Show Dashboard")
    print("2. Add New Video")
    print("3. Search Video")
    print("4. Top 3 Videos")
    print("5. Save Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Dashboard Option (1)

    if choice == "1":

        print("\n===== DASHBOARD =====")

    print("Total Videos:", len(df))
    print("Total Views:", df["Views"].sum())
    print("Total Likes:", df["Likes"].sum())
    print("Average Views:", np.mean(df["Views"]))

    # Add New Video (Option 2)

    elif choice == "2":
    title = input("Enter Video Title: ")
    views = int(input("Enter Views: "))
    likes = int(input("Enter Likes: "))
    comments = int(input("Enter Comments: "))
    month = input("Enter Month: ")

    new_data = pd.DataFrame([[title, views, likes, comments, month]],
        columns=df.columns)

    df = pd.concat([df, new_data], ignore_index=True)

    print("Video Added Successfully!")


    # Video Search (Option 3)

    elif choice == "3":
    name = input("Enter Video Name: ")

    result = df[df["Title"].str.contains(name, case=False)]

    if len(result) == 0:
        print("Video Not Found")
    else:
        print(result)

        # Top 3 Videos (Option 4)

        elif choice == "4":
    top = df.sort_values(by="Views", ascending=False).head(3)

    print("\n===== TOP 3 VIDEOS =====")
    print(top[["Title", "Views"]])

    # Save Report (Option 5)

    elif choice == "5":
    file = open("report.txt", "w")

    file.write("YOUTUBE ANALYTICS REPORT\n")
    file.write("========================\n")

    file.write(f"Total Videos: {len(df)}\n")
    file.write(f"Total Views: {df['Views'].sum()}\n")
    file.write(f"Total Likes: {df['Likes'].sum()}\n")
    file.write(f"Average Views: {np.mean(df['Views'])}\n")

    file.close()

    print("Report Saved Successfully!")

    # Exit System (Option 6)

    elif choice == "6":
    print("Exiting System...")
    break

# Wrong Input Handle

else:
    print("Invalid Choice! Try Again.")

    # Full Phase 8 Code (Complete System)

    import pandas as pd
import numpy as np

df = pd.read_csv("youtube_data.csv")

while True:
    print("\n===== YOUTUBE DASHBOARD =====")
    print("1. Show Dashboard")
    print("2. Add New Video")
    print("3. Search Video")
    print("4. Top 3 Videos")
    print("5. Save Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n===== DASHBOARD =====")
        print("Total Videos:", len(df))
        print("Total Views:", df["Views"].sum())
        print("Total Likes:", df["Likes"].sum())
        print("Average Views:", np.mean(df["Views"]))

    elif choice == "2":
        title = input("Enter Video Title: ")
        views = int(input("Enter Views: "))
        likes = int(input("Enter Likes: "))
        comments = int(input("Enter Comments: "))
        month = input("Enter Month: ")

        new_data = pd.DataFrame([[title, views, likes, comments, month]],
                                columns=df.columns)

        df = pd.concat([df, new_data], ignore_index=True)

        print("Video Added Successfully!")

    elif choice == "3":
        name = input("Enter Video Name: ")

        result = df[df["Title"].str.contains(name, case=False)]

        if len(result) == 0:
            print("Video Not Found")
        else:
            print(result)

    elif choice == "4":
        top = df.sort_values(by="Views", ascending=False).head(3)

        print("\n===== TOP 3 VIDEOS =====")
        print(top[["Title", "Views"]])

    elif choice == "5":
        file = open("report.txt", "w")

        file.write("YOUTUBE ANALYTICS REPORT\n")
        file.write("========================\n")

        file.write(f"Total Videos: {len(df)}\n")
        file.write(f"Total Views: {df['Views'].sum()}\n")
        file.write(f"Total Likes: {df['Likes'].sum()}\n")
        file.write(f"Average Views: {np.mean(df['Views'])}\n")

        file.close()

        print("Report Saved Successfully!")

    elif choice == "6":
        print("Exiting System...")
        break

    else:
        print("Invalid Choice! Try Again.")



#   FULL PROJECT CODE  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================
# PHASE 3: LOAD DATA
# =========================
df = pd.read_csv("youtube_data.csv")


# =========================
# MAIN LOOP (PHASE 8)
# =========================
while True:

    print("\n" + "="*50)
    print("     YOUTUBE ANALYTICS DASHBOARD")
    print("="*50)

    print("\n1. Show Dashboard")
    print("2. Add New Video")
    print("3. Search Video")
    print("4. Top 3 Videos")
    print("5. Save Report")
    print("6. Show Graph")
    print("7. Exit")

    choice = input("\nEnter choice: ")


    # =========================
    # PHASE 7: DASHBOARD
    # =========================
    if choice == "1":

        print("\n===== DASHBOARD REPORT =====")

        total_videos = len(df)
        total_views = df["Views"].sum()
        total_likes = df["Likes"].sum()
        total_comments = df["Comments"].sum()
        average_views = df["Views"].mean()

        print("Total Videos:", total_videos)
        print("Total Views:", total_views)
        print("Total Likes:", total_likes)
        print("Total Comments:", total_comments)
        print("Average Views:", average_views)

        # Most Viewed
        max_view_idx = df["Views"].idxmax()
        print("\nMost Viewed Video:", df.loc[max_view_idx, "Title"])
        print("Views:", df.loc[max_view_idx, "Views"])

        # Most Liked
        max_like_idx = df["Likes"].idxmax()
        print("\nMost Liked Video:", df.loc[max_like_idx, "Title"])
        print("Likes:", df.loc[max_like_idx, "Likes"])


    # =========================
    # PHASE 8: ADD VIDEO
    # =========================
    elif choice == "2":

        title = input("Enter Title: ")
        views = int(input("Enter Views: "))
        likes = int(input("Enter Likes: "))
        comments = int(input("Enter Comments: "))
        month = input("Enter Month: ")

        new_row = pd.DataFrame([[title, views, likes, comments, month]],
                               columns=df.columns)

        df = pd.concat([df, new_row], ignore_index=True)

        print("Video Added Successfully!")


    # =========================
    # SEARCH VIDEO
    # =========================
    elif choice == "3":

        name = input("Enter video name: ")

        result = df[df["Title"].str.contains(name, case=False)]

        if result.empty:
            print("Video Not Found")
        else:
            print("\nSearch Result:\n")
            print(result)


    # =========================
    # TOP 3 VIDEOS
    # =========================
    elif choice == "4":

        top3 = df.sort_values(by="Views", ascending=False).head(3)

        print("\n===== TOP 3 VIDEOS =====")
        print(top3[["Title", "Views"]])


    # =========================
    # SAVE REPORT
    # =========================
    elif choice == "5":

        with open("report.txt", "w") as f:

            f.write("YOUTUBE ANALYTICS REPORT\n")
            f.write("========================\n\n")

            f.write(f"Total Videos: {len(df)}\n")
            f.write(f"Total Views: {df['Views'].sum()}\n")
            f.write(f"Total Likes: {df['Likes'].sum()}\n")
            f.write(f"Total Comments: {df['Comments'].sum()}\n")
            f.write(f"Average Views: {df['Views'].mean()}\n")

        print("Report Saved Successfully!")


    # =========================
    # PHASE 6: GRAPH
    # =========================
    elif choice == "6":

        plt.figure(figsize=(10,5))
        plt.bar(df["Title"], df["Views"])
        plt.title("YouTube Views Analysis")
        plt.xlabel("Videos")
        plt.ylabel("Views")
        plt.xticks(rotation=45)
        plt.show()


    # =========================
    # EXIT
    # =========================
    elif choice == "7":
        print("Exiting Dashboard...")
        break


    else:
        print("Invalid Choice! Try Again.")





