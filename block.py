Enemies="Skelton"
def skel():
    enemies="Zombie"
    print(enemies)
    print(Enemies)
skel()
print(Enemies)    
# --------------------------------------------------------------------------------------------------------
entry=1
def ent():
    # global is the keyword we can use for global variable which we want to change
    global entry
    entry+=1
    print(entry)
    # other methof instaed of changing the global variable use return statement
    return entry+1
entry=ent()
print(entry)
