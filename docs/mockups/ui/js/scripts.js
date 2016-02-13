$(document).ready(function(){
  $('.button-collapse').sideNav();
  $('.collapsible').collapsible();
  $('.dropdown-button').dropdown({
      constrain_width: false, // Does not change width of dropdown to that of the activator
      belowOrigin: true, // Displays dropdown below the button
    });
  $('select').material_select();
  $('.modal-trigger').leanModal();
  $('table.display').DataTable();
  $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year
    format: 'dd/mm/yyyy' 
  });
});