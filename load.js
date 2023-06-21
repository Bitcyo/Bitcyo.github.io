// Código JavaScript aparte
window.addEventListener('load', () => {
  // Obtener la referencia al elemento de la pantalla de carga
  const loader = document.querySelector('.loader');
  
  // Esperar un tiempo determinado (por ejemplo, 2 segundos) antes de redirigir
  setTimeout(() => {
    // Ocultar la pantalla de carga
    loader.style.display = 'none';
    
    // Redirigir a la página principal
    window.location.href = 'index.html';
  }, 3500); // Cambia el valor 2000 por el tiempo que desees en milisegundos
});
