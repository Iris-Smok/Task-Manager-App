document.addEventListener("DOMContentLoaded", function () {
  // sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // datepicker initialization
  let datepicker = document.querySelectorAll(".datepicker");
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    i18n: { done: "Select" },
  });

  // select initialization
  var selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);

  // collapsible initialization
  var collapsibles = document.querySelectorAll(".collapsible");
  M.Collapsible.init(collapsibles);

  // modal initialization
  var modal = document.querySelectorAll(".modal");
  M.Modal.init(modal, (opacity = 0.5));
});
