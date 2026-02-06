from datetime import datetime
import requests
import random
import html

learning_lines = [
    "Exploring Go & mastering concurrency patterns",
    "Diving deep into distributed systems & microservices",
    "Experimenting with Go routines & channel magic",
    "Studying backend architecture & system design",
    "Containerization & cloud orchestration adventures",
    "Exploring observability, monitoring & logging",
]

quote_lines = [
    "Simplicity is the soul of efficiency.",
    "Don’t think of cost. Think of value.",
    "So many books, so little time.",
    "So many bugs, so little time.",
    "So many things to learn, so little time.",
    "Without code, life would be a runtime error."
]

GITHUB_USERNAME = "YugShrivastava"

def fetch_github_stats():
    user_api = f"https://api.github.com/users/{GITHUB_USERNAME}"
    repos_api = f"https://api.github.com/users/{GITHUB_USERNAME}/repos?per_page=100"

    user_resp = requests.get(user_api)
    if user_resp.status_code != 200:
        print("Warning: GitHub API rate limit or error")
        user_data = {}
    else:
        user_data = user_resp.json()

    repo_count = user_data.get("public_repos", 0)

    stars = 0
    repos_resp = requests.get(repos_api)
    if repos_resp.status_code != 200:
        print("Warning: Could not fetch repos")
        repos_data = []
    else:
        repos_data = repos_resp.json()
        if isinstance(repos_data, dict) and "message" in repos_data:
            print(f"GitHub API warning: {repos_data['message']}")
            repos_data = []

    for repo in repos_data:
        if isinstance(repo, dict):
            stars += repo.get("stargazers_count", 0)

    return {
        "repos": repo_count,
        "stars": stars,
        "commits": "dynamic",
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

def calculate_uptime(start_date):
    now = datetime.utcnow()
    delta = now - start_date

    days = delta.days
    years, days = divmod(days, 365)
    months, days = divmod(days, 30)
    hours, remainder = divmod(delta.seconds, 3600)
    minutes = remainder // 60

    return f"{years}y {months}m {days}d {hours:02}h {minutes:02}m"

GREEN = "#39ff14"
WHITE = "#e6e6e6"
BG = "#0b0b0b"
BIRTH_DATE = datetime(2004, 12, 12)

uptime_text = calculate_uptime(BIRTH_DATE)
github_stats = fetch_github_stats()
github_stats["commits"] = fetch_total_commits()
learning_text = random.choice(learning_lines)
quote_text = random.choice(quote_lines)

lines = [
    "██╗   ██╗██╗   ██╗ ██████╗ ",
    "╚██╗ ██╔╝██║   ██║██╔════╝ ",
    " ╚████╔╝ ██║   ██║██║  ███╗",
    "  ╚██╔╝  ██║   ██║██║   ██║",
    "   ██║   ╚██████╔╝╚██████╔╝",
    "   ╚═╝    ╚═════╝  ╚═════╝ ",
    "",
    "───────────────────────────────────────────",
    "USER      ▸ Yug Shrivastava",
    "OS        ▸ Linux | Windows",
    "EDITOR    ▸ Zed · VS Code",
    "PL        ▸ Go · TypeScript · Python · C++",
    "LANG      ▸ English · Hindi",
    "───────────────────────────────────────────",
    "",
    "$ whoami",
    "> engineer · designs for failure, hopes for uptime",
    "",
    "$ github --stats",
    f"> Stars .......... {github_stats['stars']}",
    f"> Repositories ... {github_stats['repos']}",
    f"> Commits ........ {github_stats['commits']}",
    "",
    "$ stack --list --formatted",
    "> backend",
    "  · Node.js · Express.js · Vitest · Gin · FastAPI · REST · GraphQL",
    "> frontend",
    "  · React.js · Next.js · Tailwind CSS · Webpack · Vite",
    "> database",
    "  · PostgreSQL · MongoDB · Redis · MySQL",
    "> ai/automation",
    "  · LangChain · LangGraph · PyTorch · MCP",
    "> deployment/tools",
    "  · Docker · AWS · Nginx · YAML · Figma · Git · Cloudflare",
    "",
    "$ current --focus",
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
    f"> online · {uptime_text}",
    "",
    "$ quote",
    f'> {quote_text}',
]

y = 30
svg_lines = []

for line in lines:
    safe_line = html.escape(line)

    if line.startswith("$"):
        svg_lines.append(
            f'<text x="20" y="{y}" fill="{GREEN}">$</text>'
            f'<text x="35" y="{y}" fill="{WHITE}">{html.escape(line[1:])}</text>'
        )
    else:
        svg_lines.append(
            f'<text x="20" y="{y}" fill="{WHITE}">{safe_line}</text>'
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
