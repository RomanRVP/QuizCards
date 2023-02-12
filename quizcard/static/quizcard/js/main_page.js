

const new_deck_btn = document.getElementById('add-new-deck-btn')
new_deck_btn.onclick = () => {
    document.getElementById('create-deck').style.display = 'block';
    document.getElementById('deck-list').style.display = 'none';
}


function getDeckList() {
    return fetch('/api/deck/', {
        method: 'GET',
    }).then(response => response.json())
        .then(data => {
            const deckBox = document.getElementById('deck-list')
            console.log(data)
            for (const deck of data['deck_list']) {
                let deckElem = document.createElement('div')
                deckElem.className = 'current-deck'
                deckElem.innerHTML = deck['name']
                deckElem.id = deck['pk']
                let deckElemDescription = document.createElement('span')
                deckElemDescription.textContent = deck['description']
                deckElemDescription.className = 'current-deck-description'
                deckElem.prepend(deckElemDescription)
                deckBox.prepend(deckElem)
            }
        })
}
getDeckList()