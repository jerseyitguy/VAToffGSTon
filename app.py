from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate_tax():
    result = None

    if request.method == 'POST':
        try:
            # Get the user-entered value
            value = float(request.form['value'])

            # Remove 20% VAT
            value_without_vat = value / 1.20

            # Add 5% GST
            value_with_gst = value_without_vat * 1.05

            result = {
                'value': value,
                'value_without_vat': value_without_vat,
                'value_with_gst': value_with_gst,
            }
        except ValueError:
            result = {
                'error': 'Please enter a valid numeric value.',
            }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
