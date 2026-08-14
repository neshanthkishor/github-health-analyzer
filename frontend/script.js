async function analyzeRepository() {

    const repoUrl = document.getElementById("repoUrl").value.trim();
    const error = document.getElementById("error");
    const result = document.getElementById("result");

    error.textContent = "";

    if (!repoUrl) {
        error.textContent = "Please enter a GitHub repository URL.";
        return;
    }

    try {

        const response = await fetch("https://github-health-analyzer.onrender.com/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                repo_url: repoUrl
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        const repo = data.repository;
        const score = data.health_score;

        result.classList.remove("hidden");

        document.getElementById("score").textContent = score.overall;

        document.getElementById("repoName").textContent =
            repo.full_name;

        document.getElementById("description").textContent =
            repo.description || "No description available.";

        document.getElementById("stars").textContent =
            repo.stars;

        document.getElementById("forks").textContent =
            repo.forks;

        document.getElementById("issues").textContent =
            repo.open_issues;

        document.getElementById("language").textContent =
            repo.language || "Not specified";

        updateBar("activity", "activityBar", score.activity);
        updateBar("community", "communityBar", score.community);
        updateBar("documentation", "documentationBar", score.documentation);
        updateBar("issue", "issueBar", score.issue_management);

    } catch (err) {

        result.classList.add("hidden");
        error.textContent = err.message;
    }
}


function updateBar(textId, barId, value) {

    document.getElementById(textId).textContent = value;

    document.getElementById(barId).style.width =
        value + "%";
}
