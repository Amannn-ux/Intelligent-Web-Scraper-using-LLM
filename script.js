document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("scrapeButton").addEventListener("click", function () {
        let url = document.getElementById("urlInput").value.trim();

        if (!url) {
            alert("Please enter a valid URL.");
            return;
        }

        fetch("/scrape", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url: url })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("rawContent").textContent = "Error: " + data.error;
                document.getElementById("processedContent").textContent = "";
            } else {
                document.getElementById("rawContent").textContent = data.raw || "No raw content available.";
                document.getElementById("processedContent").textContent = data.processed || "No processed content available.";
            }
        })
        .catch(error => {
            console.error("Error:", error);
            document.getElementById("rawContent").textContent = "Error fetching data.";
            document.getElementById("processedContent").textContent = "";
        });
    });
});
