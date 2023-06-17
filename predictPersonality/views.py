from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
# from sklearn.externals import joblib
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from predictPersonality.models import Questions
import mysql.connector
# import sklearn.externals.joblib as joblib
import joblib

# k_fit_5 = KMeans()
# dataClusters5 = pd.DataFrame()

# Create your views here.
def index(request):
    request.session['EXT_ans'] = NULL
    request.session['NRT_ans'] = NULL
    request.session['AGR_ans'] = NULL
    request.session['CNS_ans'] = NULL
    request.session['OPN_ans'] = NULL
    
    
    # request.session['dataclusters5'] = dataclusters5

    return render(request, 'index.html')

def testpage1(request):
    context = {}
    context['que_1'] = Questions.objects.filter(category_id = 'C_3')
    
    if(request.session['EXT_ans'] != NULL):
        # d = pq(filename='./templates/test1.html')
        context['answers'] = []
        for i in range(1,11):
            temp = (request.session['EXT_ans'][i-1])
            tag = "input[name=EXT_" + str(i) + "][value=" + (temp) + "]"
            # print(temp)
            # print(type(temp))
            # print(tag)
            context['answers'].append(tag)
            # for j in range(0, len(context['answers'])):
                # print(context['answers'][j])
            # print(d(tag).attr('checked', 'checked'))
            # d(tag).attr('checked', 'checked')

    return render(request, 'test1.html',  context)

def process1(request):
    if(request.method == "POST"):
        if(request.session['EXT_ans'] == NULL):
            ext_quest_resp = []
            for i in range(1,11):
                ext_quest_resp.append(request.POST['EXT_'+str(i)])
        else:
            ext_quest_resp = request.session['EXT_ans']
            for i in range(0,10):
                ext_quest_resp[i] = request.POST['EXT_'+str(i+1)]

        
        request.session['EXT_ans'] = ext_quest_resp
        print(request.session['EXT_ans'])
        return redirect('/testpage2')

def testpage2(request):
    if(request.session['EXT_ans'] == NULL):
        return redirect('/testpage1')
    
    # res = request.session['EXT_ans']

    context = {}
    context['que_1'] = Questions.objects.filter(category_id = 'C_5')

    if(request.session['NRT_ans'] != NULL):
        context['answers'] = []
        for i in range(1,11):
            temp = (request.session['NRT_ans'][i-1])
            tag = "input[name=NRT_" + str(i) + "][value=" + (temp) + "]"
            context['answers'].append(tag)

    return render(request, 'test2.html', context)

def process2(request, flag):
    if(request.method == "POST"):
        if(request.session['EXT_ans'] == NULL):
            return redirect('/testpage1')
        if(request.session['NRT_ans'] == NULL):
            nrt_quest_resp = []
            for i in range(1,11):
                nrt_quest_resp.append(request.POST['NRT_'+str(i)])
        else:
            nrt_quest_resp = request.session['NRT_ans']
            for i in range(0,10):
                nrt_quest_resp[i] = request.POST['NRT_'+str(i+1)]

        request.session['NRT_ans'] = nrt_quest_resp
        print(request.session['NRT_ans'])
        print(flag)
        print(type(flag))
        if(int(flag) == 1):
            return redirect('/testpage3')
        else:
            return redirect('/testpage1')

def testpage3(request):
    if(request.session['EXT_ans'] == NULL):
        return redirect('/testpage1')
    if(request.session['NRT_ans'] == NULL):
        return redirect('/testpage2')
    context = {}
    context['que_1'] = Questions.objects.filter(category_id = 'C_4')

    if(request.session['AGR_ans'] != NULL):
        context['answers'] = []
        for i in range(1,11):
            temp = (request.session['AGR_ans'][i-1])
            tag = "input[name=AGR_" + str(i) + "][value=" + (temp) + "]"
            context['answers'].append(tag)

    return render(request, 'test3.html', context)

