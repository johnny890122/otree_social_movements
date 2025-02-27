function renderOutcome(revoltSuccess, totalParticipants, rewardLoss) {
    // Ensure proper formatting of values
    let revoltText = revoltSuccess ? "Yes" : "No";
    let participantsText = Math.max(0, parseInt(totalParticipants)); // Ensure non-negative
    let rewardText = parseFloat(rewardLoss).toFixed(2); // Format to 2 decimal places

    // Create the table HTML
    let tableHTML = `
        <table border="1" cellpadding="8" cellspacing="0">
            <tr>
                <th>Outcome</th>
                <td>${revoltText}</td>
            </tr>
            <tr>
                <th>Total Participants</th>
                <td>${participantsText}</td>
            </tr>
            <tr>
                <th>Your Reward/Loss</th>
                <td>${rewardText}</td>
            </tr>
        </table>
    `;

    // Render table inside the div
    document.getElementById("outcomeTable").innerHTML = tableHTML;
}