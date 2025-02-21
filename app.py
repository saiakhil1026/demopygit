from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for demonstration purposes
data_store = {
    'parent_pin': '',
    'child_pin': '',
    'transfer_limit': 0,
    'balance': 0,
    'bank_account': '',
    'backup_bank_account': '',
    'total_transferred': 0,
    'parent_mobile_numbers': [],  # Store parent mobile numbers
    'pending_requests': []  # Store pending requests for approval
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/set_parent_pin', methods=['POST'])
def set_parent_pin():
    pin = request.json.get('pin')
    if pin:
        data_store['parent_pin'] = pin
        return jsonify({'message': 'Parent PIN set successfully!'}), 200
    return jsonify({'message': 'Please enter a valid PIN.'}), 400


@app.route('/set_limit_and_balance', methods=['POST'])
def set_limit_and_balance():
    limit = request.json.get('limit')
    initial_balance = request.json.get('initial_balance')

    if limit > 0 and 0 <= initial_balance <= limit:
        data_store['transfer_limit'] = limit
        data_store['balance'] = initial_balance
        return jsonify({'message': 'Transfer limit and initial balance set successfully!'}), 200
    return jsonify({'message': 'Please enter a valid limit and balance (balance ≤ limit).'}), 400


@app.route('/link_bank_account', methods=['POST'])
def link_bank_account():
    bank_account = request.json.get('bank_account')
    backup_bank_account = request.json.get('backup_bank_account')
    parent_mobile_1 = request.json.get('parent_mobile_1')
    parent_mobile_2 = request.json.get('parent_mobile_2')

    if bank_account:
        data_store['bank_account'] = bank_account
        data_store['backup_bank_account'] = backup_bank_account
        data_store['parent_mobile_numbers'] = [parent_mobile_1, parent_mobile_2]
        return jsonify({'message': 'Bank accounts and mobile numbers linked successfully!'}), 200
    return jsonify({'message': 'Please enter a valid bank account number.'}), 400


@app.route('/fund_wallet', methods=['POST'])
def fund_wallet():
    fund_amount = request.json.get('fund_amount')

    if fund_amount > 0:
        data_store['balance'] += fund_amount
        return jsonify({'message': f'Wallet funded with ₹{fund_amount}!', 'balance': data_store['balance']}), 200
    return jsonify({'message': 'Please enter a valid amount to fund.'}), 400


@app.route('/create_child_wallet', methods=['POST'])
def create_child_wallet():
    pin = request.json.get('pin')

    if pin:
        data_store['child_pin'] = pin
        return jsonify({'message': 'Child wallet created successfully!'}), 200
    return jsonify({'message': 'Please enter a valid PIN.'}), 400


@app.route('/request_money', methods=['POST'])
def request_money():
    amount = request.json.get('amount')
    user_pin = request.json.get('user_pin')

    if amount > 0:
        if user_pin == data_store['child_pin']:
            # Deduct the amount immediately from the wallet
            if amount <= data_store['balance']:
                data_store['balance'] -= amount
                data_store['total_transferred'] += amount
                return jsonify({'message': 'Transfer successful!', 'balance': data_store['balance']}), 200
            else:
                # Notify parent for approval if the amount exceeds the balance
                data_store['pending_requests'].append({'amount': amount, 'child_pin': user_pin})
                notify_parent_for_approval(amount)
                return jsonify({'message': 'Insufficient funds! Parent notified for approval.',
                                'balance': data_store['balance']}), 200
        else:
            return jsonify({'message': 'Incorrect PIN. Transaction failed.'}), 400
    return jsonify({'message': 'Please enter a valid amount.'}), 400


def notify_parent_for_approval(amount):
    # Here you would implement the logic to send a notification to the parent's mobile numbers
    # For demonstration, we will just print to the console
    for mobile in data_store['parent_mobile_numbers']:
        print(f"Notification sent to {mobile}: Request for ₹{amount} exceeds limit. Approve?")


@app.route('/approve_request', methods=['POST'])
def approve_request(request):
    user_pin = request.json.get('user_pin')
    amount = request.json.get('amount')

    if user_pin == data_store['parent_pin']:
        # Check if there is a pending request for this amount
        for request in data_store['pending_requests']:
            if request['amount'] == amount:
                # The amount has already been deducted, just notify the child
                data_store['balance'] += amount  # Add the amount back to the balance
                data_store['total_transferred'] += amount
                data_store['pending_requests'].remove(request)  # Remove the approved request
                return jsonify({'message': 'Transfer approved! Child notified.', 'balance': data_store['balance']}), 200
        return jsonify({'message': 'No pending request found for this amount.'}), 400
    else:
        return jsonify({'message': 'Incorrect Parent PIN.'}), 400


@app.route('/request_additional_funds', methods=['POST'])
def request_additional_funds():
    amount = request.json.get('amount')
    user_pin = request.json.get('user_pin')

    if user_pin == data_store['parent_pin']:
        # Logic to transfer funds from parent's account to child's wallet
        data_store['balance'] += amount
        return jsonify({'message': f'₹{amount} transferred from parent account to child wallet!',
                        'balance': data_store['balance']}), 200
    else:
        return jsonify({'message': 'Incorrect Parent PIN.'}), 400


if __name__ == '__main__':
    app.run(debug=True)