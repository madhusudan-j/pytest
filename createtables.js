
function tableFromJson(mtc_versions) {
    // the json data. (you can change the values for output.)
    console.log(mtc_versions);
    localStorage.setItem('mtc_versions', JSON.stringify(mtc_versions));
    var mainDiv = document.getElementById("myDIV");
    
    // Extract value from table header. 
    var col = ['version', 'isinstalled', 'review', 'twiki'];
    var tablehead = ['MTC Version', 'Installed?', 'Review', 'Twiki'];
    
    // Create a table.
    var table = document.createElement("table");
    table.className = "table table-bordered";
    table.id = "tableMTC";
    // Create table header row using the extracted headers above.
    var tr = table.insertRow(-1);               // table row.
    for (var i = 0; i < col.length; i++) {
        var th = document.createElement("th");      // table header.
        th.innerHTML = tablehead[i];
        tr.appendChild(th);
    }
    // add json data to the table as rows.
    for (var i = mtc_versions.length - 1; i >= 0; i--) {
        tr = table.insertRow(-1);
        tr.id = mtc_versions[i][col[0]];
        tr.className = "mtcrow";
        // tr.id.onmousedown = function() {GetSelectedRows(this,false)};
        tr.setAttribute("onmousedown","GetSelectedRows(this,false);");
        var tdver = document.createElement("td");
        tdver.innerHTML = mtc_versions[i][col[0]];
        var tdinstall = document.createElement("td");
        tdinstall.innerHTML = mtc_versions[i][col[1]];

        var tdreview = document.createElement("td");
        // var areview = document.createElement('a');
        // areview.setAttribute('href', "/mtc/"+mtc_versions[i][col[0]]+"/"+mtc_versions[i][col[2]]+"/");
        // areview.innerHTML = mtc_versions[i][col[2]];
        // tdreview.appendChild(areview);
        var button = document.createElement("BUTTON");
        // var btext = document.createTextNode(mtc_versions[i][col[2]]);
        button.innerHTML = mtc_versions[i][col[2]];
        // button.appendChild(btext); <button type="button" class="btn btn-primary" data-toggle="modal" data-target=".bd-example-modal-lg">Large modal</button>
        button.className = "btn btn-primary";
        button.setAttribute('data-toggle',"modal");
        button.setAttribute('data-target',".bd-example-modal-lg");
        var m = mtc_versions[i][col[0]];
        var r = mtc_versions[i][col[2]];
        button.value = m+"-"+r;
        button.addEventListener("click", instal_uninstal_mtc, this);
        tdreview.appendChild(button);

        var tdtwiki = document.createElement("td");
        var atwiki = document.createElement('a');
        atwiki.setAttribute('href',mtc_versions[i][col[3]]);
        atwiki.innerHTML = "Twiki";
        tdtwiki.appendChild(atwiki);

        tr.appendChild(tdver);
        tr.appendChild(tdinstall);
        tr.appendChild(tdreview);
        tr.appendChild(tdtwiki);

    }
    // Now, add the newly created table with json data, to a container.
    mainDiv.appendChild(table);
}

// $(document).ready(function(){
//     $(".mtcrow").click(function(){
//         mtc_id = this.id;
//         showUsedTools(mtc_id)
//         });
//     });

function showUsedTools(id) {
    console.log(id);
    var mtc_versions = localStorage.getItem('mtc_versions');
    mtc_versions = JSON.parse(mtc_versions);
    var find_mtc = mtc_versions.find(find_mtc => find_mtc.version === id);
    var used_tools = find_mtc["used_tools"]
    console.log(used_tools);
    removeTableBody()
    var usedtoolsdiv = document.getElementById("usedtoolsdiv");
    // Extract value from table header. 
    var col = ['tool_name', 'version'];
    var toolstablehead = ['Tool Name', 'MTC ' + id];

    toolshead = document.getElementById("toolshead");
    toolshead.innerHTML = "Internal tools used by MTC"; 

    // var table = document.createElement("table");
    // table.id = "toolstable";
    
    table = document.getElementById("toolstable");
    table.className = "table table-bordered";
    // Create table header row using the extracted headers above.
    var tr = table.insertRow(-1);               // table row.
    tr.id = "used_tools_th";
    for (var i = 0; i < col.length; i++) {
        var th = document.createElement("th");      // table header.
        th.innerHTML = toolstablehead[i];
        tr.appendChild(th);
    }
    // add json data to the table as rows.
    for (var i = 0; i < used_tools.length; i++) {
        tr = table.insertRow(-1);
        tr.id = used_tools[i][col[0]];
        for (var j = 0; j < col.length; j++) {
            var tabCell = tr.insertCell(-1);
            tabCell.innerHTML = used_tools[i][col[j]];
        }
    }
    // Now, add the newly created table with json data, to a container.
    usedtoolsdiv.appendChild(table);
}

