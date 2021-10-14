Text = "dgdhjdghdf"
Given = "fgh"

for x in range(len(Text)):
        Given_Text = Text[x:x+3]
        print(Given_Text)
        if Given in Given_Text :
                print("1")
                break
        else:
                print("-1")