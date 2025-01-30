// script.js
function getPrediction() {
    fetch('http://127.0.0.1:5000/predict')
        .then(response => response.json())
        .then(data => {
            // Update the HTML with the prediction result
            document.getElementById("prediction").textContent = "Predicted Next Action: " + data.predicted_action;
        })
        .catch(error => console.error('Error:', error));
}
