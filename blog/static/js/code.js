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

// $(".own").change(function() {
//     if(this.checked) {
//         if(this.id == "own"){
//             $( ".own" ).prop("checked", true);
//             own.push(parseInt(this.value))        
//         }
//         else{
//             own.push(parseInt(this.value))        
//         }
//     }
//     else{
//         if(this.id == "own0"){
//             $( ".own" ).prop("checked", false);
//         }
//         var index = own.indexOf(parseInt(this.value));
//         console.log(index)

//         if (index > -1) {
//             own.splice(index, 1);
//         }
//     }
//     $( "#own" ).val(own);
//     console.log(own);
// });

own = []
other = []
original = []
auto = []
init = []

$(".all").change(function() {
    pk = this.id
    count = $( "." + this.classList[1] ).length;
    if(this.id.includes('own')){
        list = own;
    }
    else if(this.id.includes('other')){
        list = other;
    }
    else if(this.id.includes('original')){
        list = original;
    }
    else if(this.id.includes('auto')){
        list = auto;
    }
    else if(this.id.includes('init')){
        list = init;
    }
    
    if(this.checked) {
        if(this.id.includes('0')){        
            $("." + this.classList[1]).prop("checked", true);
            list = []
            for(var i=1; i<count; i++){
                list.push(i)        
            }
        }
        else{
            list.push(parseInt(this.value)) 
        }

        if(this.id.includes('own')){
            own = list;
        }
        else if(this.id.includes('other')){
            other = list;
        }
        else if(this.id.includes('original')){
            original = list;
        }
        else if(this.id.includes('auto')){
            auto = list;
        }
        else if(this.id.includes('init')){
            init = list;
        }
    }
    else{
        if(this.id.includes('0')){
            $( "." + this.classList[1] ).prop("checked", false);
            list = []
        }
        else{
            var index = list.indexOf(parseInt(this.value));
            console.log('labadadabdab' + index)
            
            if (index > -1) {
                list.splice(index, 1);
            }
        }
        if(this.id.includes('own')){
            own = list;
        }   
        else if(this.id.includes('other')){
            other = list;
        } 
        else if(this.id.includes('original')){
            original = list;
        }
        else if(this.id.includes('auto')){
            auto = list;
        }
        else if(this.id.includes('init')){
            init = list;
        }
    }
    $( "#" + this.classList[1] ).val(list);
});

if (window.location.href.indexOf("entity_list") > -1) {
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
}
$( "#delete" ).click(function() {
    $("#wrap").show()
    $("#delete").hide()
});


$( "#no" ).click(function() {
    $("#wrap").hide()
    $("#delete").show()
});