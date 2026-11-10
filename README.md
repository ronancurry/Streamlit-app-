# Blackjack Trainer

## Student Name
Ronan Curry

## App Description

Blackjack Trainer is an interactive learning tool for practicing blackjack decisions. Enter a hard hand total and the dealer's upcard, choose Hit, Stand, or Double, and get a simplified basic-strategy recommendation with feedback on your choice. It is for educational practice, not real-money gambling.

## Intended Users

This app is intended for people who are new to blackjack or want a simple way to practice and understand common decisions. It is for educational practice, not real-money gambling.

## Current Features

- Enter a hard hand total from 4 to 21 and select the dealer's upcard.
- Choose Hit, Stand, or Double for the practice scenario.
- See a hard-total strategy recommendation and immediate feedback on your choice.
- Recommendations assume the dealer stands on soft 17; soft hands, pairs, and surrender are not covered yet.

## Planned Features

- Deal and play complete practice hands against a simulated dealer.
- Add strategy guidance for soft hands, pairs, splits, and surrender.
- Track wins, losses, pushes, and practice history across a session.

## Run Locally

Install the project dependency and start the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```