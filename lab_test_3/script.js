function addTask() {
let taskInput = document.getElementById("taskInput");
let taskText = taskInput.value.trim();
if (taskText === "") {
alert("Please enter a task!");
return;
}
let li = document.createElement("li");
li.innerHTML = `
${taskText}
<span class="action-btns">
<button class="complete-btn" onclick="markCompleted(this)">✔</button>
<button class="delete-btn" onclick="deleteTask(this)">✖</button>
</span>
`;

document.getElementById("taskList").appendChild(li);
taskInput.value = "";
}
function deleteTask(button) {
button.parentElement.parentElement.remove();
}
function markCompleted(button) {
let li = button.parentElement.parentElement;
li.classList.add("completed");
document.getElementById("completedList").appendChild(li);
button.remove(); // Remove complete button once completed
}