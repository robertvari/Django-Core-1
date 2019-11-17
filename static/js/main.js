// console.log( document.getElementById("mobile_menu_items") )

function show_mobile_menu(){
    let mobile_menu_items = document.getElementById("mobile_menu_items")

    if(mobile_menu_items.style.display == "none" || mobile_menu_items.style.display.length == 0){

        mobile_menu_items.style.display = "block"

    }else{

        mobile_menu_items.style.display = "none"

    }

    
}