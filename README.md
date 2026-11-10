# Blackjack

## Student Name
Ronan Curry


## App Description

Blackjack is a simple interactive card game where you play a hand against a computer dealer. Cards are dealt automatically, and you choose whether to Hit or Stand. The app handles card totals, Ace values, dealer turns, and round results. It uses no real money or betting.

## Intended Users

This app is for anyone who wants to play a casual game of blackjack in a browser, including beginners learning the basic flow of a hand.

## Current Features

- Deal a shuffled deck and start a hand automatically.
- Choose Hit or Stand during your turn.
- View your total and the dealer's upcard while the hole card stays hidden.
- Score Aces as 1 or 11, resolve busts and natural blackjack, and play the dealer's turn.
- See whether the hand is a win, loss, or push, then start a new hand.
- Play with no real-money betting.

## Planned Features

- Add Double Down and Split actions.
- Track wins, losses, and pushes across multiple hands.
- Add optional rules such as surrender and dealer soft-17 settings.

## Run Locally

Install the project dependency and start the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```