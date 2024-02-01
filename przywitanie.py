imie = input("Jak masz na imię? ")
print(f"Witaj, {imie}!")

samopoczucie = input("Jak się dzisiaj czujesz? (wspaniale/dobrze/może być/źle/tragicznie): ")

if samopoczucie.lower() == "wspaniale":
    print("To wspaniale! Ciesz się dniem!")
elif samopoczucie.lower() == "dobrze":
    print("Dobrze słyszeć, że jest dobrze. Trzymaj tak dalej!")
elif samopoczucie.lower() == "może być":
    print("Pamiętaj, każdy dzień to nowa szansa. Jutro może być lepsze!")
elif samopoczucie.lower() == "źle":
    print("Przykro mi, że tak się czujesz. Pamiętaj, że to tylko chwilowe. Wszystko będzie dobrze.")
elif samopoczucie.lower() == "tragicznie":
    print("Wygląda na to, że masz naprawdę ciężki dzień. Pamiętaj, że jesteś silny i poradzisz sobie z tym. Może warto porozmawiać z kimś, kto Cię wesprze?")
else:
    print("Nie rozpoznaję tego stanu samopoczucia. Czy wszystko jest w porządku?")
