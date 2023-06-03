# Wardrobify

Team:

* Jason - Shoes
* David - Hats

## Design

## Shoes microservice

The shoe microservice contains the Shoe and BinVo models. The Bin polling function retrieves data from the wardrobe monolith and passes it to BinVo. The microservice also has RESTful APIs for listing, deleting, and creating shoes. Front-end states are connected to URLs for communication between services. This enables the activation of the delete button and the display of product details in the shoe list.

## Hats microservice

I created a Hat and Location model that handles "GET", "POST", "DELETE", "CREATE", and "PUT" functionalities in the wardrobe API through insomnia.
