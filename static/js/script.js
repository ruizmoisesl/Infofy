let button_album = document.getElementById('albums');
let button_singles = document.getElementById('singles')

let div_albums = document.querySelector('.albums')
let div_singles = document.querySelector('.singles')

button_album.addEventListener('click', () => {
      div_albums.style.display = 'block'
      div_singles.style.display = 'none' 

      button_album.classList.add('active')
      button_singles.classList.remove('active')
})

button_singles.addEventListener('click', () => {
    div_singles.style.display = 'block'
    div_albums.style.display = 'none'

    button_singles.classList.add('active')
    button_album.classList.remove('active')
})

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

