from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список для хранения заказов
orders = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/orders', methods=['GET', 'POST'])
def orders_page():
    if request.method == 'POST':
        # Получаем данные о заказе из формы
        order_data = request.form.get('order')
        if order_data:
            # Добавляем новый заказ в список
            orders.append(order_data)
        return redirect(url_for('orders_page'))
    
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
