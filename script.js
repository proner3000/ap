// script.js
document.addEventListener('DOMContentLoaded', function() {
    fetch('external.html')
        .then(response => response.text())
        .then(data => {
            // Create a temporary <div> element to hold the parsed HTML
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = data;

            // Extract the <head> content from the temporary element
            const externalHead = tempDiv.querySelector('head');

            // Find the target element where you want to insert the external content
            const targetElement = document.getElementById('externalContent');

            // Append the external <head> content to the target element
            targetElement.appendChild(externalHead);
        })
        .catch(error => console.error('Error fetching external content:', error));
});
