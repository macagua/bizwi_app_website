$(document).ready(function(){
  $('.button-collapse').sideNav();
  $('.collapsible').collapsible();
  $('.dropdown-button').dropdown({
      constrain_width: false, // Does not change width of dropdown to that of the activator
      belowOrigin: true, // Displays dropdown below the button
    });
  $('.modal-trigger').leanModal();
  $('.datepicker').pickadate({
      selectMonths: true, // Creates a dropdown to control month
      selectYears: 15, // Creates a dropdown of 15 years to control year
      formatSubmit: 'yyyy-mm-dd',
      hiddenName: true
    });
  $('select').material_select();
  
});
