const { Octokit } = require("@octokit/core");

async function run() {
  const octokit = new Octokit({ auth: process.env.PAT });

  try {
    await octokit.request("PUT /user/starred/:owner/:repo", {
      owner: "neerajcodes888",
      repo: "Loan-Approval-Prediction"
    });
    console.log("Repository starred successfully.");
  } catch (error) {
    console.error("Error starring repository:", error.message);
    process.exit(1);
  }
}

run();
