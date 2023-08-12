meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL":"bir şakaya karşılık cevap","SHEES":"onaylamak",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Sözlüğümüz yazdığınız kelimeyi içermiyor lütfen başka bir araç kullanın")
