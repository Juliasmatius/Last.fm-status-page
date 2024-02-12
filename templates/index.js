let recentTrack;

// Function to get the most recent track and update UI
async function updateUI() {
    try {
        const response = await fetch('/api/proxy');
        const responseData = await response.json();

        if (responseData && responseData.name && responseData.artist && responseData.album) {
            recentTrack = responseData;

            // Update UI elements
            document.getElementById('currentSong').innerHTML = `Song: <b>${recentTrack.name}</b> By <b>${recentTrack.artist['#text']}</b>`;
            document.getElementById('currentAlbum').innerHTML = `Album: <b>${recentTrack.album['#text']}</b>`;
            document.getElementById('albumArtImg').src = recentTrack.image[3]['#text'];
            document.getElementById('notPlayingMessage').style.display = 'none';
            document.title = `${recentTrack.artist['#text']} - ${recentTrack.name}`;

        } else {
            // Display a message when the response format is invalid
            console.error('Invalid response format:', responseData);
            document.getElementById('notPlayingMessage').innerText = 'Invalid response format';
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('notPlayingMessage').innerText = 'Error fetching data';
    }
}

// Call the updateUI function initially and then set up periodic updates
updateUI();
setInterval(updateUI, 15000)


// Function to toggle dark mode
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

// Function to hide buttons
function hideButtons() {
    document.body.classList.toggle('buttons-hidden');
}
