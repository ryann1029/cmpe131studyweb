/* Do not maniplate any of the code in this file.
 * Assigned to Ryan only */

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

// returns column count of the current table passed in parameter "tableID"
function columnCount(tableID) {
   var columnCount = 0;
   var table = document.getElementById(tableID);
   var columns = table.getElementsByTagName("th");

   for (var i = 0; i < columns.length; i++) {
      columnCount++;
   }

   document.querySelector("#columnCount").innerHTML =
   `${columnCount}`;

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
               <input type="text" style="width: 100px;" placeholder="Possible Points" id="totalpoints" name="pointspossible[]"/>\
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