function toggleNavButtonVisibility() {
    const navButton = document.querySelector('.navbutton');
    const card2 = document.querySelector('.card2')
    if (window.innerWidth < 769) {
        navButton.classList.remove('hidden');
        card2.classList.add('hidden');

    } else {
        navButton.classList.add('hidden');
        card2.classList.remove('hidden');
    }
}

// Запускаем функцию при загрузке страницы
toggleNavButtonVisibility();

// Добавляем обработчик события на изменение размера окна
window.addEventListener('resize', toggleNavButtonVisibility);

document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('.btn-warning');
    const card1 = document.querySelector('.card1'); // Убедитесь, что у вас есть элемент с классом card1
    const card2 = document.querySelector('.card2'); // Убедитесь, что у вас есть элемент с классом card2

    button.addEventListener('click', function() {
        if (card1.classList.contains('hidden')) {
            // Если card1 скрыта, показываем ее и меняем текст на кнопке
            card1.classList.remove('hidden');
            card2.classList.add('hidden');
            button.textContent = 'Обо мне';
        } else {
            // Если card1 видима, скрываем ее и показываем card2, меняем текст на кнопке
            card1.classList.add('hidden');
            card2.classList.remove('hidden');
            button.textContent = 'Смотреть ТЗ';
        }
    });
});