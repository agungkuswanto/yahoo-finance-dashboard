document.addEventListener('DOMContentLoaded', function () {
    // Mengambil data dari elemen HTML
    var label1 = document.getElementById("Metric").children[1].innerHTML;
    var label2 = document.getElementById("Metric").children[2].innerHTML;
    var label3 = document.getElementById("Metric").children[3].innerHTML;
    var label4 = document.getElementById("Metric").children[4].innerHTML;

    var data1 = document.getElementById("Revenue").children[1].innerHTML;
    var data2 = document.getElementById("Revenue").children[2].innerHTML;
    var data3 = document.getElementById("Revenue").children[3].innerHTML;
    var data4 = document.getElementById("Revenue").children[4].innerHTML;

    // Membuat konfigurasi chart
    var canvasElement = document.getElementById("revenueChart");
    var config = {
        type: "bar",
        data: {
            labels: [label1, label2, label3, label4],
            datasets: [{
                label: "Revenue",
                data: [data1, data2, data3, data4],
                backgroundColor: ["rgba(20, 142, 241, 0.8)"],
                borderColor: ["rgba(5, 16, 63, 0.96)"],
                borderWidth: 1,
            }],
        }
    };
    
    // Membuat chart
    var barChart = new Chart(canvasElement, config);
});
