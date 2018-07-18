$("[id*='buy_now']") .click( function(e) {
    e.preventDefault();
    var pressed_element = this.id;
    pressed_element = pressed_element.substring(7);
    if (typeof web3 !== 'undefined') {
        web3 = new Web3(web3.currentProvider);
        $("#metamask_downloaded_modal" + pressed_element).modal();
    }
    else {
        $("#metamask_download_modal" + pressed_element).modal();
    }
    return false;
});