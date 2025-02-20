let button = document.getElementById('button_menu')
let menu = document.querySelector('.options')

button.addEventListener('click', function(){
    if(menu.style.display == 'none'){
        menu.style.display = 'block'
    }
    else{
        menu.style.display = 'none'
    }
})