const inputs = document.querySelectorAll("#form input");
const bar = document.getElementById("Bar");

function updateProgress() {
    let validInputs = 0;

    inputs.forEach(input => {
        if (input.checkValidity() && input.value.trim() !== "") {
            validInputs++;
        }
    });

    const progress = (validInputs / inputs.length) * 100;

    bar.style.width = progress + "%";
}

inputs.forEach(input => {
    input.addEventListener("input", updateProgress);
});