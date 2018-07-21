// Trigger this function when user wants to buy a card
// @param tokenID: integer: unique ID of the card
// @param price: integer: selling price of the card to be bought
function buyCard(tokenID, price)
{
    console.log("LDJkhfksjhd");
	var myEvent = cryptoCricketInstance.LogSnatch({},{fromBlock: web3.eth.getBlockNumber(function(error, result){ console.log(result)}), toBlock: 'latest'});

	cryptoCricketInstance.purchase(tokenID, {value: web3.toWei(price, "ether")}, function(error,result)
	{
		if(error)
		console.error(error);
		else
		{
			myEvent.watch(function(error, result)
			{
				console.log("Bought Card Successfully");
				console.log(JSON.stringify(result.args.tokenId));
				console.log(JSON.stringify(result.args.tokenName));
				console.log(JSON.stringify(result.args.oldOwner));
				console.log(JSON.stringify(result.args.newOwner));
				console.log(JSON.stringify(result.args.oldPrice));
				console.log(JSON.stringify(result.args.newPrice));
			});
		}
	})
	myEvent.stopWatching();
}