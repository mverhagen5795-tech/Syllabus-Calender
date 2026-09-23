console.log("Script loaded successfully!");

const form = document.querySelector("form");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  console.log("check");
  const newEvent = {
    course: document.getElementById("course").value,
    title: document.getElementById("title").value,
    date: document.getElementById("date").value,
  };
  console.log(newEvent);

  const item = document.createElement("li");
  item.textContent = newEvent.course + " - " + newEvent.title + " - " + newEvent.date;
  document.getElementById("event-list").appendChild(item);

});
