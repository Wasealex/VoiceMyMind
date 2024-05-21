// Add event listener for form submission
const form = document.querySelector("form");
form.addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent form submission

  // Get form data
  const title = document.querySelector("#title").value;
  const content = document.querySelector("#content").value;

  // Create new journal entry
  const entry = {
    title: title,
    content: content,
    date: new Date().toLocaleString(),
  };

  // Add entry to journal (assuming you have a journal array)
  journal.push(entry);

  // Clear form fields
  document.querySelector("#title").value = "";
  document.querySelector("#content").value = "";

  // Display new entry or update UI as needed
  console.log("New entry added:", entry);
});
