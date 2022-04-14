const isAlpha = str => /^([a-zA-Z0-9]|\s)*$/.test(str); // Using RegEx to detect any letters.

const calculate = () => {
  
    // Getting input from user into height variable.
    let course1 = document.querySelector("#assignment").value;
    let score = document.querySelector("#score").value;
    let total_points = document.querySelector("#totalpoints").value;
    let weight = document.querySelector("#weight").value; 
    let grades = "";
    
    // Input is string so typecasting is necessary. */
    let course1_points = parseFloat(score);
    
    // Checking the condition for the providing the 
    // grade to student based on percentage
    let percentage = ((course1_points/total_points) * 100);
    
    

    // checking to see if the user added a correct value for weight 
    if (weight < 0 || weight > 100)
      document.querySelector("#showdata").innerHTML = "The weight entered must be between 0 and 100";
    else {

    if (percentage <= 100 && percentage >= 90) {
      grades = "A";
    } else if (percentage < 90 && percentage >= 80) {
      grades = "B";
    } else if (percentage < 80 && percentage >= 70) {
      grades = "C";
    } else if (percentage < 70 && percentage >= 60) {
      grades = "D";
    } else {
      grades = "F";
    }

    // Checking if inputs is either empty, contains characters not part of the alphabet, or something otherwise.
    if (course1 == "") {
    document.querySelector("#showdata").innerHTML
        = `Please enter all the fields`;
        
    } else if(!isAlpha(course1)){
        document.querySelector("#showdata").innerHTML =
        `No special characters are allowed for course name. Correct your inputs.`

    } else if (!weight) {
      document.querySelector("#showdata").innerHTML =
      `No weight inputted.`

    } else if (!score) {
      document.querySelector("#showdata").innerHTML =
      `No score inputted.`

    } else if (!total_points) {
      document.querySelector("#showdata").innerHTML =
      `No total points inputted.`

    } else {
    // Checking the condition for the fail and pass
        if (percentage >= 70) {
            document.querySelector("#showdata").innerHTML = 
            `You have ${course1_points} points out of ${total_points}, which is a percentage of ${percentage}%.<br/> 
            <b>Your grade is ${grades}, <u>a passing grade</u></b>.`;

        } else {
            document.querySelector("#showdata").innerHTML = 
            `You have ${course1_points} points out of ${total_points}, which is a percentage of ${percentage}%.<br/> 
            <b>Your grade is ${grades}. <u>Unfortunately, you failed</u></b>.`
        }
    }
  }
};