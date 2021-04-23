
$(document).ready(function () {
  $('#books').waypoint(function () {
    increment('books', 3000);
  }, { offset: '75%' });

  $('#sentences').waypoint(function () {
    increment('sentences', 6256759);
  }, { offset: '75%' });

  $('#categories').waypoint(function () {
    increment('categories', 20);
  }, { offset: '75%' });

  $('#words').waypoint(function () {
    increment('words', 77994547);
  }, { offset: '100%' });

  $('#unique-words').waypoint(function () {
    increment('unique-words', 3500191);
  }, { offset: '100%' });

  function increment(elem, finalVal) {
    // alert('in the function');
    var currVal = parseInt(document.getElementById(elem).innerHTML, 10);
    if (currVal < finalVal) {
      finalVal > 1000000 ? currVal = currVal + 10000 : currVal = currVal + 1;
      document.getElementById(elem).innerHTML = currVal;

      setTimeout(function () {
        increment(elem, finalVal);
      }, 5)
    }
  };
});

$(document).ready(function () {

  const textClassifier = document.getElementById("text-classifier");
  const lemmatizer = document.getElementById("lemmatizer");
  const algorithms = document.getElementById('algorithms');

  // textClassifier.addEventListener("mouseover", mouseEvent1);
  // textClassifier.addEventListener("mouseout", mouseEvent2);
  // lemmatizer.addEventListener("mouseover", mouseEvent3);
  // lemmatizer.addEventListener("mouseout", mouseEvent4);

  // function mouseEvent1(){
  //   textClassifier.style.backgroundColor = '#726EFF';
  // }

  // function mouseEvent2() {
  //   textClassifier.style.backgroundColor = 'transparent';
  // }

  // function mouseEvent3() {
  //   lemmatizer.style.backgroundColor = '#726EFF';
  // }

  // function mouseEvent4() {
  //   lemmatizer.style.backgroundColor = 'transparent';
  // }

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