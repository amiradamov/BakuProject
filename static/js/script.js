
$(document).ready(function () {
  $('#books').waypoint(function () {
    increment('books', 3090);
  }, { offset: '75%' });

  $('#sentences').waypoint(function () {
    increment('sentences', 6256759);
  }, { offset: '75%' });

  $('#categories').waypoint(function () {
    increment('categories', 22);
  }, { offset: '75%' });

  $('#words').waypoint(function () {
    increment('words', 77994547);
  }, { offset: '100%' });

  $('#unique-words').waypoint(function () {
    increment('unique-words', 1883105);
  }, { offset: '100%' });

  function increment(elem, finalVal) {
    // alert('in the function');
    var currVal = parseInt(document.getElementById(elem).innerHTML, 10);
    if (currVal < finalVal) { 
      currVal = currVal + 1;
      document.getElementById(elem).innerHTML = currVal;

      setTimeout(function () {
        increment(elem, finalVal);
      }, 80)
    }
  };
});

$(document).ready(function () {

  const textClassifier = document.getElementById("text-classifier");
  const lemmatizer = document.getElementById("lemmatizer");
  const algorithms = document.getElementById('algorithms');

  $("#text-classifier").on("click", changeColor1);
  $("#lemmatizer").on("click", changeColor2);

  function changeColor1() {
    textClassifier.style.backgroundColor = '#726EFF';
    lemmatizer.style.backgroundColor = 'transparent';
    algorithms.classList.remove("d-none");
  }

  function changeColor2() {
    lemmatizer.style.backgroundColor = '#726EFF';
    textClassifier.style.backgroundColor = 'transparent';
    algorithms.classList.add("d-none");
  }
})


$(document).ready(function () {
  $(function () {
    $('[data-toggle="popover"]').popover()
})

linkedin("#overlay_narmina", "#img_narmina");
linkedin("#overlay_amir", "#img_amir");
linkedin("#overlay_ismayil", "#img_ismayil");
linkedin("#overlay_gunash", "#img_gunash");
linkedin("#overlay_abzetdinm", "#img_abzetdinm");
linkedin("#overlay_samirm", "#img_samirm");

function linkedin(overlay_elem, elem) {
$(overlay_elem).hover(
   function(){
    $(elem).css('opacity','20%');
}, function(){
    $(elem).css('opacity','100%');
})}
})
