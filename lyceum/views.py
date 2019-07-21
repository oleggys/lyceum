import datetime

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, csrf_exempt

from files_in_com.models import codifier, dis_learning, other, result, training_file
from lyceum.models import Staff, Event, events_in_day, Lyceum_news, subject, message
from documents.models import plat_documents,gos_document,license_document,provision_document,provisions,ruls_document,certificate_document,charter_document,internal_document,order_document,order_exec_document,other_document,pred_org_document,prokurat_document
from offer_and_com.models import offer, complaint


def index(request):
    args={}
    return render(request,'lyceum/index.html', args)


def team(request):
    args = {}
    tearchers = 1
    educators = 2
    args['administrations_team'] = Staff.objects.all().filter(administration=True)
    args['teachers_team'] = Staff.objects.all().filter(position=tearchers)
    args['educators_team'] = Staff.objects.all().filter(position=educators)
    return render(request,'lyceum/team.html', args)


def incom(request):
    args={}
    args['codifiers'] = codifier.objects.all()
    args['dis_learning_files'] = dis_learning.objects.all()
    args['other_files'] = other.objects.all()
    args['result_files'] = result.objects.all()
    trfiles = training_file.objects.all()
    objects = dis_learning.objects.all()
    years = set()
    for object in objects:
        if object.year != None:
            years.add(object.year.year)
    subyear = {}
    obsub = set()
    training = {}
    trsub = set()
    subjects_fo_tr = set()
    for year in years:
        for object in objects:
            if object.year != None and object.year.year == year:
                obsub.add(object.subject)
        subyear.update({year: obsub})
        obsub = set()
    for file in trfiles:
        subjects_fo_tr.add(file.subject)
    for sub in subjects_fo_tr:
        for file in trfiles:
            if file.subject == sub:
                trsub.add(file)
        training.update({sub: trsub})
        trsub = set()
    args['subyear'] = subyear
    args['training_files'] = training
    return render(request, 'lyceum/incom.html', args)


def isleap(now_y):
    if now_y % 4 == 0:
        return True
    else:
        return False

def events(request):
    args = {}
    if request.is_ajax():
        if not request.GET['year'] is None:
            year = int(request.GET['year'])
            if not request.GET['year'] is None:
                month = int(request.GET['month'])
            else:
                month = datetime.datetime.now().month
        first_day_in_month = datetime.date(year, month, 1).weekday()
    else:
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        first_day_in_month = datetime.date(year, month, 1).weekday()
    month_w_31 = {1,4,6,9,11}
    if month in month_w_31:
        days = 30
    elif month == 2:
        if isleap(year):
            days = 29
        else:
            days = 28
    else:
        days = 31
    args['days'] = []
    for i in range(1-first_day_in_month, days + 1):
        args['days'].append(int(i))
    years = []
    for i in range(2015, 2020):
        years.append(int(i))
    months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
              7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    args['years'] = years
    args['year_now'] = year
    args['months'] = months
    args['month_now'] = months[month]
    args['month_now_id'] = month
    args['events'] = []
    args['first_day_in_month'] = first_day_in_month
    args['events_in_day'] = {}
    args['events_itmonth'] = Event.objects.all().filter(event_date__month=month, event_date__year=year)
    events = Event.objects.all().filter(event_date__month=month, event_date__year=year)
    for event in events:
        events_itday = []
        args['events'].append(event.event_date.day)
        inday = events_in_day.objects.all().filter(event_day=event.id)
        for d in inday:
            events_itday.append(d)
        args['events_in_day'].update({event.event_date.day: events_itday})
    lnews = Lyceum_news.objects.all().order_by('-pub_date')
    i = 0
    args['news'] = {}
    for lnew in lnews:
        i += 1
        args['news'].update({i: lnew})
    if request.is_ajax():
        return render(request, 'lyceum/calendar.html', args)
    else:
        return render(request, 'lyceum/events.html', args)



