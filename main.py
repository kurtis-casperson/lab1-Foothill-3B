import random

name = 'Kurtis Casperson'
student_id = 20629537
email = 'kcasperson7@gmail.com'
class_policies = ['Participation is required', 'Late work is 15% penalty', 
                  'Email instructor for help with name and class in subject line']
print(name)
print(student_id)
print(email)
print(class_policies)


class Card:
  """
  This class contains the suit and value lists as initializers.
  
  """
  def __init__(self):
    self.values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen','King']
    self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  


class Deck:
  """
  This class takes the values from Card class and creates a dictionary (deck of cards).
  Create a method that takes the cards and reorders randomly, 
  a new list is created and the card that was dealt is removed from the deck.
  """
  def __init__(self):
    card_instance = Card()
    self.card_values = card_instance.values
    self.card_suits = card_instance.suits

    
    self.card_dictionary = {value: self.card_suits for value in self.card_values}

  def shuffle(self):
    dict_to_list = list(self.card_dictionary.items())
    number_of_cards = len(dict_to_list) * 4
    if number_of_cards != 52:
        return 'The deck has an incorrect amount of cards' 
    random.shuffle(dict_to_list)
    print(dict_to_list)
    return dict_to_list


  def deal_card(self):
    """
    This method takes the card data and removes the card from the deck.
    """
    dict_to_list = list(self.card_dictionary.items())
    random_card = random.choice(dict_to_list) 
    random_suit = random.choice(random_card[1])
    dealt_card = random_card[0] + ' of ' + random_suit
    random_card[1].remove(random_suit)
    print(random_card)
    print(dealt_card)
    

result = Deck()
# result.shuffle()

result.deal_card()