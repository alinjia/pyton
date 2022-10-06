collection = int(input('кол-во_экспонатов'))
ages = int(input('кол-во_лет'))
if ages<=0 or collection<=0:
    print('error')
elif ages>0 and collection>0:
    ages1day = 8*60/5
    print('За данное кол-во лет', str(int(ages*365*ages1day)), 'экспонатов будет просмотрено')
    print('За ' + str(int(collection/ages1day//365)) + ' Год(лет) и ' + str(int(collection/ages1day%365)) + ' день(дней) или ' + str(int(collection/ages1day)) + ' дней' '  кол-во экспонатов будет просмотрено')
