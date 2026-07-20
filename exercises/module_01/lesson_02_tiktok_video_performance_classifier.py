# Module 1 — Lesson 02: TikTok Video Performance Classifier
#
# Business problem:
# Classify a TikTok video's performance from its number of views.
#
# Your program must:
# 1. Display this title:
#    TikTok Video Performance Classifier
# 2. Ask the user to enter the video's view count.
# 3. Convert the input into an integer.
# 4. Use comparison operators with if / elif / else to classify the video:
#    - Fewer than 300 views: Low Performance
#    - From 300 to 499 views: Normal Performance
#    - 500 views or more: High Performance
# 5. Print the classification clearly.
#
# Acceptance criteria:
# - The program contains all three classification branches.
# - The comparison boundaries correctly handle 299, 300, 499, and 500.
# - You personally write the core logic.
# - Do not copy a completed solution from another source.
#
# Manual tests to perform after writing your program:
# - 299 should produce Low Performance.
# - 300 should produce Normal Performance.
# - 499 should produce Normal Performance.
# - 500 should produce High Performance.
# - Test one additional view count of your own choice.


# Write your implementation below this line.

print("TikTok Video Performance Classifier")
video_view_count=int(input("enter view count:"))
if video_view_count<300:
    print("Low Performance")
elif video_view_count>=500: 
    print("High Performance")
else:
    print("Normal Performance")                    