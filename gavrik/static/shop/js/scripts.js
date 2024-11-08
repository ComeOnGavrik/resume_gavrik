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
    })
//
//    $('.basket-container').on('click', 'hover', function(e){
//        e.preventDefault();
//        $('.basket-item').removeClass('hidden')
//    }
//    }
});
