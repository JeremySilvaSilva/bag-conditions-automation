from django.shortcuts import render
from django.http import HttpResponse
from .models import Factor,FactorBodyTag
from dateutil.parser import parse
from lxml.builder import E

val = [
    'customerSubTypeCode','customerTypeTitle',
    'customerTypeCode','alevel','atype','cid',
    'cstatus','pind','plantype','mname',
    'stype','oname','id','name_tag'
]
 
def index(request):
    import requests
    payload = '{"msisdn": "56992387082","app": "PC","extid": "1"}'
    r = requests.post('http://10.46.0.142:11223/WSQin/services/saldo/getSaldoTest',data=payload)

    data = r.json()
    info = data['resp']['info']
    re = []
    for bolsa in info['bolsas']:
        response = ''
        for fac in Factor.objects.values(*val):
            if (
                info['customerSubTypeCode'] == fac['customerSubTypeCode'] and 
                info['customerTypeTitle'] == fac['customerTypeTitle'] and info['customerTypeCode'] == fac['customerTypeCode']
                and
                (bolsa['alevel'] == fac['alevel'] or fac['alevel'] == None) and 
                (bolsa['atype'] == fac['atype'] or fac['atype'] == None) and
                (bolsa['cid'] == fac['cid'] or fac['cid'] == None) and 
                (bolsa['cstatus'] == fac['cstatus'] or fac['cstatus'] == None) and
                (bolsa['pind'] == fac['pind'] or fac['pind'] == None) and 
                (bolsa.get('plantype',None) == fac['plantype'] or fac['plantype'] == None)and
                (bolsa['mname'] == fac['mname'] or fac['mname'] == None) and 
                (bolsa['stype'] == fac['stype'] or fac['stype'] == None)and
                (bolsa['oname'] == fac['oname'] or fac['oname'] == None) 
            ):
                print('PASO CONDICION')
                tags = FactorBodyTag.objects.values('body__name','body__req').filter(factor=fac['id'])  

                dot = False
                for ar in re:
                    if ar.tag ==  fac['name_tag']:
                        dot = True
                        if ar.find('bolsa'):
                            bag = ar.find('bolsa').text
                            new_bag = str(int(bag) + 1)
                            ar.replace(ar.find('saldo'), E.saldo(new_bag))
                        if ar.find('fechaVencimiento'):
                            fech = ar.find('fechaVencimiento').text
                            bag_date = bolsa['aedate']
                            if parse(fech) > parse(bag_date):
                                print('here')
                                print(ar.find('saldo').text)
                                texto = '4545'
                                ar.replace(ar.find('saldo'), E.saldo(texto))
                                print(ar.find('saldo').text)

                if not dot:
                    for ta in tags:
                        valu = eval(ta['body__req'])
                        dat = "E.{}(str('{}')), ".format(ta['body__name'],valu)
                        response += dat
                        print(response)
                    if len(response) > 0:
                        response += " E.bolsa('1')"
                        det = "E.{}({})".format(fac['name_tag'],response)
                        print(det)
                        re.append(eval(det))   
                        print(re)
                        print('\n') 
                else:
                    print(re)
                    for i in re:
                        print(i.tag)
    return HttpResponse('HI')



# def is_exist_replace(re,fac):

def builder_xml(request):
    import requests
    payload = '{"msisdn": "56992387082","app": "PC","extid": "1"}'
    r = requests.post('http://10.46.0.142:11223/WSQin/services/saldo/getSaldoTest',data=payload)

    data = r.json()
    info = data['resp']['info']
    re = []
    for bolsa in info['bolsas']:
        response = ''
        for fac in Factor.objects.values(*val):
            if (
                info['customerSubTypeCode'] == fac['customerSubTypeCode'] and 
                info['customerTypeTitle'] == fac['customerTypeTitle'] and info['customerTypeCode'] == fac['customerTypeCode']
                and
                (bolsa['alevel'] == fac['alevel'] or fac['alevel'] == None) and 
                (bolsa['atype'] == fac['atype'] or fac['atype'] == None) and
                (bolsa['cid'] == fac['cid'] or fac['cid'] == None) and 
                (bolsa['cstatus'] == fac['cstatus'] or fac['cstatus'] == None) and
                (bolsa['pind'] == fac['pind'] or fac['pind'] == None) and 
                (bolsa.get('plantype',None) == fac['plantype'] or fac['plantype'] == None)and
                (bolsa['mname'] == fac['mname'] or fac['mname'] == None) and 
                (bolsa['stype'] == fac['stype'] or fac['stype'] == None)and
                (bolsa['oname'] == fac['oname'] or fac['oname'] == None) 
            ):
                print('PASO CONDICION')
                tags = FactorBodyTag.objects.values('body__name','body__req').filter(factor=fac['id'])  

                dot = False
                for ar in re:
                    if ar.tag ==  fac['name_tag']:
                        dot = True
                        if ar.find('bolsa'):
                            bag = ar.find('bolsa').text
                            new_bag = str(int(bag) + 1)
                            ar.replace(ar.find('saldo'), E.saldo(new_bag))
                        if ar.find('fechaVencimiento'):
                            fech = ar.find('fechaVencimiento').text
                            bag_date = bolsa['aedate']
                            if parse(fech) > parse(bag_date):
                                print('here')
                                print(ar.find('saldo').text)
                                texto = '4545'
                                ar.replace(ar.find('saldo'), E.saldo(texto))
                                print(ar.find('saldo').text)

                if not dot:
                    for ta in tags:
                        valu = eval(ta['body__req'])
                        dat = "E.{}(str('{}')), ".format(ta['body__name'],valu)
                        response += dat
                        print(response)
                    if len(response) > 0:
                        response += " E.bolsa('1')"
                        det = "E.{}({})".format(fac['name_tag'],response)
                        print(det)
                        re.append(eval(det))   
                        print(re)
                        print('\n') 
                else:
                    print(re)
                    for i in re:
                        print(i.tag)
    return HttpResponse('HI')