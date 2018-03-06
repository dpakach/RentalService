//*******************************************************
// star from review section
//*******************************************************
//
const stars = [];
const starsinput = document.getElementById('id_stars');

if(starsinput){
        var i, j;
        for(i=0; i<5; i++){
                stars[i] = document.getElementById(`reviewformstar${i+1}`);
        }

        starsinput.value = 1;
        starsinput.style.display = 'none';
        for(i=0; i<5; i++){
                document.getElementById(`reviewformstar${i+1}`).addEventListener('click', function() {

                        this.classList.add('cta__icon--full');
                        let doo = true;
                        for(j=0; j<=i-1; j++){
                                if (doo){
                                    stars[j].classList.add('cta__icon--full');
                                }else{
                                    stars[j].classList.remove('cta__icon--full');
                                }
                                if(stars[j] === this){
                                        doo= false;
                                        starsinput.value = j+1;
                                }
                        }
                });
        }
}

//*******************************************************
// auto complete for locatioin field in retnal form
//*******************************************************
//
function activatePlacesSearch(){
        lat_field = document.getElementById('id_lat');
        lng_field = document.getElementById('id_lat');
        autoComplete(lat_field, lng_field);
};





//*******************************************************
// type ahead in the search bar
//*******************************************************

search_bar = document.getElementById('navSearch');
suggestions = document.getElementById('suggestionsUl');

searchbox = document.getElementById('search');
list = document.getElementById('suggestionsBox')
navForm = document.getElementById('navForm');
console.log(suggestions);
const endpoint = '/rentals/ajax/search/?query=' + search_bar.value;
console.log(endpoint)
let find = [];

const prom = fetch(endpoint)
                .then(blob => blob.json())
                .then(data => find=data);
console.log(prom); 


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
                return `<a class="suggestion" href="/rentals/?q=${query}">${rental}</a>`;
        }).join('');
        if(!html){
            html = `<span class="suggestions__notfound">no results found!</span>`
        }

        suggestions.innerHTML = html;
        console.log(search_bar.value);
}
search_bar.addEventListener('keyup', displayMatches);
search_bar.onfocus = function(){
        list.style.display='block';
};

search_bar.addEventListener('focusout', function(){
        setTimeout(function(){
                list.style.display='none';
        }, 200);
});

search_bar.addEventListener('keyup', (e) => {

        console.log('in suggestions');
        //if they are not pressing up, down or enter who cares
        if(![38, 40, 13].includes (e.keyCode)){
            return;
        }
        console.log(e.keycode);
        const activeClass = 'suggestion--active';
        let current = searchbox.querySelector(`.${activeClass}`);
        console.log('hello');
        const items = document.querySelectorAll('nav-suggest-li');
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
}); 

function cb(e, searchbox){

};

