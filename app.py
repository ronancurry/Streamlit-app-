import random

import streamlit as st


RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")


def hand_value(hand: list[tuple[str, str]]) -> int:
	total = 0
	aces = 0
	for rank, _ in hand:
		if rank == "Ace":
			total += 11
			aces += 1
		elif rank in {"Jack", "Queen", "King"}:
			total += 10
		else:
			total += int(rank)

	while total > 21 and aces:
		total -= 10
		aces -= 1
	return total


def draw_card() -> tuple[str, str]:
	return st.session_state.deck.pop()


def finish_round() -> None:
	while hand_value(st.session_state.dealer_hand) < 17:
		st.session_state.dealer_hand.append(draw_card())

	player_total = hand_value(st.session_state.player_hand)
	dealer_total = hand_value(st.session_state.dealer_hand)
	if dealer_total > 21 or player_total > dealer_total:
		st.session_state.result = "You win!"
	elif player_total < dealer_total:
		st.session_state.result = "Dealer wins."
	else:
		st.session_state.result = "Push. It's a tie."
	st.session_state.round_over = True


def start_round() -> None:
	deck = [(rank, suit) for rank in RANKS for suit in SUITS]
	random.shuffle(deck)
	st.session_state.deck = deck
	st.session_state.player_hand = [draw_card(), draw_card()]
	st.session_state.dealer_hand = [draw_card(), draw_card()]
	st.session_state.round_over = False
	st.session_state.result = ""

	player_natural = hand_value(st.session_state.player_hand) == 21
	dealer_natural = hand_value(st.session_state.dealer_hand) == 21
	if player_natural or dealer_natural:
		st.session_state.round_over = True
		if player_natural and dealer_natural:
			st.session_state.result = "Push. Both hands have blackjack."
		elif player_natural:
			st.session_state.result = "Blackjack! You win."
		else:
			st.session_state.result = "Dealer has blackjack."


if "deck" not in st.session_state:
	start_round()

st.title("Blackjack")
st.write("Play a hand against the dealer. Choose Hit to take another card or Stand to let the dealer play.")
st.caption("Play-money game. Dealer stands on 17. Aces count as 1 or 11, whichever helps your hand most.")

st.subheader("Your hand")
st.write("  |  ".join(f"{rank} of {suit}" for rank, suit in st.session_state.player_hand))
st.metric("Your total", hand_value(st.session_state.player_hand))

st.subheader("Dealer")
if st.session_state.round_over:
	st.write("  |  ".join(f"{rank} of {suit}" for rank, suit in st.session_state.dealer_hand))
	st.metric("Dealer total", hand_value(st.session_state.dealer_hand))
else:
	dealer_upcard = st.session_state.dealer_hand[0]
	st.write(f"{dealer_upcard[0]} of {dealer_upcard[1]}  |  Hidden card")

if st.session_state.round_over:
	st.success(st.session_state.result)
elif hand_value(st.session_state.player_hand) > 21:
	st.session_state.round_over = True
	st.session_state.result = "Bust. Dealer wins."
	st.error(st.session_state.result)
else:
	hit_column, stand_column = st.columns(2)
	with hit_column:
		if st.button("Hit", type="primary", use_container_width=True):
			st.session_state.player_hand.append(draw_card())
			if hand_value(st.session_state.player_hand) > 21:
				st.session_state.round_over = True
				st.session_state.result = "Bust. Dealer wins."
			st.rerun()
	with stand_column:
		if st.button("Stand", use_container_width=True):
			finish_round()
			st.rerun()

if st.session_state.round_over:
	st.button("New Hand", on_click=start_round, type="primary")