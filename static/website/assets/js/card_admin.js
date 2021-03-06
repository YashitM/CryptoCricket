var $ = django.jQuery;
$(".deletelink").hide();
$('[name="_addanother"]').hide();
$('[name="_continue"]').hide();
$('.field-eth_id').hide();
$('.field-transactions').hide();

function hide_unhide(selection) {

    if(selection === "Player") {
        $(".field-icc_ranking").show();
        $(".field-country").show();
        $(".field-ipl_team").show();
    } else if (selection === "Country") {
        $(".field-icc_ranking").show();
        $(".field-country").hide();
        $(".field-ipl_team").hide();
    } else {
        $(".field-icc_ranking").hide();
        $(".field-country").hide();
        $(".field-ipl_team").hide();
    }
}

hide_unhide($("#id_card_type :selected").text());


$('#id_card_type').change(function() {
    hide_unhide($(this).val());
});



