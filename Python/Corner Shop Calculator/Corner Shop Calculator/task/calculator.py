print('Earned amount:\n'
'Bubblegum: $202\n'
'Toffee: $118\n'
'Ice cream: $2250\n'
'Milk chocolate: $1680\n'
'Doughnut: $1075\n'
'Pancake: $80\n\n'
'Income: $5405')

staff_expenses = int(input('Staff expenses:\n'))
other_expenses = int(input('Other expenses:\n'))

print('Net income: $' + str(5405 - staff_expenses - other_expenses))