function renderRewardsTable(data) {
    const table = document.getElementById("revoltTable");
    let thead = table.createTHead();
    let tbody = table.createTBody();

    thead.innerHTML = `
        <tr>
            <th class="cell">👥 # of participants</th> 
            <th class="cell">🎲 Prob. of Success</th> 
            <th class="cell">💸 Loss</th>
            <th class="cell">💰 Reward</th>
        </tr>
    `;
    
    data.forEach((row, index) => {
        let tr = document.createElement("tr");
    
        tr.innerHTML = `
            <td>${row.participants}</td>
            <td>${row.probSuccess}</td>
            <td>-${row.lossFailed}</td>
            <td>${row.rewardSuccess}</td>
        `;

        tr.style.border = "2px solid white";

        tbody.appendChild(tr);
    });
}
