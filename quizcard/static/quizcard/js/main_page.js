

const new_deck_btn = document.getElementById('add-new-deck-btn')
new_deck_btn.onclick = () => {
    document.getElementById('create-deck').style.display = 'block';
    document.getElementById('deck-list').style.display = 'none';
}