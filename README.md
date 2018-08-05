# CryptoCricket

A collectible card trading game based on the ethereum blockchain.

## Getting Started

Link to the website: [yashitm.pythonanywhere.com](yashitm.pythonanywhere.com)

### Prerequisites

- Metamask Browser Extension \- [website](https://metamask.io/)
  - for [Chrome](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn?hl=en)
  - [Installation Guide](https://medium.com/@mail.bahurudeen/setup-a-metamask-ethereum-wallet-and-use-it-to-send-and-receive-ether-4f3b99360e4f)
  
  
## How to make Changes to Cards

### Add Card
* Go to the URL: http://cricket4crypto.com/admin, and login using Username:`admin` Password:`hello123`
* Click on `Cards` under the `Website` Category.
* Click on `ADD CARD` on thhe top right of the page.
* Select the `Card Type`, enter the details required and click on `SAVE` on the bottom right of the page.

### Edit Card
* Go to the URL: http://cricket4crypto.com/admin, and login using Username:`admin` Password:`hello123`
* Click on `Cards` under the `Website` Category.
* Select the Card you wish to edit from the list of Cards.
* Once done updating the details, click on the `SAVE` button on the bottom right of the page.

## DB Structure

|  Card 	| User  	|
|---	|---	|
|  id	|  id 	|
|  card_type 	|  password 	|
|   name	|  last_login 	|
|   description	|  is_superuser 	|
|   transactions	|  username 	|
|   owner	|  first_name 	|
|   last_bid	|  email 	|
|   eth_id	|  is_staff 	|
|   image	|   is_active	|
|   icc_ranking	|   date_joined	|
|   country	|   last_name	|
|   	|  eth_address 	|
|   	|  transactions 	|
