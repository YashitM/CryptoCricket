// Trigger this function when admin adds a new card
// Aparam cardName: string: name on the card
// @param cardID: integer: 0-CricketBoard 1-Country 2-Player

var $ = django.jQuery;

function addNewCard(cardName, cardID)
{
	// check network
	var networkID = "";							// change this in the future
	var networkName = "Ropsten Test Network";	// change this in the future

	web3.version.getNetwork((err, netId) => { networkID = netId;})
	console.log(networkID);
	console.log(typeof networkID);
	if(networkID !== "3")
	{
		alert("Please Switch to the " + networkName);
		return;
	}
	
	var currentAcc = "";
	var ceoAcc = "";
	web3.eth.getCoinbase(function(err,account)
	{
	if(err === null)
	{
        $('body').addClass("loading");

		currentAcc = account;
		cryptoCricketInstance.ceoAddress(function(error,result)
		{
			if(!error)
			{
				ceoAcc = result;

				var myEvent = cryptoCricketInstance.LogBirth({},{fromBlock: web3.eth.getBlockNumber(function(error, result){}), toBlock: 'latest'});
				if(currentAcc !== ceoAcc)
				{
                    $('body').removeClass("loading");
                    alert("Login from admin account");
					return;
				}
				else
				{
					// load the svg graphic
					cryptoCricketInstance.createPlayer(cardName, cardID, function(error,result)
					{
					if(error) {
                        console.error(error);
                        $('body').removeClass("loading");
                    }
					else
					{

						myEvent.watch(function(error, result)
						{
						// hide the svg graphic
						console.log("Created Card Successfully");
						
						var token = JSON.stringify(result.args.tokenId);

						// console.log(token);
						// console.log(JSON.stringify(result.args.name));
						// console.log(JSON.stringify(result.args.Price));

						var input = document.getElementById("id_eth_id");
						token = token.replace('"',"").replace('"',"");
						input.setAttribute("value", parseInt(token));
                        $('body').removeClass("loading");

						document.getElementById("card_form").submit();
						});
					}
					})
				}
				myEvent.stopWatching();
			}
			else
			{
				console.error(error);
				$('body').removeClass("loading");
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
		$('[name="_save"]').hide();

		addNewCard(cardName, id);
	}
});
