$(document).ready(function(){
    var form = $('#form-buying-product');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');

        var nmb = $('#number').val();

        console.log(nmb);
    })
});