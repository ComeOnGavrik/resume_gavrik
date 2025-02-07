$(document).ready(function(){
    console.log("Загрузился документ")
     $('#number').on('input', function() {
                this.value = this.value.replace(/[^0-9]/g, ''); // Оставляет только цифры
            });

     $('#user_phone').on('input', function() {
            this.value = this.value.replace(/[^0-9]/g, ''); // Оставляет только цифры

        });

    var form = $('#form-buying-product');
    console.log(form);

    var form1 = $('#form-csrf');

    function basketUpdating(product_id, nmb, is_delete){
        console.log("Вызвалась ф-ция basketUpdating")
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;

        var csrf_token = $('#form-csrf [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data["is_delete"] = true
        }

        var url = form.attr("action");
        if (!url){
            console.log("сработал иф")
             url = form1.attr("action");
        }
        console.log("Вывод юрл: " + url)

        console.log("!!__!!")
        console.log(data)
        console.log("!!__!!")

        $.ajax({
                    url:url,
                    type: 'POST',
                    data: data,
                    cache: true,
                    success: function (data) {
                        console.log("OK");
                        console.log(data.products_total_nmb);
                        if (data.products_total_nmb || data.products_total_nmb == 0){
                            $('#basket_total_nmb').html("<span class='circle'>" + data.products_total_nmb + "</span>");
                            console.log("Вывод словаря:");
                            console.log(data.products);
                            $('.basket-items ul').empty();
                            $.each(data.products, function(k, v){
                                $('.basket-items ul').append('<li>' + v.name + ' ' +v.nmb+ ' шт. '
                                 + v.price_per_item + '<a class="delete-item" href="" data-product_id="' + v.id + '">x</a> ' + '</li>'  );
                            })
                        }
                        else{
                            console.log("error_nmb")
                        }
                    },
                    error: function(){
                        console.log("error");
                    }
                })
    }

    form.on('submit', function(e){
        e.preventDefault();
        console.log("________Test__________");
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("product_name");
        var product_price = submit_btn.data("product_price")
        console.log("________________________");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);
        console.log("________________________");

        basketUpdating(product_id, nmb, is_delete=false);
    })



    $('form[id^="form-buying-product-"]').on('submit', function(e){
        e.preventDefault();
        console.log("________Test__________");

        var form = $(this);
        var nmb = form.find('input[name="number"]').val();
        console.log(nmb);

        var submit_btn = form.find('button[id^="submit_btn-"]');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("product_name");
        var product_price = submit_btn.data("product_price");

        console.log("_____///////////////_______");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);
        console.log("______////////////////_______");

        basketUpdating(product_id, nmb, false);
    });


//    function showingBasket(){
//        $('.basket-items').toggleClass('hidden');
//    }
//
//
//
//    $('.basket-container').mouseover(function() {
//        showingBasket();
//    })
//
//


    $(document).on('click', '.delete-item', function(e) {
        e.preventDefault();
        product_id = $(this).data("product_id");
        console.log("Вывод в консоль при удалении id=" + product_id)
        nmb = 0;
        basketUpdating(product_id, nmb, is_delete=true);
        setTimeout(() => {
        location.reload(true);
        }, 500);
    })


    $(document).on('change', ".product-in-basket-nmb", function () {
    var current_nmb = parseInt($(this).val()); // Получаем текущее количество
    var current_tr = $(this).closest('td'); // Ищем ближайший родительский <td>
    var current_price = parseFloat(current_tr.find('.product-price').text().replace(',', '.')); // Цена товара
    var total_amount = current_nmb * current_price; // Общая сумма для текущего товара
    current_tr.find('.total-product-in-basket-amount').text(total_amount.toFixed(2) + "$"); // Обновляем сумму
    calculatingBasketAmount(); // Вызываем функцию для пересчета общей суммы корзины
});

$(document).on('click', '.number-minus, .number-plus', function () {
    var input = $(this).siblings('.product-in-basket-nmb'); // Находим input внутри блока .number

    if ($(this).hasClass('number-minus')) {
        input[0].stepDown(); // Уменьшаем значение
    } else if ($(this).hasClass('number-plus')) {
        input[0].stepUp(); // Увеличиваем значение
    }

    // Программно вызываем событие change для input
    $(input).trigger('change');
});

