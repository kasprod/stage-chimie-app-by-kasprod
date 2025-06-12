// Ajoute la classe active à la nav-link correspondant à la page courante
document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll('.nav-item .nav-link');
    const currentUrl = window.location.href.split(/[?#]/)[0];
    links.forEach(link => {
      // Vérifie si le href du lien correspond à l'URL courante
      if (link.href === currentUrl || (link.href.endsWith('/') && currentUrl.endsWith(link.href))) {
        links.forEach(l => l.classList.remove('active'));
        link.classList.add('active');
      }
    });
  });