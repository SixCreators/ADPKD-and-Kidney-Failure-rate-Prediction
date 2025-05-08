document.addEventListener("DOMContentLoaded", function () {
    let graphDataElement = document.getElementById("graphData");

    if (graphDataElement) {
        let graph_data = JSON.parse(graphDataElement.textContent);  // Fetch JSON data

        var ctx = document.getElementById("predictionChart").getContext("2d");
        new Chart(ctx, {
            type: "line",
            data: {
                labels: graph_data.labels,
                datasets: [{
                    label: "Kidney Function Prediction (%)",
                    data: graph_data.dataPoints,
                    borderColor: "rgba(54, 162, 235, 1)",
                    backgroundColor: "rgba(54, 162, 235, 0.2)",
                    fill: true,
                    tension: 0.3
                }]
            },
            options: {
                scales: {
                    x: { title: { display: true, text: "Age (Years)" } },
                    y: { min: 0, max: 100, title: { display: true, text: "Chance of Kidney Failure (%)" } }
                }
            }
        });
    } else {
        console.error("Graph data not found!");
    }
});