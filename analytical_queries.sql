-- Query 1: Top 10 Most Active Users by Post Volume
SELECT u.Username, COUNT(p.PostID) AS TotalPosts
FROM Users u
JOIN Posts p ON u.UserID = p.UserID
GROUP BY u.Username
ORDER BY TotalPosts DESC
LIMIT 10;

-- Query 2: Most Engaged Categories by Average Comments Per Post
SELECT c.Name, AVG(CommentCounts.TotalComments) AS AvgComments
FROM Categories c
JOIN (
    SELECT p.CategoryID, COUNT(cm.CommentID) AS TotalComments
    FROM Posts p
    LEFT JOIN Comments cm ON p.PostID = cm.PostID
    GROUP BY p.PostID, p.CategoryID
) AS CommentCounts ON c.CategoryID = CommentCounts.CategoryID
GROUP BY c.Name
ORDER BY AvgComments DESC;

-- Query 3: Daily Post Volume Over the Last 30 Days
SELECT DATE(p.Timestamp) AS PostDate, COUNT(p.PostID) AS DailyPostCount
FROM Posts p
WHERE p.Timestamp >= NOW() - INTERVAL '30 days'
GROUP BY DATE(p.Timestamp)
ORDER BY PostDate ASC;

-- Query 4: Top 10 Highest Voted Posts
SELECT p.Title, u.Username, SUM(v.VoteType) AS TotalScore
FROM Posts p
JOIN Users u ON p.UserID = u.UserID
JOIN Votes v ON p.PostID = v.PostID
GROUP BY p.Title, u.Username
ORDER BY TotalScore DESC
LIMIT 10;

-- Query 5: Most Common Report Reasons
SELECT Reason, COUNT(ReportID) AS TotalReports
FROM Reports
GROUP BY Reason
ORDER BY TotalReports DESC;

-- Query 6: Users with the Most Followers
SELECT u.Username, COUNT(f.FollowerUserID) AS TotalFollowers
FROM Users u
JOIN Followers f ON u.UserID = f.FollowedUserID
GROUP BY u.Username
ORDER BY TotalFollowers DESC
LIMIT 10;

-- Query 7: Posts with Zero Engagement
SELECT p.PostID, p.Title, u.Username
FROM Posts p
JOIN Users u ON p.UserID = u.UserID
WHERE p.PostID NOT IN (
    SELECT DISTINCT PostID FROM Comments
)
AND p.PostID NOT IN (
    SELECT DISTINCT PostID FROM Votes
);

-- Query 8: Notification Read Rate by Message Type
SELECT Message, 
COUNT(*) AS TotalNotifications,
SUM(CASE WHEN IsRead = TRUE THEN 1 ELSE 0 END) AS TotalRead,
ROUND(SUM(CASE WHEN IsRead = TRUE THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS ReadPercentage
FROM Notifications
GROUP BY Message
ORDER BY ReadPercentage DESC;