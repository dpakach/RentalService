function autoComplete(input, latInput, lngInput) {
    if(!input) return ;//skip if no function
    const dropdown = new google.maps.places.Autocomplete(input);

    dropdown.addListener('place_changed', () => {
        const place =dropdown.getPlace();
        latInput.value = place.geometry.location.lat();
        lngInput.value = place.geometry.location.lng();
    }); 
    //dont submit on hitting enter on autocomplete
    input.on('keydown', (e) => {
        if(e.keyCode === 13) e.preventDefault();
    });
}

export default autoComplete;



