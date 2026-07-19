"""
GitHub Skill.
Wraps GitHub API operations using PyGithub.
"""

from github import Github
from github import GithubException
from config.settings import Settings


class GithubSkill:
    def __init__(self):
        token = Settings.GITHUB_TOKEN
        if not token:
            raise ValueError("GITHUB_TOKEN is not configured in .env file.")
        self.client = Github(token)

    def create_issue(self, repo_name: str, title: str, body: str = "") -> str:
        try:
            repo = self.client.get_repo(repo_name)
            issue = repo.create_issue(title=title, body=body)
            return f"Issue created successfully: {issue.html_url}"
        except GithubException as ex:
            return f"GitHub API Error: {ex}"

    def create_pr(
        self, repo_name: str, head: str, base: str, title: str, body: str = ""
    ) -> str:
        try:
            repo = self.client.get_repo(repo_name)
            pr = repo.create_pull(title=title, body=body, head=head, base=base)
            return f"Pull Request created successfully: {pr.html_url}"
        except GithubException as ex:
            return f"GitHub API Error: {ex}"
