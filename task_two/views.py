from rest_framework.decorators import api_view
from task_two.models import *
from task_two.serializers.serializer import *
from task_two.helpers.utils import *
from django.db.models import Q


#CUSTOMER VIEWS
@api_view(['GET', 'POST'])
def customer_list_view(request):

    if request.method == 'GET':
        try:
            data = Customer.objects.all()
            ser = CustomerSerializer(data, many=True)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'POST':
        try:
            ser = CustomerSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return response_success(data=ser.data)
            else:
                return response_failed('Something wrong with the input data')
        except Exception as e:
            return response_failed(e.args)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail_view(request, pk):

    if request.method == 'GET':
        try:
            data = Customer.objects.get(pk=pk)
            ser = CustomerSerializer(data)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)

    elif request.method == 'PUT':
        try:
            current_obj = Customer.objects.get(pk=pk)
            new_obj = request.data
            ser = CustomerSerializer(current_obj, data=new_obj, partial=True)
            if ser.is_valid():
                ser.save()
                return response_success(data=ser.data)
            else:
                return response_failed('Serializer not valid')
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'DELETE':
        try:
            current_obj = Customer.objects.get(pk=pk)
            current_obj.delete()
            return response_success({'message':'Object deleted!'})
        except Exception as e:
            return response_failed('Was not possible to delete object, maybe the ID informed doesnt exist')


#CURRENT ACCOUNT VIEWS
@api_view(['GET', 'POST'])
def currentaccount_list_view(request):

    if request.method == 'GET':
        try:
            data = CurrentAccount.objects.all()
            ser = CurrentAccountSerializer(data, many=True)
            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)
            
    elif request.method == 'POST':
        try:
            ser = CurrentAccountSerializer(data=request.data, context={'request': request})
            customer = Customer.objects.get(pk=request.data.get('customer_account'))
            if customer:
                if ser.is_valid():
                    ser.save()
                    return response_success(data=ser.data)
                else:
                    return response_failed('Something wrong with the input data')
        except Exception as e:
            return response_failed(e.args)

@api_view(['GET', 'PUT', 'DELETE'])
def currentaccount_detail_view(request, pk):
    output = {}
    if request.method == 'GET':
        try:
            data = CurrentAccount.objects.get(pk=pk)
            ser = CurrentAccountSerializer(data)

            customer = Customer.objects.get(pk=ser.data.get('customer_account'))
            ser_customer = CustomerSerializer(customer)

            transactions = Transaction.objects.filter(Q(from_customer = data.id) |  Q(to_customer = data.id)).values()

            output = ser.data
            output['customer_account'] = ser_customer.data
            output['transactions'] = transactions

            return response_success(data=output)
        except Exception as e:
            return response_failed(e.args)

    elif request.method == 'PUT':
        try:
            current_obj = CurrentAccount.objects.get(pk=pk)
            new_obj = request.data
            ser = CurrentAccountSerializer(current_obj, data=new_obj, partial=True)
            if ser.is_valid():
                ser.save()
                return response_success(data=ser.data)
            else:
                return response_failed('Serializer not valid')
        except Exception as e:
            return response_failed(e.args)
    
    elif request.method == 'DELETE':
        try:
            current_obj = CurrentAccount.objects.get(pk=pk)
            current_obj.delete()
            return response_success({'message':'Object deleted!'})
        except Exception as e:
            return response_failed('Was not possible to delete object, maybe the ID informed doesnt exist')


#TRANSACTION VIEWS
@api_view(['GET', 'POST'])
def transaction_list_view(request):

    if request.method == 'GET':
        try:
            data = Transaction.objects.all()
            ser = TransactionSerializer(data, many=True)

            return response_success(data=ser.data)
        except Exception as e:
            return response_failed(e.args)

    elif request.method == 'POST':
        try:
            from_customer = CurrentAccount.objects.get(pk=request.data.get('from_customer'))
            to_customer = CurrentAccount.objects.get(pk=request.data.get('to_customer'))
            amount = request.data.get('amount')
            ser = TransactionSerializer(data=request.data, context={'request': request})

            if ser.is_valid():
                ser.save()

                if from_customer.balance >= amount:
                    from_customer.balance -= amount
                    from_customer.save()

                    to_customer.balance += amount
                    to_customer.save()
                
                else:
                    return response_failed('The amount is higher than the value available in your balance')

                return response_success(data=ser.data)
            else:
                return response_failed('Something wrong with the input data')
        except Exception as e:
            return response_failed(e.args)

@api_view(['GET'])
def transaction_detail_view(request, pk):
    output = {}
    if request.method == 'GET':
        try:
            data = Transaction.objects.get(pk=pk)
            ser = TransactionSerializer(data)

            output = ser.data
            print(output.get('from_customer'))
            print(output.get('to_customer'))

            from_customer = Customer.objects.get(pk=output.get('from_customer'))
            from_customer_s = CustomerSerializer(from_customer).data

            to_customer = Customer.objects.get(pk=output.get('to_customer'))
            to_customer_s = CustomerSerializer(to_customer).data

            if from_customer and to_customer:
                output['from_customer'] = from_customer_s
                output['to_customer'] = to_customer_s

            return response_success(data=output)
        except Exception as e:
            return response_failed(e.args)



