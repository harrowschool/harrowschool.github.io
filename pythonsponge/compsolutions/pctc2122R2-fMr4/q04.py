while (txt := input()) != "goodbye":
    if txt[-1] == "?" or txt.split(" ")[0] in ["how", "what", "why", "who", "when", "where"]:
        print("not sure really")
    else:
        print("but why?")

print("see you!")