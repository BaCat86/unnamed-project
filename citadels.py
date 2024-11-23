import random
quarter_num = 68 # number of quarter maps / колличество карт кварталов
character_num = 8 # number of character cards / колличество карт персонажей
hand = [] # What the players have in their hands / То, что есть на руках у игроков
quarters_cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13','15', '16', '17', '18', '19', '20'] # quarter cards / карты кварталов
characters_cards = ["Assassin", "Thief", "Magician", "Bishop", "Merchant", "Architect", "Condottiere", "King"] # character cards / карты персонажей
player_num = int(input("Enter the number of players: ")) # number of players (from four to seven) / колличество игроков (от четырёх до семи)
open_characters_cards = []
close_characters_cards = []
def game_preparing(): # preparing for the game / подготовка к игре
    for i in range(player_num):
        player_hand = [] # What is in the player's hand / То, что в руке у игрока
        for _ in range(4): # Repeat four times, as you need to give out four cards / Повторение четыре раза, так как надо выдать четыре карты
            x = random.choice(quarters_cards) # Choosing a random quarter card / Выбор случайной карты квартала
            player_hand.append(x) # Adding a card to a player's hand / Добавление карты в руку игрока
            quarters_cards.remove(x) # Removing a card from the deck / Удаление карты из колоды
        hand.append([player_hand, 2]) # Adding to the general list / Добавляем в общий список


def open_char():
    x = random.randint(0, len(open_characters_cards) - 1)
    open_characters_cards.append(characters_cards[x])
    characters_cards.remove(characters_cards[x])


def character_selection():
    if player_num <= 5: # Yes, this is a terrible shitcode, we need to fix it / Да, это ужасный говнокод, надо исправить
        if player_num == 5:
            open_char()
        elif player_num == 4:
            open_char()
            open_char()
    x = random.randint(0, len(open_characters_cards) - 1)
    close_characters_cards.append(characters_cards[x])
    characters_cards.remove(characters_cards[x])
    print("Open cards: ", open_characters_cards)
    print("The owner of the crown") # (Перевод: Владелец короны)
    print("Select a card: ", characters_cards)
game_preparing()
print(hand)
