console.log('Data Connected!')

document.addEventListener('DOMContentLoaded', function() {

    fetch('/home')
        .then(response => response.text())
        .then(html => {
            document.querySelector('tbody').innerHTML = html;
            populateTable();
        })
        .catch(error => console.error('Error fetching TPMS data:', error))
});

const populateTable = () => {
    const dataTable = document.getElementById('data-table').getElementsByTagName('tbody')[0];
    const data = JSON.parse(document.getElementById('data').textContent);

    for(const key in data) {
        if (data.hasOwnProperty(key)) {
            const item = data[key];
            const row = dataTable.insertRow();
            const idCell = row.insertCell(0);
            const modelCell = row.insertCell(1);
            idCell.innerText = item.id;
            modelCell.innerText = item.model;

        }
    }
}