def process3(request, flag):
    if(request.method == "POST"):
        if(request.session['EXT_ans'] == NULL):
            return redirect('/testpage1')
        if(request.session['NRT_ans'] == NULL):
            return redirect('/testpage2')
        if(request.session['AGR_ans'] == NULL):
            agr_quest_resp = []
            for i in range(1,11):
                agr_quest_resp.append(request.POST['AGR_'+str(i)])
        else:
            agr_quest_resp = request.session['AGR_ans']
            for i in range(0,10):
                agr_quest_resp[0] = request.POST['AGR_'+str(i+1)]

        
        request.session['AGR_ans'] = agr_quest_resp
        print(request.session['AGR_ans'])
        if(int(flag) == 1):
            return redirect('/testpage4')
        else:
            return redirect('/testpage2')

def testpage4(request):
    if(request.session['EXT_ans'] == NULL):
        return redirect('/testpage1')
    if(request.session['NRT_ans'] == NULL):
        return redirect('/testpage2')
    if(request.session['AGR_ans'] == NULL):
        return redirect('/testpage3')
    context = {}
    context['que_1'] = Questions.objects.filter(category_id = 'C_2')

    if(request.session['CNS_ans'] != NULL):
        context['answers'] = []
        for i in range(1,11):
            temp = (request.session['CNS_ans'][i-1])
            tag = "input[name=CNS_" + str(i) + "][value=" + (temp) + "]"
            context['answers'].append(tag)

    return render(request, 'test4.html', context)

def process4(request, flag):
    if(request.method == "POST"):
        if(request.session['EXT_ans'] == NULL):
            return redirect('/testpage1')
        if(request.session['NRT_ans'] == NULL):
            return redirect('/testpage2')
        if(request.session['AGR_ans'] == NULL):
            return redirect('/testpage3')
        if(request.session['CNS_ans'] == NULL):
            cns_quest_resp = []
            for i in range(1,11):
                cns_quest_resp.append(request.POST['CNS_'+str(i)])
        else:
            cns_quest_resp = request.session['CNS_ans']
            for i in range(0,10):
                cns_quest_resp[i] = request.POST['CNS_'+str(i+1)]

        
        request.session['CNS_ans'] = cns_quest_resp
        print(request.session['CNS_ans'])
        if(int(flag) == 1):
            return redirect('/testpage5')
        else:
            return redirect('/testpage3')

def testpage5(request):
    if(request.session['EXT_ans'] == NULL):
        return redirect('/testpage1')
    if(request.session['NRT_ans'] == NULL):
        return redirect('/testpage2')
    if(request.session['AGR_ans'] == NULL):
        return redirect('/testpage3')
    if(request.session['CNS_ans'] == NULL):
        return redirect('/testpage4')
    context = {}
    context['que_1'] = Questions.objects.filter(category_id = 'C_1')

    if(request.session['OPN_ans'] != NULL):
        context['answers'] = []
        for i in range(1,11):
            temp = (request.session['OPN_ans'][i-1])
            tag = "input[name=OPN_" + str(i) + "][value=" + (temp) + "]"
            context['answers'].append(tag)

    return render(request, 'test5.html', context)

def process5(request, flag):
    if(request.method == "POST"):
        if(request.session['EXT_ans'] == NULL):
            return redirect('/testpage1')
        if(request.session['NRT_ans'] == NULL):
            return redirect('/testpage2')
        if(request.session['AGR_ans'] == NULL):
            return redirect('/testpage3')
        if(request.session['CNS_ans'] == NULL):
            return redirect('/testpage4')
        if(request.session['OPN_ans'] == NULL):
            opn_quest_resp = []
            for i in range(1,11):
                opn_quest_resp.append(request.POST['OPN_'+str(i)])
        else:
            opn_quest_resp = request.session['OPN_ans']
            for i in range(0,10):
                opn_quest_resp[i] = request.POST['OPN_'+str(i+1)]

        
        request.session['OPN_ans'] = opn_quest_resp
        print(request.session['OPN_ans'])
        if(int(flag) == 1):
            return redirect('/addResponse')
        else:
            return redirect('/testpage4')

