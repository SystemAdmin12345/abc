# Define the branch names
$localBranch = "master"
$githubBranch = "master"
$gitlabBranch = "main"

# Push to the remote branches
git push origin $localBranch:$githubBranch
git push gitlab $localBranch:$gitlabBranch
