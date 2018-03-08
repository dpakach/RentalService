const endpoint = '/rentals/ajax/9/loc';
console.log(endpoint)

const prom = fetch(endpoint)
                .then(blob => blob.json());
console.log(prom); 


const mapOptions = {
        center: {lat: 43.2, lng: -79,8},
        zoom: 10
}

function makeMap(mapDiv) {
    if(!mapDiv) return;
    //make our map
    const map = new google.maps.Map(mapDiv, mapOptions);
    console.log(map);
    const input = $('[name="geolocate"]');
    const autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.addListener('place_changed', () => {
        const place = autocomplete.getPlace();
        console.log(place);
        loadPlaces(map, place.geometry.location.lat(), place.geometry.location.lng());
    });
}

export default makeMap; 
