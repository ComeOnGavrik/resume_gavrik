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
                            $('#basket_total_nmb').text("( " + data.products_total_nmb + " )");
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


    function showingBasket(){
        $('.basket-items').toggleClass('hidden');
    }


//    $('.basket-container').on('click', function(e) {
//        showingBasket();
//    })

    $('.basket-container').mouseover(function() {
        showingBasket();
    })


//     $('.basket-container').mouseout(function() {
//        $('.basket-items').addClass('hidden');
//    })




    $(document).on('click', '.delete-item', function(e) {
        e.preventDefault();
        product_id = $(this).data("product_id");
        console.log("Вывод в консоль при удалении id=" + product_id)
        nmb = 0;
        basketUpdating(product_id, nmb, is_delete=true);
        showingBasket();

    })

    function calculatingBasketAmount(){
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function(){
            console.log(parseFloat($(this).text().replace(',', '.')));
            total_order_amount += parseFloat($(this).text().replace(',', '.'));
        })
        total_order_amount = total_order_amount.toFixed(2)
        $('#total_order_amount').text(total_order_amount)
        console.log('общая стоимость '+total_order_amount);
    };


    $(document).on('change', ".product-in-basket-nmb", function(){
        var current_nmb = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text().replace(',', '.'));
        var total_amount = current_nmb*current_price
        current_tr.find('.total-product-in-basket-amount').text(total_amount)
        calculatingBasketAmount();
    })

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
        if (inactivityTime >= 6) { // 60 секунд бездействия
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

        const formData = {
            subscriber_name: $('#subscriber_name').val(),
            subscriber_phone: $('#subscriber_phone').val()
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
                        // Обработка успешного ответа
                        console.log('Успешно отправлено:');
                        console.log("________")
                        console.log(formData)
                        console.log("________")
                        // Здесь можно добавить логику для отображения сообщения пользователю
                    },
                    error: function(xhr, status, error) {
                        // Обработка ошибки
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
            delay: 300000, // Автопрокрутка каждые 3 секунды
            disableOnInteraction: false, // Продолжать автоматическую прокрутку
        },
    });

});