function CompareUsedTools(id) {
    console.log("Id to compare " + id)
    var mtc_versions = localStorage.getItem('mtc_versions');
    mtc_versions = JSON.parse(mtc_versions);
    var find_mtc = mtc_versions.find(find_mtc => find_mtc.version === id);
    var used_tools = find_mtc["used_tools"]
    console.log("used_tools");
    var col = ['tool_name', 'version'];
    var toolstablehead = ['Tool Name', 'MTC ' + id];

    // Create table header row using the extracted headers above.
    table = document.getElementById("toolstable");
    var get_tools_th = document.getElementById("used_tools_th");
    var th = document.createElement("th");      // table header.
    th.innerHTML = toolstablehead[1];
    get_tools_th.appendChild(th);
    // var tabCell = get_tools_th.insertCell(-1);
    // tabCell.innerHTML = toolstablehead[1];

    // add json data to the table as rows.
    for (var i = 0; i < used_tools.length; i++) {
        if(!document.getElementById(used_tools[i][col[0]])){
            tr = table.insertRow(-1);
            tr.id = used_tools[i][col[0]];
            for (var j = 0; j < col.length; j++) {
                var tabCell = tr.insertCell(-1);
                tabCell.innerHTML = used_tools[i][col[j]];
            }
        }
        var get_tools_data = document.getElementById(used_tools[i][col[0]]);
        var tabCell = get_tools_data.insertCell(-1);
        tabCell.innerHTML = used_tools[i][col[1]];
    }
    // Now, add the newly created table with json data, to a container.
    usedtoolsdiv.appendChild(table);
}

function removeTableBody(){
    $('#toolstable tbody').empty();
  }

var lastSelectedRow;
var selectedRowList=new Array();
function GetSelectedRows(currenttr, lock) {
    if (window.event.ctrlKey) {
            selectedRowList.push(currenttr);
            console.log(selectedRowList)
    }
    
    if (window.event.button === 0) {
        if (!window.event.ctrlKey && !window.event.shiftKey) {
            clearAll();
			selectedRowList=new Array();
			selectedRowList.push(currenttr);
			lastSelectedRow=currenttr;
        }
        if (window.event.shiftKey) {
            selectRowsBetweenIndexes([lastSelectedRow.rowIndex, currenttr.rowIndex])
        }
    }

	currenttr.style.backgroundColor = "lightgray";
	if(selectedRowList.length>1)
	{
    //instead call the function u have written for comparing selected MTC versions.
    count = selectedRowList.length-1;
        for(var i=count; i<selectedRowList.length;i++)
		{
            CompareUsedTools(selectedRowList[i].id)
		}
	}
	else
	{
    //instead call the function written to display the details of selected MTC version.
    showUsedTools(selectedRowList[0].id)
		// alert("Selected row is "+selectedRowList[0].id);
	}
}
function selectRowsBetweenIndexes(indexes) {
    indexes.sort(function(a, b) {
        return a - b;
    });
    for (var i = indexes[0]; i <= indexes[1]; i++) {
        $("#tableMTC")[0].tBodies[0].getElementsByTagName('tr')[i-1].selected = true;
		$("#tableMTC")[0].tBodies[0].getElementsByTagName('tr')[i-1].style.background = "lightBlue";
		selectedRowList.push($("#tableMTC")[0].tBodies[0].getElementsByTagName('tr')[i-1]);
    }
}

function clearAll() {
    for (var i = 0; i < $("#tableMTC")[0].tBodies[0].getElementsByTagName('tr').length; i++) {
        $("#tableMTC")[0].tBodies[0].getElementsByTagName('tr')[i].style.background = "white";
    }
}

function instal_uninstal_mtc(){
    console.log("yessss", this.value)

    let text = this.value;
    const ver_rev = text.split("-");
    var version = ver_rev[0];
    var review = ver_rev[1];
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // var res = JSON.parse(this.responseText);
            var res = this.responseText;
            var status = res.status;
            var message = res.message;
            console.log("200 passed",message)
            show_console_data(res);
            
        }
    };
    xhttp.open("GET", "/mtc?" + "version=" + version + "&review=" + review, true);
    xhttp.setRequestHeader("Content-type",
        "application/x-www-form-urlencoded");
    xhttp.send();
}

function show_console_data(res){
    console.log("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    // var cardDiv = document.getElementById("myDIV");
    var cardDiv = document.getElementById("cardDiv");
    cardDiv.className = "modal fade bd-example-modal-lg";
    cardDiv.setAttribute('tabindex',"-1");
    cardDiv.setAttribute('rolw',"dialog");
    cardDiv.setAttribute('aria-labelledby',"myLargeModalLabel");
    cardDiv.setAttribute('aria-hidden',"true");

    var cardDivch1 = document.createElement("cardchild1");
    cardDivch1.className = "modal-dialog modal-lg";

    var cardDivch2 = document.createElement("cardchild2");
    cardDivch2.className = "modal-content";

    var par = document.createElement('p');
    par.value = res

    cardDivch2.appendChild(par)
    cardDivch1.appendChild(cardDivch2) 
    cardDiv.appendChild(cardDivch1)
}


