def calculate_health_score(data):

    stars = data["stars"]
    forks = data["forks"]
    issues = data["open_issues"]

    activity_score = 80

    if stars > 1000:
        activity_score += 5

    if forks > 100:
        activity_score += 5

    if data["updated_at"]:
        activity_score += 5

    activity_score = min(activity_score, 100)

    community_score = 50

    if stars > 100:
        community_score += 15

    if stars > 1000:
        community_score += 15

    if forks > 100:
        community_score += 10

    community_score = min(community_score, 100)

    documentation_score = 50

    if data["description"]:
        documentation_score += 20

    if data["license"] != "No license":
        documentation_score += 20

    documentation_score = min(documentation_score, 100)

    issue_score = 100

    if issues > 100:
        issue_score -= 20

    if issues > 500:
        issue_score -= 20

    issue_score = max(issue_score, 0)

    final_score = round(
        activity_score * 0.30 +
        community_score * 0.25 +
        documentation_score * 0.20 +
        issue_score * 0.25
    )

    return {
        "overall": final_score,
        "activity": activity_score,
        "community": community_score,
        "documentation": documentation_score,
        "issue_management": issue_score
    }
