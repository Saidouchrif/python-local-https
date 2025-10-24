document.addEventListener("DOMContentLoaded", () => {
  const status = document.getElementById("status");
  const btn = document.getElementById("btn");
  const responseBox = document.getElementById("response");

  status.textContent = "✅ Page loaded. Ready to connect.";

  btn.addEventListener("click", async () => {
    status.textContent = "⏳ Sending request...";

    try {
      const res = await fetch("https://localhost:4443", {
        method: "GET",
      });

      const text = await res.text();
      responseBox.textContent = text;
      status.textContent = "✅ HTTPS Request successful!";
    } catch (err) {
      status.textContent = "❌ Error connecting to HTTPS server.";
      responseBox.textContent = err.message;
    }
  });
});
