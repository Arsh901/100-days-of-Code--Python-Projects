
play_again = True
while play_again == True:
    begin = input("Do you want to play a game of blackjack? Type 'y' or 'n':")
    if begin=="y":
        logo = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """
        print(logo)
        import random 
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        my_cards = []
        comp_cards = []
        for i in range(0,2):
            my_cards.append(random.choice(cards))
        comp_cards.append(random.choice(cards))
        
        print(f"Your cards: {my_cards}, current score: {sum(my_cards)}")
        print(f"Computer first card: {comp_cards[0]}")
        
        def run():
            res = input("Type 'y' to get another card, type 'n' to pass:")
            if res == "y":
                my_cards.append(random.choice(cards))
                print(f"Your final hand: {my_cards}, final score: {sum(my_cards)}")
                print(f"Computer's first hand: {comp_cards}, final score: {sum(comp_cards)}")
                if sum(my_cards)>21:
                    print("You went over. You lose 😭")
                elif sum(my_cards)==21:
                    print("You win with a blackjack 😎")
                else:
                    run()
            if res == "n":
                com()
                
        def com():
            comp_cards.append(random.choice(cards))
            print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
            if sum(comp_cards)>21:
               print("Opponent score exceeded 21. You win 😎")
            elif sum(comp_cards)== 21:
               print("Blackjack for computer. You loose. 😭")
            else:
                if sum(comp_cards)>sum(my_cards):
                    print("Oppenent's scores more than you. You loose 😭")
                elif sum(comp_cards)==sum(my_cards):
                    print("Bust 🙃")
                else:
                    com()
               
        if sum(my_cards)==21:
            print("Win with a blackjack. 😎")
        else:
            run()
    else:
        play_again = False
        
        

    