function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const filling_js_block = document.getElementById('filling-js-block')
const create_deck_block = document.getElementById('create-deck')
const home_page = document.getElementById('home-page')

const new_deck_btn = document.getElementById('add-new-deck-btn')
new_deck_btn.onclick = () => {
    create_deck_block.style.display = 'block';
    filling_js_block.style.display = 'none';
}
home_page.onclick = getDeckList

const create_deck_confirm = document.getElementById('create-deck-confirm')
create_deck_confirm.onclick = () => {
    let data = {
        "name": document.getElementById('new_deck_name').value,
        "description": document.getElementById('new_deck_description').value
    }
    fetch('/api/deck/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
      },
      body: JSON.stringify(data)
    }).then(response => response.json())
}


function getDeckList() {
    return fetch('/api/deck/', {
        method: 'GET',
    }).then(response => response.json())
        .then(data => {
            create_deck_block.style.display = 'none';
            filling_js_block.style.display = 'block';
            const deckBox = document.getElementById('filling-js-block')
            deckBox.replaceChildren()

            const deck_list = document.createElement('div')
            deck_list.className = 'deck-list'
            deck_list.id = 'deck-list'

            for (const deck of data) {

                let deck_in_deck_list = document.createElement('button')
                deck_in_deck_list.className = 'deck-in-deck-list'
                deck_in_deck_list.onclick = () => getCurrentDeck(deck['pk'])

                let deck_name = document.createElement('span')
                deck_name.className = 'deck-name-in-deck-list'
                deck_name.innerHTML = deck['name']

                let deck_description = document.createElement('span')
                deck_description.className = 'deck-description-in-deck-list'
                deck_description.innerHTML = deck['description']

                deck_in_deck_list.append(deck_name)
                deck_in_deck_list.append(deck_description)
                deck_list.append(deck_in_deck_list)
            }
            deckBox.append(deck_list)
        })
}

function getCurrentDeck(deck_id) {
    const deckBox = document.getElementById('filling-js-block')
    deckBox.replaceChildren()
    return fetch('/api/deck/' + deck_id + '/', {
        method: 'GET',
    }).then(response => response.json())
        .then(data => {
            let currentDeckBox = document.createElement('div')
            currentDeckBox.className = 'current-deck-box'
            let currentDeckInfo = document.createElement('div')
            currentDeckInfo.className = 'current-deck-info-box'
            let currentDeckName = document.createElement('span')
            currentDeckName.className = 'current-deck-name'
            currentDeckName.innerHTML = data['name']
            let currentDeckDescription = document.createElement('span')
            currentDeckDescription.className = 'current-deck-description'
            currentDeckDescription.innerHTML = data['description']

            let currentDeckOptions = document.createElement('div')
            currentDeckOptions.className = 'current-deck-options-box'
            let currentDeckDelete = document.createElement('button')
            currentDeckDelete.className = 'current-deck-options-delete'
            currentDeckDelete.id = 'current-deck-options-delete'
            currentDeckDelete.innerHTML = 'Delete this Deck'
            currentDeckDelete.onclick = () => deleteCurrentDeck(deck_id)

            currentDeckInfo.append(currentDeckName)
            currentDeckInfo.append(currentDeckDescription)
            currentDeckBox.append(currentDeckInfo)

            currentDeckOptions.append(currentDeckDelete)
            currentDeckBox.append(currentDeckOptions)

            deckBox.append(currentDeckBox)
        })
}

function deleteCurrentDeck(deck_id) {
    const deleteCurrentDeckBlock = document.getElementById('current-deck-options-delete')
    deleteCurrentDeckBlock.replaceChildren()
    return fetch('/api/deck/' + deck_id + '/', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
    }).then(getDeckList)
}

getDeckList()