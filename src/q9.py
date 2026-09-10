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

# Step 5 — Push `my-solutions` to the remote: git push -u origin my-solutions

PS C:\Users\User\5m-data-entry-test-v2> git push -u origin my-solutions
Enumerating objects: 21, done.
Counting objects: 100% (21/21), done.
Delta compression using up to 8 threads
Compressing objects: 100% (11/11), done.
Writing objects: 100% (11/11), 3.29 KiB | 1.65 MiB/s, done.
Total 11 (delta 8), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (8/8), completed with 8 local objects.
remote:
remote: Create a pull request for 'my-solutions' on GitHub by visiting:
remote:      https://github.com/pengkwai/5m-data-entry-test-v2/pull/new/my-solutions
remote:
To https://github.com/pengkwai/5m-data-entry-test-v2.git
 * [new branch]      my-solutions -> my-solutions
branch 'my-solutions' set up to track 'origin/my-solutions'.
PS C:\Users\User\5m-data-entry-test-v2>



"""
Step 6 (short answer). You run `git status` and it says
`Changes not staged for commit`. In one sentence, what does that tell you,
and which command moves a file from there into the next commit?

    Answer:
It tell me that no file in the repository has been really been commit.

To really commit all modified files, use the command git commit -a



"""
