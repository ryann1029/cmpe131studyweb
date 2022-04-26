/* Do not maniplate any of the code in this file.
 * Assigned to Ryan only */

var numberofColumns = 1; 
var numberOfRows = [2, 2, 2, 2, 2];  


// returns row count of the current table passed in parameter "tableID"
function rowCount(tableID) {
   var rowCount = 0;
   var table = document.getElementById(tableID);
   var rows = table.getElementsByTagName("tr");

   for (var i = 0; i < rows.length; i++) {
      rowCount++;
   }

   document.querySelector("#rowCount").innerHTML =
   `${rowCount-1}`;

   return rowCount;
}

function determiningButton() {
   var table = document.getElementById("dataTable"); 

   for (var i = 0; i < table.rows.length; ++i){
      if (i != rowCount - 1){
         continue; 
      }
      for (var j = 0; j < table.rows[i].cells.length; ++j){
         document.getElementById('button').onclick = function() {
            return j;
         }; 
   }
   }
}

function addRow() {

var table = document.getElementById("dataTable"); 

var row = table.insertRow(numberOfRows[0]++); 
var cell1 = row.insertCell(0); 

cell1.innerHTML = '<td>\
    <input type="text" style="width: 120px;" placeholder="Assignment Name" id="assignment"/>\
    <input type="text" style="width: 100px;" placeholder="Score" id="score"/>\
    <input type="text" style="width: 95px;" placeholder="Points Possible" id="pointspossible"/>\
</td>'
}

function deleteRow(){
   if (rowCount("dataTable") - 2 > 1){
      document.getElementById("dataTable").deleteRow(numberOfRows[0] - 1); 
      numberOfRows[0]--; 
   }
}

function addColumn(){
   if (numberofColumns > 4){
      alert("Cannot exceed more than 5 columns.");
   }
   else{
   var table = document.getElementById("dataTable"); 
   var row0 = table.rows[0].insertCell(); 
   
   row0.innerHTML = '<tr>\
   <th>Category <input style="position: relative; float: right; width: 70px" type="text" placeholder="Weight (%)" id="weight"/></th>\
   </tr>'

   var row1 = table.rows[1].insertCell(); 
   row1.innerHTML = '<input type="text" style="width: 120px;" placeholder="Assignment Name" id="assignment"/>\
   <input type="text" style="width: 100px;" placeholder="Score" id="score"/>\
   <input type="text" style="width: 95px;" placeholder="Points Possible" id="pointspossible"/>'

   if (numberofColumns > 1){
      for (var i = 1; i <= numberofColumns - 1; ++i){
         if (numberOfRows[i] == 2){
            var row4 = table.rows[2].insertCell(); 
            row4.innerHTML = ''; 
         }
      }
   }
   
   var row3 = table.rows[2].insertCell(); 
   row3.innerHTML = '<input type="button" value="- Delete Row" onclick="deleteRow()"/>\
   <input type="button" value="+ Add Row" onclick="addRow()" id="row"/>\
   <input type="button" value="+Add Column" onclick="addColumn()"/>'
   ++numberofColumns; 
   }
}

// returns column count of the current table passed in parameter "tableID"
function columnCount(tableID) {
   var columnCount = 0;
   var table = document.getElementById(tableID);
   var columns = table.getElementsByTagName("th");

   for (var i = 0; i < columns.length; i++) {
      columnCount++;
   }

   document.querySelector("#columnCount").innerHTML =
   `${numberofColumns}`;

   return columnCount;
}

// // When the button with the id "addColumn" is pressed, do this...
var table = $('#dataTable');
var iter = 2; // starts creating at 2nd column
$('#addColumn').click(function() {
   if (iter > 5) {
      alert("Cannot exceed more than 5 columns.");
   } else {
      table.find('tr').each(
         function() {
            var trow = $(this);
            if (trow.index() === 0) {
               trow.append('<th>Category ' + (iter) + '<input style="position: relative; float: right; width: 70px" type="text" placeholder="Weight (%)" id="weight"/></th>');
            } else {
               trow.append('<td>\
               <input type="text" style="width: 120px;" placeholder="Assignment Name" id="assignment" name="assignment[]"/>\
               <input type="text" style="width: 100px;" placeholder="Score" id="score" name="score[]"/>\
               <input type="text" style="width: 100px;" placeholder="Possible Points" id="pointspossible" name="pointspossible[]"/>\
               </td>');
            }
         }
      );
   }
   iter += 1;
});

// When the button with the id "addRow" is pressed, do this...
$('#addRow').click(function() {
   var first_row = $('#firstBodyRow');
   first_row.clone().appendTo('#dataTable');
});