document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggleMenu');
    const sidenav = document.querySelector('.sidenav');

    // Устанавливаем начальное состояние меню

    toggleButton.addEventListener('click', function() {
        if (sidenav.style.display === 'none' || sidenav.style.display === '') {
            sidenav.style.display = 'block'; // Показываем меню
        } else {
            sidenav.style.display = 'none';  // Скрываем меню
        }
    });
});