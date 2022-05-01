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

    document.querySelector(".date h").innerHTML = month[date.getMonth()] + " " + date.getFullYear(); 
    document.querySelector(".date p").innerHTML = "Current Date: " + new Date().toDateString();
   
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
    
    removeCountSign = 0; 

    document.querySelector('.days').addEventListener('click', () => {
        addReminder(); 
    })

    document.querySelector('.prev').addEventListener('click', () => {
        date.setMonth(date.getMonth() - 1); 
        renderCalendar(); 
    })

    document.querySelector('.next').addEventListener('click', () => {
        date.setMonth(date.getMonth() + 1); 
        renderCalendar(); 
    })
    renderCalendar();

    const array = []
    var i = 0;
    var t;
    var reminderSection = document.getElementById("reminders2"); 
    const addReminder = () => {

        const plus = document.getElementById("Add");
        plus.remove();
        const minus = document.getElementById("Remove");
        minus.remove();
        tag = document.createElement("section"); 
        
        tag.innerHTML = `<input type="text" autofocus placeholder="Enter your reminder" id = "Text"/> 
        <input type=button class = "Add" value=+ onclick="addReminder()" id="Add"/>
        <input type=button class = "Remove" value=- onclick="AddRemoveSign()" id="Remove"/>
        <input type="date" id = "Date"/>
        <br><br>`;
        
        array.push(tag);
        
        reminderSection.appendChild(tag);
        
     }

     const AddRemoveSign = () => {
        var text = document.getElementById("Text");
        text.remove();
        var date = document.getElementById("Date");
        date.remove();
        

         /*
        var date = document.getElementById("Date");
        date.remove();
        var text= document.getElementById("Text");
        text.remove();*/
        /* 
        var reminderSet = document.getElementById('reminders2'); 
        var section = reminderSet.getElementsByTagName('section'); 
        for (var i = removeCountSign; i < section.length; ++i){
            var subSection = section[i].lastElementChild.tagName; 
            console.log(subSection.innerHTML);*/
            
        }
    const MinusSign = () =>{
        const minus = document.getElementById("Remove");
        minus.remove();
    }
    


