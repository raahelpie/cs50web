#Git


##Lecture notes (from lecture0):



Git can keep track of changes made to code, synchronize code between different people, test changes to code without losing the original, and revert back to old versions of code.
===
Basically, it is what is called as a version control system which helps us
keep track of the various versions of our files, and we get to decide what
the versions would be (our commits in the repo) (each commit would create a seperate version of all the files included in that commit).

And each one of those commits will be associated with a unique id which we would use whenever we want to revert back to old versions of the file.

How do we know the unique ids? git log would give us the various commits that we have done in that repository and provide us with the id, what changes we have made and the message we gave during our commit.


GitHub is a website that stores Git repositories on the internet to facilitate the collaboration that Git allows for. A repository is simply a place to keep track of code and all the changes to code.
===
GitHub is sort of a social platform where we can have our repositories online for other people and collaborators to check out, basically making our git repository sit remotely online. GitHub will also be useful for deployment, especially continuous deployment to sites like Heroku/Netlify.



##Git commands:

git clone <url> : take a repository stored on a server (like GitHub) and downloads it
===

This is only for when you know for sure you want to have a remote repository and so have created one in GitHub already. In this step, you are basically creating the clone of your remote repo and initializing git.

which otherwise, you would have to do it manually using: git init


git add <filename(s)> : add files to the staging area to be included in the next commit
===
OG explains well enough, just staging the files that you want to have a newer version of, so putting all these files onto a stage and getting them ready to commit.



git commit -m "message" : take a snapshot of the repository and save it with a message about the changes
===
This is where a new version for all the files in the staging area is created and is associated with an id and a message




git commit -am <filename(s)> "message" : add files and commit changes all in one
===
This is basically doing the above two steps in a single step



git status : print what is currently going on with the repository
===
The status of what files have changed, modified, created, deleted etc.,


git push : push any local changes (commits) to a remote server

git pull : pull any remote changes from a remote server to a local computer

git log : print a history of all the commits that have been made

git reflog : print a list of all the different references to commits

git reset --hard <commit> : reset the repository to a given commit

git reset --hard origin/master : reset the repository to its original state (e.g. the version cloned from GitHub)



When combining different versions of code, e.g. using git pull, a merge conflict can occur if the different versions have different data in the same location. Git will try to take care of merging automatically, but if two users edit, for example, the same line, a merge conflict will have to be manually resolved.
To resolve a merge conflict, simply locally remove all lines and code that are not wanted and push the results.
===
This automatic merging of git surprises me probably because I still don't know how it really works. I will experiment with it and update this README file stating the working. The example in the above og explains the merge conflit situation well enough.