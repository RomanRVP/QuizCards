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


const new_deck_btn = document.getElementById('add-new-deck-btn')
new_deck_btn.onclick = () => {
    document.getElementById('create-deck').style.display = 'block';
    document.getElementById('deck-list').style.display = 'none';
}

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
      .then(result => console.log(result))
}


function getDeckList() {
    return fetch('/api/deck/', {
        method: 'GET',
    }).then(response => response.json())
        .then(data => {
            const deckBox = document.getElementById('deck-list')
            for (const deck of data) {
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