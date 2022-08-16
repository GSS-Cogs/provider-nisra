# provider-nisra

Northern Ireland Statistics and Research Agency will be self-publishing [FAIR](https://www.go-fair.org/fair-principles/) data using [csvcubed](https://gss-cogs.github.io/csvcubed-docs/external/); this repo currently holds their qube-ish CSV-Ws experiments.

## Google Cloud Shell Integration Instructions

To use Google Cloud Shell and this repo click [here](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/GSS-Cogs/provider-nisra&cloudshell_image=gcr.io/optimum-bonbon-257411/cvcubed-cloudshell).

1. Step one, log into github in Google Cloud Shell

```bash
gh auth login
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: `####-####`
Press Enter to open github.com in your browser...
https://github.com/login/device
✓ Authentication complete.
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as `username`
```

2. Set your name

```bash
git config --global user.name "Your name here"
```

3. Set your email

```bash
git config --global user.email "your.email@email.gov.uk"
```

## Committing your changes

While using Google Cloud Shell, make changes, create `qube-config.json`, etc. Once you're ready click on the git-source toolbar on the left, stage your changes, provide a commit message, and then push to the repo.

## Updating output folders

Delete the out folder before rerunning the `csvcubed build` command do so using the following command from the same directory level as your csv and the `qube-config.json` file.

```bash
rm -rf out/
```
