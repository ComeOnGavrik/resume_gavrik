document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggleMenu');
    const sidenav = document.querySelector('.sidenav');

    // Устанавливаем начальное состояние меню

    toggleButton.addEventListener('click', function() {
        sidenav.classList.toggle('show'); // Переключаем класс

    });
});