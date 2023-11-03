d = {} 
more_bidder = True
while more_bidder == True:
    i = input("What is your name?\n")
    d[i] = int(input("What's your bid: $"))
    a = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if a.lower() == "yes":
        more_bidder = True
    if a.lower() == "no":
        more_bidder = False 
l = []
for key in d:
    l.append(d[key])
    max_bid = max(l)
def same_bid(name1,name2):
  print(name1,"and",name2, "have made the same bid. You are requested to bid again.")
  bid_i = int(input("Dear "+name1+", please enter your bid.\n"))
  bid_j = int(input("Dear "+name2+", please enter your bid.\n"))
  if bid_i>bid_j:
    print("The winner is",name1,"with a bid of $"+str(bid_i))
  elif bid_i ==bid_j:
    same_bid()
  else:
    print("The winner is",name2,"with a bid of $"+str(bid_j))
    
if d[i] == max_bid:
  for j in d:
    if d[j] == d[i]:
      same_bid(i,j)
    else:
      print("The winner is",i,"with a bid of $"+str(max_bid))