function renderTable(data) {
    const tbody = document.querySelector("#revoltTable tbody");
    tbody.innerHTML = ""; // Clear existing rows

    data.forEach((row, index) => {
        let tr = document.createElement("tr");

        tr.innerHTML = `
            <td>${row.participants}</td>
            <td><input type="text" value="${row.probSuccess}" id="prob${index}"></td>
            <td><input type="text" value="${row.lossFailed}" id="loss${index}"></td>
            <td><input type="text" value="${row.rewardSuccess}" id="reward${index}"></td>
        `;

        tbody.appendChild(tr);
    });
}