const stars = [];
var i, j;
for(i=0; i<5; i++){
        stars[i] = document.getElementById(`reviewformstar${i+1}`);
}
document.getElementById('starsinput').value = 0;
console.log(stars[1]);
document.getElementById('starsinput').style.display = 'none';
console.log(document.getElementById('starsinput').value);

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
                                document.getElementById('starsinput').value = j+1;
                        }
                }
        });
}
console.log(document.getElementById('starsinput').value);

