# Define the repository URLs for GitHub and GitLab
$githubRepoURL = "https://github.com/yourusername/your-repo.git"
$gitlabRepoURL = "https://gitlab.com/yourusername/your-repo.git"

# Define the branch names
$localBranch = "master"
$githubBranch = "master"
$gitlabBranch = "main"

# Add the remote repositories
git remote add github $githubRepoURL
git remote add gitlab $gitlabRepoURL

# Push to the remote branches
git push github $localBranch:$githubBranch
git push gitlab $localBranch:$gitlabBranch

# Remove the added remotes (optional)
git remote remove github
git remote remove gitlab
