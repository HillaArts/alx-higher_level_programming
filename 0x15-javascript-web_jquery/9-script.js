$(document).ready(function() {
  // Fetch the translation from the API
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    // Display the translation in the DIV#hello
    $('#hello').text(data.hello);
  });
});
