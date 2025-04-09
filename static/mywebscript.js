function RunSentimentAnalysis() {
    let text = document.getElementById("textToAnalyze").value;

    fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById("system_response").innerText = data;
        })
        .catch(error => {
            document.getElementById("system_response").innerText = "Error: " + error;
        });
}
