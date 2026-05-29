def classify_message(message):
    message = message.lower()
    if 'payment' in message or 'billing' in message:
        category = 'billing'
    elif 'buy' in message or 'price' in message:
        category = 'sales'
    else:
        category = 'support'

    if 'urgent' in message or 'failed' in message:
        priority = 'high'
    elif 'help' in message:
        priority = 'medium'
    else:
        priority = 'low'

    return {'category': category,'priority': priority,}