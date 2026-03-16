
import React, { useState } from "react";
import "./App.css";

function App() {

  const [owner, setOwner] = useState("");
  const [repo, setRepo] = useState("");
  const [issue, setIssue] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const runAI = async () => {

    setLoading(true);

    try {

      const res = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          owner,
          repo,
          issue: Number(issue)
        })
      });

      const data = await res.json();
      setResult(data);

    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };

  return (

    <div className="app">

      <div className="hero">

        <h1 className="title">
          ⚡ AI Issue → Pull Request System
        </h1>

        <p className="subtitle">
          Autonomous AI Developer Assistant
        </p>

        <div className="input-panel">

          <input
            placeholder="GitHub Owner"
            value={owner}
            onChange={(e) => setOwner(e.target.value)}
          />

          <input
            placeholder="Repository Name"
            value={repo}
            onChange={(e) => setRepo(e.target.value)}
          />

          <input
            placeholder="Issue Number"
            value={issue}
            onChange={(e) => setIssue(e.target.value)}
          />

          <button onClick={runAI}>
            Analyze Issue
          </button>

        </div>

      </div>

      {loading && (

        <div className="pipeline">

          <h2>🤖 AI Pipeline Running</h2>

          <div className="steps">

            <div className="step">🔍 Fetching Issue</div>
            <div className="step">📥 Cloning Repository</div>
            <div className="step">🧠 AI Analyzing Code</div>
            <div className="step">🛠 Generating Fix</div>
            <div className="step">🚀 Creating Pull Request</div>

          </div>

        </div>

      )}

      {result && (

        <div className="results">

          <div className="card">
            <h3>Issue</h3>
            <p>{result.issue}</p>
          </div>

          <div className="card">
            <h3>AI Analysis</h3>
            <p>{result.analysis}</p>
          </div>

          <div className="card">
            <h3>Generated Fix</h3>
            <pre>{result.fix}</pre>
          </div>

          <div className="card">
            <h3>AI Review</h3>
            <p>{result.review}</p>
          </div>

          {result.pull_request && (

            <div className="card">
              <h3>Pull Request</h3>

              <a
                href={result.pull_request}
                target="_blank"
                rel="noreferrer"
              >
                View Pull Request
              </a>

            </div>

          )}

        </div>

      )}

    </div>
  );
}

export default App;