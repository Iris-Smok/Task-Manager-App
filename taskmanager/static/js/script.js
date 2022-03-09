document.addEventListener("DOMContentLoaded", function () {
  // sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // datepicker initialization
  var datapicker = document.querySelectorAll(".datepicker");
  M.Datepicker.init(datapicker, {
    format: "dd mm, yyyy",
    i18n: { dpne: "Select" },
  });

  // select initialization
  var selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);
});

// modal initialization
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".modal");
  var instances = M.Modal.init(elems, (opacity = 0.5));
});

//
