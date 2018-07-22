// Trigger this function when user wants to buy a card
// @param tokenID: integer: unique ID of the card
// @param price: integer: selling price of the card to be bought
// @param walletAddress: string: ethereum wallet address of user
function buyCard(tokenID, price, walletAddress)
{
	var currentAcc = "";
	var storedAcc = walletAddress.toLowerCase();
	web3.eth.getCoinbase(function(err,account)
	{
		if(err === null)
		{
            $('body').addClass("loading");
            currentAcc = account;

			var myEvent = cryptoCricketInstance.LogSnatch({},{fromBlock: web3.eth.getBlockNumber(function(error, result){ console.log(result)}), toBlock: 'latest'});
            if(currentAcc !== storedAcc)
			{
                $('body').removeClass("loading");
                $("[id*='metamask_downloaded_modal']").modal("hide");

				alert("Please Use Wallet: " + walletAddress + " to make the transaction");
                return;
            }


			cryptoCricketInstance.purchase(tokenID, {value: web3.toWei(price, "ether")}, function(error,result)
			{
				if(error)
					console.error(error);
				else
				{
					myEvent.watch(function(error, result)
					{
						$('body').removeClass("loading");
						$("[id*='metamask_downloaded_modal']").modal("hide");
						
						console.log("Bought Card Successfully");
						console.log(JSON.stringify(result.args.tokenId));
						console.log(JSON.stringify(result.args.tokenName));
						console.log(JSON.stringify(result.args.oldOwner));
						console.log(JSON.stringify(result.args.newOwner));
						console.log(JSON.stringify(result.args.oldPrice));
						console.log(JSON.stringify(result.args.newPrice));
					});
				}
			});
			myEvent.stopWatching();
		}
		else
		{
			console.log(err);
		}
	});
	return;
}