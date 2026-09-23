# 🎓 Panel Kursanta — Streamlit

Efektowny panel kursanta: wybór kursu w sidebarze, formularz z danymi i poziomem, karta kursanta po zapisaniu.

## Uruchomienie w PyCharm (najprościej)

1. Otwórz projekt (**Get from VCS** → `https://github.com/UrukAn/testy.git`).
2. Otwórz `app.py` i kliknij zielony **▶ Run**.

Skrypt sam doinstaluje Streamlit do interpretera projektu, uruchomi serwer
i otworzy panel w przeglądarce. Zatrzymanie: czerwony kwadrat w PyCharmie.

## Uruchomienie z terminala

```bash
python app.py
# albo klasycznie:
pip install -r requirements.txt
streamlit run app.py
```

## Funkcje
- **Sidebar (`st.sidebar`)** — wybór kursu: Python, Java, SQL + karta kursu
- **Formularz (`st.form`)** — imię, e-mail, poziom (początkujący / średniozaawansowany / zaawansowany)
- **Układ (`st.columns`)** — pola obok siebie, formularz + statystyki kursu
- Po przesłaniu: karta „Dane kursanta” z animowanym paskiem poziomu
- Walidacja imienia i e-maila, ciemny motyw, kolory zmieniają się z kursem
