// app.js
const form = document.getElementById('order-form');
form.addEventListener('submit', async function (event) {
    event.preventDefault();
    
    const itemsInput = document.getElementById('items');
    const items = itemsInput.value.split(',').map(item => item.trim());

    try {
        const response = await axios.post('/orders', { items });
        document.getElementById('order-status').innerHTML = response.data.message;
    } catch (error) {
        document.getElementById('order-status').innerHTML = `Error: ${error.response.data.error}`;
    }
});
