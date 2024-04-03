$(document).ready(function() {
  // When the div#red_header is clicked
  $('#red_header').click(function() {
    // Select the <header> element and update the
	  // text color to red (#FF0000)
    $('header').css('color', '#FF0000');
  });
});