def addResponse(request):
    if(request.session['EXT_ans'] == NULL):
        return redirect('/testpage1')
    if(request.session['NRT_ans'] == NULL):
        return redirect('/testpage2')
    if(request.session['AGR_ans'] == NULL):
        return redirect('/testpage3')
    if(request.session['CNS_ans'] == NULL):
        return redirect('/testpage4')
    if(request.session['OPN_ans'] == NULL):
        return redirect('/testpage5')
    
    responses_given = []
    ext_ans = list(request.session['EXT_ans'])
    nrt_ans = list(request.session['NRT_ans'])
    agr_ans = list(request.session['AGR_ans'])
    cns_ans = list(request.session['CNS_ans'])
    opn_ans = list(request.session['OPN_ans'])

    ext_ans = [eval(i) for i in ext_ans]
    nrt_ans = [eval(i) for i in nrt_ans]
    agr_ans = [eval(i) for i in agr_ans]
    cns_ans = [eval(i) for i in cns_ans]
    opn_ans = [eval(i) for i in opn_ans]

    responses_given = ext_ans + nrt_ans + agr_ans + cns_ans + opn_ans
    # result = {}
    request.session['response'] = responses_given
    # result['response'] = responses_given 

    try:
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='big5test')
        if conn.is_connected():
            print("You're connected to database: ")
            cursor = conn.cursor()
            print("Hello")
            print(type(ext_ans[0]))
            insert_stmt = ( """INSERT INTO predictpersonality_responses(ext_1, ext_2, ext_3, ext_4, ext_5, ext_6, ext_7, ext_8, ext_9, ext_10, nrt_1, nrt_2, nrt_3, nrt_4, nrt_5, nrt_6, nrt_7, nrt_8, nrt_9, nrt_10, agr_1, agr_2, agr_3, agr_4, agr_5, agr_6, agr_7, agr_8, agr_9, agr_10, csn_1, csn_2, csn_3, csn_4, csn_5, csn_6, csn_7, csn_8, csn_9, csn_10, opn_1, opn_2, opn_3, opn_4, opn_5, opn_6, opn_7, opn_8, opn_9, opn_10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")
        
            data = (ext_ans[0], ext_ans[1],ext_ans[2], ext_ans[3], ext_ans[4], ext_ans[5], ext_ans[6], ext_ans[7], ext_ans[8], ext_ans[9], nrt_ans[0], nrt_ans[1], nrt_ans[2], nrt_ans[3], nrt_ans[4], nrt_ans[5], nrt_ans[6], nrt_ans[7], nrt_ans[8], nrt_ans[9],agr_ans[0], agr_ans[1], agr_ans[2], agr_ans[3], agr_ans[4], agr_ans[5], agr_ans[6], agr_ans[7], agr_ans[8], agr_ans[9], cns_ans[0], cns_ans[1], cns_ans[2], cns_ans[3], cns_ans[4], cns_ans[5], cns_ans[6], cns_ans[7], cns_ans[8], cns_ans[9], opn_ans[0], opn_ans[1], opn_ans[2], opn_ans[3], opn_ans[4], opn_ans[5], opn_ans[6], opn_ans[7], opn_ans[8], opn_ans[9])
            cursor.execute(insert_stmt, data)
            conn.commit()
            print('Record inserted successfully')

    except mysql.connector.Error as error:
        print("Failed to connect".format(error))
        conn.rollback()

    # except mysql.connector.Error as error:
    #     print(error)
        
    conn.close()
    return redirect('/finalSubmit') 

def finalSubmit(request):
    if(request.session['EXT_ans'] == NULL):
        return redirect('/testpage1')
    if(request.session['NRT_ans'] == NULL):
        return redirect('/testpage2')
    if(request.session['AGR_ans'] == NULL):
        return redirect('/testpage3')
    if(request.session['CNS_ans'] == NULL):
        return redirect('/testpage4')
    if(request.session['OPN_ans'] == NULL):
        return redirect('/testpage5')
    


    responses_given = request.session['response']

    loaded_model = joblib.load('./static/files/model.joblib')
    # result = loaded_model.score(X_test, y_test)
    ans = loaded_model.predict([responses_given])
    dataclusters5 = pd.read_csv('./static/files/dataclusters.csv')
    print(dataclusters5)
    values = dataclusters5.loc[ans[0]]
    EXT_ans = (values['extroversion']*100) / 5
    NRT_ans = (values['neurotic']*100) / 5
    AGR_ans = (values['agreeable']*100) / 5
    CNS_ans = (values['conscientious']*100) / 5
    OPN_ans = (values['open']*100) / 5
    print('EXT: ', EXT_ans, '%')
    print('NRT: ', NRT_ans, '%')
    print('AGR: ', AGR_ans, '%')
    print('CNS: ', CNS_ans, '%')
    print('OPN: ', OPN_ans, '%')

    result = {}
    result['answers'] =[]
    result['answers'].append(EXT_ans)
    result['answers'].append(NRT_ans)
    result['answers'].append(AGR_ans)
    result['answers'].append(CNS_ans)
    result['answers'].append(OPN_ans)

    extAnwerList = [EXT_ans, (100-EXT_ans)]
    plt.figure(0)
    plt.pie(extAnwerList, autopct='%1.1f%%', startangle=90)
    plt.title('Extroversion')
    # plt.axis('equal')
    # plt.show()
    plt.savefig('./static/files/ext.png',dpi=65)
    plt.close()

    nrtAnwerList = [NRT_ans, (100-NRT_ans)]
    plt.figure(1)
    plt.pie(nrtAnwerList, autopct='%1.1f%%',  startangle=90)
    plt.title('Neuroticism')
    # plt.axis('equal')
    # plt.show()
    plt.savefig('./static/files/nrt.png',dpi=65)
    plt.close()

    agrAnwerList = [AGR_ans, (100-AGR_ans)]
    plt.figure(2)
    plt.pie(agrAnwerList, autopct='%1.1f%%', startangle=90)
    plt.title('Agreeableness')
    # plt.axis('equal')
    # plt.show()
    plt.savefig('./static/files/agr.png',dpi=65)
    plt.close()

    opnAnwerList = [OPN_ans, (100-OPN_ans)]
    plt.figure(3)
    plt.pie(opnAnwerList, autopct='%1.1f%%', startangle=90)
    plt.title('Openness')
    # plt.axis('equal')
    # plt.show()
    plt.savefig('./static/files/opn.png',dpi=65)
    plt.close()

    cnsAnwerList = [CNS_ans, (100-CNS_ans)]
    plt.figure(4)
    plt.pie(cnsAnwerList, autopct='%1.1f%%', startangle=90)
    plt.title('Conscientiousness')
    # plt.axis('equal')
    # plt.show()
    plt.savefig('./static/files/cns.png',dpi=65)
    plt.close()

    return render(request, 'result.html', result)


def modelGeneration(request):
    dataset = pd.read_csv("./static/files/data-final.csv", delimiter = "\t")
    dataset.drop(dataset.columns[50:], axis=1, inplace = True)
    
    dataset.fillna(dataset.mean(numeric_only = True).round(1), inplace=True)
    kmeans = KMeans(n_clusters=5)
    k_fit_5 = kmeans.fit(dataset)

    pd.options.display.max_columns = 10
    predictions5 = k_fit_5.labels_
    data5 = dataset
    data5['Clusters'] = predictions5

    data5.Clusters.value_counts()
    pd.options.display.max_columns = 150
    data5.groupby('Clusters').mean()

    col_list = list(data5)
    ext = col_list[0:10]
    est = col_list[10:20]
    agr = col_list[20:30]
    csn = col_list[30:40]
    opn = col_list[40:50]

    data_sums5 = pd.DataFrame()
    data_sums5['extroversion'] = data5[ext].sum(axis=1)/10
    data_sums5['neurotic'] = data5[est].sum(axis=1)/10
    data_sums5['agreeable'] = data5[agr].sum(axis=1)/10
    data_sums5['conscientious'] = data5[csn].sum(axis=1)/10
    data_sums5['open'] = data5[opn].sum(axis=1)/10
    data_sums5['clusters'] = predictions5
    data_sums5.groupby('clusters').mean()

    # global dataclusters5
    dataclusters5 = data_sums5.groupby('clusters').mean()
    dataclusters5.to_csv('./static/files/dataclusters.csv')
    # dataClusters5 = dataclusters5
    # request.session['dataclusters5'] = dataclusters5

    filename = "./static/files/model.joblib"
    joblib.dump(k_fit_5, filename)
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')