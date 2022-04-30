const ExpandAll = () => {
    var detail = document.getElementsByTagName("details"); 
    for (var i = 0; i < detail.length; ++i){
        document.getElementsByTagName("details")[i].setAttribute("open", '""'); 
        console.log(i); 
    }
}

const CollapseAll = () => {
    var detail = document.getElementsByTagName("details"); 
    for (var i = 0; i < detail.length; ++i){
        document.getElementsByTagName("details")[i].removeAttribute("open"); 
    }
}