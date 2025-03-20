document.getElementById('probioticForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  // Gather form data
  const formData = {
    age: document.getElementById('age').value,
    lifestyle: document.getElementById('lifestyle').value,
    diet: document.getElementById('diet').value,
    symptoms: document.getElementById('symptoms').value
      .split(',')
      .map(symptom => symptom.trim().toLowerCase())
  };

  // Send POST request to /analyze
  fetch('/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(formData)
  })
    .then(response => response.json())
    .then(data => {
      // Display recommendation
      document.getElementById('result').innerText =
        'Recommended Probiotic: ' + data.recommendation;
    })
    .catch(error => {
      document.getElementById('result').innerText =
        'An error occurred: ' + error;
    });
});
