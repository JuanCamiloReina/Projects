from re import S, sub
import praw
from praw.reddit import Submission

reddit = praw.Reddit(
    user_agent = "Get comments by /u/Cheap-Option-5076",
    client_id = "YJ5OUxMlaosJlCZBBHBCzQ",
    client_secret = "5x9zjL5UQHR96WK6It7wo-d1UaBb7w"
)

submission = reddit.submission(id = 'nsm98m')
submission.comments.replace_more(limit=None)
[]

for comment in submission.comments:
    print(comment.body + '\n')