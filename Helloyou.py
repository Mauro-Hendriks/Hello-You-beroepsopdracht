import os


def a1():
  print("Je bent nu veilig in Iran waar je leven weer op bauw en je 4 dochters en 1 zoon krijgt")
  print("Het is nu 2015 je gaat dood door dat je te oud werd door dat je nu dood bent gaat je dochter Sara van 15 jaar werken maar Sara kan zich niet tot standhouden en het is gevaarlijk zonder man in huis en dus als Sara 18 is vluchten gaan jullie vluchten naar Turkije")
  print("Je komt aan bij de grens van Turkije en je krijgt te horen dat UNHCR met de registratie van vluchtelingen is ge stop en dat je naar de overheid moet voor onderdak")
  print("Wat ga je nu doen")
  print("A=Ga je naar de overheid B=Ga je vluchten naar Lesbos  C=Ga je gaat Turkije in zonder onder dak  (a, b of c)")
   
  answer = input(">").lower()

  if "a" in answer:
    q2
    os.system('cls')


  elif "b" in answer:
    q2
    os.system('cls')


  elif "c" in answer:
    q1
    os.system('cls')
    
def q1():
  print("Het is 1971 je wil met je vrouw vluchten naar Iran wat ga je doen")
  print("A=Met de auto over de a1  B=Door de bergen C=Via de rivier (a, b of c)")
   
  answer = input(">").lower()

  if "a" in answer:
   a1()
   os.system('cls')  

  elif "b" in answer:
   a1()
   os.system('cls')

  elif "c" in answer:
    print("je probeert met een kano de rivier over te steken maar je kapzed en besluit terug te gaan ")
    q1()
    os.system('cls')

def q2():
    print("Het is nu 2015 je gaat dood door dat je te oud werd door dat je nu dood bent gaat je dochter Sara van 15 jaar werken maar Sara kan zich niet tot standhouden en het is gevaarlijk zonder man in huis en dus als Sara 18 is vluchten gaan jullie vluchten naar Turkije") 

def q3():
    print("Je komt aan bij de grens van Turkije en je krijgt te horen dat UNHCR met de registratie van vluchtelingen is ge stop en dat je naar de overheid moet voor onderdak ")
    print("Wat ga je nu doen")
    print("A=Ga je naar de overheid B=Ga je vluchten naar Lesbos C=Ga je gaat Turkije in zonder onder dak (a, b of c)")
    answer = input(">").lower()

    if "a" in answer:
      a3
      os.system('cls')


    elif "b" in answer:
      q4
      os.system('cls')


    elif "c" in answer:
      c3
      os.system('cls')

def a3():
  print("Je komt aan bij de overheid om asiel te zoeken maar je krijgt geen kans om een asielaanvraag te doen dus doe je het een paar dagen later nog een keer en gebeurt hetzelfde dit doe je voor twee weken zonder dat je onder dak hebt en dus besluit je na twee weken naar Europa te vluchten")

def c3():
  print("je trekt alsnog Turkije in zonder dat je een plan hebt om iets te doen")  

def q7():
  print("Wat is nu het belangrijkste om te doen")
  print("A=Een huis zoeken B=Werk zoeken C=Rondvragen of mensen willen helpen")
  answer = input(">").lower()

  if "a" in answer:
    a7
    play_again


  elif "b" in answer:
    b7
    play_again


  elif "c" in answer:
    q4
    os.system('cls')

def a7():
  print ("je gaat naar huurhuizen zoeken maar omdat je geen geld hebt kan je niks huren en kan niet veder")

def b7():
  print ("je gaat werk zoeken en je gaat werken bij een fabriek nu je geld hebt ga je zoeken naar een huis en dat lukt en dus blijf je maar in Turkije leven ")

def c7():
  print ("om dat je niet goed met de mensen rond je kan communiceren besluit je alsnog terug te gaan")

def q4():
  print("Je bent nu op weg naar Lesbos zodra je daar aan komt zie je veel bossen en een prachtige zee van de overheid moet je naar het kamp moria wat wordt om schreven als de hel. Als je daar aan komt krijg je een tent en moet je maar een plek zoeken. ")
  print("Zes maanden later hebben je moeder en je zus gezondheidsproblemen en krijg je een huis twee maanden later moet je van de overheid verhuizen naar Athene maar als je daar aan komt heeft de buurt het huis gebarricadeerd en de politie wil ook niet helpen dus ga je maar terug naar camp moria en daar krijg je te horen dat we in Athene hadden moeten blijven. Nu is het je eigen verantwoordelijkheid. Zegt de overheid.")
  print("Wat ga je nu toch doen")
  print("A=Vrienden vragen voor onderdak B=blijven op Athene C=Terug naar Syrië ")

  answer = input(">").lower()

  if "a" in answer:
    a4
    os.system('cls')


  elif "b" in answer:
    b4
    play_again


  elif "c" in answer:
    c4
    os.system('cls')

def a4():
  print("e vraag of je vrienden je kunnen helpen zoeken naar onderdak op Lesbos en dat lukt maar om de huur te betalen ga je werken als naaister bij een ngo")

def b4():
  print("je blijft op Athene en bauwt je leven weer op en je blijft op Athene want alles is nu toch niet zo slecht ")

def c4():
  print("je besluit om op te geven en terug naar Syrië te gaan")

def q8():
  print("Drie maanden later besluit je alsnog te vluchten en ga je weer naar de overheid")

def q5():
  print("Na drie maanden krijg je te horen dat je weer terug moet naar Athene om dat jullie asieldossier daar wordt behandeld. Een maal in Athenea moet je weer op zoek naar onderdak en werk en dus ga je voorlopig logeren bij een vriend. Na een maand heb je nog steeds niks gehord over een uitnodiging over onze asielaanvraag")
  print("Ga je nu naar de overheid of wacht je het gewoon af ")
  print("A=Naar de overheid  B=Gewoon wachten ")
  answer = input(">").lower()

  if "a" in answer:
    a5
    os.system('cls')


  elif "b" in answer:
    b5
    os.system('cls')
    

def a5():
  print("je gaat naar de overheid en vraag waarom je nog niks hebt gehoord over je asielaanzoek en er wordt gezegd dat ze ernaar gaan kijken")

def b5():
  print("het is nu vier jaar later en je zit nog steeds vast op Athenea. Mensen zeggen dat we gewoon moeten afwachten, maar het maakt me zo moe en gefrustreerd. Ik weet nog steeds niet hoe ik mijn toekomst vorm kan geven. Zal ik een opleiding kunnen doen? ")
  play_again

def q6():
  print("Drie maanden later word je gebeld en je moet alles in pakken want je krijgt asiel in Nederland")
  print("2 jaar later je bent nu al een tijdje in Nederland en je hebt werk gevonden en je doet ook nog eens een opleiding dus de toekomst ziet er goed uit ")
  play_again

def play_again():
  answe = input("Again? y or n: ") 

  if answe == "y":
     print ("ok")
     q1


q1()