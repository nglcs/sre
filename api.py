from flask import Flask
import requests
import json
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def default():
    return "It`s Work!"

@app.route('/customers-per-purchases')
def customersPerPurchases():
    dataCustomers = {}
    dataCustomersValues = []
    
    customers = json.loads(requests.get('http://www.mocky.io/v2/598b16291100004705515ec5').text)
    customersPerPurchases = json.loads(requests.get('http://www.mocky.io/v2/598b16861100004905515ec7').text)

    # Creating json with ids and values
    for customer in customersPerPurchases:
        client = str(customer['cliente'])
        totalValue = customer['valorTotal']
        
        # Input errors resolved
        if len(client) > 14:
            client = client[1:]
            
        client = client[:11] + '-' + client[12:]

        if client in dataCustomers: 
            dataCustomers[client] = round(totalValue + dataCustomers[client],1)
            
        else:
            dataCustomers.update({ client: totalValue })

    # Adding values in list of customers
    for customer in customers:
        customer.update({"totalValue": dataCustomers[str(customer["cpf"])]})
        dataCustomersValues.append(customer)

    # Sorting by totalValue
    resp = jsonify(sorted(dataCustomersValues, key=lambda k: k['totalValue'], reverse=True))

    return resp

@app.route('/the-best-client')
def bestClient():
    year = "2016"

    customers = json.loads(requests.get('http://www.mocky.io/v2/598b16291100004705515ec5').text)
    customersPerPurchases = json.loads(requests.get('http://www.mocky.io/v2/598b16861100004905515ec7').text)

    
    customersPerPurchases = sorted(customersPerPurchases, key=lambda k: k['valorTotal'], reverse=True)

    costumerCPF = ""
    valueSale = 0
    for purchases in customersPerPurchases:
        if purchases['data'].split("-")[2] == year:
            costumerCPF = purchases["cliente"][1:]
            costumerCPF = costumerCPF[:11] + '-' + costumerCPF[12:]

            

            for costumer in customers:
                if costumer["cpf"] == costumerCPF:
                    costumer.update({"totalValue": purchases["valorTotal"]})
                    return jsonify(costumer)

                    
            

 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
