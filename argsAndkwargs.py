# With args and kwargs we can continue adding items
try:
    def players(intro,*args,**kwargs):
        print(intro)
        for items in args:
            print(items)
        print("\nNow i will tell you roles of players:\n")
        for key,values in kwargs.items():

            print(f"{key} is a {values}")

    heading="Pakistan Cricket Players:"
    players_list =["Babar","Rizwan","Shaheen"]
    players_roles={"Babar":"Batsmen","Rizwan":"Wicketkeeper","Shaheen":"Fast Bowler"}
    players(heading,*players_list,**players_roles)

except Exception as e:
    print(e)






