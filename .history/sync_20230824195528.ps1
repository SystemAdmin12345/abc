# Define the repository URLs for GitHub and GitLab
$githubRepoURL = "https://github.com/SystemAdmin12345/abc.git"
$gitlabRepoURL = "https://gitlab.com/randoritos/abc.git"

# Define the branch names
$localBranch = "master"
$githubBranch = "master"
$gitlabBranch = "main"

# Push to the remote branches
git push github $localBranch:$githubBranch
git push gitlab $localBranch:$gitlabBranch

