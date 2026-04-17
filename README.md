# Social Platform Engagement Analysis

## Overview
This project simulates a Reddit-style social platform database to analyze user behavior, content engagement, and platform health. It was designed to demonstrate end-to-end data skills from relational database design and data generation to SQL analytics and interactive visualization.

**Tools Used:** PostgreSQL, Python, DBeaver, Tableau Public, GitHub

## Project Structure
├── schema.sql                  # Database schema for all 10 tables
├── generate_data.py            # Python script to generate synthetic data
├── analytical_queries.sql      # SQL queries for product analytics
├── query1_top_users.csv        # Top 10 users by post volume
├── query2_category_engagement.csv  # Category engagement by avg comments
├── query3_daily_post_volume.csv    # Daily post volume over 30 days
├── query4_top_voted_posts.csv      # Top 10 highest voted posts
├── query5_report_reasons.csv       # Report reasons breakdown
├── query6_top_followed_users.csv   # Top 10 most followed users
├── query8_notification_read_rate.csv # Notification read rate by type

## Database Schema
The database consists of 10 tables modeling a social platform:
- **Users** — user accounts and authentication details
- **Posts** — user generated content assigned to categories
- **Comments** — user responses on posts
- **Votes** — upvotes and downvotes on posts
- **Categories** — topic groups for posts
- **Moderators** — users assigned to manage categories
- **Reports** — flagged content for moderation review
- **Messages** — private messages between users
- **Followers** — user to user follow relationships
- **Notifications** — activity alerts for users

## Data Generation
Synthetic data was generated using Python and the Faker library, simulating realistic platform activity:
| Table | Rows Generated |
|---|---|
| Users | 500 |
| Posts | 2,000 |
| Comments | 10,000 |
| Votes | 15,000 |
| Moderators | 10 |
| Reports | 500 |
| Messages | ~3,000 |
| Followers | ~5,000 |
| Notifications | 8,000 |

## Analytical Queries
Eight analytical queries were written to answer key product questions:
1. **Top 10 Most Active Users by Post Volume** — identifies power users driving content creation
2. **Most Engaged Categories by Avg Comments** — surfaces which topics generate the most discussion
3. **Daily Post Volume Over 30 Days** — tracks posting trends over time
4. **Top 10 Highest Voted Posts** — surfaces the most positively received content
5. **Most Common Report Reasons** — identifies patterns in content moderation
6. **Users with the Most Followers** — identifies the most influential users on the platform
7. **Posts with Zero Engagement** — identifies content that failed to gain traction
8. **Notification Read Rate by Message Type** — measures which notifications users actually engage with

## Dashboard
An interactive Tableau Public dashboard visualizes the analytical findings across 7 charts covering user activity, content engagement, and platform health.
🔗 [View Live Dashboard](https://public.tableau.com/app/profile/ben.muchemi/viz/SocialPlatformEngagementDashboard/SocialPlatformEngagementDashboard?publish=yes)

## Key Insights
- A small group of power users drive the majority of content creation on the platform
- Engagement is relatively consistent across categories suggesting broad topic appeal
- Daily post volume shows natural variance with no significant drop off indicating a healthy active platform
- Report reasons are evenly distributed across spam, harassment, misinformation, hate speech, and off topic content suggesting a diverse set of moderation challenges
- Notification read rates hover around 50% across all message types indicating room for improvement in notification relevance and delivery