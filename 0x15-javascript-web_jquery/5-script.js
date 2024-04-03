$(document).ready(function() {
  // When the div#add_item is clicked
  $('#add_item').click(function() {
    // Create a new <li> element with text "Item"
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to the UL.my_list
    $('ul.my_list').append(newItem);
  });
});
