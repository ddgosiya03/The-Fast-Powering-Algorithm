document.getElementById('computeForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const p = document.getElementById('p').value;
    const g = document.getElementById('g').value;
    const s = document.getElementById('s').value;

    fetch('/compute', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ p: p, g: g, s: s }),
    })
    .then(response => response.json())
    .then(data => {
        let resultHtml = '<h3>Computation Steps:</h3><ul>';
        data.steps.forEach(step => {
            resultHtml += `<li>${step}</li>`;
        });
        resultHtml += '</ul>';
        resultHtml += `<p><strong>Equation:</strong> ${data.equation}</p>`;
        resultHtml += `<p><strong>Power List:</strong> ${data.plist.join(', ')}</p>`;
        resultHtml += `<p><strong>Result:</strong> ${g}^${s} ≡ ${data.result} mod ${p}</p>`;
        document.getElementById('result').innerHTML = resultHtml;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = '<p class="text-danger">An error occurred. Please try again.</p>';
    });
});

document.getElementById('themeToggle').addEventListener('click', function() {
    document.body.classList.toggle('dark');
    this.textContent = document.body.classList.contains('dark') ? '☀️' : '🌙';
});
