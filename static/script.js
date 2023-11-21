document.getElementById('questionForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const questionInput = document.getElementById('question');
    const question = questionInput.value;
    questionInput.value = ''; // Clear the input after getting the value

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        const responseDiv = document.getElementById('response');
        responseDiv.innerHTML = ''; // Clear previous response

        if (data.error) {
            responseDiv.innerHTML = `<p>Error: ${data.error}</p>`;
        } else {
            // Call a function to create a table with the data
            const table = createTable(data);
            responseDiv.appendChild(table);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('response').innerText = 'An error occurred while fetching the data.';
    });
});

function createTable(data) {
    const table = document.createElement('table');
    table.classList.add('info-table');

    const thead = table.createTHead();
    const headerRow = thead.insertRow();

    const tbody = table.createTBody();
    const dataRow = tbody.insertRow();

    // Iterate over the keys in the data object and create table headers and cells accordingly
    for (const key of Object.keys(data)) {
        const th = document.createElement('th');
        th.textContent = key.charAt(0).toUpperCase() + key.slice(1); // Capitalize the header
        headerRow.appendChild(th);

        const td = dataRow.insertCell();
        td.textContent = data[key];
    }

    return table;
}

