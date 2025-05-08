document.addEventListener("DOMContentLoaded", function () {
    var chartContainer = document.getElementById("chartContainer");
    if (!chartContainer) {
        console.error("Chart container not found!");
        return;
    }

    var chartDataElement = document.getElementById("chartData");
    if (!chartDataElement) {
        console.error("Chart data element not found!");
        return;
    }

    var chartData = JSON.parse(chartDataElement.textContent || "[]");

    if (!chartData.length) {
        console.error("Chart data is empty.");
        return;
    }

    var dataPoints = chartData.map(function (point) {
        return { x: point.age, y: point.gfr };
    });

    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        theme: "light2",
        title: { text: "eGFR Trend Over Age" },
        axisX: { title: "Age (years)", interval: 5 },
        axisY: { title: "eGFR (mL/min)", minimum: 0, maximum: 120 },
        data: [
            {
                type: "line",
                dataPoints: dataPoints,
                color: "#1f77b4", // Blue color for the line
                markerColor: "#ff7f0e", // Orange dots
                lineThickness: 2,
            }
        ]
    });

    chart.render();
});

document.addEventListener("DOMContentLoaded", function() {
    let progress = document.querySelector('.circle-bar.one .circle.one'); 
    let number = document.querySelector('.circle-bar.one .circle.one .number');

    if (!progress || !number) {
        console.error("❌ Progress or number element not found!");
        return;
    }

    console.log("✅ Initial GfrValue from Django:", GfrValue);

    if (isNaN(GfrValue) || GfrValue < 0) {
        console.error("❌ Invalid GfrValue:", GfrValue);
        return;
    }

    // ✅ Immediately set number before animation
    number.innerHTML = `${GfrValue}<span>%</span>`;

    let degree = 0;
    let targetDegree = Math.min(Math.max(GfrValue, 0), 100); 

    let interval = setInterval(function() {
        if (degree >= targetDegree) {
            clearInterval(interval);
            return;
        }
        degree += 1;
        progress.style.background = `conic-gradient(#4caf50 ${degree}%, #fff 0%)`;
        number.innerHTML = `${degree}<span>%</span>`;
    }, 20);
});

document.addEventListener("DOMContentLoaded", function() {
    let progress2 = document.querySelector('.circle2.two'); 
    let number2 = progress2.querySelector('.number');

    let targetDegree2 = serumCreatininePercentage; // Get from Django
    let degree2 = 0;
    let color2 = "#3498db"; // Change color if needed

    var interval2 = setInterval(function() {
        degree2 += 1;
        if (degree2 > targetDegree2) {
            clearInterval(interval2);
            return;
        }
        progress2.style.background = `conic-gradient(${color2} ${degree2}%, #fff 0%)`;
        number2.innerHTML = degree2 + '<span>%</span>';
    }, 50);
});