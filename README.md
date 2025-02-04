# Supermarket Basket Pricing Calculator

This project is for a coding exercise which asks to model a supermarket pricing calculator.
Given a shopping basket it will calculate the total price of the basket including any potential savings.

The basis are that each item in the shop has an item code which the price and any potential sales are connected to.
The shopping basket is represented using a list where each item bought is represented by its item code.
For example, the example given in the coding exerise is represented by *[1,1,1,2,2,(3,0.2)]*.
Here the first 3x *1* are the beans, the 2x *2* are the Cokes, and *(3,0.2)* are the oranges.

Currently there are two types of pricing options: price per item or price per kg.
There are three types of sales;

1) Percentage discount per item
2) Buy X items from a list of items for the price of Y of those items
3) Buy X items from a list of items for set price

Additional way os pricing and sales can be implemented as long as the chosen structure does not interfere with the already existing ones. Much of the existing code can be re-used when calculating different types of savings.

## Assumptions

- Only one type of sale is applied to each item
- The sales always applies to the cheapest items in the list
- Final sub-total, savings, and total are rounded to 2 decimal places rather than the contribution from each item
- Different dictionaries have been implemented for prices and savings as items with different types of pricing can be included in the same offer (for example, the beans prices per item and the oranges priced per kg.)

## Notes

- The *items* dictionary is kept as to allow for the implementation of printing a receipt using the list of items.
- It would be beneficial to include more unittests, testing for each possible combination of types of sales.