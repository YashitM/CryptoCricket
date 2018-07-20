// Trigger this function when admin adds a new card
// Aparam cardName: string: name on the card
// @param cardID: integer: 0-CricketBoard 1-Country 2-Player

var $ = django.jQuery;

function addNewCard(cardName, cardID)
{
	console.log("h");
	var currentAcc = "";
	var ceoAcc = "";
    web3.eth.getCoinbase(function(err,account)
    {
	  if(err === null)
	  {
	    currentAcc = account;
	    cryptoCricketInstance.ceoAddress(function(error,result)
	    {
			if(!error)
			{
				ceoAcc = result;
			}
			else
		    {
		    	console.error(error);
		    	return;
		    }
		});
	  }
	  else
	  {
	  	console.log(err);
	  	return;
	  }
	});

	var myEvent = cryptoCricketInstance.LogBirth({},{fromBlock: 0, toBlock: 'latest'});
	if(currentAcc !== ceoAcc)
	{
        alert("Login from admin account.");
		return;
	}
	else
	{
		cryptoCricketInstance.createPlayer(cardName, cardID, function(error,result)
		{
		  if(error)
		    console.error(error);
		  else
		  {
		    myEvent.watch(function(error, result)
		    {
		      console.log("Created Card Successfully");
		      console.log(JSON.stringify(result.args.tokenId));
		      console.log(JSON.stringify(result.args.name));
		      console.log(JSON.stringify(result.args.Price));
		    });
		  }
		})
	}
	myEvent.stopWatching();
}

$('input[name="_save"]').click(function(event) {

    var cardName = document.getElementById("id_name").value;
    var cardType = $("#id_card_type :selected").text();
    var id;
    if(cardType === "Board") {
        id = 0;
    } else if (cardType === "Country") {
        id = 1;
    } else {
        id = 2;
    }

    if(id && cardName) {
        event.preventDefault();
        document.getElementsByName("_save")[0].disabled = true;

        addNewCard(cardName, id);
        document.getElementById("card_form").submit();
    }
});