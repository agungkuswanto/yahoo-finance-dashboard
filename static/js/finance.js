// Fungsi untuk mengambil data dari elemen HTML
function getChartData(metricId, rowId) {
    const labels = [];
    const data = [];
    const metricRow = document.getElementById(metricId).children;
    const dataRow = document.getElementById(rowId).children;

    for (let i = 1; i < metricRow.length; i++) {
        labels.push(metricRow[i].innerHTML); // Ambil label (misal: Quarter)
        data.push(parseFloat(dataRow[i].innerHTML)); // Ambil data numerik
    }

    return { labels, data };
}

// Fungsi untuk membuat konfigurasi chart
function createChartConfig(labels, data, label, backgroundColor, borderColor) {
    return {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                backgroundColor: backgroundColor,
                borderColor: borderColor,
                borderWidth: 1,
            }],
        },
    };
}

// Fungsi untuk membuat chart
function renderChart(canvasId, config) {
    const canvasElement = document.getElementById(canvasId);
    new Chart(canvasElement, config);
}

document.addEventListener('DOMContentLoaded', function () {

    // Revenue Chart
    const revenueData = getChartData("Metric", "Revenue");
    const revenueConfig = createChartConfig(
        revenueData.labels,
        revenueData.data,
        "Revenue",
        "rgba(20, 142, 241, 0.8)",
        "rgba(5, 16, 63, 0.96)"
    );

    renderChart("revenueChart", revenueConfig);

    // Net Income Chart (Contoh chart tambahan)
    const netIncomeData = getChartData("Metric", "Net Income");
    const netIncomeConfig = createChartConfig(
        netIncomeData.labels,
        netIncomeData.data,
        "Net Income",
        "rgba(241, 142, 20, 0.8)",
        "rgba(63, 16, 5, 0.96)"
    );
    renderChart("netIncomeChart", netIncomeConfig);

    // Dividends Chart (Contoh chart tambahan)
    const dividendData = getChartData("Metric", "Dividends");
    const dividendConfig = createChartConfig(
        dividendData.labels,
        dividendData.data,
        "Dividends",
        "rgba(12, 71, 47, 0.8)",
        "rgba(21, 130, 11, 0.96)"
    );
    renderChart("dividendsChart", dividendConfig);

    // Dividends Chart 
    const EPSData = getChartData("Metric", "EPS");
    const EPSConfig = createChartConfig(
        EPSData.labels,
        EPSData.data,
        "Earning Per Share",
        "rgba(28, 12, 129, 0.8)",
        "rgba(22, 64, 205, 0.96)"
    );
    renderChart("EPSChart", EPSConfig);

    // FREE CASH FLOW Chart 
    const FCFData = getChartData("Metric", "Free Cash Flow");
    const FCFConfig = createChartConfig(
        FCFData.labels,
        FCFData.data,
        "Free Cash Flow",
        "rgba(207, 61, 8, 0.8)",
        "rgba(174, 88, 21, 0.96)"
    );
    renderChart("FreeCashFlowChart", FCFConfig);

    // Dividends Chart 
    const LTDebtData = getChartData("Metric", "LT Debt");
    const LTDebtConfig = createChartConfig(
        LTDebtData.labels,
        LTDebtData.data,
        "LT Debt",
        "rgba(13, 100, 44, 0.8)",
        "rgba(7, 129, 44, 0.96)"
    );
    renderChart("LTDebtChart", LTDebtConfig);
    
});
