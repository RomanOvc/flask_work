function submit_entry() {
    var input_text = document.getElementById('input_text');
    var entry = {
        input_text: input_text.value,
    };
    console.log(entry);
}
