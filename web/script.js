async function get_numbers() {
    let place = document.getElementById('input_number').value;

    let result_bin = await eel.binary(place)();
    let result_oct = await eel.octal(place)();
    let result_hex = await eel.hexadecimal(place)();
    
    document.getElementById('output-info__bin').innerHTML = result_bin;
    document.getElementById('output-info__oct').innerHTML = result_oct;
    document.getElementById('output-info__hex').innerHTML = result_hex;
};   