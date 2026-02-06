from datetime import datetime
from shlex import quote
import requests
import json
import random

with open("tokei.json") as f:
    data = json.load(f)

loc = sum(lang["code"] for lang in data.values())

GITHUB_USERNAME = "YugShrivastava"
learning_lines = [
    "Exploring Go & mastering concurrency patterns",
    "Building scalable backend systems",
    "Diving deep into distributed systems & microservices",
    "Optimizing DevOps pipelines for max efficiency",
    "Experimenting with Go routines & channel magic",
    "Studying backend architecture & system design",
    "Scaling services for millions of users",
    "Containerization & cloud orchestration adventures",
    "Exploring observability, monitoring & logging",
    "Making systems faster, reliable, and elegant"
]

quotes = [
    "Stay curious, keep coding.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Simplicity is the soul of efficiency.",
    "Hack the planet!",
    "Eat, Sleep, Code, Repeat.",
    "Good code is its own best documentation.",
    "Debugging is like being the detective in a crime movie where you are also the murderer.",
    "The best way to predict the future is to invent it.",
    "Programs must be written for people to read, and only incidentally for machines to execute.",
    "Performance is not about faster code, it's about smarter architecture."
]

def fetch_github_stats():
    user_api = f"https://api.github.com/users/{GITHUB_USERNAME}"
    repos_api = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100"

    # User profile
    user_data = requests.get(user_api).json()
    repo_count = user_data.get("public_repos", 0)

    # Stars
    stars = 0
    repos_data = requests.get(repos_api).json()
    for repo in repos_data:
        stars += repo.get("stargazers_count", 0)

    return {
        "repos": repo_count,
        "stars": stars,
        "commits": "dynamic",  # placeholder for now
    }

def fetch_total_commits():
    repos_api = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100"
    total_commits = 0

    repos_data = requests.get(repos_api).json()
    for repo in repos_data:
        commits_api = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo['name']}/commits?per_page=1"
        # Get total commits from 'Link' header if paginated
        r = requests.get(commits_api)
        if "Link" in r.headers:
            link_header = r.headers["Link"]
            # extract last page number
            import re
            m = re.search(r'&page=(\d+)>; rel="last"', link_header)
            if m:
                total_commits += int(m.group(1))
            else:
                total_commits += len(r.json())
        else:
            total_commits += len(r.json())

    return total_commits


USERNAME = "Yug Shrivastava"
GREEN = "#39ff14"
WHITE = "#e6e6e6"
BG = "#0b0b0b"

github_stats = fetch_github_stats()
github_stats["commits"] = fetch_total_commits()
learning_text = random.choice(learning_lines)
quote_text = random.choice(quotes)

lines = [
    "██╗   ██╗██╗   ██╗ ██████╗ ",
    "╚██╗ ██╔╝██║   ██║██╔════╝ ",
    " ╚████╔╝ ██║   ██║██║  ███╗",
    "  ╚██╔╝  ██║   ██║██║   ██║",
    "   ██║   ╚██████╔╝╚██████╔╝",
    "   ╚═╝    ╚═════╝  ╚═════╝ ",
    "",
    "────────────────────────────────────────",
    f"USER      ▸ {USERNAME}",
    "OS        ▸ Linux | Windows",
    "EDITOR    ▸ Zed · VS Code",
    "STACK     ▸ Go · TypeScript · Python · C++",
    "LANG      ▸ English · Hindi",
    "────────────────────────────────────────",
    "",
    "$ whoami",
    "> engineer · builder · curious by default",
    "",
    "$ github --stats",
    f"Stars .......... {github_stats['stars']}",
    f"Repositories ... {github_stats['repos']}",
    f"Commits ........ {github_stats['commits']}",
    f"Line of Code .... {loc}",
    "",
    "$ learning",
    f"> {learning_text}",
    "",
    # "$ current-project",
    # "> dynamic",
    # "",
    # "$ spotify --status",
    # "> dynamic",
    # "",
    # "$ discord --presence",
    # "> celestial_nomad12 · dynamic",
    # "",
    "$ uptime",
    f"> online · {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
    "",
    "$ quote",
    f'> {quote_text}',
]

y = 30
svg_lines = []

for line in lines:
    if line.startswith("$"):
        svg_lines.append(
            f'<text x="20" y="{y}" fill="{GREEN}">$</text>'
            f'<text x="35" y="{y}" fill="{WHITE}">{line[1:]}</text>'
        )
    else:
        svg_lines.append(
            f'<text x="20" y="{y}" fill="{WHITE}">{line}</text>'
        )
    y += 22

svg = f"""
<svg width="900" height="{y+20}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="{BG}" rx="12"/>
  <style>
    text {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 16px;
      white-space: pre;
    }}
  </style>
  {''.join(svg_lines)}
</svg>
"""

with open("terminal.svg", "w") as f:
    f.write(svg.strip())
