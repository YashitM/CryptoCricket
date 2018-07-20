var $ = django.jQuery;

var selection = $("#id_card_type :selected").text();

$('#id_card_type').change(function() {
    updated_selection = $(this).val();
    if(updated_selection !== "Player") {
        $(".field-icc_ranking").hide();
        $(".field-country").hide();
        $(".field-ipl_team").hide();
    }
    else {
        $(".field-icc_ranking").show();
        $(".field-country").show();
        $(".field-ipl_team").show();
    }
});


