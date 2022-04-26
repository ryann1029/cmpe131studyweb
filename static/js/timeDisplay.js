// Time Display Refresher (creates a real-time clock that updates every second)
function realTimeClockDisplay() {
    var refresh = 1000; // Refresh rate in milli seconds
    mytime=setTimeout('timeDisplay()', refresh)
}

// Time Display Generator
function timeDisplay() {
    var today = new Date();
    var month = today.getMonth() + 1;
    month = getMonthString(month);

    var date = today.getDate();
    var year = today.getFullYear();
    var date = month + " " + date + ", " + year;

    var hours = today.getHours();
    var am_pm = hours >= 12 ? ' PM' : ' AM';
    if (hours < 10 && hours != 0) {
        hours = '0' + hours;
    }
    else if (hours > 12) {
        hours = hours - 12;
    }
    else if (hours == 0) {
        hours = 12;
    }
    else {
        hours = hours;
    }

    var minutes = today.getMinutes();
    if (minutes < 10) {
        minutes = '0' + minutes;
    }

    var seconds = today.getSeconds();
    if (seconds < 10) {
        seconds = '0' + seconds;
    }
    var time = hours + ":" + minutes + ":" + seconds + " " + am_pm;
    realTimeClockDisplay();
    document.querySelector("#timedisplay").innerHTML = `
     <div style="color: red;">${date} ${time}</div>
     `;
}

// Conversion from month integer to month string
function getMonthString(monthInt){
    var monthString;
    if (monthInt == 1) {
        monthString = "January";
    }
    else if(monthInt == 2) {
        monthString = "February";
    }
    else if(monthInt == 3) {
        monthString = "March";
    }
    else if(monthInt == 4) {
        monthString = "April";
    }
    else if(monthInt == 5) {
        monthString = "May";
    }
    else if(monthInt == 6) {
        monthString = "June";
    }
    else if(monthInt == 7) {
        monthString = "July";
    }
    else if(monthInt == 8) {
        monthString = "August";
    }
    else if(monthInt == 9) {
        monthString = "September";
    }
    else if(monthInt == 10) {
        monthString = "October";
    }
    else if(monthInt == 11) {
        monthString = "November";
    }
    else if(monthInt == 12) {
        monthString = "December";
    }
    return monthString;
}