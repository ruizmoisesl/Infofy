document.addEventListener("DOMContentLoaded", function () {
    const loader = document.querySelector(".loader");
    const albumsList = document.querySelector(".albums_list");

    if (!loader || !albumsList) {

        return;
    }


    const images = albumsList.querySelectorAll("img");
    let loadedImages = 0;

    if (images.length === 0) {

        loader.style.display = "none";
        albumsList.style.display = "grid";
        return;
    }


    function checkAllImagesLoaded() {
        loadedImages++;

        if (loadedImages === images.length) {
            loader.style.display = "none";
            albumsList.style.display = "grid";
        }
    }

    images.forEach((img, index) => {
        if (img.complete) {
            checkAllImagesLoaded(); // Si la imagen ya está en caché, contarlo inmediatamente
        } else {
            img.onload = () => {

                checkAllImagesLoaded();
            };
            img.onerror = () => {

                checkAllImagesLoaded();
            };
        }
    });
});


document.addEventListener("DOMContentLoaded", function () {


    const loader2 = document.querySelector(".loader2");
    const singlesList = document.querySelector(".singles_list");

    if (!loader2 || !singlesList) {
        return;
    }
    const images = singlesList.querySelectorAll("img");
    let loadedImages2 = 0;

    if (images.length === 0) {
        loader2.style.display = "none";
        singlesList.style.display = "grid";
        return;
    }

    console.log(`🖼 Se encontraron ${images.length} imágenes. Esperando a que carguen...`);

    function checkAllImagesLoaded() {
        loadedImages2++;

        if (loadedImages2 === images.length) {

            loader2.style.display = "none";
            singlesList.style.display = "grid";
        }
    }

    images.forEach((img, index) => {
        if (img.complete) {
            checkAllImagesLoaded(); 
        } else {
            img.onload = () => {
                checkAllImagesLoaded();
            };
            img.onerror = () => {
                checkAllImagesLoaded();
            };
        }
    });
});
