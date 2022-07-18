$('div.Question6CheckBoxes.required :checkbox:checked').length > 0
$('div.Question7CheckBoxes.required :checkbox:checked').length > 0
$('div.Question8CheckBoxes.required :checkbox:checked').length > 0

$(document).ready(function(){
        $("#myModal").modal('show');
    });

var header = document.getElementById("chart-scale");
var btns = header.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
  var current = document.getElementsByClassName("active");
  current[0].className = current[0].className.replace(" active", "");
  this.className += " active";
  });
}


function PlaneFunction() {
  var checkBox = document.getElementById("Plane");
  var SubQuesions = document.getElementById("SubQuesions");
  if (checkBox.checked == true){
    SubQuesions.style.display = "block";
  } else {
     SubQuesions.style.display = "none";
  }
}
function Other3Function() {
  var checkBox = document.getElementById("Other3");
  var lname3 = document.getElementById("lname3");
  if (checkBox.checked == true){
    lname3.style.display = "block";
  } else {
     lname3.style.display = "none";
  }
}
function Other2Function() {
  var checkBox = document.getElementById("Other2");
  var lname2 = document.getElementById("lname2");
  if (checkBox.checked == true){
    lname2.style.display = "block";
  } else {
     lname2.style.display = "none";
  }
}
