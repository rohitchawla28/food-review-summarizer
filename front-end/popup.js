document.addEventListener('DOMContentLoaded', function () {
  var dropdown = document.getElementById('dropdown');
  var selectedOptionText = document.getElementById('selectedOptionText');

  dropdown.addEventListener('change', function () {
    var selectedOption = dropdown.options[dropdown.selectedIndex].text;
    
    // Update the displayed text
    selectedOptionText.textContent = 'Selected Option: ' + selectedOption;

    // Make a request to the Flask API to get additional data
    fetchData(selectedOption);
  });

  // Function to fetch data from the Flask API
  function fetchData(selectedOption) {
    // Replace with your Flask API endpoint
    var apiUrl = 'http://127.0.0.1:5000/api/data?selectedOption=' + encodeURIComponent(selectedOption);

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        // Update the displayed text with data from the API
        selectedOptionText.textContent += ' - API Data: ' + data.message;
      })
      .catch(error => console.error('Error:', error));
  }
});
