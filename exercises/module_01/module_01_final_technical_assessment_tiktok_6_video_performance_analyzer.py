"""
Module 1 Final Technical Assessment
TikTok 6-Video Performance Analyzer

Write the program personally in the STUDENT CODE AREA below.

Requirements:
- Process exactly 6 videos with for + range().
- Ask: Enter Video X Views:
- Convert the input with int().
- Views >= 0 are valid.
- For a negative value, print "Invalid Views" and ask again for the same video.
- Track total views and the number of videos with views >= 500.
- Track the highest views with its video number.
- Track the lowest views with its video number.
- The first valid video initializes both highest and lowest pairs.
- Use strict comparisons so the earliest video wins a tie.
- After all 6 valid videos, calculate average, high-view rate, and spread.
- Print all 9 required outputs using the specified formatting.

Do not use:
lists, tuples, dictionaries, functions, classes, nested for loops,
enumerate(), min(), max(), sum(), abs(), break, continue, None,
try/except, CSV, JSON, APIs, pandas, databases, or Streamlit.
"""


# STUDENT CODE AREA
total_views=0
high_view_count=0
highest_views=0
highest_video=0
lowest_views=0
lowest_video=0

for video in range(1,7):
    views=int(input(f"Enter Video {video} Views:"))
    while views<0:
        print("Invalid Views")
        views=int(input(f"Enter Video {video} Views:"))
    if views>=0:
        total_views+=views
    if views>=500:
        high_view_count+=1
    if video==1 or highest_views<views:
        highest_views=views
        highest_video=video
    if video==1 or lowest_views>views:
        lowest_views=views
        lowest_video=video

average_views=total_views/6
high_view_rate=(high_view_count/6)*100
view_spread=highest_views-lowest_views

print(f"Total Views: {total_views}")
print(f"Average Views: {average_views:.2f}")
print(f"500+ View Videos: {high_view_count}")
print(f"500+ View Rate: {high_view_rate:.2f}%")
print(f"Best Video: Video {highest_video}") 
print(f"Highest Views: {highest_views}")       
print(f"Worst Video: Video {lowest_video}")
print(f"Lowest Views: {lowest_views}")
print(f"View Spread: {view_spread}")

