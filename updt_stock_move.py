import xmlrpc.client

# Odoo server details
url = 'http://localhost:8016'
db = 'mar_21'
username = 'admin'
password = 'Gi77@05'

# Authenticate
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

# Connect to the models endpoint
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Stock Move ID to update
stock_move_id = 2700541  # Replace with the ID of the stock move you want to update

# Update the `forecast_availability` field

models.execute_kw(db, uid, password, 'stock.move', 'write', [[stock_move_id], {
    'locaion_id': 1568,
}])

# Fetch the updated record details
updated_record = models.execute_kw(db, uid, password, 'stock.move', 'read', [stock_move_id], {
    'fields': ['name', 'product_id'],
})

# Print the updated record details
print("Updated Record Details:")
print(f"Name: {updated_record[0]['name']}")
print(f"Product ID: {updated_record[0]['product_id'][1]}")  # product_id is a tuple (id, name)
print(f"Forecast Availability: {updated_record[0]['forecast_availability']}")

# git push to revert

