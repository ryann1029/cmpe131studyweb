const isAlpha = str => /^[a-zA-Z]*$/.test(str); // Using RegEx to detect any letters.

const calculate = () => {
  
    // Getting input from user into height variable.
    let course1 = document.querySelector("#course1").value;
    let total_points = document.querySelector("#totalpoints").value;
    let grades = "";
    
    // Input is string so typecasting is necessary. */
    let course1_points = parseFloat(course1);
    
    // Checking the condition for the providing the 
    // grade to student based on percentage
    let percentage = ((course1_points/total_points) * 100);

    if (percentage <= 100 && percentage >= 90) {
      grades = "A";
    } else if (percentage < 90 && percentage >= 80) {
      grades = "B";
    } else if (percentage < 80 && percentage >= 70) {
      grades = "C";
    } else {
      grades = "F";
    }

    // Checking if inputs is either empty, contains alphabets, or something otherwise.
    if (course1 == "") {
    document.querySelector("#showdata").innerHTML
        = "Please enter all the fields";
        
    } else if(isAlpha(course1)){
        document.querySelector("#showdata").innerHTML =
        `Your input can only be numbers. Correct your inputs.`

    } else {
    // Checking the condition for the fail and pass
        if (percentage >= 39.5) {
            document.querySelector(
            "#showdata"
            ).innerHTML = 
            `You have ${total_points} points out of ${course1_points}, which is a percentage of ${percentage}%.<br/> 
            <b>Your grade is ${grades}, <u>a passing grade</u></b>.`;

        } else {
            document.querySelector("#showdata").innerHTML = 
            `You have ${total_points} points out of ${course1_points}, which is a percentage of ${percentage}%.<br/> 
            <b>Your grade is ${grades}. <u>Unfortunately, you failed</u></b>.`
        }
    }
};  