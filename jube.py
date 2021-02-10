poli=[{'viewCount': '8185', 'likeCount': '179', 'dislikeCount': '30', 'favoriteCount': '0', 'commentCount': '54'},
{'viewCount': '129372', 'likeCount': '905', 'dislikeCount': '22', 'favoriteCount': '0', 'commentCount': '228'},
{'viewCount': '1461516', 'likeCount': '36386', 'dislikeCount': '890', 'favoriteCount': '0', 'commentCount': '1319'},
{'viewCount': '63635', 'likeCount': '636', 'dislikeCount': '7', 'favoriteCount': '0', 'commentCount': '58'},
{'viewCount': '0', 'likeCount': '0', 'dislikeCount': '0', 'favoriteCount': '0', 'commentCount': '0'},
{'favoriteCount': '0', 'commentCount': '1152'}]
for i in range(len(poli)):
    b=poli[i].get("viewCount","pan") or "pan"
    print(b)