def documents(request):
    args={}
    internal_documents = internal_document.objects.all()
    internal = {}
    prov = {}
    folders = set()
    args['gos_document'] = gos_document.objects.all()
    args['license_document'] = license_document.objects.all()
    provision_documents = provision_document.objects.all()
    args['provisions'] = provisions.objects.all()
    args['order_exec_document'] = order_exec_document.objects.all()
    args['order_document'] = order_document.objects.all()
    args['ruls_document'] = ruls_document.objects.all()
    args['prokurat_document'] = prokurat_document.objects.all()
    args['pred_org_document'] = pred_org_document.objects.all()
    args['plat_documnets'] = plat_documents.objects.all()
    args['certificate_document'] = certificate_document.objects.all()
    args['charter_document'] = charter_document.objects.all()
    args['other_document'] = other_document.objects.all()
    doc = set()
    for document in internal_documents:
        folders.add(document.provision)
    for folder in folders:
        for document in internal_documents:
            if document.provision == folder:
                doc.add(document)
        internal.update({folder: doc})
        doc = set()
    args['internal_documents'] = internal
    folders = set()
    doc = set()
    for document in provision_documents:
        folders.add(document.provision)
    for folder in folders:
        for document in provision_documents:
            if document.provision == folder:
                doc.add(document)
        prov.update({folder: doc})
        doc = set()
    args['provision_document'] = prov
    return render(request,'lyceum/documents.html', args)


@csrf_exempt
def messages(request):
    if request.is_ajax():
        email = request.POST['send_email']
        topic = request.POST['send_topic']
        name = request.POST['send_name']
        text = request.POST['send_text']
       # res = send_mail(topic, message, "oleggys1@mail.ru", [email])
       # res ='%s' % res''
        mes = message(email=email, topic=topic, name=name, text=text)
        mes.save()
        return HttpResponse()


def offers(request):
    args = {}
    args['offers'] = offer.objects.all()
    args['complaints'] = complaint.objects.all()
    return render(request, 'lyceum/offer.html', args)

@csrf_exempt
def make_offer(request):
    args = {}
    args.update(csrf(request))
    warrning = {}
    if request.POST:
        name = request.POST.get('o_name', "")
        email = request.POST.get('o_email', "")
        topic = request.POST.get('o_topic', "")
        phone = request.POST.get('tel', "")
        text = request.POST.get('o_text', "")
        if name == "":
            warrning.update({'name': "name"})
        if email == "":
            warrning.update({'email': "email"})
        if topic == "":
            warrning.update({'topic': "topic"})
        if phone == "" or len(phone) < 17:
            warrning.update({'phone': "phone"})
        if text == "":
            warrning.update({'text': "text"})
        if warrning == {}:
            of = offer(name=name, email=email, topic=topic, phone=phone, text=text)
            of.save()
            return render(request, 'lyceum/thanks.html', args)
        else:
            args['warnings'] = warrning
            args['offers'] = offer.objects.all()
            args['complaints'] = complaint.objects.all()
            args['o_name'] = name
            args['o_email'] = email
            args['o_topic'] = topic
            args['o_phone'] = phone
            args['o_text'] = text
            return render(request, 'lyceum/offer.html', args)
    return render(request, 'lyceum/thanks.html', args)


@csrf_exempt
def make_com(request):
    args = {}
    args.update(csrf(request))
    warrning = {}
    if request.POST:
        name = request.POST.get('c_name', "")
        email = request.POST.get('c_email', "")
        topic = request.POST.get('c_topic', "")
        phone = request.POST.get('tel2', "")
        text = request.POST.get('c_text', "")
        if name == "":
            warrning.update({'name': "name"})
        if email == "":
            warrning.update({'email': "email"})
        if topic == "":
            warrning.update({'topic': "topic"})
        if phone == "" or len(phone) < 17:
            warrning.update({'phone': "phone"})
        if text == "":
            warrning.update({'text': "text"})
        if warrning == {}:
            of = complaint(name=name, email=email, topic=topic, phone=phone, text=text)
            of.save()
        else:
            args['warnings_c'] = warrning
            args['offers'] = offer.objects.all()
            args['complaints'] = complaint.objects.all()
            args['c_name'] = name
            args['c_email'] = email
            args['c_topic'] = topic
            args['c_phone'] = phone
            args['c_text'] = text
            return render(request, 'lyceum/offer.html', args)
    return render(request, 'lyceum/thanks_con.html', args)