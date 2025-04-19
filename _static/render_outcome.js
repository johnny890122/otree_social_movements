function renderOutcomeTable(revolt_success, num_participants, gain_or_loss, payoff, join_revolt, is_practice) {
    let table = document.getElementById("outcome-table-container");
    table.style.margin = "16px 0";
    let className = is_practice ? "cell-dark" : "cell-light";
    let revolt_text = revolt_success ? "Success" : "Failure";
    let gan_loss_text = join_revolt ? `${gain_or_loss}`: `${gain_or_loss} (You didn't join.)`;

    table.innerHTML = `
        <tr>
            <th class="${className}">📊 Revolt Outcome</th>
            <th class="${className}">👥 Total Participants</th>
            <th class="${className}">🔁 Your gain/loss</th>
            <th class="${className}">💰 Your payoff</th>
        </tr>

        <tr>
            <td class="${className}">${revolt_text}</td>
            <td class="${className}">${num_participants}</td>
            <td class="${className}">${gan_loss_text}</td>
            <td class="${className}">${payoff}</td>
        </tr>

    `
}