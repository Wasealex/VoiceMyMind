document.addEventListener("DOMContentLoaded", function () {
  var calendarEl = document.getElementById("calendar");
  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: "dayGridMonth",
    events: JSON.parse("{{ events|tojson }}"),
    eventClick: function (info) {
      window.location.href = info.event.url;
    },
  });
  calendar.render();
});
