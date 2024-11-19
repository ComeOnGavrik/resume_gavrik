$(document).ready(function(){

    var form = $('#form-buying-product');
    console.log(form);

    form.on('submit', function(e){
        e.preventDefault();
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("product_name");
        var product_price = submit_btn.data("product_price")


                 var data = {};
                        data.product_id = product_id;
                        data.nmb = nmb;

                        var csrf_token = $('#form-buying-product [name="csrfmiddlewaretoken"]').val();
                        data["csrfmiddlewaretoken"] = csrf_token;

                        var url = form.attr("action");

                        console.log(data)
                        $.ajax({
                            url:url,
                            type: 'POST',
                            data: data,
                            cache: true,
                            success: function (data) {
                                console.log("OK");
                                console.log(data.products_total_nmb);
                                if (data.products_total_nmb){
                                    $('#basket_total_nmb').text("( " + data.products_total_nmb + " )");
                                    console.log("Вывод словаря:");
                                    console.log(data.products);
                                    $('.basket-items ul').empty();
                                    $.each(data.products, function(k, v){
                                        $('.basket-items ul').append('<li>' + v.name + ' ' +v.nmb+ ' шт. ' + v.price_per_item + '</li>' );
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
        $(this).closest('li').remove();
        showingBasket();
    })

});
