# start_dic={"a":10,"b":20}
# start_dic["c"]=7
# start_dic["d"]=[1,2,3]
# print(start_dic)
# for key in start_dic:
#     start_dic[key]+=1
#     print(start_dic)
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 4: ["Steak","hello"]},
    "dessert": {1: ["Ice Cream"], 2: []},

}
print(order["main"][4][1])