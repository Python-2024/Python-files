a = 0
def accelerationn():
    global a
    print("Note: v and u should be in m/s and t should be in sec.\n")
    a = input("a -> ")
    v = input("v -> ")
    u = input("u -> ")
    t = input("t -> ")

    if a == "not given":
        a= (float(v)-float(u))/float(t)
        print(f"Acceleration Will Be {a} m/s^2")
    if v == "not given":
        v = float(u) + float(a)*float(t)
        print(f"Final velocity of the object is {v}")
    elif u == "not given":
        u = float(v) - float(a)*float(t)
        print(f"Initial Velocity of the object is {u}")
accelerationn()