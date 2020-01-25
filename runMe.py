
    import os
 
   
    command = "git branch | grep -v "master" | grep -v "dev"| g ep -v  "release" | xargs git branch -D"
    os.system(command)

   