# CryptoCricket

A collectible card trading game based on the ethereum blockchain.

## Getting Started

Link to the website: [http://cricket4crypto.com](http://cricket4crypto.com)

### Prerequisites

- Metamask Browser Extension \- [website](https://metamask.io/)
  - for [Chrome](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn?hl=en)
  - [Installation Guide](https://medium.com/@mail.bahurudeen/setup-a-metamask-ethereum-wallet-and-use-it-to-send-and-receive-ether-4f3b99360e4f)

## How to Buy a Card
* Go to the URL: http://cricket4crypto.com, and login/register with your ETH wallet address.
* Choose your favourite player, check it's price, and click on `Buy Now`.
* In the metamask notification that pops us, set an appropriate gas price and `Accept` the transaction.
* As soon as the transaction is mined and included in a block, the page will automatically reload.
* Congratulations! You are now the proud owner of your favourite card.
  
## How to make Changes to Cards

### Add Card
* Go to the URL: http://cricket4crypto.com/admin, and login using the admin credentials.
* Click on `Cards` under the `Website` Category.
* Click on `ADD CARD` on thhe top right of the page.
* Select the `Card Type`, enter the details required and click on `SAVE` on the bottom right of the page.
* In the metamask notification that pops us, set an appropriate gas price and `Accept` the transaction.
* As soon as the transaction is mined and included in a block, the page will automatically reload.
* Congratulations! You have successfully created a new card.


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

### Edit DB Structure

* Clone the Repository and move to the `CryptoCricket/website` directory.
* Open the `models.py` file.
* To Change:
  * User Profile: Scroll to the `Profile` Class
  * Card: Scroll to the `Card` Class.
* Add/Edit the fields required (according to the documentation: https://docs.djangoproject.com/en/2.1/topics/db/models/), under the corresponding class.
* Open a terminal in the main Directory (inside `CryptoCricket` folder)
* Enter the following commands:
  ```
  python manage.py makemigrations website
  python manage.py migrate
  ```
