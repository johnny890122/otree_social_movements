function RenderThreshold(nodes, me, is_practice) {
    // Decide the class based on the round number
    const cellClass = is_practice ? "cell-dark" : "cell-light";
    const tableClass = is_practice ? "tabular-data-dark" : "tabular-data-light";

    document.getElementById("threshold-table").className = tableClass;
    // // Populate the player heaer
    const tableHeader = document.getElementById('player-table-header');
    tableHeader.innerHTML = ''; // Clear existing header
    const headerRow = document.createElement('tr');
    ["👤 Player", "ℹ️ Threshold"].forEach(column => {
        const th = document.createElement('th');
        th.className = cellClass;
        th.textContent = column;
        headerRow.appendChild(th);
    });
    tableHeader.appendChild(headerRow);

    const tableBody = document.getElementById('player-table-body');
    tableBody.innerHTML = ''; 

    nodes.forEach(node => {
        const row = document.createElement('tr');
        
        // Player cell
        const idCell = document.createElement('td');
        idCell.textContent = node.id === me ? `${node.id} (You)` : node.id;
        idCell.className = cellClass;
        row.appendChild(idCell);

        // Threshold cell
        const thresholdCell = document.createElement('td');
        thresholdCell.textContent = node.threshold;
        thresholdCell.className = cellClass;
        row.appendChild(thresholdCell);

        tableBody.appendChild(row);
    });
}