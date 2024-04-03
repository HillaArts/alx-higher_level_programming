$(document).ready(function() {
  // Fetch character data from the API
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    // Extract the character name from the response
    const characterName = data.name;

    // Display the character name in the DIV#character
    $('#character').text(characterName);
  });
});
