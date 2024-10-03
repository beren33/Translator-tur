meme_dict = {
    "LOL": "Komik bir şeye verilen cevap",
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Sinirlenmek",
    "Prefer": "Tercih etmek",
    "TEMPLE": "Tapınak",
    "MAZE RUNNER": "ÖLÜMCÜL KAÇIŞ",
    "CREATURE": "Yaratık",
    "TREASURE": "Hazine",
}

while True:
    words = list(meme_dict.keys())[:12] 
    print("Aşağıdaki kelimelerden birinin anlamını isteyin:")
    for word in words:
        print("-", word)
    
    user_input = input("Bir kelime yazın veya çıkmak için 'exit' yazın: ").strip().upper()
    
    if user_input == 'EXIT':
        print("Programdan çıkılıyor")
        break
    elif user_input in meme_dict:
        print(meme_dict[user_input])
    else:
        print(" Lütfen listedeki kelimelerden birini girin.")
