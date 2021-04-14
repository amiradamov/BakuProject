
$( document ).ready(function() {
$('#books').waypoint(function() {
    increment('books', 3000);
  }, {offset: '75%'});
  
  $('#sentences').waypoint(function() {
    increment('sentences', 6256759);
  }, {offset: '75%'});
  
  $('#categories').waypoint(function() {
    increment('categories', 20);
  }, {offset: '75%'});
  
  $('#words').waypoint(function() {
    increment('words', 77994547);
  }, {offset: '100%'});
  
  $('#unique-words').waypoint(function() {
    increment('unique-words', 3500191);
  }, {offset: '100%'});

  function increment(elem, finalVal) {
    // alert('in the function');
    var currVal = parseInt(document.getElementById(elem).innerHTML, 10);
    if (currVal < finalVal) {
      finalVal > 1000000 ? currVal = currVal + 10000 : currVal = currVal + 1;
    document.getElementById(elem).innerHTML = currVal;
  
      setTimeout(function() {
        increment(elem, finalVal);
      }, 5)
    }
  };
});

// $( document ).ready(function() {
//   $('select').selectpicker();
// });