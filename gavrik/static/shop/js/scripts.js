$(document).ready(function(){

    var form = $('#form-buying-product');
    console.log(form);

    form.on('submit', function(e){
        e.preventDefault();
        console.log('Test');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("product_name");
        var product_price = submit_btn.data("product_price")
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        $('.basket-items ul').append('<li>' + product_name + ' ' +nmb+ ' шт. ' + product_price + '<a class="delete-item" href=""> X </a>'+ '</li>' );
    })

    function showingBasket(){
        $('.basket-items').removeClass('hidden');
    }

    $('.basket-container').on('click', function(e) {
        e.preventDefault();
        showingBasket();
    })

    $('.basket-container').mouseover(function() {
        showingBasket();
    })


     $('.basket-container').mouseout(function() {
        $('.basket-items').addClass('hidden');
    })

    $(document).on('click', '.delete-item', function(e) {
        e.preventDefault();
        $(this).closest('li').remove();
    })

});
