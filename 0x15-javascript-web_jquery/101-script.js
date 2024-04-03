$(document).ready(function() {
  // When the div#add_item is clicked
  $('#add_item').click(function() {
    // Create a new <li> element with text "Item"
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to UL.my_list
    $('ul.my_list').append(newItem);
  });

  // When the div#remove_item is clicked
  $('#remove_item').click(function() {
    // Remove the last <li> element from UL.my_list
    $('ul.my_list li:last-child').remove();
  });

  // When the div#clear_list is clicked
  $('#clear_list').click(function() {
    // Remove all <li> elements from UL.my_list
    $('ul.my_list').empty();
  });
});
