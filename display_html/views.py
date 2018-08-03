from django.shortcuts import render
import json
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
import os
import xml.etree.ElementTree as ET
import xml.etree.ElementTree
from django.utils.datastructures import MultiValueDict
from django.utils.http import urlencode
def FileDisplayTable(request):
    fileHandle = open('Process_list.txt', 'r')
    whole_data = [x.strip().split("|") for x in fileHandle]
    whole_data.pop(1)
    str_list = [list(filter(None, lst)) for lst in whole_data]
    keys=str_list[0]
    values=str_list[1:]
    data_output = {x:list(y) for x,y in zip(keys, zip(*values))}
    #data_output={'test':['Lemma','Whiskey'],'Precision':['53%','43'],'Recall':['52%','43%'],'Latency':['30ms','25ms']}
    print data_output
    return render_to_response('kpi_de.html',{'obj':data_output})


def XmlFileDisplay (request):
    filename = "xunit.xml"
    full_filename= os.path.abspath(os.path.join('data',filename))
    dom = ET.parse(full_filename)
    collection_element=dom.findall("./assembly/")
    xunit = [elem.attrib for elem in collection_element]
    print xunit
    return render_to_response('xunit.html',{'obj':xunit[1:]})


def mstest(request):
   filename = "mstest.xml"
   MSTEST_NAMESPACE = 'http://microsoft.com/schemas/VisualStudio/TeamTest/2010'
   tree = xml.etree.ElementTree.parse(filename)
   root = tree.getroot()
   results_node = root.find('{%s}ResultSummary' % MSTEST_NAMESPACE)
   results = results_node.findall('{%s}Counters' % MSTEST_NAMESPACE)
   mstest = [elem.attrib for elem in results]
   print mstest
   return render_to_response('mstest.html',{'obj':mstest})



def kpi(request):
    f = open("kpi.tsv","r")
    d = {}
    d = dict(x.rstrip().split(None, 1) for x in f)
    return render_to_response('kpi.html',{'kpi':d,},context_instance=RequestContext(request))


def total(request):
    f = open("kpi.tsv", "r")
    d = {}
    kpi = dict(x.rstrip().split(None, 1) for x in f)

    dom = ET.parse("xunit.xml")
    collection_element=dom.findall("./assembly/")
    xunit = [elem.attrib for elem in collection_element]
        
    fileHandle = open('Process_list.txt', 'r')
    whole_data = [x.strip().split("|") for x in fileHandle]
    whole_data.pop(1)
    str_list = [list(filter(None, lst)) for lst in whole_data]
    keys=str_list[0]
    values=str_list[1:]
    data_output = {x:list(y) for x,y in zip(keys, zip(*values))}

    MSTEST_NAMESPACE = 'http://microsoft.com/schemas/VisualStudio/TeamTest/2010'
    tree = xml.etree.ElementTree.parse("mstest.xml")
    root = tree.getroot()
    results_node = root.find('{%s}ResultSummary' % MSTEST_NAMESPACE)
    results = results_node.findall('{%s}Counters' % MSTEST_NAMESPACE)
    mstest = [elem.attrib for elem in results]
    print
    return render_to_response('total.html',{'obj1':kpi,'obj2':xunit[1:],'obj3':data_output,'obj4':mstest})

  
    


