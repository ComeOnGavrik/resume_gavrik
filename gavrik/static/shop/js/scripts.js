$(document).ready(function(){

//    var data = {};
//    var csrf_token = $('#form-csrf [name="csrfmiddlewaretoken"]').val();
//    data["csrfmiddlewaretoken"] = csrf_token;

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

        console.log(data)

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
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("product_name");
        var product_price = submit_btn.data("product_price")


        basketUpdating(product_id, nmb, is_delete=false);
    })

    function showingBasket(){
        $('.basket-items').toggleClass('hidden');
    }

    $('.basket-container').on('click', function(e) {
        e.preventDefault();
        showingBasket();
    })

//    $('.basket-container').mouseover(function() {
//        showingBasket();
//    })
//
//
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

});
