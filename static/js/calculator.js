const isAlpha = str => /^([a-zA-Z0-9]|\s)*$/.test(str); // Using RegEx to detect any letters.\

const checkExceptionAssignment  = (assignmentName) => {
  if (assignmentName == "") {
    //assignment.value=="0";
    console.log("assignment: " + assignment.value)
    document.querySelector("#showdata").innerHTML = `
   <div style="color: red;">Please enter all the fields.</div>
   `;
   windows.stop(); 
  }
  if (!/^[\w\d\s]+$/.test(assignmentName)) { //special characters aren't being detected for the second row
    console.log("assignment: " + assignment.value)
      document.querySelector("#showdata").innerHTML = `
         <div style="color: red;">No special characters are allowed for course name. Correct your inputs.</div>
         `;
         windows.stop();
   }
}

const CheckWeightException = (weightValue) => {
  if (weightValue == "") {
  document.querySelector("#showdata").innerHTML = `
 <div style="color: red;">No weight inputted.</div>
 `;
    windows.stop();
  }
  if (!/^[0-9]+$/.test(weightValue)) {

  document.querySelector("#showdata").innerHTML = `
    <div style="color: red;">Please include valid numbers for the weight.</div>
    `;
    windows.stop(); 
}
}

const calculate = () => {

  // Getting input from user into height variable
  let grades = "";

  // store the ((total pts / total possible pts) * weight) of each column the user made 
  // make an empty array first, this will hold all the values
  let total_score_sum = [0, 0, 0, 0, 0];
  let total_points_possible = [0, 0, 0, 0, 0];
  let weighted_grade_points = [0, 0, 0, 0, 0];
  let temp_weight = [0, 0, 0, 0, 0]
  column_counter = 0;
  let data_table = ['dataTable1', 'dataTable2', 'dataTable3', 'dataTable4', 'dataTable5']

  // this should calculate the total weight, if it is less than 100 after the for loop, terminate 
  // and let the user know the total weight should sum to 100 or greater. 
  let total_weight = 0;
  let score_sum = 0;
  //let total_points_sum = 0;
 

  var boundary_temp = 0; 
  // check the weight first and get the column count
  for (var i = 0; i < 5; ++i){
    var Table = document.getElementById(data_table[i]); 
    var row_weight = Table.rows[0].cells[0]; 
    CheckWeightException(parseFloat(row_weight.querySelector("#weight").value)); 
    boundary_temp += parseFloat(row_weight.querySelector("#weight").value); 
    temp_weight[i] = parseFloat(row_weight.querySelector("#weight").value); 
    weighted_grade_points[i] += parseFloat(row_weight.querySelector("#weight").value)
    ++column_counter; 
    if (boundary_temp >= 100){
      break; 
    }
  }

  for (var i = 0; i < column_counter; ++i){
    var Table = document.getElementById(data_table[i]); 
    for (var j = 0; j < Table.rows.length - 1; ++j){
      if (j == 0){
        continue; 
      }
      var row = Table.rows[j].cells[0]; 
      var nameOfAssignment = row.querySelector("#assignment").value; 
      checkExceptionAssignment(nameOfAssignment); 
      total_score_sum[i] += parseFloat(row.querySelector("#score").value); 
      total_points_possible[i] += parseFloat(row.querySelector("#pointspossible").value); 
    }
  }


  

  // let CalcTable = document.getElementById('dataTable');

  let total_grade_points = 0;

  

  for (var i = 0; i < column_counter; ++i) {
    weighted_grade_points[i] = (total_score_sum[i] / total_points_possible[i]) * temp_weight[i];
    total_grade_points += weighted_grade_points[i];
  }


  let percentage = total_grade_points;
  console.log(percentage); 

  // checking to see if the user added a correct value for weight 
  if (total_weight < 0 || total_weight > 100) {
    document.querySelector("#showdata").innerHTML = `
      <div style="color: red;">The weight entered must be between 0% and 100%.</div>
      `;
  } else {

    if (percentage >= 90) {
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

    console.log("WRVDS: "+ total_score_sum[0])
    // Checking if inputs is either empty, contains characters not part of the alphabet, or something otherwise.
    //console.log("ASSIGNMENT: " + /^[\w\d\s]+$/.test(assignment.value))
    if (assignment.value == "") {
      //assignment.value=="0";
      console.log("assignment: " + assignment.value)
      document.querySelector("#showdata").innerHTML = `
     <div style="color: red;">Please enter all the fields.</div>
     `;

    } else if (!/^[\w\d\s]+$/.test(assignment.value)) { //special characters aren't being detected for the second row
    console.log("assignment: " + assignment.value)
      document.querySelector("#showdata").innerHTML = `
         <div style="color: red;">No special characters are allowed for course name. Correct your inputs.</div>
         `;

    } else if (weight.value == "") {
      document.querySelector("#showdata").innerHTML = `
     <div style="color: red;">No weight inputted.</div>
     `;
    } else if (!/^[0-9]+$/.test(weight.value)) {

      document.querySelector("#showdata").innerHTML = `
        <div style="color: red;">Please include valid numbers for the weight.</div>
        `;
    } else if (!/^[0-9]+$/.test(temp_weight[1])) {

      document.querySelector("#showdata").innerHTML = `
        <div style="color: red;">Please include valid numbers for the weight in column 2.</div>
        `;
    } else if (!/^[0-9]+$/.test(temp_weight[2])) {

      document.querySelector("#showdata").innerHTML = `
        <div style="color: red;">Please include valid numbers for the weight in column 3.</div>
        `;
    } 
    else if (!/^[0-9]+$/.test(temp_weight[3])) {

      document.querySelector("#showdata").innerHTML = `
        <div style="color: red;">Please include valid numbers for the weight in column 4.</div>
        `;
    } 
    else if (!/^[0-9]+$/.test(temp_weight[4])) {

      document.querySelector("#showdata").innerHTML = `
        <div style="color: red;">Please include valid numbers for the weight in column 5.</div>
        `;
    } 
    else if (Number.isNaN(total_score_sum[0]) || Number.isNaN(total_points_possible[0])) {

      console.log("score: " +total_score_sum[0])
      console.log("possible: " +total_points_possible[0])
      document.querySelector("#showdata").innerHTML = `
     <div style="color: red;">Please make sure score and/or total point fields in column 1 only contains numbers</div>
     `;

    }
    else if (Number.isNaN(total_score_sum[1]) || Number.isNaN(total_points_possible[1])) {
      console.log("weight: " +weight.value)
      console.log("score: " +total_score_sum[1])
      console.log("possible: " +total_points_possible[1])
      document.querySelector("#showdata").innerHTML = `
     <div style="color: red;">Please make sure score and/or total point fields in column 2 only contains numbers</div>
     `;
    }
    else if (Number.isNaN(total_score_sum[2]) || Number.isNaN(total_points_possible[2])) {
      console.log("weight: " +weight.value)
      console.log("score: " +total_score_sum[2])
      console.log("possible: " +total_points_possible[2])
      document.querySelector("#showdata").innerHTML = `
     <div style="color: red;">Please make sure score and/or total point fields in column 3 only contains numbers</div>
     `;
    }
    else if (Number.isNaN(total_score_sum[3]) || Number.isNaN(total_points_possible[3])) {
      console.log("weight: " +weight.value)
      console.log("score: " +total_score_sum[3])
      console.log("possible: " +total_points_possible[3])
      document.querySelector("#showdata").innerHTML = `
     <div style="color: red;">Please make sure score and/or total point fields in column 4 only contains numbers</div>
     `;
    }
    else if (Number.isNaN(total_score_sum[4]) || Number.isNaN(total_points_possible[4])) {
      console.log("weight: " +weight.value)
      console.log("score: " +total_score_sum[4])
      console.log("possible: " +total_points_possible[4])
      document.querySelector("#showdata").innerHTML = `
     <div style="color: red;">Please make sure score and/or total point fields in column 5 only contains numbers</div>
     `;
    }
    else if ((boundary_temp)<100){
      console.log("final weight: " +(temp_weight[0]+temp_weight[1]+temp_weight[2]+temp_weight[3]+temp_weight[4]))
      document.querySelector("#showdata").innerHTML = `
     <div style="color: red;">Please make sure total weight value is 100.</div>
     `;
    }
    else { // when else statement is here, itll detect special characters but not weight

       
        // Checking the condition for the fail and pass
        if (percentage >= 70) {
          console.log("final weight: " +(temp_weight[0]+temp_weight[1]+temp_weight[2]+temp_weight[3]+temp_weight[4]))
          document.querySelector("#showdata").innerHTML =
            `Your percentage is ${percentage}%.<br/> 
            <b>Your grade is a ${grades}, <u>a passing grade</u></b>.`;

        } else {
          document.querySelector("#showdata").innerHTML =
            `Your percentage is ${percentage}%.<br/> 
            <b>Your grade is a ${grades}. <u>Unfortunately, you failed</u></b>.`
        }
      
    }

  }
};