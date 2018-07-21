var $ = django.jQuery;
$(".deletelink").hide();
$('[name="_addanother"]').hide();
$('[name="_continue"]').hide();
$("").hide();

var input = document.getElementsByClassName("field-eth_id")[0];
input.setAttribute("type", "hidden");

function hide_unhide(selection) {
    if(selection !== "Player") {
        $(".field-icc_ranking").hide();
        $(".field-country").hide();
        $(".field-ipl_team").hide();
    }
    else {
        $(".field-icc_ranking").show();
        $(".field-country").show();
        $(".field-ipl_team").show();
    }
}

hide_unhide($("#id_card_type :selected").text());


$('#id_card_type').change(function() {
    hide_unhide($(this).val());
});



