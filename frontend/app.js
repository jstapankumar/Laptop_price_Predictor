const price = document.querySelector('#price');
const company = document.querySelector('#company');
const typename = document.querySelector('#type');
const ram = document.querySelector('#ram');
const weight = document.querySelector('#weight');
const touch_screen = document.querySelector('#touch_screen');
const resolution = document.querySelector('#resolution');
const ips = document.querySelector('#ips');
const inches = document.querySelector('#inches');
const cpu_brand = document.querySelector('#cpu_brand');
const HDD = document.querySelector('#HDD');
const SSD = document.querySelector('#SSD');
const gpu_brand = document.querySelector('#gpu_brand');
const os = document.querySelector('#os');

form = document.querySelector('form');


/*
{
  "company": "Apple",
  "typename": "Ultrabook",
  "ram": "8",
  "weight": "1.78",
  "touch_screen": "0",
  "resolution": "1920x1080",
  "ips": "1",
  "inches": "15.6",
  "cpu_brand": "Intel Core i5",
  "HDD":"1024",
  "SSD": "512",
  "gpu_brand": "Intel",
  "os": "Mac"
}
*/

const url = 'http://127.0.0.1:8000/api/predict/'

form.addEventListener('submit', (e) => {
    
    e.preventDefault();
    const data = {
        "company": company.value,
        "typename": typename.value,
        "ram":parseInt(ram.value),
        "weight": parseFloat(weight.value),
        "touch_screen": parseInt(touch_screen.value),
        "resolution": resolution.value,
        "ips": parseInt(ips.value),
        "inches": parseFloat(inches.value),
        "cpu_brand": cpu_brand.value,
        "HDD": parseInt(HDD.value),
        "SSD": parseInt(SSD.value),
        "gpu_brand": gpu_brand.value,
        "os": os.value
    }

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    };

    fetch(url, options)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            price.innerHTML = data['price']
        });
});

