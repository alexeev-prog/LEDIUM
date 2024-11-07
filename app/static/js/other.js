

const inputField = document.querySelector('input[list="options"]');
const nextInput = document.getElementById('next-input');

inputField.addEventListener('change', () => {
	nextInput.focus(); // Перемещение фокуса
});

inputField.addEventListener('input', () => {
	if (inputField.value === '') {
		nextInput.innerText = '';
	}
});
