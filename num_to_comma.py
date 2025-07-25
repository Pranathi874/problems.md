def format_indian_currency(number):
    num_str = str(number)

    
    if '.' in num_str:
        whole, decimal = num_str.split('.')
        decimal = '.' + decimal
    else:
        whole = num_str
        decimal = ''

    
    n = len(whole)
    
    if n <= 3:
        return whole + decimal
    else:
        
        last3 = whole[-3:]
        rest = whole[:-3]
        
        
        parts = []
        while len(rest) > 2:
            parts.insert(0, rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.insert(0, rest)
        
        
        formatted = ','.join(parts) + ',' + last3 + decimal
        return formatted


7
user_input = int(input())
number = float(user_input)
formatted = format_indian_currency(number)
print(formatted)
