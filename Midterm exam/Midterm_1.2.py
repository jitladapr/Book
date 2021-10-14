Text = "ghhfhfdjdu"
Given = "hhfhf"

for x in range(len(Text)):
        Given_Text = Text[x:x+5]
        print(Given_Text)
        if Given in Given_Text:
           print("1")
           break
        else:
             print("-1")