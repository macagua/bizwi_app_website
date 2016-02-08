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
});