function calculatingBasketAmount() {
    var totalBasketAmount = 0;
    $('.total-product-in-basket-amount').each(function () {
        totalBasketAmount += parseFloat($(this).text().replace(',', '.')) || 0;
    });

        $('#total_order_amount').text(totalBasketAmount.toFixed(2))
    // Здесь вы можете обновить общую сумму корзины в нужном месте
    console.log("Total Basket Amount: ", totalBasketAmount.toFixed(2));
}

    calculatingBasketAmount()


    let inactivityTime = 0;

    function resetTimer() {
        inactivityTime = 0; // Сброс таймера при активности
    }

    function showModal() {
        $('#orderCallModal').css('display', 'flex'); // Показываем модальное окно
        setTimeout(function() {
            $('#orderCallModal').addClass('show'); // Добавляем класс для анимации
        }, 10); // Небольшая задержка для корректной анимации
    }

    const timer = setInterval(function() {
        inactivityTime++;
        if (inactivityTime >= 30) { // 60 секунд бездействия
            showModal(); // Запускаем анимацию
            clearInterval(timer);
        }
    }, 1000); // Проверка каждую секунду

    $(window).on('mousemove keydown click scroll', resetTimer);

    $('#closeModal').on('click', function() {
        $('#orderCallModal').removeClass('show'); // Удаляем класс для анимации
        setTimeout(function() {
            $('#orderCallModal').css('display', 'none'); // Скрываем модальное окно после анимации
        }, 300); // Ждем завершения анимации
    });

    $('#orderCallForm').on('submit', function(e) {
        e.preventDefault();
        const name = $('#subscriber_name').val();
        const phone = $('#subscriber_phone').val();

        console.log(`Заказан звонок от ${name} с номером ${phone}`);

        $('#orderCallModal').removeClass('show'); // Удаляем класс для анимации
        setTimeout(function() {
            $('#orderCallModal').css('display', 'none'); // Скрываем модальное окно после анимации
        }, 300); // Ждем завершения анимации


        var data = {}
        var csrf_token = $('#form-csrf [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        const subscriberName = $('#subscriber_name').val();
        const subscriberPhone = $('#subscriber_phone').val();

        // Переменная для отслеживания ошибок
        let isValid = true;
        let errorMessage = '';

        // Валидация имени
        if (subscriberName.length > 20) {
            isValid = false;
            errorMessage += 'Имя не может превышать 20 символов.\n';
        }
        if (/[^a-zA-Zа-яА-ЯёЁ\s]/.test(subscriberName)) {
            isValid = false;
            errorMessage += 'Имя может содержать только буквы.\n';
        }

        // Валидация телефона
        if (subscriberPhone.length > 12) {
            isValid = false;
            errorMessage += 'Телефон не может превышать 12 символов.\n';
        }
        if (!/^\d+$/.test(subscriberPhone)) {
            isValid = false;
            errorMessage += 'Телефон может содержать только цифры.\n';
        }

        // Если есть ошибки, выводим сообщение и прерываем отправку формы
        if (!isValid) {
            alert(errorMessage);
            return;
        }

        // Если данные валидны, собираем данные для отправки
        const formData = {
            subscriber_name: subscriberName,
            subscriber_phone: subscriberPhone
        };



        var form2 = $('#orderCallForm');
        var url = form2.attr("action");

        $.ajax({
            url:url,
            type: 'POST',
            data: formData,
            headers: {
                'X-CSRFToken': csrf_token // Добавляем CSRF-токен в заголовок
            },
            cache: true,
            success: function(response) {
                console.log('Успешно отправлено:');
            },
            error: function(xhr, status, error) {
                console.error('Ошибка:', error);
            }
        })


        this.reset();
    });

});


document.addEventListener('DOMContentLoaded', function() {
    const swiper = new Swiper('.swiper-container', {
        // Настройки слайдера
        loop: true, // Зацикливание
        pagination: {
            el: '.swiper-pagination',
            clickable: true, // Кликабельные точки
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        autoplay: {
            delay: 10000, // Автопрокрутка каждые 3 секунды
            disableOnInteraction: false, // Продолжать автоматическую прокрутку
        },
    });

});