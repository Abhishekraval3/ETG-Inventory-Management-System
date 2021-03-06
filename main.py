
# Creating a dictionary for the list of items.
Inventory = {1001 : {"Product_num": 1,"Name":"Long grain basmati rice","Description" :"Basmati Rice has been an integral part of different rice recipes in every Indian household.","Price" :60},
             1002 : {"Product_num": 2 ,"Name" :"Biryani Rice","Description" :"It is highly nutritious as this rice is processed under the supervision of experts.","Price" :85},
             1003 : {"Product_num": 3 ,"Name" :"Sona masuri rice","Description" :"Sona Masuri Rice is a medium grained rice with premium quality." ,"Price" :50},
             1004 : {"Product_num": 4 ,"Name" :"Idli rice","Description" :"Idli Rice is famous in the southern regions of India." ,"Price" :72},
             1005 : {"Product_num": 5 ,"Name" :"Wheat flour/chakki aata","Description" :"The taste and nutrition ensure that this atta contains 0% Maida." ,"Price" :25},
             1006 : {"Product_num": 6 ,"Name" :"Besan/chickpeas flour","Description" :"It is made by grinding Chickpea Flour and serves as an excellent source of important nutrients and fibers.","Price" :40},
             1007 : {"Product_num": 7 ,"Name" :"Moong dal flour","Description" :"This flour is not only tasty but rich in nutrients as well." ,"Price" :64},
             1008 : {"Product_num": 8 ,"Name" :"Ragi flour","Description" :"Ragi is a good source of complex carbohydrates, a fair source of protein & fiber and very low in fat which contributes towards fullness and achieving ideal body weight.","Price" :70},
             1009 : {"Product_num": 9 ,"Name" :"Maida","Description" :"It is a self-rising flour and is suited for making cakes, pastries and other baking food items. ","Price" :30},
             1010 : {"Product_num" :10 ,"Name" :"Millet flour","Description" :"This flour can be used as a healthier alternative to wheat flour because it's not only tasty but rich in nutrients. ","Price" :33},
             1011 : {"Product_num" :11 ,"Name" :"Maize flour/makki aata","Description" :"Maize flour is derived from ground and desiccated seeds of maize plant. ","Price" :61},
             1012 : {"Product_num" :12 ,"Name" :"Toor Dal","Description" :"Tur / Arhar Dal, also called pigeon peas, are used to prepare the most common dishes in homes on a daily basis.","Price" :100},
             1013 : {"Product_num" :13 ,"Name" :"Bengal gram dal","Description" :"Roasted Chana Dal / Split Bengal Gram is a mild-tasting bean which is generally used in curries and to make besan flour.","Price" :59},
             1014 : {"Product_num" :14 ,"Name" :"Green Gram Dal","Description" :"The moong is easy to digest, has a pleasant sugary flavour and feels soft. The beans are best consumed after being sprouted since the sprouts are rich in vitamin C.","Price" :76},
             1015 : {"Product_num" :15 ,"Name" :"Whole Black gram dal ","Description" :"Urad Dal is one of the richest sources of Protein and Vitamin B. Urad dal is also good for women as it has Iron, Folic Acid, Calcium, Magnesium, Potassium,etc.","Price" :80},
             1016 : {"Product_num" :16 ,"Name" :"Kidney beans","Description" :"Best Farms Red Rajma has a higher nutritional value than conventional food as it is rich in Vitamins and Minerals.","Price" :63},
             1017 : {"Product_num" :17 ,"Name" :"Brown chickpeas","Description" :"It has constituted an important part of Indian cuisine. It can fulfil the nutritional and dietary requirements of an entire meal.","Price" :97},
             1018 : {"Product_num" :18 ,"Name" :"Whole Pink lentils","Description" :"It is then air packed in a way that it provides optimal freshness when opened.","Price" :90},
             1019 : {"Product_num" :19 ,"Name" :"Coriander seeds","Description" :"They can be used in whole or ground form to add flavour, aroma and texture to delicacies.","Price" :98},
             1020 : {"Product_num" :20 ,"Name" :"Mustard seeds","Description" :"hey are commonly used in pickling, sausage-making and tempering vegetable dishes. Use Shree Rai to give your dish a spicy touch and appealing texture. Buy this product online today Benefits.","Price" :39},
             1021 : {"Product_num" :21 ,"Name" :"Fenugreek Seeds","Description" :"They are commonly used in pickling, sausage-making and tempering vegetable dishes. Use Shree Rai to give your dish a spicy touch and appealing texture. Buy this product online today.","Price" :88},
             1022 : {"Product_num" :22 ,"Name" :"cumin seed","Description" :"Along with stemless chilli, mustard seeds, and onions, it is used to saute and temper dal and vegetable curries. ","Price" :47},
             1023 : {"Product_num" :23 ,"Name" :"Kashmiri red chilli","Description" :"Guntur Chilly is named after its origin in the Guntur district of Andhra Pradesh.","Price" :20},
             1024 : {"Product_num" :24 ,"Name" :"Tamarind","Description" :"Popularly known as Imli or Date of India Tamarind is a tangy, sweet-sour tasting fruit that is grown mostly in India, Pakistan and other tropical regions","Price" :30},
             1025 : {"Product_num" :25 ,"Name" :"salt","Description" :"Salt is one of the most important ingredients used in Indian households. It has a plethora of health benefits and it is a great addition to your diet for maintaining a healthy lifestyle. ","Price" :20},
             1026 : {"Product_num" :26 ,"Name" :"Turmeric Powder","Description" :"It has antiseptic qualities as well as properties of flavouring agent and is also a natural beauty aid. It gives musky flavour and yellow colour to curries.","Price" :180},
             1027 : {"Product_num" :27 ,"Name" :"Cardamom 50 gram","Description" :"Elaichi (Cardamom) is also known as the 'Queen of Spices'. Best Farms Green Cardamom lends a distinct smoky flavour and strong aroma when added to dishes.","Price" :33},
             1028 : {"Product_num" :28 ,"Name" :"Cinnamon 50 gram","Description" :"Cinnamon or Dalchini is one of the oldest spices known to mankind. It adds a slightly warm and spicy touch to every dish.","Price" :46},
             1029 : {"Product_num" :29 ,"Name" :"bay leaves 50 gram","Description" :"Tej Patta (Indian Bay Leaf) are olive coloured leaves that are prized for their unique fragrance. They are used as a condiment in Biryani and Kormas.","Price" :17},
             1030 : {"Product_num" :30 ,"Name" :"Cloves 25 gram","Description" :"Cloves are tiny flower buds that have a spicy and pungent taste." ,"Price" :20}}

