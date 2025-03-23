function renderRewardsTable(data) {
    const table = document.getElementById("revoltTable");
    let thead = table.createTHead();
    let tbody = table.createTBody();

    thead.innerHTML = `
        <tr>
            <th class="cell-light">👥 # of players</th> 
            <th class="cell-light">🎲 Success Prob.</th> 
            <th class="cell-light">💸 Loss</th>
            <th class="cell-light">💰 Gain</th>
        </tr>
    `;
    
    data.forEach((row, index) => {
        let tr = document.createElement("tr");
    
        tr.innerHTML = `
            <td class="cell-light">${row.participants}</td>
            <td class="cell-light">${row.probSuccess}</td>
            <td class="cell-light">-${row.lossFailed}</td>
            <td class="cell-light">${row.rewardSuccess}</td>
        `;
        tr.className = "cell-light";

        tbody.appendChild(tr);
    });
}
