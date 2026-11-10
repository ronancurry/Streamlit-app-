import streamlit as st

def recommend_action(player_total: int, dealer_upcard: int) -> tuple[str, str]:
	if player_total >= 17:
		return "Stand", "Hard totals of 17 or more should stand."
	if player_total <= 8:
		return "Hit", "A hard total of 8 or less should hit."
	if player_total == 9:
		if 3 <= dealer_upcard <= 6:
			return "Double", "Double 9 against a dealer 3 through 6; otherwise hit."
		return "Hit", "Double 9 only against a dealer 3 through 6; otherwise hit."
	if player_total == 10:
		if dealer_upcard <= 9:
			return "Double", "Double 10 against a dealer 2 through 9; otherwise hit."
		return "Hit", "Hit 10 against a dealer 10 or Ace."
	if player_total == 11:
		if dealer_upcard == 11:
			return "Hit", "With the dealer standing on soft 17, hit hard 11 against an Ace."
		return "Double", "A hard 11 is a strong hand to double."
	if player_total == 12:
		if 4 <= dealer_upcard <= 6:
			return "Stand", "Stand on 12 against a dealer 4 through 6; otherwise hit."
		return "Hit", "Stand on 12 only against a dealer 4 through 6; otherwise hit."
	if dealer_upcard <= 6:
		return "Stand", "Stand on hard 13 through 16 against a dealer 2 through 6."
	return "Hit", "Hit hard 13 through 16 against a dealer 7 or higher."


st.title("Blackjack Trainer")
st.write(
	"Practice a blackjack decision by entering your hard hand total and the "
	"dealer's upcard. Get a basic-strategy suggestion and compare it with your choice."
)
st.caption(
	"Recommendations assume the dealer stands on soft 17 and cover hard totals only. "
	"Soft hands, pairs, and surrender are not included yet."
)

st.subheader("Practice a hand")
left_column, right_column = st.columns(2)

with left_column:
	player_total = st.number_input(
		"Your hard hand total",
		min_value=4,
		max_value=21,
		value=16,
		step=1,
		help="Enter your total without treating an Ace as 11.",
	)

with right_column:
	dealer_card = st.selectbox(
		"Dealer's upcard",
		[str(value) for value in range(2, 11)] + ["Ace"],
		index=8,
	)

decision = st.radio(
	"What would you do?",
	["Hit", "Stand", "Double"],
	horizontal=True,
)
dealer_value = 11 if dealer_card == "Ace" else int(dealer_card)
recommended_action, explanation = recommend_action(player_total, dealer_value)

st.markdown("### Recommendation")
st.info(f"**{recommended_action}.** {explanation}")

if decision == recommended_action:
	st.success("Your choice matches the basic-strategy recommendation for this hand.")
else:
	st.warning(f"You chose {decision.lower()}. For this hand, basic strategy recommends {recommended_action.lower()}.")