//bling.js
//
const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

Node.prototype.on = window.on = function (name, fn) {
  this.addEventListener(name, fn);
}

NodeList.prototype.__proto__ = Array.prototype;

NodeList.prototype.on = NodeList.prototype.addEventListener = function (name, fn) {
  this.forEach(function (elem, i) {
    elem.on(name, fn);
  });
}



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

$('#id_location').on('keydown', (e) => {
        if(e.keycode == 13) e.preventDefault();
})



function activatePlacesSearch(){
        autoComplete($('#id_lat'), $('#id_lng'));
}
