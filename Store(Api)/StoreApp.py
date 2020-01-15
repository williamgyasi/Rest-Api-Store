from flask import Flask,request,jsonify
from flask_restful import Api,Resource
app=Flask(__name__)

stores=[
    {
        'name':'The Store of the Century',
        'location':'Dome-Kwabenya',
        'number_of_employees':32,
        'items':[
            {
                "item":"Milk",
                "price":20,
                "quantity":10
            },
{
                "item":"Rice",
                "price":16,
                "quantity":5
            },
{
                "item":"Goat",
                "price":500,
                "quantity":5
            }],
        'employeeofthemonth':[{
            'name':'William KWABENA GYASI',
            'age':20,
            'expensespermonth':100,
            'salary':5000
        },
{
            'name':'John Kojo GYASI',
            'age':25,
            'expensespermonth':500,
            'salary':5000
        }
        ]
        },
{
        'name':'the Century',
        'location':'Dome-Kwabenya',
        'number_of_employees':32,
        'items':[
            {
                "item":"Yam",
                "price":20,
                "quantity":10
            },
{
                "item":"Shoe",
                "price":16,
                "quantity":5
            },
{
                "item":"Rice",
                "price":500,
                "quantity":5
            }],
'employeeofthemonth':[{
            'name':'Johnson Adu Kwame',
            'age':18,
            'expensespermonth':500,
            'salary':200
        },
{
            'name':'Adu John Kwadjo',
            'age':28,
            'expensespermonth':600,
            'salary':10000
        }]

        }
]


@app.route('/store',methods=["POST"])
def create_store():
    data_set=request.get_json()
    newstore={
        'name':data_set['name'],
        'location':data_set['location'],
        'number_of_employees':['number_of_employees'],
        'items':[]
    }
    stores.append(newstore)
    return jsonify(newstore)

@app.route('/store/<string:name>')
def get_store(name):
    #iterate over stores if name==desiredstoreName
    for store in stores:
        if store['name']==name:
            return jsonify(store)


@app.route('/store')
def get_stores():
    return jsonify({
        'All-Available Stores':stores
    })
    pass

@app.route('/store/<string:name>/item',methods=["POST"])
def create_item_in_store(name):
    itemset = request.get_json()
    for store in stores:
        if store['name']==name:
            item={
                'item':itemset['item'],
                'price':itemset['price'],
                'quantity':itemset['quantity']
            }
            store['items'].append(item)
            return jsonify({
                'store':store['name']
            })
    return jsonify({
        'Message':'Store Not Found',
        'Status Code':404
    })

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
   for store in stores:
       if store['name']==name:
           return jsonify({
               'Items in store include':store['items']
           })
   return jsonify({
       'message':'Store Items Not Found.....'
   })
#Acess Store Emoloyeee
@app.route('/store/<string:name>/employees')
def get_employees(name):
    for store in stores:
        if store['name']==name:
            return jsonify({
                'Employee of the month are':store['employeeofthemonth']
            })
    return jsonify({
        'Message':'Employeeess Not Found',
        'Status Code':404
    })
#Create New Employee of the month
@app.route('/store/<string:name>/employees',methods=["POST"])
def create_employee_of_month(name):
    dataSet=request.get_json()
    for store in stores:
        if store['name']==name:
            employee_data={
                 'name':dataSet['name'],
                'age':dataSet['age'],
                'expensespermonth':dataSet['expensespermonth'],
                'salary':dataSet['salary']
            }
            store['employeeofthemonth'].append(employee_data)
            return jsonify({
                'employeeofthemonth':store['name']
            })

#acess a particular employee in a store
@app.route('/store/<string:name>/employees/<string:employee>')
def get_specific_employee(name,employee):
    for store in stores:
        if store['name']==name:
            for user in store['employeeofthemonth']:
                if user['name']==employee:
                    return jsonify(user)
            return jsonify({
                'message':'Employeee Not Found'
            })





if __name__=="__main__":
    app.run(debug=True)


