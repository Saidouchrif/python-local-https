document.addEventListener("DOMContentLoaded", () => {
    const status = document.getElementById("status");
    const btn = document.getElementById("btn");
    const responseBox = document.getElementById("response");

    status.textContent = "🔍 Ready to send a request.";

    btn.addEventListener("click", async () => {
        status.textContent = "⏳ Sending request...";

        try {
            const res = await fetch("https://localhost:4443/api/test");
            const data = await res.text();
            responseBox.textContent = data;
            status.textContent = "✅ HTTPS Request successful!";
        } catch (err) {
            status.textContent = "❌ Error connecting to HTTPS server.";
            responseBox.textContent = err.message;
        }
    });
});
