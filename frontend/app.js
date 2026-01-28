document.getElementById("newsForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const topic = document.getElementById("topicInput").value;
  const responseDiv = document.getElementById("result");
  const headlineEl = document.getElementById("headline");
  const bodyEl = document.getElementById("body");
  const issuesEl = document.getElementById("issues");

  try {
    const res = await fetch("/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ topic })
    });

    if (!res.ok) {
      throw new Error("Failed to generate article");
    }

    const data = await res.json();
    headlineEl.textContent = data.headline;
    bodyEl.textContent = data.body;

    issuesEl.innerHTML = "";
    data.issues.forEach(issue => {
      const li = document.createElement("li");
      li.textContent = issue;
      issuesEl.appendChild(li);
    });

    responseDiv.classList.remove("hidden");
  } catch (err) {
    alert("Error: " + err.message);
  }
});
