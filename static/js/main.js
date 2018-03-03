//bling.js
//
// const $ = document.querySelector.bind(document);
// const $$ = document.querySelectorAll.bind(document);
// 
// Node.prototype.on = window.on = function (name, fn) {
//   this.addEventListener(name, fn);
// }
// 
// NodeList.prototype.__proto__ = Array.prototype;
// 
// NodeList.prototype.on = NodeList.prototype.addEventListener = function (name, fn) {
//   this.forEach(function (elem, i) {
//     elem.on(name, fn);
//   });
// }
// 
// 

function autoComplete(latInput, lngInput){
        var input = document.getElementById('id_location')
        var autocomplete = new google.maps.places.Autocomplete(input);

        const dropdown = new google.map.places.Autocomplete(input);

        dropdown.addListener('place_changed', () => {
                const place = dropdown.getPlace();
                latInput.value = place.geometry.location.lat();
                lngInput.value = place.geometry.location.lng();;
        });
}

//if someone hit enter in location field dont submit the form

//$$('#id_location').on('keydown', (e) => {
//        if(e.keycode == 13) e.preventDefault();
//});



function activatePlacesSearch(){
        lat_field = document.getElementById('id_lat');
        lng_field = document.getElementById('id_lat');
        autoComplete(lat_field, lng_field);
};

// type ahead in the search bar
//
//
//
//
//
//
//



// based on https://gist.github.com/paulirish/12fb951a8b893a454b32

const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

Node.prototype.on = window.on = function (name, fn) {
  this.addEventListener(name, fn);
};

NodeList.prototype.__proto__ = Array.prototype; // eslint-disable-line

NodeList.prototype.on = NodeList.prototype.addEventListener = function (name, fn) {
  this.forEach((elem) => {
    elem.on(name, fn);
  });
};


search_bar = document.getElementById('navSearch');
suggestions = document.getElementById('suggestionsUl');
suggestions_box = document.getElementById('suggestionsBox');
navForm = document.getElementById('navForm');
console.log(suggestions);
const endpoint = '/rentals/ajax/search/?query=' + search_bar.value;
console.log(endpoint)
let find = [];

const prom = fetch(endpoint)
                .then(blob => blob.json())
                .then(data => find=data);
console.log(prom); 
testVar  = 'deepak';


function findMatches(wordToMatch, find){
        return find.rentals.filter(rental => {
                const regex = new RegExp(wordToMatch, 'gi');
                return rental.match(regex);
        });
}

function displayMatches(){
        const matchArray = findMatches(this.value, find);
        console.log(matchArray);
        let html = matchArray.map(rental => {
                query = rental.split(" ").join('+')
                return `
                <a class="nav-suggest-li" href="/rentals/?q=${query}">${rental}</a></br>
                        `;
        }).join('');
        if(!html){
            html = 'no results found!'
        }

        suggestions.innerHTML = html;
        console.log(search_bar.value);
}
suggestions_box.style.display = 'none';
search_bar.addEventListener('keyup', displayMatches);
search_bar.onfocus = function(){
        suggestions_box.style.display='block';
};

search_bar.addEventListener('focusout', function(){
        setTimeout(function(){
                suggestions_box.style.display='none';
        }, 200);
});
console.log(document.querySelector('.container'));

search_bar.addEventListener('keyup',cb); 
function cb(e, $('#suggestions_box')){
        //if they are not pressing up, down or enter who cares
        if(![38, 40, 13].includes (e.keyCode)){
            return;
        }
        const activeClass = 'nav-suggest-li--active';
        let current = suggestions_box.querySelector(`.${activeClass}`);
        console.log(current);
        console.log(suggestions_box.querySelector('.container'))
        const items = document.querySelectorAll('nav-suggest-li');
        console.log('items', items)
        if(!current){
                current = items[0];
        }
        let next;

        if(e.keyCode === 40 && current) {
            next = current.nextElementSibling || items[0];
        }else if(e.keyCode === 40 ){
            next = items[0];
        }else if(e.keyCode === 38 && current) {
            next = current.previousElementSibling || items[items.length - 1]
        }else if(e.keyCode === 38) {
            next = items[items.length - 1];
        }else if (e.keyCode === 13 && current.href){
            window.location = current.href;
            return;
        }
        if(current){
            current.classList.remove(activeClass);
        }
        next.classList.add(activeClass);

};

