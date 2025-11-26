async function sendMessage() {
  const msgInput = document.getElementById("msg");
  const msg = msgInput.value.trim();
  const chatDiv = document.getElementById("chat");

  if (!msg) return;

  // Show user message
  chatDiv.innerHTML += `<p><b>You:</b> ${msg}</p>`;

  try {
    const res = await fetch("http://127.0.0.1:9000/chat/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg }),
    });

    if (!res.ok) {
      throw new Error(`HTTP ${res.status}`);
    }

    const data = await res.json();

    // Pick what to show from ChatResponse
    // data = { original_question, is_valid, refined_question, similar_questions }
    let botText = "";

    if (data.is_valid) {
      botText = data.refined_question || "I refined your question, but got an empty response.";
    } else {
      botText = "This doesn't look like a valid math question.";
    }

    chatDiv.innerHTML += `<p><b>Bot:</b> ${botText}</p>`;
  } catch (err) {
    chatDiv.innerHTML += `<p style="color:red;"><b>Error:</b> ${err}</p>`;
  }

  msgInput.value = "";
}
