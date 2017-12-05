body1 = input('enter SenWeb, SenPhone or SenEmail: ')
if body1 == 'SenPhone':
    body = input("Welcome to PollText! Reply with Zip for Senators Phone Num's: ")

    try:
        if len(body) == 5:
            url = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
            z_c = str(body)
            key = '&key=AIzaSyBI4HcpedG-wMZPyVV8Sy7Q9Kal5i0EOy4'
            serviceurl = url + z_c + key
            address = serviceurl
            print(str(serviceurl + "Phone"))
        else:
            print('Error')
    except ValueError:
            pass

if body1 == 'SenWeb':
    body = input("Welcome to PollText! Reply with Zip for Senators Website.")

    try:
        if len(body) == 5:
            url = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
            z_c = str(body)
            key = '&key=AIzaSyBI4HcpedG-wMZPyVV8Sy7Q9Kal5i0EOy4'
            serviceurl = url + z_c + key
            address = serviceurl
            r = print(str(serviceurl + "Website"))
        else:
            print('Error')
    except ValueError:
        pass
if body1 == "SenEmail":
    body = input("Welcome to PollText! Reply with Zip for Senators Email's.")
    try:
        if len(body) == 5:
            url = 'https://www.googleapis.com/civicinfo/v2/representatives?address='
            z_c = str(body)
            key = '&key=AIzaSyBI4HcpedG-wMZPyVV8Sy7Q9Kal5i0EOy4'
            serviceurl = url + z_c + key
            address = serviceurl
            r = print(str(serviceurl + "Email"))

    except:
        r = print('Sorry, that was not a valid input message.')














