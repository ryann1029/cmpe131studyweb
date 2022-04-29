/* Do not maniplate any of the code in this file.
 * Assigned to Ryan only */


// returns row count of the current table passed in parameter "tableID"
function rowCount(dataTable) {
   var rowCount = 0;
   var table = document.getElementById(dataTable);
   var rows = table.getElementsByTagName("tr");

   for (var i = 0; i < rows.length; i++) {
      rowCount++;
   }

   return rowCount;
}

function addRow(dataTable){
   var table = document.getElementById(dataTable); 
   var row = table.insertRow(rowCount(dataTable) - 1); 
   var cell = row.insertCell();

   cell.innerHTML = `<input type="text" style="width: 100px;" placeholder="Assignment Name" id="assignment"/>
                     <input type="text" style="width: 100px;" placeholder="Score" id="score"/>
                     <input type="text" style="width: 95px;" placeholder="Points Possible" id="pointspossible"/>`; 
}

function deleteRow(dataTable){
   if (rowCount(dataTable) > 3){
      document.getElementById(dataTable).deleteRow(rowCount(dataTable) - 2)
   }

}