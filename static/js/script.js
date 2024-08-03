// Get the email list element
const emailList = document.getElementById('email-list');

// Get the progress bar element
const progressBar = document.getElementById('progress-bar');

// Set up event listeners for the email list and progress bar
emailList.addEventListener('click', () => {
    // Send a request to retrieve the emails
    fetch('/get_emails/')
        .then(response => response.json())
        .then(emails => {
            // Update the email list with the new emails
            emailList.innerHTML = '';
            for (const email of emails) {
                const emailListItem = document.createElement('li');
                emailListItem.textContent = `${email.subject} (${email.sent_at})`;
                emailList.appendChild(emailListItem);
            }
        });
});

progressBar.addEventListener('click', () => {
    // Send a request to update the progress bar
    fetch('/update_progress_bar/')
        .then(response => response.json())
        .then(progress => {
            // Update the progress bar with the new value
            progressBar.value = progress;
        });
});
