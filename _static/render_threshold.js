function RenderThreshold(nodes, me) {
    // Populate the player table
    const tableBody = document.getElementById('player-table-body');
    tableBody.innerHTML = ''; 

    nodes.forEach(node => {
        const row = document.createElement('tr');
        
        const idCell = document.createElement('td');
        const thresholdCell = document.createElement('td');
        idCell.textContent = node.id === me ? `${node.id} (You)` : node.id;
        thresholdCell.textContent = node.example_threshold;

        row.appendChild(idCell);
        row.appendChild(thresholdCell);

        // Add thicker borders
        idCell.style.border = "2px solid white";
        thresholdCell.style.border = "2px solid white";

        tableBody.appendChild(row);
    });
}