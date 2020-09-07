var check_list = document.getElementById("check_list").childElementCount;
list = []
var i = 0;
for(i; i<check_list; i++){
    var current = ((document.getElementById("check_list").children[i]).className);
    if(list.includes(current)){
        document.getElementById("check_list").children[i].classList.add("hidden")
    }
    else{
        list.push(current);
    }
}
// console.log(list);

// var elist = document.getElementById("elist").childElementCount;
// for(var j=0; j<elist; j++){
//     var current = ((document.getElementById("elist").children[j]).className);
//     if(list.includes(current)){
//         document.getElementById(current).classList.add("visible")
//     }
//     else{
//         document.getElementById(current).classList.add("hidden")        
//     }
// }