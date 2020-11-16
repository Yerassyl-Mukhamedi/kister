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
        if(this.value == '0'){        
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
        if(this.value == '0'){
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




if (window.location.href.indexOf("mail_new") > -1) {
    $('#id_in_number').prop('readonly', true);
    $('#id_out_number').prop('readonly', true);
}

$("#id_own_company").change(function() {
    var company_id = $("#id_own_company").val()
    var number = parseInt($("#"+company_id+" .sec2").html())
    // $("#id_in_number").val(8)
    $("#id_in_number").val(number+1);
    $("#id_out_number").val(number+1);
})


if (window.location.href.indexOf("mail_edit") > -1) {
    var company_id = $("#company_id").html()
    var init_id = $("#init_id").html()
    var side_two_id = $("#side_two_id").html()
    var number = $("#number").html()
    var text = $("#text").html()
    var track = $("#track").html()
    $("[name*='number']").prop('readonly', true);
    $("#id_own_company").val(company_id);
    $("#id_init").val(init_id);
    $("#id_side_two").val(side_two_id);
    $("#id_topic").val(text);
    $("#id_track").val(track);
    $("[name*='number']").val(number)

}



if (window.location.href.indexOf("mail_detail") > -1) {
    let dok = document.getElementById('topic').innerHTML;
    const array = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
    let list = []
    let counter = 0;
    let b = '<br>' 
    for(i=0;i<dok.length;i++){
        if(dok[i]=='.' && array.includes(dok[i-1])){
            // list.push(i-2)
            if(!array.includes(dok[i-2])){
                dok = [dok.slice(0, i-1), b , dok.slice(i-1)].join('');
                i = i + 5
            }
            else{
                dok = [dok.slice(0, i-2), b , dok.slice(i-2)].join('');
                i = i + 5
            }
        }
    }
    // for(i=1; i<list.length+1; i++){
    //     dok = [dok.slice(0, list[i]+(2*i)), b , dok.slice(list[i]+(4*i))].join('');
    // }
    console.log(dok)
    document.getElementById('topic').innerHTML = dok;
    // console.log(list)
    // console.log(dok[97])
}
if (window.location.href.indexOf("some_view") > -1) {
    $(".header").hide()

    let dok = document.getElementById('topic').innerHTML;
    const array = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];
    let list = []
    let counter = 0;
    let b = '<br>' 
    for(i=0;i<dok.length;i++){
        if(dok[i]=='.' && array.includes(dok[i-1])){
            // list.push(i-2)
            if(!array.includes(dok[i-2])){
                dok = [dok.slice(0, i-1), b , dok.slice(i-1)].join('');
                i = i + 5
            }
            else{
                dok = [dok.slice(0, i-2), b , dok.slice(i-2)].join('');
                i = i + 5
            }
        }
    }
    // for(i=1; i<list.length+1; i++){
    //     dok = [dok.slice(0, list[i]+(2*i)), b , dok.slice(list[i]+(4*i))].join('');
    // }
    console.log(dok)
    document.getElementById('topic').innerHTML = dok;
    // console.log(list)
    // console.log(dok[97])
}