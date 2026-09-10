"""
Question 9 — GitHub: Git Workflow  [Short Answer]

This is the same workflow you used to SUBMIT this assessment, so you have
already done most of it. Write the exact git command for each step.

Scenario
--------
You have a local copy of a repo. You want to:
1. Create a new branch called `my-solutions`.
2. Switch to that branch.
3. After editing `q4.md`, stage that file for commit.
4. Commit the staged change with the message "Add Q4 answers".
5. Push the `my-solutions` branch to GitHub.

Write the exact git command for each step (one per line).
"""

# Step 1 — Create a new branch called `my-solutions`: 

PS C:\Users\User\5m-data-entry-test-v2> git checkout -b my-solutions
Switched to a new branch 'my-solutions'

# Step 2 — Switch to `my-solutions`:

PS C:\Users\User\5m-data-entry-test-v2> git switch my-solutions
M       src/q1.md
M       src/q2.md
M       src/q3.md
M       src/q4.md
M       src/q5.md
M       src/q6.md
M       src/q7.py
M       src/q8.py
Switched to branch 'my-solutions'


# Step 3 — Stage q4.md: 

cd src
notepad q4.md to stage q4.md
 
# Step 4 — Commit with message "Add Q4 answers": 
PS C:\Users\User\5m-data-entry-test-v2> git commit -m "Add Q4 answers"
[my-solutions 0761734] Add Q4 answers
 8 files changed, 105 insertions(+), 41 deletions(-)
PS C:\Users\User\5m-data-entry-test-v2>

# Step 5 — Push `my-solutions` to the remote: 

PS C:\Users\User\5m-data-entry-test-v2> git checkout main
M       src/q9.py
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
PS C:\Users\User\5m-data-entry-test-v2> git merge my-solutions
Updating ffa6acc..0761734
Fast-forward
 src/q1.md | 30 +++++++++++++++---------------
 src/q2.md | 29 +++++++++++++++++++++++++++--
 src/q3.md | 16 +++++++++++++---
 src/q4.md | 17 ++++++++++-------
 src/q5.md |  9 ++++++---
 src/q6.md | 28 ++++++++++++++++++++++------
 src/q7.py | 11 ++++++++---
 src/q8.py |  6 ++++--
 8 files changed, 105 insertions(+), 41 deletions(-)
PS C:\Users\User\5m-data-entry-test-v2> git commit -m "Add Q4 answers"
[main 0593c99] Add Q4 answers
 1 file changed, 50 insertions(+), 4 deletions(-)
PS C:\Users\User\5m-data-entry-test-v2> git commit -a
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

"""
Step 6 (short answer). You run `git status` and it says
`Changes not staged for commit`. In one sentence, what does that tell you,
and which command moves a file from there into the next commit?

    Answer:
It tell me that no file in the repository has been staged for commit.

To really commit a modified file, use the command git add file



"""
