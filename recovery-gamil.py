class GitHub:
    def __init__(self):
        self.repos = []

    def create_repo(self, name):
        repo = Repo(name)
        self.repos.append(repo)

    def get_repos(self):
        return self.repos


class Repo:
    def __init__(self, name):
        self.name = name
        self.commits = []

    def add_commit(self, commit):
        self.commits.append(commit)

    def get_commits(self):
        return self.commits


class Commit:
    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message


class Gmail:
    def __init__(self):
        self.emails = []

    def send_email(self, subject, content, recipient):
        email = Email(subject, content, recipient)
        self.emails.append(email)

    def get_emails(self):
        return self.emails


class Email:
    def __init__(self, subject, content, recipient):
        self.subject = subject
        self.content = content
        self.recipient = recipient

    def get_subject(self):
        return self.subject

    def get_content(self):
        return self.content

    def get_recipient(self):
        return self.recipient


# Usage example
github = GitHub()
github.create_repo("dummy-repo")
repo = github.get_repos()[0]

repo.add_commit(Commit("Initial commit"))
repo.add_commit(Commit("Add feature A"))
repo.add_commit(Commit("Fix issue #12"))

commits = repo.get_commits()
for commit in commits:
    print(commit.get_message())

gmail = Gmail()
gmail.send_email("Hello", "This is a dummy email", "example@gmail.com")
emails = gmail.get_emails()
for email in emails:
    print(email.get_subject(), email.get_content(), email.get_recipient())
