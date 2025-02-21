document.addEventListener("DOMContentLoaded", function () {
    console.log("📌 DOM completamente cargado.");

    const loader = document.querySelector(".loader");
    const albumsList = document.querySelector(".albums_list");

    if (!loader || !albumsList) {
        console.error("❌ Error: No se encontró el loader o la lista de álbumes en el DOM.");
        return;
    }

    console.log("✅ Loader y lista de álbumes encontrados en el DOM.");

    // Obtener todas las imágenes dentro de la lista de álbumes
    const images = albumsList.querySelectorAll("img");
    let loadedImages = 0;

    if (images.length === 0) {
        console.log("⚠ No hay imágenes en la lista de álbumes. Ocultando loader inmediatamente.");
        loader.style.display = "none";
        albumsList.style.display = "block";
        return;
    }

    console.log(`🖼 Se encontraron ${images.length} imágenes. Esperando a que carguen...`);

    function checkAllImagesLoaded() {
        loadedImages++;
        console.log(`🔄 Imagen cargada (${loadedImages}/${images.length})`);

        if (loadedImages === images.length) {
            console.log("✅ Todas las imágenes han cargado. Mostrando la lista de álbumes.");
            loader.style.display = "none";
            albumsList.style.display = "grid";
        }
    }

    images.forEach((img, index) => {
        if (img.complete) {
            console.log(`🟢 Imagen ${index + 1} ya estaba en caché.`);
            checkAllImagesLoaded(); // Si la imagen ya está en caché, contarlo inmediatamente
        } else {
            img.onload = () => {
                console.log(`🖼 Imagen ${index + 1} cargada correctamente.`);
                checkAllImagesLoaded();
            };
            img.onerror = () => {
                console.warn(`❌ Error al cargar la imagen ${index + 1}.`);
                checkAllImagesLoaded();
            };
        }
    });
});


document.addEventListener("DOMContentLoaded", function () {
    console.log("📌 DOM completamente cargado.");

    const loader = document.querySelector(".loader");
    const albumsList = document.querySelector(".singles_list");

    if (!loader || !albumsList) {
        console.error("❌ Error: No se encontró el loader o la lista de álbumes en el DOM.");
        return;
    }

    console.log("✅ Loader y lista de álbumes encontrados en el DOM.");

    // Obtener todas las imágenes dentro de la lista de álbumes
    const images = albumsList.querySelectorAll("img");
    let loadedImages = 0;

    if (images.length === 0) {
        console.log("⚠ No hay imágenes en la lista de álbumes. Ocultando loader inmediatamente.");
        loader.style.display = "none";
        albumsList.style.display = "block";
        return;
    }

    console.log(`🖼 Se encontraron ${images.length} imágenes. Esperando a que carguen...`);

    function checkAllImagesLoaded() {
        loadedImages++;
        console.log(`🔄 Imagen cargada (${loadedImages}/${images.length})`);

        if (loadedImages === images.length) {
            console.log("✅ Todas las imágenes han cargado. Mostrando la lista de álbumes.");
            loader.style.display = "none";
            albumsList.style.display = "grid";
        }
    }

    images.forEach((img, index) => {
        if (img.complete) {
            console.log(`🟢 Imagen ${index + 1} ya estaba en caché.`);
            checkAllImagesLoaded(); // Si la imagen ya está en caché, contarlo inmediatamente
        } else {
            img.onload = () => {
                console.log(`🖼 Imagen ${index + 1} cargada correctamente.`);
                checkAllImagesLoaded();
            };
            img.onerror = () => {
                console.warn(`❌ Error al cargar la imagen ${index + 1}.`);
                checkAllImagesLoaded();
            };
        }
    });
});
