import requests
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Kalkulator Vat", layout="centered")


parametry = {"amount": 1, "from": "JPY", "to": "PLN"}

jeny = requests.get("https://api.frankfurter.app/latest", params=parametry)
odczytanajpy = jeny.json()
jen=odczytanajpy["rates"]["PLN"]

parametryeuro = {"amount": 150, "from": "EUR", "to": "PLN"}

euro = requests.get("https://api.frankfurter.app/latest", params=parametryeuro)
odczytanaeur = euro.json()
czyclo=odczytanaeur["rates"]["PLN"]


def przelicz1():
    global kwota
    global kwotavat
    global clo
    
    kwota = round(wprowadz, 2)
    kwotavat = round((kwota * 23) /100, 2)


    if kwota == 0:
        tekst1 = st.write(f"""Nie podałeś kwoty.""")
    elif kwota >= czyclo:
        tekst1 = st.write(f"Kwota twojego zamówienia to {kwota} zł. \n Zapłacisz {kwotavat} zł podatku VAT + 8,50 zł opłaty pocztowej (´⊙ω⊙`)！")
        tekst2 = st.write(f"""Kwota zamówienia przekracza 150 EUR ({czyclo} zł).\n Możliwe oclenie paczki ಥ‿ಥ""")
        clo = "Tak"
    else:
        tekst1 = st.write(f"Kwota twojego zamówienia to {kwota} zł. \n Zapłacisz {kwotavat} zł podatku VAT + 8,50 zł opłaty pocztowej (´⊙ω⊙`)！")
        tekst2 = st.write(f"Kwota zamówienia nie przekracza 150 EUR ({czyclo} zł). \n Nie musisz płacić cła ٩(•̤̀ᵕ•̤́๑)ᵒᵏᵎᵎᵎᵎ")
        clo = "Nie"

def przelicz2():
    global kwota
    global kwotavat
    global clo
    
    kwota = round(wprowadz*jen, 2)
    kwotavat = round((kwota * 23) /100, 2)

    if kwota == 0:
        tekst1 = st.write(f"""Nie podałeś kwoty.""")
    elif kwota >= czyclo:
        tekst1 = (f"Kwota twojego zamówienia to {kwota} zł. \n Zapłacisz {kwotavat} zł podatku VAT + 8,50 zł opłaty pocztowej (´⊙ω⊙`)！")
        tekst2 = st.write(f"Kwota zamówienia przekracza 150 EUR ({czyclo} zł). \n Możliwe oclenie paczki ಥ‿ಥ")
        clo = "Tak"

    else:
        tekst1 = st.write(f"Kwota twojego zamówienia to {kwota} zł. \n Zapłacisz {kwotavat} zł podatku VAT + 8,50 zł opłaty pocztowej (´⊙ω⊙`)！")
        tekst2 = st.write(f"Kwota zamówienia nie przekracza 150 EUR ({czyclo} zł). \n Nie musisz płacić cła ٩(•̤̀ᵕ•̤́๑)ᵒᵏᵎᵎᵎᵎ")
        clo = "Nie"



st.header("Kalkulator VAT dla paczek z Japonii", divider="violet")


st.write("Wpisz kwotę zamówienia wraz z kosztami przesyłki w jenach lub złotówkach:")
wprowadz = st.number_input(label="Kwota", min_value=1)
#st.write(wprowadz)

st.write("Wybierz walutę, w której podałeś cenę paczki i przesyłki:")

columns = st.columns([1, 1, 1, 1])

with columns[1]:
    przycisk1 = st.button('Złoty polski PLN')

with columns[2]:
    przycisk2 = st.button('Jen japoński JPY')

st.divider()

kolumny = st.columns([1, 1, 1])

if przycisk1:
    przelicz1()
    tabelka = pd.DataFrame({"Kwota":kwota,"VAT":kwotavat,"Cło?":clo}, index=([1]))
    tabelka2 = tabelka.transpose()
    with kolumny[1]:
        st.dataframe(tabelka, hide_index=True)

if przycisk2:
    przelicz2()
    tabelka = pd.DataFrame({"Kwota":kwota,"VAT":kwotavat,"Cło?":clo}, index=([1]))
    tabelka2 = tabelka.transpose()
    with kolumny[1]:
        st.dataframe(tabelka, hide_index=True)
