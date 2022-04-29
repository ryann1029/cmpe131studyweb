const date = new Date();

const renderCalendar = () => {

    date.setDate(1); 
    const month = ["January", "February", "March", "April", "May", "June",
                   "July","August","September","October","November","December"];
    

    const monthDays = document.querySelector(".days");
    const firstDayIndex = date.getDay(); 

    const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();

    const lastDayIndex = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDay();

    const nextDays = 42 - (lastDay + firstDayIndex)

    document.querySelector(".date h").innerHTML = month[date.getMonth()];
    document.querySelector(".date p").innerHTML = new Date().toDateString();
   
    let days = ""; 

    for (let x = firstDayIndex; x > 0; x--){
        days += `<div class="prev-date"> ${prevLastDay - x + 1}</div>`; 
    }
    
    for (let i = 1; i <= lastDay; i++){
        if (i === new Date().getDate() && date.getMonth() === new Date().getMonth()){
            days += `<div class="today"> ${i} </div>`; 
        }
        else{
            days += `
            <div> ${i} </div>
            `;
            monthDays.innerHTML = days; 
        }
    }

    for (let i = 1; i <= nextDays; ++i){
        days += `<div class="next-date"> ${i} </div>`; 
        monthDays.innerHTML = days;
    }
    }
    
    document.querySelector('.prev').addEventListener('click', () => {
        date.setMonth(date.getMonth() - 1); 
        renderCalendar(); 
    })

    document.querySelector('.next').addEventListener('click', () => {
        date.setMonth(date.getMonth() + 1); 
        renderCalendar(); 
    })
    renderCalendar();

    const addReminder = () => {
        var tag = document.createElement("section"); 
        tag.innerHTML = `<input type="text" autofocus placeholder="Enter your reminder">
        <input type="date"/>
        <input type=button value=+ onclick="addReminder()">`; 

        console.log(tag.innerHTML);
    
        var reminderSection = document.getElementById("reminders2"); 
        reminderSection.appendChild(tag); 
        getDate(); 
    }

    const  getDate = () => {
        var remin = document.getElementById("reminders2"); 
        var section = remin.getElementsByTagName("section"); 
        var sectionCount = 0; 
        for (var i = 0; i < section.length; ++i){
            let date = section.getAttribute("date"); 
            console.log(date); 
        }
    }