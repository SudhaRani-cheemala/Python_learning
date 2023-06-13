row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Enter matrix")
horizontal=int(position[0])
vertical=int(position[1])
# print(map[vertical-1])
# print(map[horizontal-1])
sel_row=map[horizontal-1]
sel_row[vertical-1]="*"
print(f"{row1}\n{row2}\n{row3}")
