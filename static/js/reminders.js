const addReminder = () => {
    var tag = document.createElement("section"); 
    tag.innerHTML = `<input type=text autofocus>
    <input type="date"/>
    <input type=button value=+ onclick="addReminder">`; 

    var reminderSection = document.getElementById("reminders"); 
    reminderSection.appendChild(tag); 
}