#Displaying the Items list
print("Product_num | Product_Name | Price")
for items in Inventory:
    print(Inventory[items]['Product_num'] ,":" ,Inventory[items]['Name'],  "-->" ,Inventory[items]['Price'],"--",Inventory[items]['Description'])


# Taking Input for the User
print("Enter n if you want to stop shopping")
Pro_num = 2
qua = 2
Pur_no = []
Pur_qua = []
while Pro_num > 1 or qua > 1:
    Pro_num = int(input("Enter the product number you want to buy:"))
    qua = float(input("Enter the Quantity in Kg/packets:"))
    if (Pro_num >= 1 and Pro_num <= 30 ):
        if (qua >= 1 ):
            Pur_qua.append(qua)
            Pur_no.append(Pro_num)
        else:
            print("Please enter the valid quantity")
    else:
        print("Please enter the valid number")

# Converting the Product number into keys in dictionary
k = 1000
res = [x + k for x in Pur_no]

#Creating Bill for the user
print("Elite Techno Group")
print("*************Bill*************")
print("  Product Name  ------ Amount")
list = []
total = 0
for i in res:
    j = 0
    a = Pur_qua[j]
    j = j + 1
    price = Inventory[i]['Price'] * a
    list.append(price)
    print(Inventory[i]['Name'],":",price)
for ele in range(0, len(list)):
    total = total + list[ele]
print("Total Price =", total)
print("Thanks for Shopping with Us")

# Creating a Sales Dictionary
sales = {}
for i in res:
    Pro_number = Inventory[i]['Product_num']
    Pro_name = Inventory[i]['Name']
    for a in Pur_qua:
        dict = {Pro_number:[Pro_name,a]}
        sales.update(dict)

import json

#Creating a Json file for Inventory
js = json.dumps(Inventory)
fd = open("Inventory.json", 'w')
fd.write(js)
fd.close()

#creating a Json file for Sales
sl = json.dumps(sales)
sale = open("sales.json", 'w')
sale.write(sl)
sale.close()