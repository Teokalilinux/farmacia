window.onload = function () {
    console.log("Archivo script.js cargado correctamente");
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    console.log(csrfToken);

    function reducir() {
        console.log("Función reducir() invocada");
        return fetch('/menosstock/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        })
            .then(response => response.json())
            .then(data => console.log("Datos recibidos:", data))
            .catch(error => console.error("Error en reducir():", error));
    }
    const button = document.querySelector('button[type="button"]');
    button.addEventListener('click', reducir);  // Ahora manejas el click con JS
};
