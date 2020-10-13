
def load_profile():
    with open("profile.txt","r") as f:
        start = int(f.readline())
        end = int(f.readline())
        w = f.readline().strip("\n").strip("[").strip("]").split(",")
    f.close()
    return start,end,w
print(load_profile())