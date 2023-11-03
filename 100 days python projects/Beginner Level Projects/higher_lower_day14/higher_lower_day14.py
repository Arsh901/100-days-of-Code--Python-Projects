import art, game_data, random
print(art.logo) 
sc = 0
def process(scr):
    a = random.choice(game_data.data)
    b = random.choice(game_data.data)
    if a!=b:
        print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}.")
        print(art.vs) 
        print(f"\nCompare B: {b['name']}, a {b['description']} from {b['country']}.")
        highest_count = max(a['follower_count'], b['follower_count'])
        correct_guess = True
        while correct_guess:
            resp = input("Who has more followers? Type 'A' or 'B': ")
            if resp=="A":
                if highest_count == a['follower_count']:
                    scr +=1
                    print(f"You are right! Current score: {scr}")
                    print("---------------------------------------\n")
                    process(scr)
                    break
                else:
                    print("---------------------------------------------\n")
                    print(f"***Sorry, that's wrong, final score: {scr}***")
                    print("---------------------------------------------\n")
                    correct_guess = False
                    
            else:
                if highest_count == b['follower_count']:
                    scr +=1
                    print(f"You are right! Current score: {scr}")
                    print("---------------------------------------\n")
                    process(scr)
                    break
                else:
                    print("---------------------------------------\n")
                    print(f"***Sorry, that's wrong, final score: {scr}***")
                    print("---------------------------------------\n")
                    correct_guess = False
                    
    else:
        process(scr)

process(sc)